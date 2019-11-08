from flask import Flask , render_template , request
import requests
from decouple import config
from pprint import pprint
import random


 #이제 따로 저장한 비밀키를 불러올 것이다.

app = Flask(__name__)
token = config('TOKEN') 
base_url = f'https://api.telegram.org/bot{token}'


@app.route('/telegram')
def telegram():
    #.json()이 없으면   
    res = requests.get(f'{base_url}/getUpdates').json() #request 는 .ars.get 이지만 requests는 .get이다.
    chat_id = res['result'][0]['message']['chat']['id']
    lotto = random.sample(range(1,47) , 6)
    
    send_url = f'/sendMessage?chat_id={chat_id}&text={lotto}'

    ress = requests.get(base_url + send_url)
    
    return ''

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_msg')
def send_msg():
    #form 에서 chat라는 이름의 데이터를 받아오는 곳.
    req = request.args.get("chat")

    #chat_id값을 받아 오기 위해 사용된 2종
    res = requests.get(f'{base_url}/getUpdates').json() #request (응답)는 .ars.get 이지만 requests(요청)는 .get이다.
    chat_id = res['result'][0]['message']['chat']['id']
    
    #telegram 에 메세지를 보내기 위한 url
    send_url = f'/sendMessage?chat_id={chat_id}&text={req}'
    response = requests.get(base_url + send_url)
    return "보내기 완료"

@app.route('/' , methods=['POST'])
def tel_web():

    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = "https://openapi.naver.com/v1/papago/n2mt"
    #받는 건 request 주고 받고는 requests
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" ,
        "X-Naver-Client-Id": C_ID ,
        "X-Naver-Client-Secret": C_SC
    }
    
    req = request.get_json().get('message')
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
    #각각에서 랜덤으로 하나 뽑기 위핸
    l1 = random.choice(yy)
    l2 = random.choice(mm)
    l3 = random.choice(dd)

    if req is not None:
        chat_id = req.get('chat').get('id')
        text = req.get('text')
    lotto = random.sample(range(1 , 46) , 6)
    send_url = f'/sendMessage?chat_id={chat_id}&text='

    # if text == "로또":
    if "로또" in text:
    
        msg= f'{lotto}'

    elif "인디언" in text:

        msg =  f'{l1+l2+l3}'
    elif "/번역" in text:
        #/번역 내용
        re_txt = text.replace("/번역" , "")
        data = {
            "source" : "ko",
            "target" : "en",
            "text"  : re_txt
        }
        res = requests.post(url, headers = headers , data = data).json() #json()이 없으면 <Response[200]>으로 응답만 날아온다.
        msg = res.get('message').get('result').get('translatedText')

    else:
        msg = text
    #응답이 없으면 텔레그램에서 계속 데이터를 보내므로 return을 아래처럼!

    response = requests.get(base_url + send_url + msg)   


    return '', 200


@app.route('/papago' , methods=['POST'])
def papago():

   
    url = "https://openapi.naver.com/v1/papago/n2mt"
    C_ID = config('C_ID')
    C_SC = config('C_SC')
   
    


    #headers가 필요하기 때문에 (키 값 보내기위한)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" ,
        "X-Naver-Client-Id": C_ID ,
        "X-Naver-Client-Secret": C_SC
    }
    data = {
        "source" : "ko",
        "target" : "en",
        "text"  : "안녕하세요."
    }
    

    req = requests.post(url, headers = headers , data = data).json() #json()이 없으면 <Response[200]>으로 응답만 날아온다.
    
    
    


    return "Finish!"


if __name__=="__main__":
    app.run(debug=True)  