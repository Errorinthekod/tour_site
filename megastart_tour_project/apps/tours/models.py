from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


def validate_max_32_images(tour):
    if tour.images.count() >= 32:
        raise ValidationError("Нельзя загружать больше 32 изображений.")



class Tour(models.Model):

    DIFFICULTY_CHOICE = [
        ('easy', 'Лёгкая'),
        ('medium', 'Средняя'),
        ('hard', 'Сложная'),
    ]

    name = models.CharField('Название тура', max_length=255)
    poster = models.ImageField('Фотография тура', upload_to='images/', blank=True, null=True)
    author = models.ForeignKey('accounts.User', verbose_name='Автор тура', on_delete=models.CASCADE, related_name='tours')
    description = models.TextField('О туре')
    price = models.PositiveIntegerField('Цена', default=0)
    is_active = models.BooleanField('В архиве', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    date = models.DateTimeField('Дата тура')
    available_spots = models.PositiveIntegerField('Свободные места', default=0)
    meeting_point = models.CharField('Место встречи', max_length=255)
    duration = models.PositiveIntegerField('Длительность тура / дней', default=1)
    difficulty = models.CharField('Сложность', choices=DIFFICULTY_CHOICE, default='medium', max_length=255)
    min_age = models.PositiveIntegerField('Допустимый возраст', default=0)
    group_size = models.PositiveIntegerField('Размер группы', default=0)
    meals = models.BooleanField('Питание', default=True)
    accommodation = models.BooleanField('Проживание', default=True)

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.score for r in ratings) / ratings.count(), 1)  # 1 знак после запятой
        return 0.0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour_images/')

    def clean(self):
        validate_max_32_images(self)

    def save(self, *args, **kwargs):
        validate_max_32_images(self.tour)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фотография тура"
        verbose_name_plural = "Фотографии тура"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="ratings")
    score = models.DecimalField(max_digits=2, decimal_places=1)  # дробные значения от 1.0 до 5.0
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tour')

    def __str__(self):
        return f"{self.user.username} → {self.tour.name}: {self.score}"


"""Келечекте бул файл өзгөрүш мүмкүн"""