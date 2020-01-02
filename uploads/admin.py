from django.contrib import admin
from .models import FileUpload

# Register your models here.
class FileUploadAdmin(admin.ModelAdmin):
    fields = ('upload',)
    list_display = ['id', 'upload_at', 'upload']
    list_display_links = ['upload_at']


admin.site.register(FileUpload, FileUploadAdmin)
