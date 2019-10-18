import factory
from factory import django
from faker import Faker

from ..conf import settings
from ..models import UploadedFile

faker = Faker(settings.FAKER_SETTINGS_LOCALE)


class FakeUploadedFileFactory(django.DjangoModelFactory):

    class Meta:
        model = UploadedFile

    filename = factory.LazyAttribute(lambda x: faker.word())
    mimetype = factory.LazyAttribute(lambda x: faker.mime_type())

    @classmethod
    def create(cls, **kwargs):
        """Create an instance of the associated class, with overriden attrs."""
        visibility = kwargs.pop('visibility', [])

        instance = super().create(**kwargs)

        if visibility:
            visibility_related = instance.get_visibility_relation()
            visibility_related.visibility = visibility
            visibility_related.save(update_fields=['visibility'])

        return instance
