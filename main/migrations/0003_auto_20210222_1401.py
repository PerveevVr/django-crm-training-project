# Generated by Django 3.0.5 on 2021-02-22 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'E-mail', 'verbose_name_plural': 'E-mail'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='descripе',
            new_name='descript',
        ),
    ]
