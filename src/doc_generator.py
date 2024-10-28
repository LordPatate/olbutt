import sys
from argparse import ArgumentParser, Namespace

from src.buttfile import load_buttons

TEMPLATE = """\
## {title}
{description}
```shell
{command}
```
"""


def generate_doc(default_title: str, default_description: str) -> str:
    buttons = load_buttons()
    button_doc_paragraphs = (
        TEMPLATE.format(
            title=button.title or default_title or button_name,
            description=button.description or default_description,
            command=button.command,
        )
        for button_name, button in buttons.items()
    )
    return "\n".join(button_doc_paragraphs)


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "--default_title",
        default="",
        help=("When generating the documentation for title-less buttons, if --default_title is left empty,"
              " their names will be used as titles instead.")
    )
    parser.add_argument("--default_description", default="")
    return parser.parse_args()


def main():
    args = get_args()
    doc = generate_doc(args.default_title, args.default_description)
    print(doc, end="")
    sys.exit(0)


if __name__ == "__main__":
    main()
