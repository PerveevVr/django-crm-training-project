# Generated by Django 3.0.5 on 2021-02-22 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Клиент')),
                ('contact', models.CharField(max_length=255, verbose_name='Контактное лицо')),
                ('descripе', models.TextField(verbose_name='Информация о клиенте')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('date_creat', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('date_updat', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['name', 'date_creat'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('category', models.CharField(blank=True, choices=[(None, 'Выберите тип номера телефона'), ('w', 'Рабочий телефон'), ('h', 'Домошний телефон'), ('m', 'Мобильный телефон'), ('o', 'другой...')], max_length=1, verbose_name='Категория')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
                'ordering': ['client_id', 'category'],
            },
        ),
    ]
