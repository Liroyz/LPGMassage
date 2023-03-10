from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MAX_LINE_LENGTH = 254


class Service(models.Model):
    name = models.CharField(
        max_length=MAX_LINE_LENGTH,
        db_index=True,
        verbose_name='Название услуги'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Specialist(models.Model):
    name = models.CharField(
        max_length=MAX_LINE_LENGTH,
        db_index=True,
        verbose_name='Имя специалиста'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Appointment(models.Model):
    PHONE_NUMBER_LENGTH = 17

    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, verbose_name='Услуга')
    specialist = models.ForeignKey(to=Specialist, on_delete=models.CASCADE, verbose_name='Специалист')
    first_name = models.CharField(max_length=MAX_LINE_LENGTH, verbose_name='Имя')
    last_name = models.CharField(max_length=MAX_LINE_LENGTH, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=PHONE_NUMBER_LENGTH, blank=True, verbose_name='Номер телефона')
    fact_date = models.DateTimeField(verbose_name='Дата и время записи')

    def __str__(self):
        return ''.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


