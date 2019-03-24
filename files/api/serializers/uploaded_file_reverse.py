from rest_framework import serializers

from ...models import UploadedFile


class UploadedFileGenericReverseSerializerMixin(serializers.Serializer):

    uploadedFile = serializers.SerializerMethodField()

    def get_uploadedFile(self, obj):
        return UploadedFileRelatedGenericSerializer(obj).data


class UploadedFileReverseSerializerMixin(serializers.Serializer):

    uploadedFile = serializers.SerializerMethodField()

    def get_uploadedFile(self, obj):
        return UploadedFileRelatedSerializer(obj).data


class UploadedFileRelatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ['filename', 'mimetype', 'url', 'version']


class UploadedFileRelatedGenericSerializer(serializers.ModelSerializer):

    type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    iframe = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    order = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = [
            'pk',
            'type',
            'status',
            'name',
            'description',
            'thumbnail',
            'iframe',
            'link',
            'order',
        ]

    def get_type(self, obj):
        return obj.file_mimetype

    def get_status(self, obj):
        return obj.latest.filestack_status

    def get_name(self, obj):
        return obj.filename

    def get_description(self, obj):
        return ''

    def get_thumbnail(self, obj):
        return ''

    def get_iframe(self, obj):
        return ''

    def get_link(self, obj):
        return obj.url

    def get_order(self, obj):
        return ''
