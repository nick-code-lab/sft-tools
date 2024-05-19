import sys
from enum import Enum, unique

from . import __version__
from .api.app import run_api
from .chat.chat_model import run_chat
from .eval.evaluator import run_eval
from .train.tuner import export_model, run_exp

USAGE = """
Usage:
    sft-cli api -h: launch an API server
    sft-cli chat -h: launch a chat interface in CLI
    sft-cli eval -h: do evaluation
    sft-cli export -h: merge LoRA adapters and export model
    sft-cli train -h: do training
    sft-cli version: show version info
"""


@unique
class Command(str, Enum):
    API = "api"
    CHAT = "chat"
    EVAL = "eval"
    EXPORT = "export"
    TRAIN = "train"
    VERSION = "version"

def main():
    command = sys.argv.pop(1)
    if command == Command.API:
        run_api()
    elif command == Command.CHAT:
        run_chat()
    elif command == Command.EVAL:
        run_eval()
    elif command == Command.EXPORT:
        export_model()
    elif command == Command.TRAIN:
        run_exp()
    elif command == Command.VERSION:
        print("Welcome to SFT Tools, version {}".format(__version__))
    elif command == Command.HELP:
        print(USAGE)
    else:
        raise NotImplementedError("Unknown command: {}".format(command))
