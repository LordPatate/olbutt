from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def make_buttfile_from_example():
    buttfile = Path("buttfile.toml")
    buttfile.symlink_to("example_buttfile.toml")
    yield buttfile
    buttfile.unlink()
