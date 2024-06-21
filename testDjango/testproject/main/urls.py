from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name='main'),
    path('addinfo/', views.addinfo, name='info')
]
