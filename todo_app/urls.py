from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('create/', views.create,name="create"),
    path('delete/<Todos_id>', views.delete,name="delete"),
    path('finished/<Todos_id>', views.finished,name="finished"),
    path('not_finished/<Todos_id>', views.not_finished,name="not_finished"),
    path('update/<Todos_id>', views.update,name="update"),
]