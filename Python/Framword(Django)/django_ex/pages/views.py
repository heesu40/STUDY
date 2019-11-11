from django.shortcuts import render
from django.http import HttpResponse #Text를 보낼 떄 사용
import random
from faker import Faker
from datetime import datetime

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

def profile(request , name, age):
    yy = [
            "시끄러운, 말 많은",
            "푸른",
            "어두운 →적색",
            "조용한",
            "웅크린",
            "백색",
            "지혜로운",
            "용감한",
            "날카로운",
            "욕심 많은",
    ]
    mm = [
            "늑대",
            "태양",
            "양",
            "매",
            "황소",
            "불꽃",
            "나무",
            "달빛",
            "말",
            "돼지",
            "하늘",
            "바람"
    ]
    dd = [
            "와(과) 함께 춤을",
            "의 기상",
            "은(는) 그림자 속에",
            "",
            "",
            "",
            "의 환생",
            "의 죽음",
            "아래에서",
            "을(를) 보라.",
            "이(가) 노래하다.",
            "의 그늘 → 그림자",
            "의 일격",
            "에게 쫒기는 남자",
            "의 행진",
            "의 왕",
            "의 유령",
            "을 죽인 자.",
            "은(는) 맨날 잠잔다.",
            "처럼..",
            "의 고향",
            "의 전사",
            "은(는) 나의 친구",
            "의 노래",
            "의 정령",
            "의 파수꾼",
            "의 악마",
            "와(과) 같은 사나이",
            "의 심판자→을(를) 쓰러뜨린 자",
            "의 혼",
            "은(는) 말이 없다."
    ]
    l1 = random.choice(yy)
    l2 = random.choice(mm)
    l3 = random.choice(dd)
    ll = l1 + l2 + l3

    
    lotto = random.sample(range(1,46) , 6)
    lotto.sort()
    print(lotto)
    print(lotto[0])


    prof = {
        'name': name,
        'age' : age,
        'fullname' : ll,
        'a' : lotto[0],
        'b' : lotto[1],
        'c' : lotto[2],
        'd' : lotto[3],
        'e' : lotto[4],
        'f' : lotto[5],
    }
    return render(request, 'ex.html' , prof)
def job(request, name):
    fake = Faker("ko_KR")
    job = fake.job()

    result = {
        'name' : name,
        'job' : job
    }

    return render(request , 'faker.html', result)

def image(request):
    num = random.choice(range(1,100))
    url = f"https://picsum.photos/id/{num}/200/300"
    #id를 랜덤하게 바꿔줄것이다! {num}두의 숫자는 폭이랑 너비다

    context = {
        'url' : url
    }
    return render(request, 'image.html' , context)

def dtl(request):
        foods = ["짜장면" , "탕수육" , "짬뽕" , "양장피" , "군만두" , "고추잡채" , "칠리새우"]
        my_sentence = "life is short, you need python"
        messages = ["apple", "banana" , "cucumber" , "mango"]
        datetimenow = datetime.now() #현재 시간이 저장이 된다. 참고로 import 해야한다.
        empty_list = []

        context ={
            "foods" : foods,
            "my_sentence" : my_sentence,
            "messages" : messages,
            "timenow": datetimenow,
            "empty_list" : empty_list,
        }
        return render(request , "dtl.html" , context)
def chmas(request):
    datetimenow = datetime.now()
    print(datetimenow.month)
    print(datetimenow.year)

    if datetimenow.month == 9 and datetimenow.date == 1:
        res = True
    else :
        res = False
    birthday = datetime(2020 , 9 , 1)

    d_day = (datetimenow - birthday).days
    result ={
        'date' : datetimenow,
        'result' : res,
        "D_day" : d_day
    }
    return render(request, 'chmas.html' , result)