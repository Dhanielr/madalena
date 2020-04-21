from django.db import models


class ResultImage(models.Model):

    id = models.AutoField('Id', primary_key=True)
    image = models.ImageField('Imagem de saída', upload_to='result_images', blank=False, null=False)
    entry_image = models.ForeignKey('funnel.EntryImages', verbose_name='Imagem de entrada', on_delete=models.CASCADE, blank=False, null=False)
    added_at = models.DateTimeField('Adicionada em', auto_now_add=True)
    modified = models.DateTimeField('Modificada em', auto_now=True)

    class Meta:
        verbose_name = 'Imagem de saída'
        verbose_name_plural = "Imagems de saída"
        ordering = ['added_at']

    def __str__(self): 
        return self.image

