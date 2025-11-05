# pyOpenSci packaging template Changelog

## [Unreleased]

* Fix docs CI builds to to simplify maintenance and feedback on jobs (@lwasser, #127, #138)

## [v0.6.7]

### Fixed
* Fix RTD build for Sphinx and move docs dependencies to `optional-dependencies` (@lwasser, #126, #130, #131)
* Remove typing annotations in FULL template mode (@lwasser, #134)
* Make `test_audit` script that doesn't fail (@erik-whiting, #120)
* Remove readthedocs.io URL from pyproject.toml for minimal version (@Michael-Howes, #119)
* Move all dependencies to `optional-dependencies` and use hatch features (@lwasser, #132)
* bug: ensure sphinx build works by @lwasser in https://github.com/pyOpenSci/pyos-package-template/pull/130
* Move all dependencies to `optional.deps` and use hatch features (@lwasser, #131)

### Added
* Add and configure Dependabot (@agriyakhetarpal, #79)

### Contributors
* @erik-whiting made their first contribution in #120
* @Michael-Howes made their first contribution in #119
* @agriyakhetarpal made their first contribution in #79
* @dependabot[bot] made their first contribution in #128

## New Contributors
* @erik-whiting made their first contribution in https://github.com/pyOpenSci/pyos-package-template/pull/120
* @Michael-Howes made their first contribution in https://github.com/pyOpenSci/pyos-package-template/pull/119
* @agriyakhetarpal made their first contribution in https://github.com/pyOpenSci/pyos-package-template/pull/79


## [0.6.0]

### Added

* Update release workflow to follow PyPA / PyPI recommended practices (@lwasser, #48)
* development instructions for hatch envt by @lwasser in #115
* uv by @lwasser in #116
