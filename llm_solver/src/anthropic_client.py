import json
import logging
import os
import typing
from dataclasses import dataclass

import anthropic
from diskcache import Cache

from src import consts

cache = Cache(str(consts.CLAUDE_CACHE_DIR))


@dataclass
class ChatMessage:
    role: str
    content: str

    def to_dict(self):
        return {"role": self.role, "content": str(self.content)}


class SchemaValidationError(AssertionError):
    pass


class AnthropicWrapper:
    def __init__(self):
        api_key = os.environ.get("LEETCODE_SOLVER_CLAUDE_API_KEY")
        if not api_key:
            raise RuntimeError("API key env var was not set")
        self._client = anthropic.Anthropic(api_key=api_key, max_retries=5)

    def send_prompt(self, system_prompt: str, contents: typing.List[ChatMessage]) -> ChatMessage:
        if len(contents) == 0:
            raise ValueError("Received empty prompt contents")
        messages = [msg.to_dict() for msg in contents]
        cache_key = (system_prompt, contents)
        cached_res = cache.get(cache_key)
        if cached_res:
            logging.debug("cache hit: %s", system_prompt)
            return cached_res
        logging.info("Cache miss")
        logging.debug("Cache miss for: %s(%d)", system_prompt, len(messages))
        resp = self._client.messages.create(
            max_tokens=4096,
            model="claude-3-5-sonnet-20240620",
            system=system_prompt,
            temperature=0,
            messages=messages,
        )
        logging.info("Completed initial analysis. usage: %s", resp.usage)
        logging.debug("Initial analysis response: %s", resp.content)
        if len(resp.content) == 0:
            logging.error("received an empty response to prompt: %s", messages)
            raise RuntimeError("received an empty response to prompt")
        if len(resp.content) > 1:
            # TODO - make sure resp.content contains only the model's response
            logging.warning("received more that one block for prompt: %s\n\n\nresponse:%s", messages, resp)
        wrapped_resp = ChatMessage(role=consts.ASSISTANT_ROLE, content=resp.content[0].text)
        cache.set(cache_key, wrapped_resp)
        return wrapped_resp


def extract_json_from_prompt_text_block(text_block: str):
    res = {}
    if "```json" in text_block:
        start = text_block.index("```json")
        end = text_block.rindex("```")
        if end <= start:
            logging.error("detected an invalid json annotation in text block")
            return {}
        text_block = text_block[start + len("```json"):end]
    try:
        res = json.loads(text_block)
    except json.JSONDecodeError as e:
        logging.error("could not decode json from string with error: %s", e)
    return res
