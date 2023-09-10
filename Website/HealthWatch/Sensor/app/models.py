from django.db import models


class StoredData(models.Model):
    numerical_value = models.FloatField(default=0.0)
    date = models.TextField()
    time = models.TextField()
    body_temp = models.FloatField(default=98.6)
    env_temp = models.FloatField(default=88.0)
    air_quality = models.FloatField(default=150)
    pulse_rate = models.FloatField(default=75)
    spo2_level = models.FloatField(default=98)

    def __str__(self):
        return f"Date: {self.date} | Time: {self.time}"
