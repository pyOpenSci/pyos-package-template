"""Provide fixtures to the entire test suite."""

import shutil
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any, Generator

import pytest
from funcy import lflatten
from _pytest.monkeypatch import MonkeyPatch
from jinja2 import Environment, FileSystemLoader
from ruamel.yaml import YAML, Loader
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.nodes import ScalarNode

if TYPE_CHECKING:
    from _pytest.config.argparsing import Parser
    from _pytest.tmpdir import TempPathFactory

COPIER_CONFIG_PATH = Path(__file__).parents[1] / "copier.yml"
INCLUDES_PATH = Path(__file__).parents[1] / "includes"

# handle copier's !include tags - 
# they went and did us the favor of making their entire package private,
# so to respect their wishes to touch nothing we copy it here
# with mild modifications for our use case and for ruamel.yaml
# https://github.com/copier-org/copier/blob/24e842d838cf41b90a024ae4f80834add0ea95c2/copier/_template.py#L86
def _include(loader: Constructor, node: ScalarNode) -> Any:
    if not isinstance(node, ScalarNode):
        raise ValueError(f"Unsupported YAML node: {node!r}")
    include_file = str(loader.construct_scalar(node))
    if PurePosixPath(include_file).is_absolute():
        raise ValueError("YAML include file path must be a relative path")
    path = next(COPIER_CONFIG_PATH.parent.glob(include_file))
    return [YAML(typ="safe").load(path.read_bytes())]


def _load_copier_config() -> dict:
    yaml = YAML(typ="safe")
    yaml.constructor.add_constructor("!include", _include)

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
