from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index-url'),
    path('component/<int:pk>', views.addComponent, name='add-component')
]