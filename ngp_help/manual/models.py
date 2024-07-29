from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User


class Manual(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления", auto_now=True)
    category = models.ForeignKey(
        "Category", verbose_name="Категория", on_delete=models.PROTECT)
    # creator = models.ForeignKey(
    #     "User", verbose_name="Создатель", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('manual_item', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководства"
        ordering = ['name']


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Категория')

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
