from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Reading(models.Model):
    sensor = models.ForeignKey(Sensor)
    read_at = models.DateTimeField(auto_now_add=True)
    reading = models.DecimalField(max_digits=5, decimal_places=3)

    class Meta:
        ordering = ('-read_at',)
