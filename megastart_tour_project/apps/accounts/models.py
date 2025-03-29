from django.db import models  # Импортируем модуль моделей Django
from django.contrib.auth.models import AbstractUser, BaseUserManager  # Импорт базовых классов для создания кастомного пользователя

# Кастомный менеджер пользователей
class UserManager(BaseUserManager):
    # Метод для создания обычного пользователя
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле Email должно быть заполнено")  # Проверяем, передан ли email
        email = self.normalize_email(email)  # Приводим email к стандартному виду (например, к нижнему регистру)
        extra_fields.setdefault('is_active', True)  # По умолчанию делаем пользователя активным
        user = self.model(email=email, **extra_fields)  # Создаём объект пользователя
        user.set_password(password)  # Устанавливаем хешированный пароль
        user.save(using=self._db)  # Сохраняем пользователя в базу данных
        return user

    # Метод для создания суперпользователя
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # Делаем суперпользователя членом персонала
        extra_fields.setdefault("is_superuser", True)  # Делаем суперпользователя суперпользователем

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Пользователь должен иметь is_staff=True")  # Проверяем флаг is_staff
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Пользователь должен иметь is_superuser=True")  # Проверяем флаг is_superuser
        return self.create_user(email=email, password=password, **extra_fields)  # Создаём пользователя с переданными параметрами

# Кастомная модель пользователя
class User(AbstractUser):
    username = None  # Отключаем стандартное поле username (будем использовать email)
    date_joined = None  # Убираем стандартное поле даты регистрации

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Электронная почта",  # Указываем, как будет называться поле в админке
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Фамилия",
    )
    age = models.PositiveSmallIntegerField(
        default=18,
        verbose_name="Возраст",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активен",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Персонал"
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="Суперпользователь"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Дата создания пользователя
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")  # Дата последнего изменения

    USERNAME_FIELD = 'email'  # Используем email как основное поле для аутентификации
    REQUIRED_FIELDS = []  # Дополнительные обязательные поля (оставляем пустым)

    objects = UserManager()  # Подключаем кастомный менеджер пользователей

    class Meta:
        verbose_name = "Пользователь"  # Название модели в админке (единственное число)
        verbose_name_plural = "Пользователи"  # Название модели во множественном числе
        ordering = ['-updated_at']  # Сортировка по дате обновления (от новых к старым)

    def __str__(self):
        return self.email  # Возвращаем email пользователя при вызове str(user)









