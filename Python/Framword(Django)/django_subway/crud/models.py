from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #추가될때 마다 현재시간으로 저장
    updated_at = models.DateTimeField(auto_now=True) #editable옵션이 False로 자동 저장된다.

    def __str__(self):
        return f'{self.id} {self.title}'
  

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    #ForeignKey(어떤 테이블 참조할지 , 그 테이블이 삭제될때 어떻게 할지!)
    #models.CASCADE : 부모테이블이 삭제시 같이 삭제하는 옵션
    #models.PROTECT : 부모테이블이 삭제될 때 오류를 발생(삭제가 되면 안되기 때문에!)
    #models.SET_NULL : 부모테이블이 삭제될때 null값을 채운다.(but not null 옵션일때는 불가능하다.)
    #models.SET() : 특정 함수를 호출.
    #models.DO_NOTHING : 암것도 안함.
    article = models.ForeignKey(Article , on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


