from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField('Название', max_length=299)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class City(models.Model):
    name = models.CharField('Город', max_length=299)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Advert(models.Model):
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    title = models.CharField('Название', max_length=3999)
    description = RichTextUploadingField('Статья')
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.city} - {self.category} : {self.created} - {self.views}"

