from django.urls import path

from teasers import views

urlpatterns = [
    path('', views.index, name='index'),
]
