# HTTP Client-Server Architecture

피씨에 입력된 도메인 서버 

도메인 요청시 도메인서버에 ip address가 요청되고 다운된다. (http request라 한다.)

http request 는 header구조(메타정보가 포함되어 있다.)와 body구조를 가지고 있다.

webserver 는http request를 받아서 서비스 응답 하는 것! 기본 포트는 80포트이다.  

도메이만 요청시 만약 페이지 지정을 하지 않았다면 welcom페이지를 자동으로  index.html,main .html 로...... 구성은 httprequest 에 html바디를 가지고 있다.

html해석을 한다.객체 모델,트리구조 

renderer모델? 이 css를 적용한다. 각.....각 이후 브라우저에 스타일이 쭈욱 보이는 것이다.

 web server 기능만 있는 것을 예를 들어 Apache http web server

가 있으며 web sever+webContainer(JVM포함)(JSP/server)

WAS(web application Server)

## 웹 어플리케이션

#### HTTP MESSAGE

- 웹 어플리케이션은 요청과 응답으로 서버의 데이터를 클라이언트에 보여준다. 모든것은 요청과 응답으로 이루어진다.
  -  즉 비연결 프로토콜이다.(소켓은 대표적으로 계속 연결되어 있다. 예를 들어 카톡 같은 대화)
- HTTP Request 메시지의 구성--요청라인, 요청헤더,  공백라인, 메시지 본문
- HTTP Resopnse 메시지의 구성- 상태라인(아주 중요), 응답헤더,공백라인,메시지 본문
  - 상태라인이 200이면 성공, 500은 서버 에러 ,400은 가장많이 만나는 에러

#### HTTP Request

- HTTP 요청은 형식이 있다

  1. get 

     - 얻는 방식으로
     - 단순 페이지 요청,검색어 요청
     - 절대 민감한 내용을 담으면 안된다. 길이 제한도 있다.

  2. post

     - 서버에 데이터를 보내기위해 사용

     -  http프로토콜 바디에 넣어 보내던가 보안처리해서 보내야할떄 사용

     - 회원가입,로그인 같은 중요 내용 요청시 필요하다

       

  3. put

  4. head

  5. ....등

####  HTTP 응답

- 도메인/(요 짝대기를 root contes?)  bbs/ test.html 구조다
- HTTP 응답에는 응답상태와 헤더, 그리고 메시지 바디를 포함한다.
- 브라우저는 메시지 바디의 내용을 파싱하여 브라우저 화면에 보여준다.

![1560385888604](../../sole/1560385888604.png)

body에 중요 포스트 정보가 있는 것을 확인 할 수 있다.

#### 응답코드



###  톰캣 설치&이클립스연동

1.  http://tomcat.apache.org 에서 Tomcat  9 버전 설치(최신으로 하자)
2. 그후 연동을 해야하는데 이클립스를 실행하고
3. window->  Preferences -> Server-> Runtime Environment  에서 add를 하는데 경로는 톰캣폴터를 잡는다.(가장 큰 톰켓 폴더를 말한다.) 
4.  import된 파일을 연동하기 위해서 이클립스 실행후 아래쪽 창에서( Console이 있는) Servers에서 연결된 서버가 없으므로 클릭하여 원하는 파일을  넘겨주어 연결시킨다. 만약 오류가 뜬다면 서버를 삭제한후 다시 이클립스 실행후 연결해보자. 잘 연결될 것이다.

# 웹 역사

## www

- 1990년대 초반  팀리버스가 만들었다.

- window95 고 browser 는 nescape 와 ie 가 있다.

- 단순 html서비스 , 단순 view 

- 요청, 응답 방식인데 **동기방식**이다. 요청을  하면 응답이 올때까지 아무작업을 하지 못한다. 또는 **전체페이지갱신방식**이라 한다.

- **정적 서비스**로 복잡한 작업을 하지 못한다.

  ----그 후 방식이 좀 바뀌었다.(**CGI 방식**)-----------

-  정보를 OS에 넘긴다. CGI Process가 계산하고, htmlpage 를 생성하고 OS에 리턴하면 OS가 웹서버를 통해 넘겨준다. 문제점은 사람이 몰리면 재기능을 하지 못한다.

  ----이 방식을 개선하기 위해서 (**스레드방식**)------

