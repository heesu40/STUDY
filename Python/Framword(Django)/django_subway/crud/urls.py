from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('' , views.index , name= 'index'), #crud/
    path('new/' , views.new , name = 'new'), #crud/new
    # path('create/' , views.create , name='create'), #crud/create
    path('<int:pk>/', views.detail , name= 'detail'), #crud/detail하게 내용 보는 페이지
    path("<int:pk>/update/", views.update ,  name = 'update'), # crud/update/ 수정하는 페이지
    # path("<int:pk>/revise/" , views.revise , name = 'revise'),
    path("<int:pk>/delete/" , views.delete , name = 'delete'),

]