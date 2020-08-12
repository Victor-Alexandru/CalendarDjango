from django.db import models


# Create your models here.
class Day(models.Model):
    number = models.IntegerField()
    made_sport = models.BooleanField(default=False)
    made_reading = models.BooleanField(default=False)
    made_health_eating = models.BooleanField(default=False)
    made_r = models.BooleanField(default=False)
    made_pos_afir = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)
