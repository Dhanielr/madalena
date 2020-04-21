from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import ResultImage
from madalena.celery import app

# Extra libs
from io import BytesIO
from PIL import Image
from resizeimage import resizeimage
from celery import shared_task, Task
from time import sleep

@shared_task
def sleepy_test(duration):
    sleep(duration)
    return None

class ResizeImageTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    def run(self, *args, **kwargs):
        self.start_resizer(*args, **kwargs)

    def resizer(self, instance):
        image = f'{settings.MEDIA_ROOT}/{instance.image}'
        width = instance.width
        height = instance.height
        crop = instance.crop
        buffer = BytesIO()

        if crop:
            with Image.open(image) as img:
                resizer = resizeimage.resize_cover(img, [width, height])
                resizer.save(buffer, img.format)
        else:
            with Image.open(image) as img:
                resizer = img.resize((width, height), Image.ANTIALIAS)
                resizer.save(fp=buffer, format=img.format)
    
        return ContentFile(buffer.getvalue())


    def start_resizer(self, instance):
        img_name = f'{instance.image}'.split('/')[-1]
        image_resized = self.resizer(instance)
        
        result_image_model = ResultImage()
        
        result_image_model.entry_image = instance
        result_image_model.image.save(img_name, InMemoryUploadedFile(
            image_resized,
            None,
            img_name,
            'image',
            image_resized.tell,
            None)
        )
# @app.task
# def resize_image_task(instance):
#      task = ResizeImageTask()
#      task.run(instance)
#      return None

# resize_image_task = app.tasks.register(ResizeImageTask())
resize_image_task = app.register_task(ResizeImageTask())

# ####### Function Based Tasks

# def resizer(self, instance):
#     image = f'{settings.MEDIA_ROOT}/{instance.image}'
#     width = instance.width
#     height = instance.height
#     crop = instance.crop
#     buffer = BytesIO()

#     if crop:
#         with Image.open(image) as img:
#             resizer = resizeimage.resize_cover(img, [width, height])
#             resizer.save(buffer, img.format)
#     else:
#         with Image.open(image) as img:
#             resizer = img.resize((width, height), Image.ANTIALIAS)
#             resizer.save(fp=buffer, format=img.format)
    
#     return ContentFile(buffer.getvalue())


# def start_resizer(self, instance):
#     img_name = f'{instance.image}'.split('/')[-1]
#     image_resized = self.resizer(instance)
    
#     result_image_model = ResultImage()
    
#     result_image_model.entry_image = instance
#     result_image_model.image.save(img_name, InMemoryUploadedFile(
#         image_resized,
#         None,
#         img_name,
#         'image',
#         image_resized.tell,
#         None)
#     )
