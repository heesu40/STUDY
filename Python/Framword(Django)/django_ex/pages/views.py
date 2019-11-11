from django.shortcuts import render
from django.http import HttpResponse #Text를 보낼 떄 사용
# Create your views here.
def index(request):
    #return HttpResponse("Hello Django")
    return render(request, 'index.html')

def age(request , age):
    context = {
        'age' : age
        } # 키 : value값
    return render(request, 'age.html' , context)
    #함수 이름은 urls에서 정의한 것과 같아야 하며 딕셔너리 형식으로 보내기 위해 {}로 덮어준다.
def num(request , num):
    result = num*num # num**2 하면 같다
    re= {'re' : result}

    return render(request , 'num.html' , re)

def count(request , one, two, three):
    if(one == 'plus'):
        result = two + three
    elif(one == 'minus'):
        result = two - three
    elif(one == 'multi'):
        result = two*three
    else:
        result = two/three
    re = {
        're' : result,
        'num1' : two,
        'num2' : three
        }
    return render(request , 'count.html' , re)