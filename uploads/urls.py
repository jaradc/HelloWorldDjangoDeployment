from django.urls import path
from .views import uploads_page, ajax_delete

app_name = "uploads"
urlpatterns = [
    path('', uploads_page, name='uploads'),
    path('ajax-delete/', ajax_delete, name='ajax_delete'),
]

