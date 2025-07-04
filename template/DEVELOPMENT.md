# Development Guide

Welcome to your shiny new package. This page will help you get started with using Hatch to manage your package.

If you look at your project, you will see that a `pyproject.toml` file. This file stores both your package configuration and settings for development tools like Hatch that you will use to work on your package.

This file is written using a `.toml` format. [You can learn more about toml here.](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html) Here's the TL&DR:

* Each `[]` section in the toml file is called a table. 
* You can nest tables with double brackets like this`[[]]`
* Tables contain information about a element that you want to configure. 

We are using Hatch as the default packaging tool.
Hatch allows you to configure and run environments and scripts similar to workflow tools like tox or nox. 

Hach, by default, uses virtual environments (venv) to manage environments. But you can configure it to use other environment tools.[ Read the hatch documentation to learn more about environments. ](https://hatch.pypa.io/1.13/tutorials/environment/basic-usage/)

For this template, we have set up Hatch environments for you to use. At the bottom of your pyproject.toml file, notice a [hatch environment](https://hatch.pypa.io/1.13/environment/) section that looks like this: 

```
########################################
# Hatch Environments
########################################
```

Below is the Hatch environment to install your package. Notice that it defines pip and twine as two packages that the environment needs.

```toml
[tool.hatch.envs.build]
description = """Test the installation the package."""
dependencies = [
    "pip",
    "twine",
]
```

The table below defines the scripts that you will run build and check your package.

```toml
[tool.hatch.envs.build.scripts]
check = [
    "pip check",
    "hatch build {args:--clean}",
    "twine check dist/*",
]
detached = true
```

You can enter that environment to check it out:

```console
$ hatch shell build
```

If you run `pip list`, in the environment, **twine** will be there:

```console
$ pip list
```

Hatch by default, installs your package in **editable mode (`-e`)** into its  virtual environments. But if `detached=True` is set, then it will skip installing your package into the virtual enviornment. 

### Hatch and matrix environments

Below you see the Hatch environment test table. 

`tool.hatch.envs` says, "Hey, Hatch, this is the definition for an environment."
`test` is the name of the environment.

The environment below defines the dependencies that Hatch needs to install into the environment named test. 

```toml
[tool.hatch.envs.test]
description = """Run the test suite."""
dependencies = [
    "pytest",
    "pytest-cov",
    "pytest-raises",
    "pytest-randomly",
    "pytest-xdist",
]
```

To enter a Hatch environment use:

`hatch shell environmentname`

So you can enter the test environment above with:

`hatch shell test`

### Your test environment has a matrix associated with it

If the environment has a matrix associated with it, that tells Hatch to run the test scripts across different Python versions.

```toml
[[tool.hatch.envs.test.matrix]]
python = ["3.10", "3.11", "3.12", "3.13"]
```

If you run `hatch shell test`, you will see the output below. To enter an environment with a matrix attached to it, you need to pick the Python environment version that you want to open. 

```console
$ hatch shell test                           
Environment `test` defines a matrix, choose one of the following instead:

test.py3.10
test.py3.11
test.py3.12
test.py3.13
```
 
Open the Python 3.13 environment like this:

```console
$ hatch shell test.py3.13
```

To leave an environment use: 

```console
$ deactivate
```

### Hatch scripts

In the tests section of your pyproject.toml, you will see a `tool.hatch.envs.test.scripts` table. 

This table defines the commands that you want Hatch to run in the test environment. Notice that the script has one command called `run`.

```toml
[tool.hatch.envs.test.scripts]
run = "pytest {args:--cov=greatproject --cov-report=term-missing}"
```

To run this script , use:

`hatch run test:run`

* `hatch run`: calls Hatch and tells it that it will be running a command
* `test:run`: defines the environment you want it to run (`test`) and defines the name of the "script" to be`run`.

If you have a Hatch matrix setup for tests, it will both install the necessary Python version using UV and run your tests on each version of the Python versions that you declare in the matrix table. In this case, there are 4 Python versions in the environment, so your tests will run 4 times, once in each Python version listed in the matrix table. 

```
@lwasser ➜ /workspaces/pyopensci-scipy25-create-python-package (main) $ hatch run test:run
──────────────────────────────────────────────────────────────────────── test.py3.10 ────────────────────────────────────────────────────────────────────────
==================================================================== test session starts ====================================================================
platform linux -- Python 3.10.16, pytest-8.4.1, pluggy-1.6.0
Using --randomly-seed=1490740387
rootdir: /workspaces/pyopensci-scipy25-create-python-package
configfile: pyproject.toml
testpaths: tests
plugins: xdist-3.8.0, randomly-3.16.0, raises-0.11, cov-6.2.1
collected 2 items                                                                                                                                           

tests/system/test_import.py .                                                                                                                         [ 50%]
tests/unit/test_example.py .                                                                                                                          [100%]

====================================================================== tests coverage =======================================================================
_____________________________________________________ coverage: platform linux, python 3.10.16-final-0 ______________________________________________________

Name                           Stmts   Miss Branch BrPart    Cover   Missing
----------------------------------------------------------------------------
src/greatproject/__init__.py       0      0      0      0  100.00%
src/greatproject/example.py        2      0      0      0  100.00%
----------------------------------------------------------------------------
TOTAL                              2      0      0      0  100.00%
===================================================================== 2 passed in 0.05s =====================================================================
──────────────────────────────────────────────────────────────────────── test.py3.11 ────────────────────────────────────────────────────────────────────────
==================================================================== test session starts ====================================================================
platform linux -- Python 3.11.12, pytest-8.4.1, pluggy-1.6.0
Using --randomly-seed=1596865075
rootdir: /workspaces/pyopensci-scipy25-create-python-package
configfile: pyproject.toml
testpaths: tests
plugins: xdist-3.8.0, randomly-3.16.0, raises-0.11, cov-6.2.1
collected 2 items                                                                                                                                           

tests/system/test_import.py .                                                                                                                         [ 50%]
tests/unit/test_example.py .                                                                                                                          [100%]

====================================================================== tests coverage =======================================================================
_____________________________________________________ coverage: platform linux, python 3.11.12-final-0 ______________________________________________________

Name                           Stmts   Miss Branch BrPart    Cover   Missing
----------------------------------------------------------------------------
src/greatproject/__init__.py       0      0      0      0  100.00%
src/greatproject/example.py        2      0      0      0  100.00%
----------------------------------------------------------------------------
TOTAL                              2      0      0      0  100.00%
===================================================================== 2 passed in 0.05s =====================================================================
```

## Build your package

You can build your package using the environment and scripts defined in the `build` tables:  

`hatch run build:check` 

This script builds and checks the output distribution files of your package. 

This build environment table declares that `pip` and `twine` should be added to that environment. Adding pip to the environment ensures that it is a current, up-to-date version.

```toml
[tool.hatch.envs.build]
description = """Build and test your package."""
dependencies = [
    "pip",
    "twine",
]
detached = true
```

```toml
# This table installs created the command hatch run install:check which will build and check your package.
[tool.hatch.envs.install.scripts]
check = [
    "pip check",
    "hatch build {args:--clean}",
    "twine check dist/*",
]
```
This uses the above environment and tells hatch to run 

* `pip check`,  # verifies your dependencies
* `hatch build --clean`  
* `twine check dist/*` # this checks your distribution for metadata and other potential issues. 
to build and test your package.  
