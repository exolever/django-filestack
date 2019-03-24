=====
Usage
=====

To use Django Filestack in a project, add it to your `INSTALLED_APPS`:

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
