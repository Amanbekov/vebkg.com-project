from django.db import models
from apps.company.models import Company
# Create your models here.


class Vacancii(models.Model):
    doljnost=models.CharField(max_length=120,verbose_name='Должность')
    oklad=models.CharField(max_length=120,verbose_name='Оклад')
    type=models.CharField(max_length=120,verbose_name='Тип')
    company=models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='vacancii',verbose_name='Компания')
    description= models.TextField(verbose_name='Описание')
    
    def __str__(self) -> str:
        return self.doljnost
    
    class Meta:
        verbose_name='Вакансия'
        verbose_name_plural='Вакансии'