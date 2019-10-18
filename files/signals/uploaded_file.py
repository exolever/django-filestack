def post_save_uploaded_file(sender, instance, created, *args, **kwargs):
    if created:
        instance.create_visibility_relation()
