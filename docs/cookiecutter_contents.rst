Template Contents
=================

After you run cookiecutter to create your package from the template, you'll have a directory full of files and subdirectories. What are they all for? This page explains. For starting out, the most important files and directories are marked with \*.

First, here is the full contents of the template project that cookiecutter creates:

.. code-block:: bash

    example_project/
    ├── .editorconfig
    ├── .gitignore
    ├── .travis.yml
    ├── CONTRIBUTING.rst
    ├── CONTRIBUTORS.rst
    ├── docs\*
    │   ├── conf.py 
    │   ├── contributing.rst
    │   ├── contributors.rst
    │   ├── history.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   └── usage.rst\*
    ├── HISTORY.rst
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── example_project\*
    │   ├── __init__.py
    │   └── example_project.py
    ├── README.rst\*
    ├── requirements_dev.txt
    ├── setup.cfg
    ├── setup.py
    ├── tests\*
    │   └── test_example_project.py
    └── tox.ini

Top-level .rst files: CONTRIBUTING, CONTRIBUTORS, HISTORY, README\*
-------------------------------------------------------------------
These documents store important info about your project.

* **README.rst**:\* This is usually the first document users will look at. It will show up in the main page of your GitHub repository. Be sure to include the essential info about your package, including how to install and use it (or at least direct them to other documentation with this info).

* **CONTRIBUTING.rst**: Contains guidelines for others who want to contribute code or documentation to your project. The template has some basic, common sense guidelines to start out. Feel free to modify or add to them, but be welcoming to new contributors! Their work can help improve your project.

* **CONTRIBUTORS.rst**: List of contributors to your project. Starts with just you. As others contribute, you should credit them here.

* **HISTORY.rst**: Use this to track changes to your package as you release new versions. 

docs/\*
-------
Documentation files that will be used to build your ReadTheDocs website.

* **usage.rst**\*: Instructions for how to use your package. Starts with the barebones: how to import your package. You should build on it as you add functionality to your package. Be sure to include examples for all the major functions in your package.

* **conf.py**, **make.bat**, and **Makefile** are there to help ReadTheDocs build your documentation. They don't need modification, at least not at first.

* Some of the .rst files share names with the top-level .rst files we just discussed (e.g. docs/readme.rst and README.rst). These files just point to the top-level .rst files. The rest have their own content

* **index.rst**: The index file for your documentation. Only change this if you add new files to your docs/ directory.

* **installation.rst**: Installation instructions. Starts with a basic outline for installing from github or PyPI (once your project is released there).

LICENSE
-------
A text file containing the software license you selected in the cookiecutter prompts. This describes the legal terms of use, distribution, and modification of your package. You shouldn't have to touch this file, but if you would like to use a different open source license than the options in the set up you can replace the LICENSE file with the text of your chosen license.

Makefile and MANIFEST.in
------------------------
You shouldn't have to modify either of these files.

* **Makefile**: Includes instructions for make to perform various setup/testing tasks. For example, running "make test" with run through your package's testing suite.

* **MANIFEST.in**: Defines the list of files to include in the release distribution of your package.

example_project/\*
------------------
The actual code for your Python package. Comes with a single main module template file. If your package is contained within a single file, copy and paste it into this template. Otherwise, you can add more files as needed.

* **example_project.py**: Template main module file for your package. Contains two very basic example functions: sum_numbers and max_number. These are used for example tests (more on that in a minute).

* **__init__.py**: This file tells Python to treat the directory as containing a package. It also has some basic metadata (author, email, version #). You don't have to modify anything here. 

tests/
------
Contains your testing files. These files provide functions that test that your module's functions are producing the expected results. pytest automatically discovers files starting with "test\_" and runs the functions prefixed by "test\_". An example file is included:

* **test_example_project.py**: Includes two example tests: test_sum_numbers and test_max_number. These check that the functions are returning the expected results. The "generate_numbers" pytest fixture generates a list of random numbers for the tests. As you add your code to the project, be sure to replace these examples with tests for all the major functions and methods in your package.

requirements_dev.txt, setup.py, and setup.cfg
---------------------------------------------
Files to facilitate installing your package.

* **requirements_dev.txt**: List of Python packages required for working on developing your package.Includes the version numbers. If you add more dependencies to your package, be sure to add them here as well. All of these packages can be installed at once:

.. code-block::bash

    pip install -r requirements_dev.txt

* **setup.py**: Allows users to install your package from the commandline: "python setup.py install". You should not have to modify this at all. 

* **setup.cfg**: Contains extra configuration options for setup.py. 

tox.ini
-------
Config file for tox_. tox runs your tests on several versions of Python. The default is 2.7, 3.4, 3.5, and 3.6. If your package is only Python3 compatible, you can remove 2.7 from this config file. Otherwise, you can leave this file as-is. Notice that tox calls pytest for each version of Python. 

.. _tox: https://tox.readthedocs.io/en/latest/

.travis.yml
-----------
Configuration file for `Travis CI`_. Travis builds and tests your package each time you commit to GitHub. This makes it a lot easier to guard against changes that break your package. This .yml file tells Travis how to install and test your package. It even includes the option for Travis to automatically deploy your package to PyPI when you commit a new version of your package. To start with, you can ignore that part. When you are ready to publish your package on PyPI, you can add your encrypted PyPI password to this config file and Travis will automatically release new versions to PyPI. We have instructions for setting up Travis and PyPI here_.

.. _`Travis CI`: https://travis-ci.org/
.. _here: https://cookiecutter-pyopensci.readthedocs.io/en/latest/travis_pypi_setup.html

.gitignore and .editorconfig
----------------------------
These simple files make working on your package easier. You shouldn't need to modify them.

* **.gitignore**: Tells git which files and patterns to exclude from tracking. If you do "git add .", git will add all files and directories EXCEPT those that match patterns in .gitignore. 

* **.editorconfig**: Specifies text editor options like tabs vs. spaces, trailing whitespace handling, etc. editorconfig allows you to specify these options at the project level and distribute them to contributors. You probably don't have to use it: many code editors will already adopt the typical standards for Python. Not all editors come with support for .editorconfig files built in, but most have a plugin you can install. Read more: http://editorconfig.org
