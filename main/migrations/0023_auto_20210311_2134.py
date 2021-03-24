# Generated by Django 3.0.5 on 2021-03-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_manager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Менеджер', 'verbose_name_plural': 'Менеджеры'},
        ),
        migrations.AddField(
            model_name='manager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
