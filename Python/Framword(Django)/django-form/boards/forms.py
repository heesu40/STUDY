from django import forms
from .models import Board

#이름지을때 앱의 이름의 Form이라 지어주자.
class BoardForm(forms.ModelForm): #일반적으로는 forms.Form이지만 이번엔 modelform을 받자
    class Meta:
        model = Board
        fields = ['title' ,'content'] #요 두개만 만든다. 

