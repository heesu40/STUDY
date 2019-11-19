from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('' , views.index , name= 'index'), #crud/
    path('new/' , views.new , name = 'new'), #crud/new
    # path('create/' , views.create , name='create'), #crud/create
    path('<int:art_pk>/', views.detail , name= 'detail'), #crud/detail하게 내용 보는 페이지
    path("<int:art_pk>/update/", views.update ,  name = 'update'), # crud/update/ 수정하는 페이지
    # path("<int:pk>/revise/" , views.revise , name = 'revise'),
    path("<int:art_pk>/delete/" , views.delete , name = 'delete'),
    path("<int:art_id>/comment" , views.comment , name='comment'),
    #부모의 아이디는 art_id로 바꿔주겠다. 
    path('<int:art_id>/comment/<int:com_id>/edit/' , views.comedit, name = 'comedit'),
    path('<int:art_id>/comment/<int:com_id>/del/' , views.comdel, name = 'comdel'),

]