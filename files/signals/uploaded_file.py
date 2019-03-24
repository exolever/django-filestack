
def pre_delete_uploaded_file(sender, instance, *args, **kwargs):
    instance._related.clear()