- 단순 웹서버기능뿐만 아니라  http listerner(Demon),web container로 나뉘어 있으며 web container는 JSP /Servlet에서 html페이지를 생성하고 JUM의 GC로 응답한 내용을 삭제한다. 스레드방식으로 효율적이다.

  

- Front end/ Back end 방식으로도 나눌수 있는데

  - Front end
    - 이용자의 눈에 보이는 부분 개발(HTML,CSS,JAVASCRIPT)
    - html(구조)
      - 문서 구조만 담당
    - Css(표현)
    - javascrip(동작)
    - RIch Client internet
      - flash IE(active X)
      - Ajax(비동기 자바스트립트를 이용한 and xml)
        - 요청후 전체 페이지 갱신 방식이 아니라서 다른 작업을 해도 된다. 
        - 가장 많이 사용되는 것은 검색어 top10
    - w3c->웹표준화 (2000년대 쯤)
  - Back end
    1. 이용자의 눈에 보이지 않는 부분 개발(Server DB API)
    2. servlet(Server Applet) 
    3. JSP(mode1방식)
    4. EJB(분산처리)
    5. servlet(controler),JSP<view>
    6. framwork(stauts),Spring?
    7. 전자정부표준화

## HTML5

- web workers 통해 백그라운드에서 javaScript처리하는 것으로 javaScript로 게임을 만드는 것이 가능해짐

- server-sent 

  - 서버가 요청하는 ,..알림같은

- socet

  - 비연결 프로토콜을 연결 프로토콜을 연결로 해주는

  

  

## HTML 과 웹브라우저

- 생성시 반드시 문서 유형 선언이 있어야한다.

- ```html
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="uft-8">
  <title>hello.html</title>
      <style>
      body{
      font-size: 20px;
          color: red;}
      </style>
  </head>
  <body>
  안녕하세요? 처음 만들어보는 html문서인가요?
  </body>
  </html>
  ```

style 보기 위해서

<https://www.w3schools.com/> 참고하자!

css 는 너무 양이 방대하기 때문에 필요할떄마다 찾아 쓰도록 하자. 밑에는 그 중 하나의 내용을 클릭해 보았다.  name 부분이다.

a 앵커 태그로 href와 함께 웹 페이지 내부에서 특정한 위치로 이동할때 사용

```html
<!DOCTYPE html>
<html>
<body>

<p>
<a href="#C4">See also Chapter 4</a>
    <!--c4라 이름지어진 장소로 이동-->
</p>

<p>
<h2>Chapter 1</h2>
<p>This chapter explains ba bla bla</p>

<h2>Chapter 2</h2>
<p>This chapter explains ba bla bla</p>

<h2>Chapter 3</h2>
<p>This chapter explains ba bla bla</p>

<h2><a name="C4">Chapter 4</a></h2>
<p>This chapter explains ba bla bla</p>
</body>
</html>

```

## 속성

- 태그
- 태그+내용 = 요소(element)

## html 구조

기본 구조

```html
<!DOCTYPE html>
<html>
<head>
  <title>제목</title>
  <meta charset="utf-8" /><!--전세계 문자와 기호를 표시하기 위해 utf-8를 사용-->
</head>
<body>
  <h1>Hello</h1>
  <div>
    <p>쓰고자 하는 글</p>
    <img src="주소"/>
  </div>
</body>
</html>
```

### 입력양식 태그

- type속성에는 이런것을 작성한다.
- `< input type=" 속성">`으로 작성해준다.

![1560409360019](../../sole/1560409360019.png)

### 공간분할 태그

- html5는 다음과 같은 시멘틱 공간 분할 태그를 가지고 있다.

![1560411576964](../../sole/1560411576964.png)

- div 공간 차지 
- embed  별도의 플러그인 영역을 넣어준다. 혹은 외부 어플리케이션이 들어갈 영역
- fielset  범례제목과 테두리를 넣어서 그룹핑 해준다. 테두리 넣어주는 기능
- figcaption ,figure img와 figcaption을 figure로 쌓아주어야 한다. 이 기능으로 인해 이미지와 글이 관련이 있음을 알 수 있게 해 준다. 
- iframe   다른 사이트 넣어주기!
- label   특정 input태그를 연결시킬 때 라벨링 한다. 관련있음을 알수 있다.
- link    head 태크안에 css파일을 적용시킬때 사용 type은 생략하면 text/css
- mian   article작성시 결론에 해당하는 내용
- map    image-map은 클릭가능한 이미지의 maping을 보여준다.(이미지 클릭시 그 관련 이미지를 보여 줄 수 있다.)
- mark   형광펜 같은 효과
- meta   html를 실행시키는 환경에 따라 (모바일,pc등) 적절하게 변하는 것, 크기가 다른 html를 여러개 만드는 것이 아니다.

