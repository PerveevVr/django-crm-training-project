# Generated by Django 3.0.5 on 2021-03-06 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210303_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='descript',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информация о клиенте'),
        ),
        migrations.AlterField(
            model_name='interplay',
            name='channel',
            field=models.CharField(blank=True, choices=[(None, '- неопределён -'), ('app', 'Заявка клиента'), ('let', 'Письмо клиента'), ('sit', 'Сайт компании'), ('ini', 'Инициатива компании')], max_length=3, null=True, verbose_name='Канал обращения'),
        ),
    ]