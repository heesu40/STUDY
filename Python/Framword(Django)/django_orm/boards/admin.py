from django.contrib import admin
from .models import Board
from .models import Subway

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    #admin 안에 Model를 상속을 받아서
    #Field순서 바꾸기
    fields = ['content' , 'title']
    list_display = ["title" , 'updated_at' , 'content']
    list_filter = ["updated_at"]
    second_ = ["title" , "content"]

class SubwayAdmin(admin.ModelAdmin):
    fields = ['title' , 'sandwitch', 'size' ,'bread' , 'source']
    #실제 만들때 조건을 준 auto_now_add 때문에 fields를 만들시 다시 생성 문제 떄문에 오류가 뜨는 것! date넣어주면 오류 뜬다.
    
    list_display = ['title' , 'nowdate' ]


admin.site.register(Board , BoardAdmin)
admin.site.register(Subway , SubwayAdmin)