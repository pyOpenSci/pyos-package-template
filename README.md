# pyOpenSci Package Template
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!