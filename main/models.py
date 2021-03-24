from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
"""
The tag manager allows us to add, list and 
remove tags for objects of articles.
"""

class Manager(models.Model):
    """
    Manager profile model.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, 
        verbose_name='Менеджер')
    bio = models.TextField(null=True, blank=True, 
        verbose_name='Информация о менеджере')
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('client_list')


class Client(models.Model):
    """
    Client model
    """
    name = models.CharField(max_length=255, unique=True, db_index=True, 
        verbose_name='Клиент'
    )
    contact = models.CharField(max_length=255, verbose_name='Контактное лицо')
    descript = RichTextField(null=True, blank=True, verbose_name='Информация о клиенте')
    # descript = models.TextField(null=True, blank=True, verbose_name='Информация о клиенте')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    date_creat = models.DateTimeField(auto_now_add=True, db_index=True, 
        verbose_name='Дата создания'
    )
    date_updat = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[self.id])


class Phone(models.Model):
    """
    Phone model associated with customer model.
    """
    KINDS = (
        (None, 'Выберите тип номера телефона'),
        ('w', 'Рабочий телефон'),
        ('h', 'Домошний телефон'),
        ('m', 'Мобильный телефон'),
        ('o', 'другой...'),
    )

    number = models.CharField(max_length=20, verbose_name='Номер телефона')
    category = models.CharField(max_length=1, choices=KINDS, null=True, 
                                blank=True, verbose_name='Категория')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, 
                               verbose_name='Клиент')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.number


class Email(models.Model):
    """
    Email model linked to customer model.
    """
    email = models.EmailField(verbose_name='E-mail')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mail'

    def __str__(self):
        return self.email


class Project(models.Model):
    """
    Project model linked to customer model.
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, 
        blank=False, null=False, verbose_name='Клиент'
    )
    name = models.CharField(max_length=255, db_index=True, verbose_name='Проект')
    descript = RichTextField(null=True, blank=True, verbose_name='Информация о проекте')
    # descript = models.TextField(blank=True, null=True, verbose_name='Информация о проекте')
    start_date = models.DateTimeField(default=timezone.now, blank=True, null=True, 
        db_index=True, verbose_name='Дата начала проекта'
    )
    end_date = models.DateTimeField(default=timezone.now, blank=True, null=True, 
        db_index=True, verbose_name='Дата завершения проекта'
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Стоимость проекта')
    # price = models.FloatField(null=True, blank=True, verbose_name='Стоимость проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-start_date']

    def __str__(self):
        return str(self.client) + ' | ' + self.name

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id])


class Interplay(models.Model):
    """
    Interaction model associated with the project model.
    """
    # Channel of reference
    APPEAL = (
        (None, '- неопределён -'),
        ('app', 'Заявка клиента'),
        ('let', 'Письмо клиента'),
        ('sit', 'Сайт компании'),
        ('ini', 'Инициатива компании'),
    )

    # Interaction type
    COMTYPE = (
        ('comm', 'Комментарий'),
        ('task', 'Задача'),
        ('lett', 'Письмо'),
        ('bell', 'Звонок'),
        ('even', 'Событие'),
    )    

    project = models.ForeignKey(Project, on_delete=models.CASCADE, 
        blank=False, null=False, verbose_name='Проект'
    )
    channel = models.CharField(max_length=3, choices=APPEAL, null=True, 
        blank=True, verbose_name='Канал обращения'
    )
    type_comm = models.CharField(max_length=4, choices=COMTYPE, null=False, 
        blank=False, default='comm', verbose_name='Тип взаимодействия'
    )
    manager = models.ForeignKey(User, null=True, on_delete=models.PROTECT, 
        verbose_name='Менеджер'
    )
    descript = RichTextField(null=True, blank=True, verbose_name='Информация')
    rating = models.BooleanField(null=True, verbose_name='Оценка взаимодействия')
    date_comm = models.DateTimeField(auto_now_add=True, db_index=True,
        verbose_name='Дата взаимодействия'
    )
    tags = TaggableManager(verbose_name='Теги')

    class Meta:
        verbose_name = 'Взаимодействие'
        verbose_name_plural = 'Взаимодействия'
        ordering = ['-date_comm']

    def __str__(self):
        return str(self.project) + ' | ' + str(self.project.client)

    def get_absolute_url(self):
        return reverse('interplay_detail', args=[self.id])
