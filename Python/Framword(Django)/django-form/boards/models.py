from django.db import models
from django.conf import settings
# Create your models here.
class Board(models.Model):
    title  = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_boards" , blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200) #댓글은 대게 200자가 length다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE) #장고에 있는 기본 settings를 외래키 연결
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment