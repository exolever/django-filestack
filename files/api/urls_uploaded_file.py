from django.conf.urls import url

from .views import uploaded_file


urlpatterns = [
    url(r'upload-file/(?P<class_name>[a-z]+)/(?P<object_id>\d+)/$',
        uploaded_file.UploadedFileCreateView.as_view(),
        name='add'),
    url(r'upload-file/(?P<class_name>[a-z]+)/(?P<object_id>\d+)/(?P<pk>\d+)/$',
        uploaded_file.UploadedFileDeleteUpdateView.as_view(),
        name='update-delete'),
    url(r'upload-file/(?P<class_name>[a-z]+)/(?P<object_id>\d+)/(?P<pk>\d+)/(?P<version>\d+)/$',
        uploaded_file.UploadedFileVersionDeleteView.as_view(),
        name='version-delete'),
    url(r'(?P<pk>\d+)/$', uploaded_file.UploadedFileRetrieveView.as_view(),
        name='retrieve'),
]
