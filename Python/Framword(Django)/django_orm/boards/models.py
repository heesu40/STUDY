from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10) #CharField는최대 글자를 설정해 주어야 한다.
    content = models.TextField() #Text Field는 maxlength주어도 DB에서 글자수 제한이 주어지지 않는다.
    created_at = models.DateTimeField(auto_now_add=True) #글이 생성되면 날짜가 자동으로 저장되기 위해서 auto_now_add
    updated_at = models.DateTimeField(auto_now=True) #수정될때마다 시간 자동으로 저장하기 위해서
    #장고는 아이디를 자동으로 만들어주기 때문에 컬럼명만 신경 쓰면 된다! VO생성 안해도 된다

    def __str__(self):
        return f'{self.id} : {self.title}'