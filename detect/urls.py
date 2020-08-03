from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Pnemonia import settings
from . import views


urlpatterns = [
                path('', views.Home, name = 'home'),
                path('result', views.result, name = 'result'),
                path('predict', views.predict, name='predict'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)