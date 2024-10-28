from argparse import ArgumentParser, Namespace


def olbutt(button: str):
    # load buttons file
    ...
    # execute corresponding entry
    ...


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("button")
    return parser.parse_args()


def main():
    args = get_args()
    olbutt(args.button)


if __name__ == "__main__":
    main()
