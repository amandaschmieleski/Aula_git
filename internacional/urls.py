from django.urls import path #define padrao de url no django
from . import views

urlpatterns = [
    path('', views.info, name='info_internacional'),
]
