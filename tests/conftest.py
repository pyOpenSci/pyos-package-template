"""Provide fixtures to the entire test suite."""

import shutil
from collections.abc import Generator
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from _pytest.monkeypatch import MonkeyPatch
from jinja2 import Environment, FileSystemLoader
from ruamel.yaml import YAML

if TYPE_CHECKING:
    from _pytest.config.argparsing import Parser
    from _pytest.tmpdir import TempPathFactory

COPIER_CONFIG_PATH = Path(__file__).parents[1] / "copier.yml"
INCLUDES_PATH = Path(__file__).parents[1] / "includes"


def _load_copier_config() -> dict:
    yaml = YAML(typ="safe")
    with COPIER_CONFIG_PATH.open("r") as yfile:
        return yaml.load(yfile)


# don't mutate or else i'll have to get out the spray bottle (make it a fixture)
COPIER_CONFIG = _load_copier_config()

# --------------------------------------------------
# pytest hooks
# --------------------------------------------------


def pytest_addoption(parser: "Parser") -> None:
    """Add options to pytest."""
    parser.addoption(
        "--reuse-envs",
        action="store_true",
        help="After tests run, don't remove hatch environments created for "
        "generated projects (not the test environments for the "
        "pyos-package-template project itself).\n"
        "otherwise, use a temporary directoy and remove it afterwards.",
    )


# --------------------------------------------------
# Fixtures - autouse
# --------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def cleanup_hatch_envs(
    pytestconfig: pytest.Config,
    tmp_path_factory: "TempPathFactory",
    monkeypatch_session: MonkeyPatch,
) -> None:
    """
    Use a temporary directory for hatch envs & cleanup after session.

    Unless --reuse-envs flag present.
    """
    if pytestconfig.getoption("--reuse-envs"):
        yield
        return

    hatch_dir = tmp_path_factory.mktemp("hatch")
    monkeypatch_session.setenv("HATCH_DATA_DIR", str(hatch_dir))

    try:
        yield
    finally:
        shutil.rmtree(hatch_dir, ignore_errors=True)


# ---------------------------------------------
# Fixtures - exports
# ---------------------------------------------


@pytest.fixture(scope="session")
def monkeypatch_session() -> Generator[MonkeyPatch, None, None]:
    """Monkeypatch you can use with a session scoped fixture."""
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


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
