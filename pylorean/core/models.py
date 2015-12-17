from django.conf import settings
from django.db import models
from django.utils.dates import WEEKDAYS


class Appointment(models.Model):
    title = models.CharField(max_length=256)
    responsible_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       related_name="responsible")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    descripton = models.TextField(blank=True, null=True)
    attendants = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="attendant")
    guests = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="guest")

    def __str__(self):
        return self.title


class Schedule(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    busy_weekday = models.IntegerField(choices=WEEKDAYS.items())
    busy_time = models.TimeField()