### footer 하단 에 놓기

```html
      <div class="clear"></div>
<footer>
        꼬리말입니다. 회사 연락처 등
 </footer>
```

- 웹사이트 구조 만들어 보기

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>semantic3</title> 
	<style>
		header { background:yellow; border:2px solid blue;
		    position:relative;
			margin-bottom:10px;}
		nav { background:lime; border:1px solid red;position:absolute;
			right:5px;bottom:2px;width:300px; }
		section { padding:10px;maring:10px;border:1px solid black;
			background:lightgray;width:70%; }
		article { padding:20px;margin:10px;border:1px solid black;
			border-radius:8px;background:beige; }
		aside { float:right;width:20%;background:orange;
		padding:10px; }
		footer { background:yellow; border:1px solid blue;
		margin-top:10px; }

	</style>
<body>
	<header> <h2>머리말입니다.</h2>
		<nav> 내비게이션 영역. 이전, 이후, 홈</nav>
	</header>
	<aside> 광고입니다. 계란 사세요. 계란</aside>
	<section>
		<article> 첫 번째 기사 </article>
		<article> 두 번째 기사 </article>
		<article> 세 번째 기사 </article>
	</section>
	<footer> 꼬리말입니다. 회사 연락처 등</footer>
</body>
</html>

```

### 가볍게 강아지 설명 만들어보기

```html

<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="utf-8">
	<title>강아지 키우기</title>
	<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>
	<header>
		<h1>입양하기</h1>
		<nav>
			<ul>
				<li><a href="#">애완견 종류</a></li>
				<li><a href="#">입양하기</a></li>
				<li><a href="#">건강돌보기</a></li>
				<li><a href="#">더불어살기</a></li>
			</ul>
		</nav>
	</header>
	<section>
		<h2>강아지 용품 준비하기</h2>
		<img src="puppy.png" id="puppy">
		강아지 집
		강아지가 편히 쉴 수 있는 포근한 집이 필요합니다. 강아지의 집은 강아지가 다 큰 후에도 계속 쓸 수 있는 집으로 구입하세요.집을 구입하실 때는 박음질이 잘 되어 있는지, 세탁이 간편한 제품인지 꼭 확인하시고 고르시는 것이 좋습니다.
		
		강아지 먹이
		강아지의 먹이는 꼭 어린 강아지용으로 나와있는 사료를 선택하세요. 강아지들은 사람에 비해 성장속도가 8배정도 빠르답니다. 따라서 강아지에게는 성장속도에 맞는 사료를 급여하셔야 합니다. 사람이 먹는 음식을 먹게 되면 양념과 향신료에 입맛이 익숙해지고, 비만이 될 가능성이 매우 높아집니다. 강아지용 사료는 생후 12개월까지 급여하셔야 합니다.
		
		밥그릇, 물병
		밥그릇은 쉽게 넘어지지 않도록 바닥이 넓은 것이 좋습니다.물병은 대롱이 달린 것으로 선택하세요. 밥그릇에 물을 주게 되면 입 주변에 털이 모두 젖기 때문에 비위생적이므로 대롱을 통해서 물을 먹을 수 있는 물병을 마련하시는 것이 좋습니다.
		
		이름표, 목줄
		강아지를 잃어버릴 염려가 있으니 산책할 무렵이 되면 이름표를 꼭 목에 걸어주도록 하세요. 그리고 방울이 달린 목걸이를 하고자 하실 때는 신중하셔야 합니다. 움직일 때마다 방울이 딸랑 거리면 신경이 예민한 강아지들에게는 좋지 않은 영향을 끼칠 수 있기 때문입니다.
	</section>
	<footer>
		<p>Copyright 2012 funnycom</p>
	</footer>
