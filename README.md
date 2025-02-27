# pyOpenSci Python Package Template
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14052273.svg)](https://doi.org/10.5281/zenodo.14052273)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)

> A Python package template that supports the pyOpenSci
> pure [Python packaging tutorial](https://www.pyopensci.org/python-package-guide/tutorials/intro.html).
This template can be used with [copier](https://copier.readthedocs.io) to initialize a
new Python package project structure following the practices outlined in the pyOpenSci
tutorial.

## Get started

To use this template:

1. Install copier using [pipx](https://pipx.pypa.io/stable/) or pip preferably with a [virtual environment](https://www.pyopensci.org/python-package-guide/CONTRIBUTING.html#create-a-virtual-environment).

    Global Installation:
    
    ```console
    pipx install copier
    ```
   
    or Environment specific installation:

    ```console
    pip install copier
    ```

2. Run the below copier command. Please note that copier creates a target directory if
   it doesn't exist yet. It will also **create and possibly overwrite files in the given
   directory, even if it already exists!** That includes your current directory if that
   is your target.

    ```console
    copier copy gh:pyopensci/pyos-package-template path/here
    ```
    
   The command below will create the package directory in your current working directory. 
    ```console
    copier copy gh:pyopensci/pyos-package-template .
    ```

   Used in the above way, copier will use the latest tagged release, which is probably
   the safest option. You can provide an option `--vcs-ref` to choose specific branches
   as your source. You can read more about generating your project
   in the [copier documentation](https://copier.readthedocs.io/en/stable/generating/).


## Run the template workflow

Once you have installed copier, you are ready to create your Python package template. 
First, run the command below from your favorite shell. Note that this is copying our template from GitHub so it 
will require internet access to run properly.

The command below will create the package directory in your current working directory. 

`copier copy gh:pyopensci/pyos-package-template .`

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

### Stay up-to-date

The community will likely continue to develop this template. If at any point, you want
to adopt those changes for your project, you can update it. Read more about that process
in the [copier documentation](https://copier.readthedocs.io/en/stable/updating/).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Midnighter"><img src="https://avatars.githubusercontent.com/u/135653?v=4?s=100" width="100px;" alt="Moritz E. Beber"/><br /><sub><b>Moritz E. Beber</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/commits?author=Midnighter" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3AMidnighter" title="Reviewed Pull Requests">👀</a> <a href="#ideas-Midnighter" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/steven-silvester-90318721/"><img src="https://avatars.githubusercontent.com/u/2096628?v=4?s=100" width="100px;" alt="Steven Silvester"/><br /><sub><b>Steven Silvester</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/commits?author=blink1073" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3Ablink1073" title="Reviewed Pull Requests">👀</a> <a href="#ideas-blink1073" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/commits?author=sneakers-the-rat" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3Asneakers-the-rat" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://blog.ucodery.com"><img src="https://avatars.githubusercontent.com/u/28751151?v=4?s=100" width="100px;" alt="Jeremy Paige"/><br /><sub><b>Jeremy Paige</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/commits?author=ucodery" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3Aucodery" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/commits?author=lwasser" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3Alwasser" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/agriyakhetarpal"><img src="https://avatars.githubusercontent.com/u/74401230?v=4?s=100" width="100px;" alt="Agriya Khetarpal"/><br /><sub><b>Agriya Khetarpal</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyos-package-template/pulls?q=is%3Apr+reviewed-by%3Aagriyakhetarpal" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
