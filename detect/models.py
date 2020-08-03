from django.db import models

# Create your models here.
class PneumoniaPredict(models.Model):
    img_path = models.CharField(max_length = 20)
    prediction = models.CharField(max_length = 20)
