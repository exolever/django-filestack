from django.conf import settings

from rest_framework import serializers

from ...models import UploadedFile
from .uploaded_file_version import UploadedFileVersionSerializer
from .uploaded_file_reverse import UploadedFileRelatedGenericSerializer


class UploadedFileToRepresentationMix:

    def to_representation(self, obj):
        return UploadedFileRelatedGenericSerializer(obj).data


class UploadedFileSerializer(
        UploadedFileToRepresentationMix,
        serializers.ModelSerializer):

    filestack_status = serializers.ChoiceField(
        choices=settings.FILES_UPLOADED_FILE_STATUS_CH)
    filename = serializers.CharField()
    mimetype = serializers.CharField()
    url = serializers.URLField()

    class Meta:
        model = UploadedFile
        fields = ['filestack_status', 'filename', 'mimetype', 'url']

    def create(self, validated_data):
        return UploadedFile.create(
            self.context.get('request').user,
            validated_data.get('filename'),
            validated_data.get('mimetype'),
            validated_data.get('url'),
            validated_data.get('filestack_status'),
            validated_data.get('related_to'))


class UploadedFileUpdateSerializer(
        UploadedFileToRepresentationMix,
        serializers.ModelSerializer):

    filestack_status = serializers.ChoiceField(
        choices=settings.FILES_UPLOADED_FILE_STATUS_CH)
    url = serializers.URLField()

    class Meta:
        model = UploadedFile
        fields = ['filestack_status', 'url']


class UploadedFileVersionsSerializer(
        UploadedFileToRepresentationMix,
        serializers.ModelSerializer):

    versions = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ['filename', 'filename_slug', 'url', 'version', 'versions']

    def get_versions(self, obj):
        return UploadedFileVersionSerializer(
            obj.versions.all(),
            many=True,
        ).data

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['versions'] = self.get_versions(obj)

        return data


class UploadedFileVisibilitySerializer(serializers.ModelSerializer):
    visibility = serializers.CharField(source='get_visibility_code', read_only=True)

    class Meta:
        model = UploadedFile
        fields = ['visibility']

    def validate(self, attrs):
        user_from = self.context.get('request').user
        instance = self.context.get('view').get_object()
        assignment_step = instance.related
        version = instance.latest
        assignment_step.can_update_uploaded_file(user_from, version, raise_exception=True)
        return attrs

    def update(self, instance, validated_data):
        instance.toggle_visibility()
        return instance
