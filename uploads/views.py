from django.shortcuts import render, redirect
from .forms import ModelFormWithFileField


def uploads_page(request):
    form = ModelFormWithFileField(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, "upload_page.html", context={'form': ModelFormWithFileField(), 'message': 'Upload completed'})
    return render(request, "upload_page.html", context={'form': form})

