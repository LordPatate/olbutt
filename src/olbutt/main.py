import subprocess
import sys
import tomllib
from argparse import ArgumentParser, Namespace
from typing import NamedTuple


class Button(NamedTuple):
    command: str
    title: str | None = None
    description: str | None = None


def olbutt(button: str):
    # load buttons file
    with open("buttfile.toml", "rb") as f:
        buttons = tomllib.load(f)
    # execute corresponding entry
    selected_button = Button(**buttons[button])
    completed_process = subprocess.run(
        selected_button.command,
        shell=True,
    )
    return completed_process.returncode


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("button")
    return parser.parse_args()


def main():
    args = get_args()
    code = olbutt(args.button)
    sys.exit(code)


if __name__ == "__main__":
    main()
