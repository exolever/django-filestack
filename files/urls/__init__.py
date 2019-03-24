from django.conf.urls import url

app_name = 'files'

from ..views import uploaded_file

urlpatterns = [
    url(
        r'^versioned/(?P<hash>.*)$',
        uploaded_file.UploadedFileDownload.as_view(),
        name='versioned-download',
    ),
]
