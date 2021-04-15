from django.db import models
from django_celery_results.models import TaskResult

# Create your models here.
class FileUpload(models.Model):
    upload_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to="music")
    task_id = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="CHECKING")

    def __str__(self):
        return self.upload.name

    class Meta:
        ordering = ['-upload_at']

# TODO: https://docs.djangoproject.com/en/3.0/ref/signals/#django.db.models.signals.pre_delete
# Add pre_delete or post_delete
