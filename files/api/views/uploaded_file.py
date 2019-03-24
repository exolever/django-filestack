from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from rest_framework.permissions import IsAuthenticated

from ...models import UploadedFile, UploadedFileVersion
from ..serializers import (
    UploadedFileSerializer,
    UploadedFileVersionsSerializer,
    UploadedFileUpdateSerializer,
)
from .uploaded_file_mixin import UploadedFileViewMixin


class UploadedFileRetrieveView(RetrieveAPIView):
    """
    Retrieve `UploadedFile` data with all existing versions
    """

    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileVersionsSerializer
    permission_classes = (IsAuthenticated,)


class UploadedFileCreateView(UploadedFileViewMixin, CreateAPIView):
    """
    Creates a new `UploadedFile` associated to the <related_to_class> object
    for this pk and create a new `UploadedFileVersion` for it.
    """
    model = UploadedFile
    serializer_class = UploadedFileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        related_instance = self.validate_uploaded_file(serializer, self.kwargs)

        filestack_url = serializer.validated_data.pop('url')
        filestack_status = serializer.validated_data.pop('filestack_status')
        instance = serializer.save()

        instance.create_version(
            url=filestack_url,
            status=filestack_status,
            user=self.request.user,
            related_to=related_instance,
        )
        instance.link_file(related_instance)


class UploadedFileDeleteUpdateView(
        UploadedFileViewMixin,
        DestroyAPIView,
        UpdateAPIView):
    """
    Delete a `UploadedFile` instance with all existing `UploadedFileVersion`.\n
    Update a `UploadedFile` instance creating a new `UploadedFileVersion`.
    """
    model = UploadedFile
    serializer_class = UploadedFileUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.model.objects.all()

    def perform_update(self, serializer):
        self.validate_uploaded_file(serializer, self.kwargs)
        filestack_url = serializer.validated_data.pop('url')
        filestack_status = serializer.validated_data.pop('filestack_status')
        instance = self.get_object()
        instance.create_version(
            url=filestack_url,
            status=filestack_status,
            user=self.request.user,
        )


class UploadedFileVersionDeleteView(DestroyAPIView):
    """
    Delete a `UploadedFileVersion` for a concrete `UploadedFile` instance
    """

    model = UploadedFileVersion
    permission_classes = (IsAuthenticated, )
    lookup_field = 'version'

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self):
        uploaded_file = get_object_or_404(
            UploadedFile.objects.all(),
            **{'pk': self.kwargs.get('pk')}
        )
        uploaded_file_version = get_object_or_404(
            uploaded_file.versions.all(),
            **{self.lookup_field: self.kwargs.get(self.lookup_field)}
        )
        self.check_object_permissions(self.request, uploaded_file_version)

        return uploaded_file_version
