from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('addart/' , views.addart),
    path('upart/' , views.upart),
    path('<int:pk>/artcon/', views.artcon),
    path('<int:pk>/artmod/' , views.artmod),
    path('<int:pk>/artdel/' , views.artdel),
    path('<int:pk>/artmod2/' , views.artmod2),
] 