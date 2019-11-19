from django.urls import path
from . import views

app_name='btest'

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('create/' , views.create, name='create'),
    path('detail/<int:btest_id>/' , views.detail , name = 'detail'),
    path('vote_mod/<int:btestchild_id>/<int:btest_id>/' , views.vote_mod , name='vote_mod'),
    path('question_del/<int:btest_id>' , views.question_del , name= "question_del"),
    path('vote/<int:btestchild_id>/<int:btest_id>/' , views.vote , name = 'vote'),
]