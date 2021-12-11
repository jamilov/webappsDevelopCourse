from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    placeOfBirth = models.CharField(null=True, max_length=50, verbose_name='Место произрастания')
    date = models.DateTimeField(null=True, db_index=True, verbose_name='Время сбора')

    class Meta:
        verbose_name_plural = 'Сорта винограда'
        verbose_name = 'Сорт винограда'
        ordering = ['-date']


class wineKind(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    type = models.CharField(max_length=20, verbose_name='Тип')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    grapeKind = models.ForeignKey('Bb', null=True, on_delete=models.PROTECT, verbose_name='Сорт винограда')
    AgeYears = models.FloatField(null=True, blank=True,verbose_name='Время выдержки бочки в годах')
    AgeMonths = models.FloatField(null=True, blank=True,verbose_name='Время выдержки в бутылках в месяцах')

    class Meta:
        verbose_name_plural = 'Сорта вин'
        verbose_name = 'Сорт вина'
        ordering = ['name']


class Barrel(models.Model):
    cellarPosition = models.TextField(null=True, blank=True, verbose_name='Местоположение в погребе')
    productionDate = models.DateTimeField(null=True, db_index=True, verbose_name='Дата изготовления')
    vol = models.FloatField(null=True, blank=True,verbose_name='Объем')
    isEmpty = models.BooleanField(verbose_name='Пустая')
    dateOfFilling = models.DateTimeField(null=True, auto_now_add=True, db_index=True, verbose_name='Дата заполнения')
    wineKind = models.ForeignKey('wineKind', null=True, on_delete=models.PROTECT, verbose_name='Сорт вина')

    class Meta:
        verbose_name_plural = 'Бочки'
        verbose_name = 'Бочка'
        ordering = ['dateOfFilling']
