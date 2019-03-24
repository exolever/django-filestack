class UploadedFileMixin:

    @property
    def uploaded_files(self):
        return self.files.all()

    def can_upload_files(self, user, raise_exception=True):
        raise NotImplementedError

    def can_view_uploaded_file(self, user, raise_exception=True):
        raise NotImplementedError

    def can_update_uploaded_file(self, user, uploaded_file_version, raise_exception=True):
        raise NotImplementedError

    def can_delete_uploaded_file(self, user, uploaded_file, raise_exception=True):
        raise NotImplementedError
