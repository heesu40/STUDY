from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm , PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from IPython import embed
from .forms import UserCustomChangedForm
from django.contrib.auth import update_session_auth_hash as update_session
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')  #로그인 한사람은 회원가입 다시 못하도록!!!

    if request.method=="POST":
        form=UserCreationForm(request.POST) #폼에 해당부분이 채워져있을 것이다.
        # embed()
        if form.is_valid():
            user = form.save() 
            #회원가입하고 이 정보를 유지하기 위해서
            auth_login(request, user)
            return redirect("boards:index")
    else:
        form=UserCreationForm()
        # embed()

  
    context= {
        'form' :form,
        'label' : "회원가입"
    }
    return render(request , 'accounts/auth_form.html' , context)

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'boards:index') #next로 받을게 있따면....
            #실제 글을 쓰려할떄 로그인이 필요하다면 로그인 페이지 갔따가 다시 NEW로 가는 NEXT가 있기 때문에 바로 이동 가능하게 해준다!
        else:
            form = AuthenticationForm()
    form  = AuthenticationForm()


    context = {
        'form' : form,
        'label' : '로그인'
    }
    return render(request, 'accounts/auth_form.html' , context)

def logout(request):
    if request.method=="POST": #POST일때만 동작 하겠끔.

        auth_logout(request)

    return redirect('boards:index')

def edit(request):
    if request.method =="POST":
        form = UserCustomChangedForm(request.POST, instance=request.user) #user정보 넣기 위해 instance를 넣는다.
        if form.is_valid():
            form.save()
            return redirect("boards:index")
    else:
    # 유저 정보 수정 하기
    # form = UserChangeForm()
        form = UserCustomChangedForm() #이렇게 해야 이상한게 안뜬다 즉 이용자에게 적절한것이 뜬다.


    context= {
        'form' : form,
        'label' : '회원 정보 수정'
    }
    return render(request , 'accounts/auth_form.html' , context)

def chg_pwd(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST) # 패스워드도 폼이 있기 때문에 import하고 불러온다.
        #또한 ()안에 들어가는 인자 위치가 저 순서여야 한다.
        if form.is_valid():
            user = form.save()
            update_session(request.user) #import 해야 쓸 수 있따.
            return redirect('accounts:edit')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
        'label' : "비번 수정"
    }
    return render(request , 'accounts/auth_form.html' , context)
@login_required
def delete(request):
    if request.method=="POST":
        request.user.delete()

    return redirect('boards:index')
    

