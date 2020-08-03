from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os
import tensorflow as tf
from tensorflow import keras
import cv2

# Create your views here.
from detect.models import PneumoniaPredict


def predict(request):
    if request.method == 'POST':
        try:
            folder = 'media/images/'
            image = request.FILEs['cd']
            print("The name of the file:", image.name)

            filename = str(image.name)
            fs = FileSystemStorage(location = folder)
            name = fs.save(image.name, image)

            mediapath = folder + "{}"
            filepath = os.path.join(mediapath).format(name)

            # Loading the model
            model = tf.keras.models.load_model('models\pneumonia.h5')

            img_size = 300
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (img_size, img_size))
            new_array.reshape(-1, img_size, img_size, 1)

            Labels = ['pneumonia', 'normal']

            prediction = model.predict([new_array])

            result = Labels[int(prediction[0][0])]
            print(result)

            pn = PneumoniaPredict()

            pn.img_path = filepath
            pn.prediction = result
            pn.save()

            if result == 'pneumonia':
                messages.info(request, "The patient condition is: Pneumonia")
            else:
                messages.info(request,"The patient condition is: Normal")

            return render(request, 'results.html')

        except Exception as e:
            print("The Error is:",e)

    else:
        return render(request, 'index.html')
