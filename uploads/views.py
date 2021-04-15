from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ModelFormWithFileField
from celery.result import AsyncResult

from .models import FileUpload
from .tasks import some_task

def uploads_page(request):
    form = ModelFormWithFileField(data=request.POST or None, files=request.FILES or None)
    audiofiles = FileUpload.objects.all()
    if request.method == "POST":
        if form.is_valid():
            task = some_task.delay()
            obj = form.save(commit=False)
            obj.task_id = task.id
            obj.status = task.status
            obj.save()

            context = {
                'form': ModelFormWithFileField(),
                'message': 'Upload completed',
                'audiofiles': audiofiles,
            }

            return render(request, "upload_page.html", context=context)
    return render(request, "upload_page.html", context={'form': form, 'audiofiles': audiofiles})

def ajax_delete(request):
    track_id = int(request.POST.get('track_id'))
    FileUpload.objects.get(id=track_id).delete()
    return JsonResponse({'message': 'success'})

def ajax_update(request):
    task_id = request.POST.get('task_id')
    status = request.POST.get('status')
    FileUpload.objects.filter(task_id=task_id).update(status=status)
    return JsonResponse({'message': 'success'})

def ajax_get_progress(request, task_id):
    result = AsyncResult(task_id)
    response_data = {
        'state': result.state,
        'result': result.info,
    }
    return JsonResponse(response_data)
