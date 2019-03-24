from django.db import models
from django.conf import settings
from django.urls import reverse

from model_utils.models import TimeStampedModel

from utils.models import CreatedByMixin


class UploadedFileVersion(CreatedByMixin, TimeStampedModel):

    uploaded_file = models.ForeignKey(
        'UploadedFile',
        on_delete=models.CASCADE,
        related_name='versions')
    version = models.IntegerField(default=1)
    download_hash = models.CharField(
        max_length=255,
        unique=True,
    )

    filestack_status = models.CharField(
        max_length=20,
        choices=settings.FILES_UPLOADED_FILE_STATUS_CH,
        default=settings.FILES_UPLOADED_FILE_STATUS_ACTIVE)
    filestack_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'UploadedFile version'
        verbose_name_plural = 'UploadedFile versions'
        ordering = ['-version']

    def __str__(self):
        return 'v.{}'.format(self.version)

    @property
    def filename(self):
        return self.uploaded_file.filename_sanitized

    @property
    def url(self):
        return '{}{}'.format(
            settings.ROOT,
            reverse(
                'files:versioned-download',
                kwargs={'hash': self.download_hash},
            )
        )

    @property
    def filestack_hash(self):
        return self.filestack_url.split(
            '{}/'.format(settings.FILES_CDN_FILESTACK))[1]

    def can_view(self, user, raise_exception=True):
        can_view = False
        try:
            can_view = self.uploaded_file._can_view_uploaded_file(
                user, raise_exception)
        except Exception as e:
            if raise_exception:
                raise e

        return can_view

    def can_update(self, user, raise_exception=True):
        can_update = False
        try:
            can_update = self.uploaded_file._can_update_uploaded_file(
                user, raise_exception)
        except Exception as e:
            if raise_exception:
                raise e

        return can_update

    def can_delete(self, user, raise_exception=True):
        can_delete = False
        try:
            can_delete = self.uploaded_file._can_delete_uploaded_file(
                user, raise_exception)
        except Exception as e:
            if raise_exception:
                raise e

        return can_delete
