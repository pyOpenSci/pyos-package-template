# Contributing to the pyOpenSci Python package template

To work on the template locally, you can call the copier template directly. Note that by default, `copier` uses the latest tag in your commit history. To ensure it uses the latest commit on your current active branch use:

`copier copy -r HEAD /path/to/your/template destination-dir`

If you want to test it against the latest tag in your local commit history, you can use:

`copier copy /path/to/your/template destination-dir`

## Run the tests

You can use Hatch to run all of the tests for the template:

`hatch run test:run`
