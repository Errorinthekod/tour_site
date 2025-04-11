# Generated by Django 5.1.7 on 2025-04-11 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название тура')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фотография тура')),
                ('description', models.TextField(verbose_name='О туре')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('is_active', models.BooleanField(default=True, verbose_name='В архиве')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date', models.DateTimeField(verbose_name='Дата тура')),
                ('available_spots', models.PositiveIntegerField(default=0, verbose_name='Свободные места')),
                ('meeting_point', models.CharField(max_length=255, verbose_name='Место встречи')),
                ('duration', models.PositiveIntegerField(default=1, verbose_name='Длительность тура / дней')),
                ('difficulty', models.CharField(choices=[('easy', 'Лёгкая'), ('medium', 'Средняя'), ('hard', 'Сложная')], default='medium', max_length=255, verbose_name='Сложность')),
                ('min_age', models.PositiveIntegerField(default=0, verbose_name='Допустимый возраст')),
                ('group_size', models.PositiveIntegerField(default=0, verbose_name='Размер группы')),
                ('meals', models.BooleanField(default=True, verbose_name='Питание')),
                ('accommodation', models.BooleanField(default=True, verbose_name='Проживание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to=settings.AUTH_USER_MODEL, verbose_name='Автор тура')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_images/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.tour')),
            ],
            options={
                'verbose_name': 'Фотография тура',
                'verbose_name_plural': 'Фотографии тура',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='tours.tour')),
            ],
            options={
                'unique_together': {('user', 'tour')},
            },
        ),
    ]
