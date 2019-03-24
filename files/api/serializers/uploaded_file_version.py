from rest_framework import serializers

from ...models import UploadedFileVersion


class UploadedFileVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFileVersion
        fields = ['version', 'url']
