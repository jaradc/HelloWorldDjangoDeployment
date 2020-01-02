from django.db import models

# Create your models here.
class FileUpload(models.Model):
    upload_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to="music")

    def __str__(self):
        return self.upload.name

# TODO: https://docs.djangoproject.com/en/3.0/ref/signals/#django.db.models.signals.pre_delete
# Add pre_delete or post_delete
