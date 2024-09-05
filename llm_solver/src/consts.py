import pathlib

RUN_DIR = logs_dir = pathlib.Path(__file__).parent.parent.resolve() / "run"
LOGS_DIR = RUN_DIR / "logs"
CLAUDE_CACHE_DIR = RUN_DIR / "cache" / "claude_cache"

ASSISTANT_ROLE = "assistant"
USER_ROLE = "user"
