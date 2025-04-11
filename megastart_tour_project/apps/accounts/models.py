from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


"""Колдонуучуларды жаратуучу класс. """

class UserManager(BaseUserManager):

    """ Жөнөкөй колдонуучу (клиент). """

    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    """
    Супер колдонуучу (админ).
    келечекте ошол эле функция колдонуп башка ролдор ишке ашырылат.
    Бирок ошону башкача жазайт окшойбуз. Максат агайдан сурайм.
    """


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


"""Колдонуучунун модели"""

class User(AbstractUser):
    number = models.CharField('Телефон', max_length=25, unique=True)
    birthday = models.DateField(null=True, blank=True)
    children = models.PositiveIntegerField(default=0, null=True, blank=True)
    city = models.CharField('Город', max_length=200, blank=True, null=True)
    raiting = models.DecimalField('Рейтинг', max_digits=3, decimal_places=1, default=0.0)
    fav_tours = models.ManyToManyField('tours.Tour', blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username  # колдонуучуну чыгаруу - string

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


"""Келечекте бул файл өзгөрүш мүмкүн"""