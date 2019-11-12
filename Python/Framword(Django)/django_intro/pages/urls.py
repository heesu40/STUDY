from django.urls import path
from . import views #views의 위치를 알려주기 위해서 import한다. . 은 현재 경로라는 뜻

urlpatterns = [
    path('throw/', views.throw),
    path('catch/' , views.catch),
    path('lotto/' , views.lotto),
    path('lottoresult/' , views.lottoresult),
    path('artiii/' , views.artiii),
    path('artiiisend/' , views.artiiisend),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('subway/' , views.subway),
    path('subway_result/' , views.subway_result),
    path('static_ex/', views.static_ex),
    path('index/', views.index),
]
#실행하기 위해서는 localhost:8000/pages/throw/ 로 해야 실행이 된다
#url분리 완료!