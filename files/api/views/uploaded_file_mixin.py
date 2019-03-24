from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from ...exceptions import UploadFileException


class UploadedFileViewMixin:

    def validate_uploaded_file(self, serializer, raise_exception=True, **kwargs):
        class_name = self.kwargs.get('class_name')
        object_id = self.kwargs.get('object_id')

        try:
            RelatedClass = ContentType.objects.get(model__iexact=class_name)

        except ContentType.DoesNotExist:
            raise UploadFileException(
                '{} is not a valid Object'.format(
                    class_name))

        try:
            related_instance = RelatedClass.get_object_for_this_type(
                pk=object_id)

        except ObjectDoesNotExist:
            raise UploadFileException(
                '{} instance with #id {} does not exist.'.format(
                    RelatedClass.name,
                    object_id,
                )
            )

        if not hasattr(related_instance, 'uploaded_files'):
            raise UploadFileException(
                '{} can not be linked with files'.format(
                    RelatedClass.name))

        return related_instance
