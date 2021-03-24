# Generated by Django 3.0.5 on 2021-02-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210228_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interplay',
            options={'verbose_name': 'Взаимодействие', 'verbose_name_plural': 'Взаимодействия'},
        ),
        migrations.AlterField(
            model_name='interplay',
            name='channel',
            field=models.CharField(blank=True, choices=[(None, 'Выберите канал обращения'), ('app', 'Заявка'), ('let', 'Письмо'), ('sit', 'Сайт'), ('ini', 'Инициатива компании')], max_length=3, null=True, verbose_name='Канал обращения'),
        ),
    ]