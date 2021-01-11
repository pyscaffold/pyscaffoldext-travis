.. image:: https://api.cirrus-ci.com/github/pyscaffold/pyscaffoldext-travis.svg?branch=main
    :alt: Built Status
    :target: https://cirrus-ci.com/github/pyscaffold/pyscaffoldext-travis
.. image:: https://readthedocs.org/projects/pyscaffoldext-travis/badge/?version=latest
    :alt: ReadTheDocs
    :target: https://pyscaffoldext-travis.readthedocs.io/
.. image:: https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-travis/main.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/pyscaffold/pyscaffoldext-travis
.. image:: https://img.shields.io/pypi/v/pyscaffoldext-travis.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/pyscaffoldext-travis/
.. image:: https://pepy.tech/badge/pyscaffoldext-travis/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/pyscaffoldext-travis

====================
pyscaffoldext-travis
====================


    Configure your `PyScaffold`-generated project to work with `Travis CI`_.


`PyScaffold`_ is a development tool focused in creating distributable Python packages.
This extension automatically configures the generated packages to use `Travis CI`_,
a very popular and mature `continuous integration`_ solution that allows devs to
test their code and perform a series of automated tasks, bringing confidence to
their workflow.

    **LOOKING FOR CONTRIBUTORS** - If you use PyScaffold or Travis CI and would
    like to help us as a contributor (or even as one of the maintainers) for
    this extension, please send us an email or open an issue, we would love to
    have you on board.


Quickstart
==========

This extension can be directly installed with ``pip``:

.. code-block:: bash

    pip install pyscaffoldext-travis

Or, if you prefer ``pipx``:

.. code-block:: shell

    pipx install pyscaffold  # if you haven't installed pyscaffold yet
    pipx inject pyscaffold pyscaffoldext-travis

Note that, after the installation, ``putup -h`` will show a new option
``--travis``. Use this option to indicate when you are want to create a
package with automated tasks running on the `Travis CI`_ platgorm.
For example:

.. code-block:: shell

    putup --travis myapp

Please refer to `Travis' docs`_ to get started.

.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

     pip install pre-commit
     cd pyscaffoldext-travis
     pre-commit install

It is a good idea to update the hooks to the latest version::

     pre-commit autoupdate

Please also check PyScaffold's `contribution guidelines`_.

Note
====

This project has been set up using PyScaffold 4.0b1. For details and usage
information on PyScaffold see https://pyscaffold.org/.


.. _PyScaffold: https://pyscaffold.org
.. _Travis CI: https://travis-ci.com
.. _pre-commit: http://pre-commit.com/
.. _continuous integration: https://en.wikipedia.org/wiki/Continuous_integration
.. _Travis' docs: https://docs.travis-ci.com
.. _contribution guidelines: https://pyscaffold.org/en/latest/contributing.html
