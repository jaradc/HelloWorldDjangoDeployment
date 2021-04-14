from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ModelFormWithFileField

from .models import FileUpload
from .tasks import some_task

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
            some_task.delay()
            return render(request, "upload_page.html", context=context)
    return render(request, "upload_page.html", context={'form': form, 'audiofiles': audiofiles})

def ajax_delete(request):
    track_id = int(request.POST.get('track_id'))
    FileUpload.objects.get(id=track_id).delete()
    return JsonResponse({'message': 'success'})
