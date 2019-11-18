from django.urls import path
from . import views

app_name = 'subway'
urlpatterns = [
    #name 을 설정하면 url관리가 수월하다.
    #{% url 'name설정한것' %} appname지정안했다면
    #{% url 'app_name:name설정한것' %} 위에 app name지정한다면
    #url이 바뀌어도 일일히 찾아서 바꿀 필요가 없다.
    path('' , views.index , name = 'index'),
    path('menu/' , views.menu , name='menu'), #메뉴 선택하는 링크
    # path('addmenu/' , views.addmenu, name = 'add'), #메뉴 추가 링크
    path('<int:id>/', views.detail , name = 'detail'),
    path('mod/<int:id>/' , views.mod , name  = 'mod'),
    path('delete/<int:id>/' , views.delete , name = "delete"),

    
]