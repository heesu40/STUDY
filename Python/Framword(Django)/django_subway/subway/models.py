from django.db import models

# Create your models here.
class Subway(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    bread = models.CharField(max_length=20)
    vegetable = models.CharField(max_length=20)
    sauce = models.CharField(max_length=20)
    drink = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # 수정일자 auto_now 생성일자 auto_now_add
    def __str__(self):
        return f'{self.name} : {self.create_at}' 