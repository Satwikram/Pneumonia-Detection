from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import tensorflow as tf
from tensorflow import keras
import cv2

# Create your views here.
def predict(request):
    if request.method == 'POST':
        try:
            folder = 'media/images/'
            image = request.FILEs['cd']
            print("The name of the file:", image.name)

            filename = str(image.name)
            fs = FileSystemStorage(location = folder)
        except Exception as e:
            print("The Error is:",e)


    else:
        return render(request, 'index.html')
