from django.conf import settings
from django.db import models


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    picture = models.ImageField(upload_to='person_picture')

    def __str__(self):
        return self.user.username
