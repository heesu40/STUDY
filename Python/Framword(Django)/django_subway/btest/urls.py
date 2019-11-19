from django.urls import path
from . import views

app_name='btest'

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('create/' , views.create, name='create'),
    path('detail/<int:btest_id>/' , views.detail , name = 'detail'),
    path('survey/<int:btest_id>/' , views.survey , name='survey'),
    path('<int:btestchild_id>/survey_mod/', views.survey_mod , name = 'survey_mod'),
    
]