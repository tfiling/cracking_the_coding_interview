import logging
import typing

import questionary

from run.input import question
from src import anthropic_client
from src import consts
from src.prompts import initial_analysis, system, generate_test_cases


class Solver:
    def __init__(self):
        self._client = anthropic_client.AnthropicWrapper(system.PROMPT)
        self._chat_history: typing.List[anthropic_client.ChatMessage] = []

    def solve(self):
        print(f"Solving the following question:\n{question.CONTENT}\n\n{question.SOLUTION_TEMPLATE}")
        print("=" * 150)
        print("=" * 150)
        self._send_initial_analysis_prompt()
        self._generate_test_cases()

    def _send_initial_analysis_prompt(self):
        prompt = initial_analysis.PROMPT.format(question=question.CONTENT,
                                                solution_template=question.SOLUTION_TEMPLATE)
        self._chat_history.append(anthropic_client.ChatMessage(role=consts.USER_ROLE, content=prompt))
        resp = self._client.send_prompt(self._chat_history)
        resp.content = anthropic_client.extract_json_from_prompt_text_block(resp.content)
        self._chat_history.append(resp)
        print(f"Initial analysis result:")
        for prop, val in resp.content.items():
            print(f"{prop}: {val}")
        print("=" * 150)
        print("=" * 150)
        # TODO - validate extracted args from argument_names prop
        if not prompt_yes_no_question("Approve Initial analysis"):
            raise RuntimeError(f"Could not solve the question - invalid initial analysis")

    def _generate_test_cases(self):
        # TODO - flow for generating additional test cases
        generate_test_cases_msg = anthropic_client.ChatMessage(role=consts.USER_ROLE,
                                                               content=generate_test_cases.PROMPT)
        self._chat_history.append(generate_test_cases_msg)
        resp = self._client.send_prompt(self._chat_history)
        resp.content = extract_valid_test_cases(resp.content)
        self._chat_history.append(resp)


def extract_valid_test_cases(resp_contents: str) -> list:
    approved_cases = []
    resp_contents = anthropic_client.extract_json_from_prompt_text_block(resp_contents,
                                                                         generate_test_cases.EXPECTED_RESP_SCHEMA)
    print("Approve suggested test cases:")
    for test_case in resp_contents:
        print(f"Test case name: {test_case["name"]}")
        print(f"Args: {test_case["arguments"]}\n")
        print(f"Expected res: {test_case["expected"]}")
        if prompt_yes_no_question("Show use case explanation?"):
            print(f"Explanation: {test_case["explanation"]}")
        if prompt_yes_no_question("Is this test case valid?"):
            approved_cases.append(test_case)
    logging.info("approved %d of %d test cases", len(approved_cases), len(resp_contents))
    return approved_cases


def prompt_yes_no_question(asked_question: str) -> bool:
    answer = questionary.select(asked_question, choices=["yes", "no"]).ask()
    return answer == "yes"


def solve_question():
    instance = Solver()
    instance.solve()
