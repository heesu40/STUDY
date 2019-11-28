from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 술꾼 {self.name}'

class Alcohol(models.Model):
    name = models.CharField(max_length=20)
    #알콜에서는 Person을 설정하지 않으려 한다. 왜냐하면 그렇게 해서 관리되는게 아니기 때문에!
    # people = models.ManyToManyField(Person,through='Sales', related_name='alcohols')
    people = models.ManyToManyField(Person, related_name='alcohols')

    def __str__(self):
        return f'주류 No.{self.id} : {self.name}'

#1:1은 관리가 어려워 중계모델은 두어야 한다.

# class Sales(models.Model):
#     person = models.ForeignKey(Person , on_delete=models.CASCADE)
#     alcohol = models.ForeignKey(Alcohol , on_delete=models.CASCADE)
#     판매시간 = models.DateTimeField()        

#     def __str__(self):
#         return f'{self.person}이 마시는 {self.alcohol}'



