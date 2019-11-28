from django import forms
from .models import Board , Comment

#이름지을때 앱의 이름의 Form이라 지어주자.
class BoardForm(forms.ModelForm): #일반적으로는 forms.Form이지만 이번엔 modelform을 받자
    class Meta:
        model = Board
        fields = ['title' ,'content'] #요 두개만 만든다. 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] #댓글만 있으면 되기 때문에~ comment만!튜플로도 만들수 있는데, ('comment',) 
                            #튜플은 하나만 있어도 꼬옥 , 를 찍어 주어야 한다.

        

