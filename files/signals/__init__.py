from django.db.models.signals import post_save
from django.apps import apps

from .uploaded_file import post_save_uploaded_file


def setup_signals():
    UploadedFile = apps.get_model(
        app_label='files', model_name='UploadedFile')

    post_save.connect(post_save_uploaded_file, sender=UploadedFile)
