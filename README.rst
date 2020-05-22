Cookiecutter pyOpenSci
======================

.. image:: https://travis-ci.org/pyOpenSci/cookiecutter-pyopensci.svg?branch=master
    :target: https://travis-ci.org/pyOpenSci/cookiecutter-pyopensci

.. image:: https://ci.appveyor.com/api/projects/status/github/pyOpenSci/cookiecutter-pyopensci?branch=master&svg=true
    :target: https://ci.appveyor.com/project/pyOpenSci/cookiecutter-pyopensci/branch/master

**Cookiecutter** template for a pyOpenSci Python packge.

-  GitHub repo: https://github.com/pyOpenSci/cookiecutter-pyopensci
-  Documentation: https://cookiecutter-pyopensci.readthedocs.io/
-  pyOpenSci Guidebook: https://pyopensci.github.io/dev_guide
-  Free software: BSD license

Features
--------

-  **Tox** and **pytest** testing: Setup to easily test for Python 3.6,
   3.7, 3.8
-  **Travis-CI**: Ready for Travis Continuous Integration testing
-  **codecov**: Code coverage report and badge using codecov and Travis
-  **Sphinx** docs: Documentation ready for generation with, for
   example, **ReadTheDocs**
-  **Bumpversion**: Pre-configured version bumping with a single command
-  Auto-release to **PyPI** when you push a new tag to master (optional)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher)

::

    pip install -U cookiecutter

Generate a Python package project:

::

    cookiecutter https://github.com/pyOpenSci/cookiecutter-pyopensci.git

For more details, see the
```cookiecutter-pyopensci tutorial`` <https://cookiecutter-pyopensci.readthedocs.io/en/latest/tutorial.html>`__
