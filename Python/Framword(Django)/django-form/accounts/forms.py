from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model #유저 모델을 가지고 오는 함수이다. 

class UserCustomChangedForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name' , 'last_name' , 'email']
