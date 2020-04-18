#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.add_conda_environment_file }}' == 'n':
        remove_file('environment.yml')
        remove_file('environment-dev.yml')

    if (
        '{{ cookiecutter.add_git_pre_commit_hook_isort }}' == 'n'
        and '{{ cookiecutter.add_git_pre_commit_hook_black }}' == 'n'
        and '{{ cookiecutter.add_git_pre_commit_hook_flake8 }}' == 'n'
        and '{{ cookiecutter.add_git_pre_commit_hook_mypy }}' == 'n'
    ):
        remove_file('.pre-commit-config.yaml')

    if '{{ cookiecutter.add_git_pre_commit_hook_black }}' == 'n':
        remove_file('pyproject.toml')
