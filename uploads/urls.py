from django.urls import path
from .views import uploads_page

urlpatterns = [
    path('', uploads_page, name='uploads'),
]

