# Generated by Django 3.0.5 on 2021-02-22 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mail(s)',
            },
        ),
    ]
