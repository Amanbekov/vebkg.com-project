from django.db import models
from apps.company.models import Company

class Event(models.Model):
    date = models.DateTimeField(verbose_name='дата и время')
    name = models.CharField(max_length=127,
    verbose_name='название')
    location = models.CharField(max_length=127,
    verbose_name='локация')
    image = models.ImageField(upload_to='event/images/',
    verbose_name='kartina')
    description = models.TextField(verbose_name='Opisaniye')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='events', verbose_name='компания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'