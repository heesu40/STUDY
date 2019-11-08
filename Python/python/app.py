from flask import Flask, render_template , request
import random
import requests
from pprint import pprint


app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'

@app.route('/mulcam')
def mulcam():
    return 'Hello mulcamp'

@app.route('/greeting/<string:name>') #String은 받은 것의 타입! name은 변수명!
def greeting(name):
    return f'{name}님 안녕하세요.'
#실행 방법은 http://127.0.0.1:8000/greeting/이희수

@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ["짜장면" , "짬뽕", "라면" , "스파게티", "삼격살" , "수육"] 
    order = random.sample(menu, num) #menu를 기준으로 num만큼 뽑겠다는 메서드
    return render_template('menu.html' , menu=order)

@app.route('/lotto')
def lotto():
    total = range(1,47)
    lottonum = random.sample(total, 6)
    return str(lottonum)

@app.route('/html')
def html():
    mutiline = '''
    <h1> This is H1 Tag</h1>
    <p> This is p Tag</p>
    '''
    return mutiline
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html' , name=name) #앞의 name은 html의 name, 뒤의 name은 주소에 지정한 name

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive' )
def receive():
    name = request.args.get('name') # request들 중에 args들 중에 name이라는 것을 가져오겠다 라는 뜻
    message = request.args.get('message')
    return render_template('receive.html' , name = name, msg = message)

@app.route('/makename')
def makename():
    return render_template('makename.html')

@app.route('/resultname')
def resultname():
    yy = {
            "0":"시끄러운, 말 많은",
            "1":"푸른",
            "2":"어두운 →적색",
            "3":"조용한",
            "4":"웅크린",
            "5":"백색",
            "6":"지혜로운",
            "7":"용감한",
            "8":"날카로운",
            "9":"욕심 많은",
    }
    mm = {
            "1":"늑대",
            "2":"태양",
            "3":"양",
            "4":"매",
            "5":"황소",
            "6":"불꽃",
            "7":"나무",
            "8":"달빛",
            "9":"말",
            "10":"돼지",
            "11":"하늘",
            "12":"바람"
    }
    dd = {
            "1":"와(과) 함께 춤을",
            "2":"의 기상",
            "3":"은(는) 그림자 속에",
            "4":"",
            "5":"",
            "6":"",
            "7":"의 환생",
            "8":"의 죽음",
            "9":"아래에서",
            "10":"을(를) 보라.",
            "11":"이(가) 노래하다.",
            "12":"의 그늘 → 그림자",
            "13":"의 일격",
            "14":"에게 쫒기는 남자",
            "15":"의 행진",
            "16":"의 왕",
            "17":"의 유령",
            "18":"을 죽인 자.",
            "19":"은(는) 맨날 잠잔다.",
            "20":"처럼..",
            "21":"의 고향",
            "22":"의 전사",
            "23":"은(는) 나의 친구",
            "24":"의 노래",
            "25":"의 정령",
            "26":"의 파수꾼",
            "27":"의 악마",
            "28":"와(과) 같은 사나이",
            "29":"의 심판자→을(를) 쓰러뜨린 자",
            "30":"의 혼",
            "31":"은(는) 말이 없다."
    }
    rename = ""
    for i  in yy :
        if(i==request.args.get("year")):
            rename += yy[i] + " "
    for i  in mm :
        if(i == request.args.get("month")):
            rename += mm[i] + " "
    for i in dd:
        if(i  == request.args.get("date")):
            rename += dd[i]
    
    return render_template("resultname.html" , rename = rename)

@app.route('/indian')
def indian():
    return render_template('indian.html')

@app.route('/indian_result')
def result():
    name = request.args.get("name")
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

    res = f'{name} 의 인디언 이름은 {l1+l2+l3}입니다.'
    return render_template('result.html' , res = res)


@app.route('/lotto_num')
def lotto_num():
    url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=881"
    res = requests.get(url).json() #응답만 하는데 json()형태로 변환까지!
    nums = str(res['drwtNo1']) + " "+ str(res['drwtNo2']) + " "+ str(res['drwtNo3']) + " "+ str(res['drwtNo5'])+ " "+ str(res['drwtNo6'])
    return nums

@app.route('/lotto_get')   
def lotto_get():
    return render_template('lotto_get.html')


@app.route('/lotto_num2')
def lotto_num2():
    num = request.args.get('num')
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}"  
    res = requests.get(url).json() #응답만 하는데 json()형태로 변환까지!
    # List comprehension
    # [ 받는 변수 for 받는변수 in 범위로 된 데이터 ]
    wnum = [ res[f'drwtNo{i}'] for i in range(1,7)]
    lotto = random.sample(range(1,47) , 6)
    #리스트를 집합함수로 하는 것 set
    match = list(set(wnum) & set(lotto)) #교집합!!! 같은 값만 나오게 된다.
    count = len(match)
    result = ""
    if count == 6:
        result = "1등입니다."
    elif(count == 5):
        result =  "2등입니다."
    elif(count == 4):
        result =  "3등입니다."
    elif(count == 3):
        result =  "4등입니다."
    else:
        result = "다음기회에..."

    


   
    
    #return f'{res}'
    # return f'{wnum}'
    return render_template('lotto_result.html' , num = num , wnum = wnum , lotto = lotto , msg = result)



if __name__ == "__main__":
    app.run(debug=True, port=8000) 