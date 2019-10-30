from rest_framework import serializers

from django.conf import settings

from ...models import UploadedFile
from ...utils import factory


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
    created_by = serializers.SerializerMethodField()
    visibility = serializers.CharField(source='get_visibility_code')
    can_change_visibility = serializers.SerializerMethodField()

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
            'mimetype',
            'created_by',
            'visibility',
            'can_change_visibility',
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

    def get_can_change_visibility(self, obj):
        user_from = self.context.get('request').user
        return obj.can_change_visibility(user_from)

    def get_created_by(self, obj):
        class_name = settings.FILES_USER_SERIALIZER
        user_serializer = factory(class_name, instance=obj.created_by, context=self.context)
        return user_serializer.data
