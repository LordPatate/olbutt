import subprocess
import sys
from argparse import ArgumentParser, Namespace

from src.buttfile import load_buttons


def olbutt(button: str) -> int:
    buttons = load_buttons()
    selected_button = buttons[button]
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
