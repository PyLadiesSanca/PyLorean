from django.db import models


class Appointment(models.Model):
    title = models.CharField(max_length=256)
    responsible_id = models.ForeignKey('auth.User', related_name="responsible")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    descripton = models.TextField(blank=True, null=True)
    attendants = models.ManyToManyField('auth.User', related_name="attendant")
    guests = models.ManyToManyField('auth.User', related_name="guest")

    def __str__(self):
        return self.title


class Schedule(models.Model):
    user_id = models.ForeignKey('auth.User')
    busy_weekday = models.DateField()
    busy_time = models.TimeField()
