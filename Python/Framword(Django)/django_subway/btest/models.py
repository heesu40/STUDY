from django.db import models

# Create your models here.
class Btest(models.Model):
    btest_id = models.CharField(max_length=20 , null=True)
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return {self.question}

class Btestchild(models.Model):
    btestchild_id = models.CharField(max_length=20 , null=True)
    survey = models.CharField(max_length=200)
    question = models.ForeignKey(Btest , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return {self.survey}
