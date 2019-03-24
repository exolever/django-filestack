

class UploadedFilePermissionMixin:

    def check_user_perms(self, user, perms=[], raise_exception=True):
        return self._can_upload_files(user, raise_exception)

    def _can_upload_files(self, user, raise_exception=True):
        return self.related.can_upload_files(user, raise_exception)

    def _can_view_uploaded_file(self, user, raise_exception=True):
        return self.related.can_view_uploaded_file(user, raise_exception)

    def _can_update_uploaded_file(self, user, raise_exception=True):
        return self.related.can_update_uploaded_file(user, raise_exception)

    def _can_delete_uploaded_file(self, user, raise_exception=True):
        return self.related.can_delete_uploaded_file(user, raise_exception)