</body>
</html>
```

## 글자스타일 지정

- 

## html 문서 

- < !DOCTYPE html > 로 선언을 시작한다.

  - < html >은 두개의 하위를 가진다.

    - 태크 -구조 관련 명령어, 브라우저에 포함된 파서가 해석을 한다.생성결과물은 DOM Tree(document object model)를 생성
    - element -태그+내용  Renderer가 포함시킨다.

  - < style >

    - < link  rel ="stylesheet"  type="test/css" src="문서 경로" > 

      - 문서 경로가 상위에 있다면 "../css/style.css" 점 두개를 찍어준다.
      - 같은 경로에 있다면 "./css/style.css" 점 한개를 찍어준다.
      - css 문서에서의 주석은 /* css 주석 내용 */
      - 저장  인코딩 방식 @ charset =utf-8
      - css 선택자

      ```css
      select{
          속성: 값 값;
      }
      /*body>div>p>span순서로 스타일을 주고 싶을시 -->*/
      div p span {
      }
      /*<div id="header"> #을 넣어 준다.*/
      인경우 
      #header{} 로 css작성
      /*<div class="stde" . 점 하나를 찍어 준다.*/
      .stde{} 
      
      ```

      

- dtd문서가 있어서 잘 작성됐는지 체크 해준다. 체크를 validator가 해주는데 결과가 좋으면 wellformed하다 라고 뜬다.

- dtd다음에는 schema 문서로 검증을 한다.

## 박스 모델

- 박스 형태로 된 모든 html요소
  - 경계선, 마진, 패딩 지정 가능
  - 동서남북으로 다르게 값을 지정 가능

![1560733929559](../../sole/사진)

#### border

스타일

- solid 실선
- double 이중실선
- dotted 점선
- dashed 줄선

#### pading

- padding-top, right,bottom, left 시계방향으로...

## 레이아웃

#### 관련태그(html5이전)

- < div /> 이용하여 header menu content side footer영역 만든다.  

#### 관련태그(html5)

- < header >
- < nav > - 제목의 메뉴
- < aside > 본문의 사이드
- < footer > 회사 번호 등의 내용
- < section > 본문
  - < article > 본문의 내용
- <  inline > 수평 방향 레이아웃 
- < block > 수직 방향 레이아웃



![1560752403154](../../sole/1560752403154.png)

- 너비는 80px

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
table,th,td{
    border:solid 1px blue;
    border-collapse: collapse;
}
th{
    width: 80px;
    padding:6px;
}
td{
    padding:6px;
    text-align:center;
}

#day{
    background-color: aquamarine;
}
#title{
    background-color: skyblue;
}
</style>
</head>
<body>
<h2>고속버스 예매</h2>
<table>
  <tr id='day'>
    <th colspan='4'>서울 &lt=&gt 대전 2020.9.6 수</th>
  </tr>
  <tr id='title'>
    <th>출발</th>
    <th>버스회사</th>    
    <th>등급</th>  
    <th>예약가능</th>    
  </tr>
  <tr>
    <td>11:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='매진.png'></td>
  </tr>
  <tr>
    <td>12:50</td>
    <td>천일고속</td>
    <td>고속</td>
    <td><img src='예약하기.png'></td>
  </tr>
  <tr>
    <td>13:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='매진.png'></td>
  </tr> 
</table>
</body>
</html>
```



![1560752164579](../../sole/1560752164579.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
    *{
        margin:0;
        padding:0;
    }
    ul{
        list-style-type:none;
    }
    #main_title {
    font-family:'맑은고딕';
    margin:10px;
    padding-bottom:6px;
    border-bottom:solid 2px #aaaaaa;
    }
    .lest_item{
       clear:both;
       height:130px;
       margin:10px;
       border-bottom:solid 1px #cccccc;
    }
    .image{
        float:left;
        width: 80px;
        height: 80px;
    }
    .intro{
        float:left;
        width:300px;
        margin-left:20px;

    }
    .price{
        float:left;
        width:150px;
    }
    .red{
        font-weight:bold;
        color:red;
    }
.samll{
    font-size: 12px;
    margin-top: 5px;
}
.writer{
    float:left;
    width:100px;
}
.img{
    width:100px;
    height:120px;
}

        </style>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h3 id='main_title'>판매도서 목록</h3>
    <div class='lest_item'>
        <div class='image'><img class="img" src='이미지1.jpg' ></div>
        <div class='intro'>[문학동네]여행의 이유</div>
        <ul class='price'>
            <li class='red'>13,500원</li>
            <li calss='small'>배송비 2,500원</li>
        </ul>
        <div class='writer'>김영하 저</div>
    </div>
    <div class='lest_item'>
            <div class='image'><img class="img" src='이미지2.jpg' ></div>
            <div class='intro'>[문학동네]천년의 질문</div>
            <ul class='price'>
                <li class='red'>14,800원</li>
                <li calss='small'>배송비 2,500원</li>
            </ul>
            <div class='writer'>조정래 저</div>
        </div>
