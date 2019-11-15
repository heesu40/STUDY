from django.db import models

# Create your models here.
class ctest(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    new_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'{ctest.title} {ctest.content}'
