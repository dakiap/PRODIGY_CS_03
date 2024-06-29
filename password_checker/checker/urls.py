from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assess/', views.assess, name='assess'),
]
