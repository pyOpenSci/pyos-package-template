"""Test jinja template partials."""

from pathlib import Path

import pytest
from jinja2 import Environment

_license_stub_names = {
    "MIT": "MIT License",
    "BSD-3-Clause" : "3-Clause BSD License",
    "Apache-2.0": "Apache Software License 2.0",
    "GPL-3.0-only": "GNU Public License 3.0",
    "EUPL-1.2": "EUPL 1.2 or later",
    "MPL-2.0": "Mozilla Public License, v2.0",
}

@pytest.mark.parametrize("license_path", [None, False, "../LICENSE"])
def test_license_stub(license: str, license_path: Path, includes: Environment):
    """License stub generates with the correct license and link to license file."""
    year = "100"
    copyright_holder = "The Commons"
    license_name = _license_stub_names[license]

    template = includes.get_template("licenses/stub.md.jinja")
    stub = template.render({
        "license": license,
        "license_path": license_path,
        "copyright_holder": copyright_holder,
        "year": year,
        })

    for substring in ("Copyright", year, copyright_holder, license_name):
        assert substring in stub

    if license_path is None:
        # default location
        assert f"[{license_name}](./LICENSE)" in stub
    elif not license_path:
        # aka an explicit false to not make a link
        # aka the worst way to test this
        assert "[" not in stub
        assert "]" not in stub
    else:
        assert f"[{license_name}]({license_path})" in stub
