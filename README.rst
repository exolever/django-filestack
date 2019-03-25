=============================
Django Filestack
=============================

.. image:: https://badge.fury.io/py/django-filestack.svg
    :target: https://badge.fury.io/py/django-filestack

.. image:: https://requires.io/github/exolever/django-filestack/requirements.svg?branch=master
     :target: https://requires.io/github/exolever/django-filestack/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://travis-ci.org/exolever/django-filestack.svg?branch=master
    :target: https://travis-ci.org/exolever/django-filestack

.. image:: https://codecov.io/gh/exolever/django-filestack/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/exolever/django-filestack

.. image:: https://sonarcloud.io/api/project_badges/measure?project=exolever_django-filestack&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=exolever_django-filestack

Add Model support for Filestack files

Documentation
-------------

The full documentation is at https://django-filestack.readthedocs.io.

Quickstart
----------

Install Django Filestack::

    pip install django-filestack

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'files.apps.FilesConfig',
        ...
    )

Add Django Filestack's URL patterns:

.. code-block:: python

    from files import urls as files_urls


    urlpatterns = [
        ...
        url(r'^', include(files_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
