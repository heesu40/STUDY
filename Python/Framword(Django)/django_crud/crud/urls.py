from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index), #crud/
    path('new/' , views.new), #crud/new
    path('create/' , views.create), #crud/create
    path('<int:pk>/article/', views.detail), #crud/detail하게 내용 보는 페이지
    path("<int:pk>/update/", views.update), # crud/update/ 수정하는 페이지
    path("<int:pk>/revise/" , views.revise),
    path("<int:pk>/delete/" , views.delete),
   
]