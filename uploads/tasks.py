from celery import shared_task
from time import sleep

@shared_task(bind=True)
def some_task(self, seconds=2):
    print(f'Sleeping for {seconds} seconds.')
    sleep(seconds)
    print(f'Slept for {seconds} seconds.')
    return f"Sleep for {seconds} seconds complete!"
