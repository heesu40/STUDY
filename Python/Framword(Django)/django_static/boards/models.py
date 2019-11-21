from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill , Thumbnail , ResizeToFit


# Create your models here.
def board_img_path(instance, filename):
    return f'boards/{instance.pk}번글/{filename}'
    # return f'boards/user_{instance.pk}번글/{filename}' 유저가 설정 된 경우 이렇게 할 수도 있다.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #ResizeToFill Ver.1    이미지의 사이즈를 지정한 사이즈로 나머지는 잘라내기
    # image = ProcessedImageField(
    #     upload_to = 'boards/test2',
    #     processors= [ResizeToFit(100,200)],
    #     format = 'JPEG',
    #     options={
    #         'quality' : 90
    #     }
    # )
    #Thumbnail Ver.1 (원번 저장 하고 썸네일은 캐쉬형태로)
    # image_thumb = ImageSpecField(
    #     source = 'image',
    #     processors = [Thumbnail(10,10)],
    #     format="JPEG",
    #     options = {
    #         'quality' : 90
    #     }
    # )
    #Thumbnail Ver. 2(원본 저장 안하고 썸네일만)

    # image = models.ImageField(blank=True)
    image = models.ImageField(blank=True  ,upload_to=board_img_path)
    
    image_thumb = ImageSpecField(
        source = 'image',
        # upload_to='boards/thumb' , 
        # processors = [ResizeToFill(200,300)],
        processors = [Thumbnail(200,300)],
        format = "JPEG" , 
        options = {
            'quality' : 90
            }

    )
    def __str__(self):
        return self.title 

