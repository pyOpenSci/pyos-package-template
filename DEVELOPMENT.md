# Development Guide

If you are working on development locally and on the main branch, you can run the template
using the following command:

`copier copy .  dirnam_here`

If you have made local changes to the template, you will see a warning
telling you that the template's current version control state is "dirty".
This means that you have changed things and they aren't committed  to
version control, yet.

```console
/your/path/python3.12/site-packages/copier/vcs.py:201: DirtyLocalWarning: Dirty template changes included automatically.
```

If you are working on a branch, then you need to use the `--vcs-ref`
flag to tell copier to use the template from that branch.

`copier copy . dir-name-here --vcs-ref branch-name-here`

## Linting & code style

The test suite for our template uses a hatch environment to check for
style issues.

## Customizing the template

We use [copier](https://copier.readthedocs.io/en/stable/) to manage the
template. The `copier.yml` file is the main configuration file for the template.
