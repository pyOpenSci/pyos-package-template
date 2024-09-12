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

import pytest
from copier import run_copy
from git import Repo

TEMPLATE = Path(__file__).parents[1]

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", params=["GitHub", "GitLab"])
def dev_platform(request: pytest.FixtureRequest) -> str:
    """Provide a recognized development platform."""
    return request.param


@pytest.fixture(
    scope="module",
    params=["MIT", "BSD-3-Clause", "Apache-2.0"],
)
def license(request: pytest.FixtureRequest) -> str:
    """Provide a recognized license classification."""
    return request.param


@pytest.fixture
def destination_path(
    tmp_path_factory: pytest.TempPathFactory,
    dev_platform: str,
) -> Path:
    """Provide a destination directory based on the development platform."""
    return tmp_path_factory.mktemp("instance") / dev_platform


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


def test_init_template(
    destination_path: Path,
    answers: dict[str, str],
    dev_platform: str,
    license: str,
) -> None:
    """Expect that the template can be initialized with any provided license."""
    parent = destination_path / license / answers["project_slug"]
    run_copy(
        src_path=str(TEMPLATE),
        dst_path=parent,
        vcs_ref="HEAD",
        data={
            **answers,
            "dev_platform": dev_platform,
            "license": license,
        },
        defaults=True,
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


def test_template_suite(
    destination_path: Path,
    dev_platform: str,
    answers: dict[str, str],
) -> None:
    """Expect that the test suite passes for the initialized template."""
    parent = destination_path / answers["project_slug"]
    run_copy(
        src_path=str(TEMPLATE),
        dst_path=parent,
        vcs_ref="HEAD",
        data={
            **answers,
            "dev_platform": dev_platform,
            "license": "MIT",
        },
        defaults=True,
    )

    # Initialize a git repository such that hatch-vcs can be used.
    project_dir = parent.resolve(strict=True)
    repo = Repo.init(project_dir)
    repo.index.add(
        [
            Path(dirpath, name)
            for dirpath, _, filenames in os.walk(project_dir)
            for name in filenames
        ],
    )
    repo.index.commit("chore: initialize template")

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
            "hatch run docs:build",
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
        subprocess.run(
            "pre-commit run --all-files -v check-readthedocs",
            cwd=project_dir,
            check=True,
            shell=True,
        )
        if dev_platform.lower() == "github":
            subprocess.run(
                "pre-commit run --all-files -v check-github-workflows",
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
