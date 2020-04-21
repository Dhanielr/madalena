from django.db import models
from django.conf import settings
from django.dispatch import receiver
import os

from resizer.processors import ResizingPreProcessor


class EntryImages(models.Model):

    id = models.AutoField('Id', primary_key=True)
    added_at = models.DateTimeField('Adicionada em', auto_now_add=True)
    modified = models.DateTimeField('Modificada em', auto_now=True)
    image = models.ImageField('Imagem de entrada', upload_to='entry_images', blank=False, null=False)
    crop = models.BooleanField('Cortar', default=True)
    resized = models.BooleanField('Redimencionada', default=False)
    resized_image = models.ImageField('Imagem redimensionada', upload_to='resized_image', blank=True, null=True)
    height = models.PositiveIntegerField('Altura', default=384, blank=False, null=False)
    width = models.PositiveIntegerField('Largura', default=384, blank=False, null=False)

    class Meta:
        verbose_name = 'Imagem de entrada'
        verbose_name_plural = "Imagems de entradas"
        ordering = ['added_at']

    def __str__(self):
        return f'{self.image}'

    def filename(self):
        return os.path.basename(self.image.name)

@receiver(models.signals.post_save, sender=EntryImages)
def processor_call(sender, instance, created, **kwargs):
    processor = ResizingPreProcessor()
    processor.start_processing(instance)
