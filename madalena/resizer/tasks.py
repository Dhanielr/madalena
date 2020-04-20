from celery import shared_task
from time import sleep

@shared_task
def sleepy_test(duration):
    sleep(duration)
    return None