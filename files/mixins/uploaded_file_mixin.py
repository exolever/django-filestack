from django.contrib.contenttypes.models import ContentType

from genericm2m.models import RelatedObjectsDescriptor


class UploadedFileMixin:

    _related = RelatedObjectsDescriptor()

    @property
    def uploaded_files(self):
        uploaded_file_ct = ContentType.objects.get(
            app_label='files',
            model='uploadedfile')
        return self._related.related_to().filter(
            parent_type=uploaded_file_ct).generic_objects()

    def can_upload_files(self, user, raise_exception=True):
        raise NotImplementedError

    def can_view_uploaded_file(self, user, raise_exception=True):
        raise NotImplementedError

    def can_update_uploaded_file(self, user, uploaded_file_version, raise_exception=True):
        raise NotImplementedError

    def can_delete_uploaded_file(self, user, uploaded_file, raise_exception=True):
        raise NotImplementedError
