import tomllib

from src.model import Button


def load_buttons() -> dict[str, Button]:
    with open("buttfile.toml", "rb") as f:
        config_dict = tomllib.load(f)
    return {
        b_name: Button(**b_dict)
        for b_name, b_dict in config_dict.items()
    }