</body>
</html>
```



#### 속성 선택자

![1560749722556](../../sole/1560749722556.png)

- id 와 class 를 사용하지 않고도 속성을 선택할 수 있다. 

#### 자손 선택자

- header  밑에 h3 div div , div 밑에 h3이 있는 경우

  

  ```html
   header h3{
   color: blue;
   } <!-- 모든 h3 이 다 변한다.-->
  header >h3{
  color:red;
  }<!--바로 아래의 자손의 h3만 변한다.-->
  
  ```

  #### 동위 선택자

  - 형제태그중 뒤에 오는 형제태크를 선택할 떄 사용
  - 선택지 a+선택지b 
    - a선택지 바로 뒤에 오는 선택지 b
  - 선택지 a~선택지b
    -  a선택지 뒤에 위치하는 모든 선택지b

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        h1+h2{
color:Red;
        }
        h1~h2{
            background-color:orange;
        }
        </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>header-1</h1>
    <h2>header-2</h2>
    <h2>header-2</h2>
    <h4>header-2</h4>
    <h5>header-2</h5>
</body>
</html>
```

#### 반응선택자

- 마우스를 올렸을때의 색 바뀜은 h1:hover
- 클릭했을때의 색 바뀜은 h1:active

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        h1:hover{
            color:skyblue;

        }
        h1:active{
            color:red;
        }
        h2:hover{
            color:orange;
        }
        h2:active{
            color:red;
        }
        </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>header-1</h1>
    <h2>header-2</h2>
   
</body>
</html>
```

#### 상태선택자

- 입력 양식의 상태를 선택할 때 사용하는 선택자

![1560753582389](../../sole/1560753582389.png)



#### 구조선택자

![1560753534893](../../sole/1560753534893.png)

- 일반적으로 자손 선택자와 병행해서 많이 사용하며 특정한 위치에 있는 태그를 선택하는 선택지이다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        ul{
            overflow:hidden;
        }
        li{
            list-style: none;
            float:left;padding:15px;
        }
        li:first-child{
            border-radius:10px 0 0 10px;
        }
        li:last-child{
            border-radius:0 10px 10px 0;
        }
        li:nth-child(2n){
            background-color:skyblue;
        }
        li:nth-child(2n+1){
            background-color:paleturquoise;
        }
        </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>first</li>
        <li>second</li>
        <li>third</li>
        <li>fourth</li>
        <li>fifth</li>
        <li>sixth</li>
        <li>seventh</li>
    </ul>
</body>
</html>
```



#### 형태 구조 선택자

![1560753833894](../../sole/1560753833894.png)

#### 문자 선택자

- p::first-letter     첫번째 문자
- p::first-line	   첫번째 줄

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        p::first-letter{font-size: 3em} <!-- em은 배 수다 3배의 크기란 뜻 -->
       	
        p::first-line{ color:red;}
        </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>우리에게 저녁이 있는가!</h1>
    <p>저녁은 우리의 힐링이요 사랑으로써 반드시 먹어야 하는것이다.</p>
    <p>허나 멀캠은 저녁은 주지 않는 만행을 저질렀으며! 심지어 식권을 무료 지급하지 않았다!</p>
</body>
</html>
```

#### 반응문자선택자

- 드래그 하면 배경과 글 색이 바뀌는 것으로 ::selection 이다.

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        p::first-letter{font-size: 3em}
        p::first-line{ color:red;}
        p::selection{
            background:skyblue; color :orange;
        }
        
        </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>우리에게 저녁이 있는가!</h1>
    <p>저녁은 우리의 힐링이요 사랑으로써 반드시 먹어야 하는것이다.</p>
    <p>허나 멀캠은 저녁은 주지 않는 만행을 저질렀으며! 심지어 식권을 무료 지급하지 않았다!</p>
</body>

</html>
```

#### 링크 선택자

- 하이퍼링크가 연결된 문자열은 처음은 파란색이고 클릭시 빨간색, 갔다 왔던 곳은 보라색으로 남는다. 이 색을 바꿀 수 있다.
- : link  
  - href 속성을 가지고 있는 a태그를 선택한다.
