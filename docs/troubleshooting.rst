.. _troubleshooting:

===============
Troubleshooting
===============

.. note:: Can you help improve this file? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/pyOpenSci/cookiecutter-pyopensci/blob/master/docs/troubleshooting.rst


Windows Issues
--------------

* Some people have reported issues using git bash; try using the
Command Terminal instead.

* If you're on Windows 10, you may also want to try `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/about>`_, which allows you to run a linux command line from within Windows. It is still somewhat experimental, but is useful for developing and testing code written in linux.

* Virtual environments can sometimes be tricky on Windows. If you
have Python 3.5 or above installed (recommended), this should get
you a virtualenv named ``myenv`` created inside the current folder:

.. code-block:: powershell

    > c:\Python35\python -m venv myenv

Or:

.. code-block:: powershell

    > c:\Python35\python c:\Python35\Tools\Scripts\pyvenv.py myenv

* Some people have reported that they have to re-activate their
virtualenv whenever they change directory, so you should remember
the path to the virtualenv in case you need it.
