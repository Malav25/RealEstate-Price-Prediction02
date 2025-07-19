from django.db import models

# Create your models here.
class Dataset(models.Model):
    locality_name = models.CharField(max_length=100)
    bhks = models.IntegerField()
    per_sq_ft_area = models.IntegerField()
    price_per_sq_ft_area = models.IntegerField()
    construction_status = models.CharField(max_length=150)
    price = models.BigIntegerField()
    appt_name = models.TextField(max_length=200)
    appt_link = models.URLField(blank=False)

    def __str__(self):
        return self.appt_name