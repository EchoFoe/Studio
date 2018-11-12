from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'