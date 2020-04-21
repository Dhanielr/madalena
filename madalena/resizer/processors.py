from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile

import os

from .tasks import  resizer

class ResizingPreProcessor(object):

    def start_processing(self, instance):
        data = self.get_instance_data(instance)
        task = self.call_resizer_task(data)

        # if task:
        #     self.post_resizer_save(instance, task)

    def get_instance_data(self, instance):
        data = {
            'image' : f'{settings.MEDIA_ROOT}/{instance.image}',
            'width' : instance.width,
            'height' : instance.height,
            'crop' : instance.crop,
        }

        return data

    def call_resizer_task(self, data):
        if not os.path.exists(settings.RESIZER_RESULT_PATH):
            os.makedirs(settings.RESIZER_RESULT_PATH)
        return resizer.delay(data)

    # def post_resizer_save(self, instance, task_obj):
    #     img_name = f'{instance.image}'.split('/')[-1]
    #     image_resized = task_obj
        
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