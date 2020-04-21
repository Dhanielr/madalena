from django.conf import settings
from .utils import random_chars

# Extra libs
import os
from PIL import Image
from resizeimage import resizeimage
from celery import shared_task
from time import sleep

@shared_task
def sleepy_test(duration):
    sleep(duration)
    return None

@shared_task
def resizer(data):
    image = data['image']
    width = data['width']
    height = data['height']
    crop = data['crop']

    image_name = image.split('/')[-1]
    save_path = f'{settings.RESIZER_RESULT_PATH}/{image_name}'

    if crop:
        with Image.open(image) as img:
            resizer = resizeimage.resize_cover(img, [width, height])
            if os.path.exists(save_path):
                save_path = f'{settings.RESIZER_RESULT_PATH}/{random_chars(7)}-{image_name}'
            resizer.save(save_path, img.format)
    else:
        with Image.open(image) as img:
            resizer = img.resize((width, height), Image.ANTIALIAS)
            if os.path.exists(save_path):
                save_path = f'{settings.RESIZER_RESULT_PATH}/{random_chars(7)}-{image_name}'
            resizer.save(save_path, format=img.format)

    return 'Imagem redimensionada com sucesso.', True



