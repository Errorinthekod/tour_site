from django.db import models


class Apply(models.Model):
    name = models.CharField("Name", max_length = 50)
    email = models.EmailField("Mail", max_length = 50, unique = True)
    phone = models.CharField("Phone", max_length = 50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"