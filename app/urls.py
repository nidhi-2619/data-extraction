import django.contrib.auth.urls
from django.urls import path, include
from .views import uploadData

urlpatterns = [
    path('', uploadData, name='uploadData'),

]