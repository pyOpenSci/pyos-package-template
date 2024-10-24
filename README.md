# pyOpenSci Package Template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)

> A Python package template that supports the pyOpenSci
> pure [Python packaging tutorial](https://www.pyopensci.org/python-package-guide/tutorials/intro.html).

This template can be used with [copier](https://copier.readthedocs.io) to initialize a
new Python package project structure following the practices outlined in the pyOpenSci
tutorial.

## Getting Started

To use this template:

1. install copier using [pipx](https://pipx.pypa.io/stable/) or pip preferably with a [virtual environment](https://www.pyopensci.org/python-package-guide/CONTRIBUTING.html#create-a-virtual-environment).

    ```sh
    pipx install copier
    ```
   
    or

    ```sh
    pip install copier
    ```

2. Run the below copier command. Please note that copier creates a target directory if
   it doesn't exist yet. It will also **create and possibly overwrite files in the given
   directory, even if it already exists!** That includes your current directory if that
   is your target.

    ```sh
    copier copy gh:pyopensci/pyos-package-template <target>
    ```

   Where `<target>` could be your current directory `.` or some other path.

   Used in the above way, copier will use the latest tagged release, which is probably
   the safest option. You can provide an option `--vcs-ref` to choose specific branches
   as your source. You can read more about generating your project
   in the [copier documentation](https://copier.readthedocs.io/en/stable/generating/).

### Staying Up-to-date

The community will likely continue to develop this template. If at any point, you want
to adopt those changes for your project, you can update it. Read more about that process
in the [copier documentation](https://copier.readthedocs.io/en/stable/updating/).
