from django.urls import path
from . import views

app_name = 'movie'
urlpatterns=[
    path('' , views.index , name = 'index'),
    path('movies/' ,views.movies, name = 'movies'),
    path('movies/<int:m_id>' , views.mtitle, name = 'moviesdetail'),
    path('new/' , views.new , name = 'new'),
    path('edit/<int:m_id>/' , views.edit, name = "edit" ),
    path('delete/<int:m_id>' , views.delete , name ="delete"),
    

]