from django.db import models
from apps.company.models import Company


class Video(models.Model):
    name = models.CharField(max_length=127, verbose_name='Nazvaniye')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='videos', verbose_name='company')
    video = models.FileField(upload_to='video/video/', verbose_name='video')
    date = models.DateField(verbose_name='date')
    description = models.TextField('Opisaniye')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'