import factory
from factory import django, fuzzy
from faker import Faker

from ..conf import settings
from ..models import UploadedFile

faker = Faker(settings.FAKER_SETTINGS_LOCALE)


class FakeUploadedFileFactory(django.DjangoModelFactory):

    class Meta:
        model = UploadedFile

    status = fuzzy.FuzzyChoice(
        [x[0] for x in settings.FILES_UPLOADED_FILE_STATUS_CH],
    )
    filename = factory.LazyAttribute(lambda x: faker.word())
    mimetype = factory.LazyAttribute(lambda x: faker.mime_type())
