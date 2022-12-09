from django.urls import path
from nikita import views

urlpatterns = [
    path ("", views.index),
    path ("appointment/", views.postuser),
]

