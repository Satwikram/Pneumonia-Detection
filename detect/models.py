from django.db import models

# Create your models here.
class ImageSorce:
    img: str
    
class PneumoniaPredict(models.Model):
    img_path = models.CharField(max_length = 200)
    prediction = models.CharField(max_length = 200)
