from django import forms
from .models import FileUpload

class ModelFormWithFileField(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ['upload']
