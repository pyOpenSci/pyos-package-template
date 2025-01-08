# pyOpenSci Package Template

> A Python package template that supports the pyOpenSci
> pure [Python packaging tutorial](https://www.pyopensci.org/python-package-guide/tutorials/intro.html).
This template can be used with [copier](https://copier.readthedocs.io) to initialize a
new Python package project structure following the practices outlined in the pyOpenSci
tutorial.

## How to use this template

To begin install copier. You can either use pipx to install copier globally if you are a pipx user or you can install it into a local Python envirnment using pip.

Local installation:

`pip install copier`

Global installation:

`pipx install copier`

## Run the template workflow

Once you have installed copier, you are ready to create your Python package template. 
First, cun the command below from your favorite shell. Note that this is copying our template from GitHub so it 
will require internet access to run properly.

The command below will create the package directory in your current working directory. 

`copier copy gh:pyopensci/pyos-package-template . `

If you wish to create the package directory in another directory you can specify it like this:

`copier copy gh:pyopensci/pyos-package-template dirname-here`

## Template overview
The copier template will ask you a series of questions which you can respond to. The questions will 
help you customize the template. 

Below is what the template workflow will look like when you run it. In the example below, you  
"fully customize" the template.  


```console
➜ copier copy gh:pyopensci/pyos-package-template .      
🎤 Who is the copyright holder, for example, yourself or your organization? Used in the license
   pyos
🎤 Who is the author of the package to be? Used in the package description.
   pyos
🎤 The author's email address. Used in the package description.
   youremail@youremail.com
🎤 What is the name of the project? Used as the title in the README.md and other places.
   mypkg
🎤 Please provide a short description for the package.
    (Finish with 'Alt+Enter' or 'Esc then Enter')
> description here
🎤 Do you want to skip all remaining questions and simply use the provided default values?
   No, I want to fully customize the template.
🎤 What is the project slug? Used in hyperlinks.
   mypkg
🎤 What is the Python package name? Used as the name of the package and the top-level import.
   mypkg
🎤 Do you want to use dynamic versioning of your package or static? Dynamic means that versions
   No
🎤 Do you want to use git with a development platform, like GitHub or GitLab?
   Yes
🎤 Which development platform are you planning to use? Used to generate certain documentation an
   GitHub
🎤 Your or your organization's username on GitHub. Used to generate certain documentation and hy
   pyopensci
🎤 Do you want to include documentation for your project and which framework do you want to use?
   Sphinx (https://www.pyopensci.org/pyos-sphinx-theme)
🎤 Do you want to use hatch environments for running isolated commands like linting, building do
   Yes
🎤 Do you want to lint your code and generally check the formatting of your files?
   Yes
🎤 Do you want to use typing annotations and type check your code?
   No
🎤 Do you want to test your code? Generally, we strongly recommend that you do, but for a quick
   Yes
🎤 Which license do you want to use? Used in the license file.
   MIT
🎤 What is the starting year of the project? Used in copyright statements.
   2024
```






