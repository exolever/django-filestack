import requests
import logging

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, Http404

from ..models import UploadedFileVersion
from ..exceptions import UploadFileException


logger = logging.getLogger('files')


class UploadedFileDownload(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        response = None
        uploaded_file_version = get_object_or_404(
            UploadedFileVersion,
            download_hash=kwargs.get('hash'),
        )

        if uploaded_file_version.can_view(request.user):
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename={}'.format(
                str(uploaded_file_version.filename),
            )
            try:
                filestack_hash = uploaded_file_version.filestack_hash
            except Exception as e:
                logger.error(
                    'Retrieving file {} <pk:{}> for user {}: {}'.format(
                        uploaded_file_version,
                        uploaded_file_version.pk,
                        request.user,
                        e,
                    )
                )
                raise UploadFileException(
                    'An unexpected error occurred retrieving the file')

            if settings.DEBUG:
                response.content = requests.get(
                    'https://{}/{}'.format(
                        settings.FILES_CDN_FILESTACK,
                        filestack_hash,
                    )
                )
            else:
                response['X-Accel-Redirect'] = '/{}/{}/{}'.format(
                    settings.INTERNAL_REDIRECT,
                    settings.FILES_CDN_FILESTACK,
                    filestack_hash,
                )

        else:
            raise Http404

        return response
