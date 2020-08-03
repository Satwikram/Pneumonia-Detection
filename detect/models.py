from django.db import models

# Create your models here.
class PneumoniaPredict:
    img_path = models.CharField(max_length = 20)
    predict = models.CharField(max_length = 20)
