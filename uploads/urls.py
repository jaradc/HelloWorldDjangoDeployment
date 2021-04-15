from django.urls import path
from .views import uploads_page, ajax_delete, ajax_get_progress

app_name = "uploads"
urlpatterns = [
    path('', uploads_page, name='uploads'),
    path('ajax/delete/', ajax_delete, name='ajax_delete'),
    path('ajax/get-progress/<task_id>/', ajax_get_progress, name='get_progress'),
]

