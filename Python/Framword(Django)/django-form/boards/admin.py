from django.contrib import admin
from .models import Board, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    #처음에 보여지는 항목
    list_display = ['comment']

admin.site.register(Board) #admin사이트에 등록! 이라고 외우자
admin.site.register(Comment, CommentAdmin) #두개의 인자를 넣어서 등록 한다. 코멘트는 위에 설정 한 것 까지!


