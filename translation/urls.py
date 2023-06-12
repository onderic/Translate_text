from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import api

urlpatterns = [
    
    path('translate/', api.translate, name='translate'),
]