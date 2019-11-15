from django.urls import path
from . import views

urlpatterns = [
    path('subwayresult/' , views.subwayresult),
    path('subway/' , views.subway),
    path('' , views.index),
    path('subwayid/<int:id>/' , views.subwayid),
]