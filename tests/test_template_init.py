# Copyright (c) 2024 pyOpenSci.
# Copyright (c) 2022 Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test the template initialization."""

from __future__ import annotations

import logging
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import pytest
from copier import run_copy
from git import Repo
from validate_pyproject import api as validator_api

try:
    import tomllib
except ImportError:
    # < python3.11
    # same thing right
    import tomli as tomllib

TEMPLATE = Path(__file__).parents[1]

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", params=["GitHub", "GitLab"])
def dev_platform(request: pytest.FixtureRequest) -> str:
    """Provide a recognized development platform."""
    return request.param


@pytest.fixture(
    scope="module",
    params=["mkdocs", "sphinx", ""],
)
def documentation(request: pytest.FixtureRequest) -> str:
    """Provide a documentation option."""
    return request.param


@pytest.fixture(scope="module")
def answers() -> dict[str, str]:
    """Provide a full project context."""
    today = datetime.now(tz=timezone.utc).date()
    return {
        "copyright_holder": "Citadel of Ricks",
        "author_name": "Rick Sanchez",
        "author_email": "rick@galaxybrain.science",
        "project_name": "Alien Clones",
        "project_slug": "alien-clones",
        "package_name": "alien_clones",
        "package_description": "Wubba Lubba Dub-Dub",
        "username": "rickprime",
        "year": str(today.year),
    }


@pytest.fixture
def generated(tmp_path: Path, answers: dict[str, str]) -> Callable[..., Path]:
    """Fixture closure to generate a template project, overriding passed data values."""
    def _generated(**kwargs) -> Path:
        run_copy(
            src_path=str(TEMPLATE),
            dst_path=tmp_path,
            vcs_ref="HEAD",
            data={
                **answers,
                **kwargs,
            },
            defaults=True,
        )

        init_git(tmp_path)

        return tmp_path
    return _generated


def init_git(path: Path):
    """Initialize a git repository such that hatch-vcs can be used."""
    project_dir = path.resolve(strict=True)
    repo = Repo.init(project_dir)
    repo.index.add(
        [
            Path(dirpath, name)
            for dirpath, _, filenames in os.walk(project_dir)
            for name in filenames
        ],
    )
    repo.index.commit("chore: initialize template")


def test_init_template(
    dev_platform: str,
    license: str,
    documentation: str,
    generated: Callable[..., Path],
) -> None:
    """Expect that the template can be initialized with all combinations of choices."""
    parent = generated(
        dev_platform=dev_platform,
        license=license,
        documentation=documentation,
    )

    project_files = {path.relative_to(parent) for path in parent.rglob("*")}
    expected = {
        Path("README.md"),
        Path("pyproject.toml"),
        Path("src"),
        Path("tests"),
        Path("LICENSE"),
    }
    assert expected.issubset(project_files), expected.difference(project_files)


@pytest.mark.installs
def test_template_suite(
    generated: Callable[..., Path],
) -> None:
    """Expect that the test suite passes for the initialized template."""
    project_dir = generated()

    # Run the local test suite.
    try:
        subprocess.run(
            "hatch run install:check",
            cwd=project_dir,
            check=True,
            shell=True,
        )
        subprocess.run(
            f"hatch run +py={sys.version_info.major}.{sys.version_info.minor} test:run",
            cwd=project_dir,
            check=True,
            shell=True,
        )
        subprocess.run(
            "hatch run style:check",
            cwd=project_dir,
            check=True,
            shell=True,
        )
        subprocess.run(
            "hatch run audit:check",
            cwd=project_dir,
            check=True,
            shell=True,
        )

    except subprocess.CalledProcessError as error:
        logger.error(  # noqa: TRY400
            "Command = %r; Return code = %d.",
            error.cmd,
            error.returncode,
        )
        raise


@pytest.mark.docs
@pytest.mark.installs
def test_docs_build(documentation: str, generated: Callable[..., Path]):
    """The docs should build."""
    if not documentation:
        return

    project = generated(documentation=documentation)

    subprocess.run(
        "hatch run docs:build",
        cwd=project,
        check=True,
        shell=True,
    )
    subprocess.run(
        "pre-commit run --all-files -v check-readthedocs",
        cwd=project,
        check=True,
        shell=True,
    )


@pytest.mark.installs
def test_dev_platform_github(generated: Callable[..., Path]):
    """Test github stuff idk!."""
    project = generated(use_git=True, dev_platform="GitHub")

    workflows_dir =  project / ".github" / "workflows"
    assert workflows_dir.exists()
    workflows = list(workflows_dir.iterdir())
    assert len(workflows) > 0
    assert all(workflow.suffix in (".yml", ".yaml") for workflow in workflows)

    subprocess.run(
        "pre-commit run --all-files -v check-github-workflows",
        cwd=project,
        check=True,
        shell=True,
    )


@pytest.mark.installs
def test_dev_platform_gitlab(generated: Callable[..., Path]):
    """Test gitlab stuff idk!."""
    project = generated(use_git=True, dev_platform="GitLab")

    subprocess.run(
        "pre-commit run --all-files -v check-gitlab-ci",
        cwd=project,
        check=True,
        shell=True,
    )


def test_non_hatch_deps(
    documentation: str,
    generated: Callable[..., Path],
) -> None:
    """When we aren't using hatch, we should still get the optional dependencies."""
    project = generated(
        use_hatch_envs=False,
        use_lint=True,
        use_types=True,
        use_test=True,
        use_git=False,
        documentation=documentation,
    )

    pyproject_file = project / "pyproject.toml"
    with pyproject_file.open("rb") as pfile:
        pyproject = tomllib.load(pfile)

    # validate pyproject.toml file if present
    validator_api.Validator()(pyproject)

    optional_deps = pyproject["project"]["optional-dependencies"]
    groups = ("dev", "tests", "style", "types", "audit")
    assert all(group in optional_deps for group in groups)

    # we don't want to hardcode all our deps here,
    # bc that would be a very fragile test indeed.
    # Instead, we just assume their presence and that the validity of the pyproject file
    # means that they have been correctly specified.
    # except for the docs, where we want to test our switch works :)
    if documentation:
        assert "docs" in optional_deps
        assert any(dep.startswith(documentation) for dep in optional_deps["docs"])
