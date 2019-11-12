from django.shortcuts import render
from pprint import pprint
import random
from requests import get
import requests

# Create your views here.
def throw(request):
    return render(request, 'pages/throw.html')
def catch(request):
    # pprint(request)
    # pprint(request.path)
    # pprint(request.method) 
    # pprint(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message')
    context = {
        'msg' : message,
        'msg2' : message2
    }
    return render(request , 'pages/catch.html' , context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lottoresult(request):
    co = request.GET.get('count') #request로 넘어오는 값 중 GET방식의 count를 얻을 것이다
    print(type(co)) #확인해보자 어떤 타입인지! 결과는 str!

    count = int(request.GET.get('count')) #형변환 해준다.
    lotto_num = []
    for i in range(count):
        lotto_num.append(random.sample(range(1,46), 6)) #랜덤한 로또번호 추출해서 넣어준다.
    context = {
        'count' : count ,
        'lotto' : lotto_num
    }
    return render(request, "pages/result.html", context)
def artiii(request):
    return render(request, 'pages/artiii.html')

def artiiisend(request):
    txt = request.GET.get("artiii")

    f_url = "http://artii.herokuapp.com/fonts_list"
    fonts = requests.get(f_url).text #text이기 때문에
    print(fonts) #터미널에는 안보이지만 \n으로 되어있을 것이다.
    font = fonts.split('\n')
    print(font) #배열에 담겨있는 폰트들을 확인 가능하다
    
    font = random.choice(font)

    url = f"http://artii.herokuapp.com/make?text={txt}&font={font}"
    print(url)
    res = requests.get(url).text
    
    
  
    context = {
        "res" : res
    }
    
    return render(request, 'pages/artiiire.html' , context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')
    context = {
        'username' : username,
        'pw' : pw
    }
    return render(request , "pages/user_create.html" , context)
def subway(request):
    return render(request, "pages/subway.html")
def subway_result(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get('bb')
    source = request.POST.get('source')

    context = {
        'name' : name,
        'date' : date,
        'sandwitch' : sandwitch,
        'size' : size,
        'bread' : bread,
        'source' : source
    }
    return render(request , "pages/subway_result.html" , context )
def static_ex(request):
    return render(request, 'pages/static_ex.html')
def index(request):
    return render(request, 'pages/index.html')