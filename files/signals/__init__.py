from django.apps import apps
from django.db.models.signals import pre_delete

from .uploaded_file import pre_delete_uploaded_file


def setup_signals():

    UploadedFile = apps.get_model(
        app_label='files',
        model_name='UploadedFile',
    )

    pre_delete.connect(pre_delete_uploaded_file, sender=UploadedFile)