- : visited
  - 방문했던 링크를 가지고 있는 a태그를 선택한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
    a:visited{ color:green;
    }
    a:link:after{
        content:' -  'attr(href)
      
    }

    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1><a>Nothing</a></h1>a
    <h1><a href ="http://www.naver.com">네이버</a></h>
    <h1><a href="http://www.daum.net">다음</a></h1>
</body>
</html>
```

#### 부정선택자

- :not  선택자를 반대로 적용

### CSS3

#### 단위

````html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { }
        p:nth-child(2) { font-size: 100%; }<!--기본과 같은 사이즈-->
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }
    </style>
</head>
<body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</body>
</html>
````

#### 색상단위

![1560756269764](../../sole/1560756269764.png)

#### 가시 속성

##### display

- none - 태그를 화면에 안보이게
- block - 수직으로
- inline - 수평으로, 한줄에 들어간다. margin-padding속성이 좌우로
- inline-block - inline-block형식 , 한줄에 들어간다. margin-padding속성이 상하좌우 적용

##### visibility 속성

- 대상을 보이거나 보이지 않게 지정하는 속성.
- visuble 태그를 보이게 한다.
- hidden 태그를 보이지 않게 한다.
- collapse table 태그를 보이지 않게 만든다.

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { }
        p:nth-child(2) { font-size: 100%; }
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }
        table{
            visibility: collapse;
        }
    </style>
</head>
<body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <table>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
    </table>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</body>
</html>
```

##### opacity 속성

- 대상의 투명도를 지정하는 속성
- 0~1사이의 숫자인데 0은 투명 1은 불투명이다.

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { }
        p:nth-child(2) { font-size: 100%; }
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }
        
        #box{
            background-color:red;
            color:white;
            opacity:0.2;
        }
    </style>
</head>
<body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <table id="box">
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
    </table>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</body>
</html>
```

#### 배경속성

##### position 속성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
    .box{
        width:100px;height: 100px;
        position:absolute;
    }
    .red{
        background-color:red;
        left:10px; top:10px;
    }
    .green{
        background-color: green;
        left:50px; top: 50px;
    }
    .blue{
        background-color: blue;
        left:90px; top: 90px;
    }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <div class="box red"></div>
        <div class="box green"></div>
        <div class="box blue"></div>
</body>
</html>
```

##### z-index 속성

- z-index가 큰 순서대로 앞으로 나오게 된다. 아래에 주어진 1000은 과하게 크게 쓴 것이고 3,2,1로만 작성해도 충분히 출력된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
    .box{
        width:100px;height: 100px;
        position:fixed;
    }
    .red{
        background-color:red;
        left:10px; top:10px;
        z-index:10000;
    }
    .green{
        background-color: green;
        left:50px; top: 50px;
        z-index: 9999;
    }
    .blue{
        background-color: blue;
        left:90px; top: 90px;
        z-index: 9998;
    }
    </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <div class="box red"></div>
        <div class="box green"></div>
        <div class="box blue"></div>
</body>
</html>
```

##### overflow 영역

- hidden -영역을 벗어나는 부분은 보이지 않게
- scroll- 영역을 벗어나는 부분을 스크롤로

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
 <style>
        .box {
            width: 100px; height: 100px;
            position: absolute;
        }
        .box:nth-child(1) {
            background-color: red;
            left: 10px; top: 10px;

            z-index: 100;
        }
        .box:nth-child(2) {
            background-color: green;
            left: 50px; top: 50px;

            z-index: 10;
        }
        .box:nth-child(3) {
            background-color: blue;
            left: 90px; top: 90px;

            z-index: 1;
        }
        
        body > div {
            width: 400px; height: 100px;
            border: 3px solid black;

            position: relative;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <h1>Lorem ipsum dolor amet</h1>
    <div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
    <h1>Lorem ipsum dolor amet</h1>
</body>
</html>
```

##### 벤더 프리픽스

- 웹 브라우스 공급업체에서 제공하는 실험적인 기능 사용시 이용하는 것
- 새로운 기능을 모두 제공해야 함으로 벤더 프리픽스를 사용해 지원

##### 그레이디언트

- 2가지 이상의 색상을 혼합한 색을 만들어 채색하는 기능

<https://tomcat.apache.org/download-90.cgi> 사이트에 들어가 tomcat 9 의 zip를 다운받는다.

다운을 풀고 bin 파일에 startup (window~ )파일을 실행시킨상태에서 브라우저 localhost:8080을 로그인한다!

