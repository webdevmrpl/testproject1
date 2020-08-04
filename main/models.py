from django.db import models
from django.core import validators


class SubRubric(models.Model):
    name = models.CharField(max_length=20, default='SomeData')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Побочные рубрики'
        verbose_name = 'Побочная рубрика'
        ordering = ['name']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')
    sub_rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT, verbose_name='Побочная рубрика',
                                   default='SomeData')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    img = models.ImageField(verbose_name='Изображение', validators=[validators.FileExtensionValidator(
        allowed_extensions=('jpg', 'png', 'gif'))],
                            error_messages={'invalid_extension': 'Этот формат файла - не поддерживается'},
                            upload_to='')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Рубрика', default='Недвижимость')

    def get_absolute_url(self):
        return '/detail/%s/' % self.pk

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
