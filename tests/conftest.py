"""Ruff is forcing me to write a docstring for conftest.py."""

from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader
from ruamel.yaml import YAML

COPIER_CONFIG_PATH = Path(__file__).parents[1] / "copier.yml"
INCLUDES_PATH = Path(__file__).parents[1] / "includes"

def _load_copier_config() -> dict:
    yaml = YAML(typ="safe")
    with COPIER_CONFIG_PATH.open("r") as yfile:
        return yaml.load(yfile)


# don't mutate or else i'll have to get out the spray bottle (make it a fixture)
COPIER_CONFIG = _load_copier_config()

# ---------------------------------------------
# Fixtures
# ---------------------------------------------

@pytest.fixture(scope="module")
def includes() -> Environment:
    """Jinja environment loaded with the partials dir."""
    return Environment(
        loader=FileSystemLoader(searchpath=str(INCLUDES_PATH.resolve())),
        autoescape=True,
    )


@pytest.fixture(
    scope="module",
    params=COPIER_CONFIG["license"]["choices"].values(),
)
def license(request: pytest.FixtureRequest) -> str:
    """Provide a recognized license classification."""
    return request.param
