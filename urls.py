from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foodsafety/', views.foodsafety, name='wellness'),
    path('about/', views.about, name='about'),
]