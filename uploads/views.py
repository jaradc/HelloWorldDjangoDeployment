from django.shortcuts import render, redirect
from .forms import ModelFormWithFileField

from .models import FileUpload

def uploads_page(request):
    form = ModelFormWithFileField(data=request.POST or None, files=request.FILES or None)
    audiofiles = FileUpload.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            context = {
                'form': ModelFormWithFileField(),
                'message': 'Upload completed',
                'audiofiles': audiofiles,
            }
            return render(request, "upload_page.html", context=context)
    return render(request, "upload_page.html", context={'form': form, 'audiofiles': audiofiles})

