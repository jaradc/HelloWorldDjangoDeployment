from celery import shared_task
from time import sleep
from .models import FileUpload

@shared_task(bind=True)
def some_task(self, seconds=20):
    print(f'Sleeping for {seconds} seconds.')
    sleep(seconds)
    print(f'Slept for {seconds} seconds.')
    return f"Sleep for {seconds} seconds complete!"
