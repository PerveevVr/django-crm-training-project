# Generated by Django 3.0.5 on 2021-02-28 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210228_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, null=True, verbose_name='Дата завершения проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, null=True, verbose_name='Дата начала проекта'),
        ),
    ]