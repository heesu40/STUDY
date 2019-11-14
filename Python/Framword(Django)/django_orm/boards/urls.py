from django.urls import path
from . import views

urlpatterns = [
    path('subwayresult/' , views.subwayresult),
    path('subway/' , views.subway),
    path('' , views.index),
]