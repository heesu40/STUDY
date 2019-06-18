# 1장 특징

### 1.1 자바스크립트

1. 인터프리터 언어
   - 한줄 씩 기계어로 번역해서 실행 하는 언어
   - 느릴 것 같지만 최근 JIT(Just in time compiler)가 내장되어 있어 실행 속도가 매우 빠르다.
2. 동적 프로토타입 기반객체 지향 언어
   - 클래스가 아닌 프로토타입을 상속하는 프로토타입 기반 객체 지향 언어
3. 동적 타입 언어
   - 타입 선언을 하지 않고, 저장되는 값에 따라 그때그때 달라진다.
4. 함수가 일급 객체
   - 함수가 
5. 함수가 클로저 정의
   - 클로저로 변수 은닉 하거나 영속성을 보장한다.

#### 기술적 요소

1. 코어 언어
   - ECMAScript
2. 클라이언트 측의 고유한 기술 목록
   - ECMAScript와 웹 브라우저의 API로 구성
     - Window 인터페이스
     - DOM
     - XMLHttpRequest
3. 서버 측 자바스크립의 고유한 기술 요소
   - Node.js   =>웹 어플리케이션 만들때 가장 많이 사용
   - Rhino
   - Aptana Jaxer

### 1.2자바스크립트 역사

# 2장 프로그램의 작성과 실행

### 2.1 웹 브라우저 Node.js실행

- 크롬과 Node.js 사용한다.
- `httts://nodejs.org/ko/download/`

#### 2.1.1 텍스트 편집기 준비

- 서브라임 텍스트 `https://www.sublimetext.com/`

- 저장시
  - 파일 이름 끝에 확장자는 .js
  - 파일

#### 2.1.2 저장시

- 

#### 2.1.3 HTML문서에 자바스크립트 포함 위치



```html
<head>
<script>
//자바스크립트 코드 -전역변수 선언, 함수 선언
    //body의 요소를 참조하거나, 사용하는 자바스크립트 실행 문장이 오면 오류발생
    </script>
</head>
<body>
<script>
//자바스크립트 코드- 즉시 실행 문장 코드
    </script>
</body>
```

- HTML문서와 자바스크립트를 분리하는 것을 권장

```html
<head>
    <script type="text/javascript" src="경로/파일.js"> //분리된 파일 설정
    </script>
</head>
<body>
    
</body>
```

#### 2.1.4 실행  과 오류

##### 실행



![1560820397326](C:\Users\student\Documents\GitHub\sole\1560820397326.png)

todcat실행후 (Start up (window) 실행을 한다.)

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
        window.alert("head 태그네에 포함된 javascript실행")
        </script>

</head>
<body>
    <script>
        alert("body 태그내에 포함된 javacript 실행")
        </script>
</body>
</html>
```

- 저장은 `C:\apache-tomcat-9.0.21\webapps\ROOT` 에 저장을 한후 저장된 파일을 실행해 보자. 주소는 `http://localhost:8080/`+ 그 이후 주소를 작성한다.
- 외부 참조 후 실행

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="./first.js">
       
        </script>

</head>
<body>
외부 javascript파일을 로딩해서 실행합니다.
</body>
</html>
```

```js
window.alert("first.js파일에 저장된 javascript코드 실행");//파일이름은 first.js
```

##### 오류

- 메모리에 저장된 상태에서만 script에서 찾을수 있다.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
        var msg=document.getElementById("div1");
        // 이 문서 객체를 찾아서........
       window.alert(msg);
        </script>

</head>
<body>
  <div id="div1">
      body태그내에 div 태그입니다.
  </div>
</body>
</html>
```

- 허나 요즘은 브라우저가 오류를 잘잡아서 오류 안뜬다......

### 2.2 프로그램 작성

- 대소문자 구별
- 유니코드 문자로 작성

# 3장 변수와 값

### 3.1변수

- 변수란 값을 담기 위해 이름 붙인 상자의 이름이 변수다.
- var 선언자
- sum 변수이름
- var sum; 로 선언한다.
-   자바 스크립트에서 문자열은 "" 또는 '' 로 감싸 준다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    #자바스크립트에서 변수 선언은 var변수명;<br>
    var 변수명=초기값; 
    자바 스크립트에서 문자열은 "" 또는 '' 로 감싸 준다.
    
    <script>
    var sum,a;
    console.log("a="+a);//콘솔에 출력 a를
    document.write("sum="+sum);
    </script>
</body>
</html>

```

- 결과 값은 `#자바스크립트에서 변수 선언은 var변수명;
  var 변수명=초기값; 자바 스크립트에서 문자열은 "" 또는 '' 로 감싸 준다. sum=undefined` 이다.
- 변수를 선언하고 초기화 하지 않으면, 아직 메모리에 생성되지 않은 상태이므로 출력을 하면 undifired로 출력된다.  여기서는 자바 스크립트가 사용하는 브라우저 프로그램의 메모리에 a변수와 sum 변수로 저장된 값이 없으므로 undifired로 출력된다.

#### 3.1.2 전역변수

- var 선언 안하고 y=3   document.write(y); 는 3으로 나온다. 실행시에 전역객체(Global Object는 window객체의 속성으로 추가된다.) 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    #자바스크립트에서 변수 선언은 var변수명;<br>
    var 변수명=초기값; 
    자바 스크립트에서 문자열은 "" 또는 '' 로 감싸 준다.
    <script>
    var sum,a;
    console.log("a="+a);//콘솔에 출력 a를
    document.write("sum="+sum+"<br>");
    y=3
    document.write("y="+y+"<br>");
    document.write("x="+x);
    </script>
</body>
</html>


```

- 결과값 y=3 =>window에 추가가 되어 f12를 누르고 console창에서 window. 를 작성하면 window함수 안에 y가 들어있음을 알 수 있다. 
- Uncaught ReferenceError: x is not defined  at 변수.html:18 =>x는 오류가 뜬다.

#### 3.1.3 변수 끌어올림, 중복 선언

- 변수와 함수 선언이 있으면 아무리 밑에 있어도 먼저 처리를 한다. hoisting 이라고 한다.(변수 선언의 끌어올림)
- 중복 선언시 오류가 뜨지 않는다. 같은 이름으로 선언된 변수는 모두 호이스팅 한 후 단 하나의 영역에만 할당.



#### 3.1.5 명명규칙

- 자바와 동일하다

##### 캐멀 표기법

##### 파스칼 표기법

##### 밑줄 표기법

### 3.2 데이터 타입

- 실수, 정수 타입 구별할까 그외에는 ?

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    #자바스크립트의 데이터 유형<br>
    primitive type-String,number,boolean,undefined,null<Br>
    객체(reference type)-funcion,object <br>
    <script>
    var a= 1;//정수와 실수 구분?
    document.write("1의변수의 타입:"+typeof(a)+"<br>");
    var b=0.5;
    document.write("0.5의변수의 타입:"+typeof(b)+"<br>");
    a="javascript";
    document.write("javascript변수의 타입:"+typeof(a)+"<br>");
    b="ECMAScript6";
    document.write("ECMAScript6변수의 타입:"+typeof(b)+"<br>");
    a=function(){};
    document.write("function(){}변수의 타입:"+typeof(a)+"<br>");
    b=[];
    document.write("[]변수의 타입:"+typeof(b)+"<br>");
    a= {}
    document.write("{} 배열 변수의 타입:"+typeof(a)+"<br>");
    b=new Object();
    document.write("new object()변수의 타입:"+typeof(b)+"<br>");
    a=true
    document.write("ture변수의 타입:"+typeof(a)+"<br>");
    a=0x2a;
    document.write("0x2a의 10진수값:"+a+"<Br>");
    a=0o73;
    document.write("0o73의 10진수값:"+a+"<Br>");
    a=0b101;
    document.write("0b101의 10진수값:"+a+"<Br>");
    a=1.161425E-11;
    document.write("1.161425E-11의 10진수값:"+a+"<Br>");

    </script>
</body>
</html>
```

- 결과값 
- #자바스크립트의 데이터 유형
  primitive type-String,number,boolean,undefined,null
  객체(reference type)-funcion,object 
  1의변수의 타입:number
  0.5의변수의 타입:number
  javascript변수의 타입:string
  ECMAScript6변수의 타입:string
  function(){}변수의 타입:function
  []변수의 타입:object
  {} 배열 변수의 타입:object
  new object()변수의 타입:object
  ture변수의 타입:boolean
  0x2a의 10진수값:42
  0o73의 10진수값:59
  0b101의 10진수값:5
  1.161425E-11의 10진수값:1.161425e-11
- 또한 ; 를 빼도 인식한다! 반드시 넣어야 하는 것이 아니다.

#### 3.2.1 데이터 타입의 분류

- primitive 원시 타입
  - String,number,boolean,undefined,null
- 객체타입
  - funcion,object 

#### 3.2.2 문자열, 논리값

- " " 나 ' ' 사이는 문자열로 취급한다

```html
<script>
a='"java"'
    document.write(a);
</script> 

```

- 결과값은 "java"

```html
   <script>
   var c=[];
    document.write("없는 배열의 요소:"+c[0]+"<br>");//없는 배열의 요소를 읽으면?
    a=function(){};
    document.write("함수 값이 없을시:"+a());//아무것도 반환하지 않는 함수가 반환하는 값
    a=function(d){
        alert(d);//함수를 호출했을 때 전달받지 못한 인수의 값?
    };
    a();
   </script>
```

- 결과값

- 없는 배열의 요소:undefined
  함수 값이 없을시:undefined

  팝업과 동시에 undefined 창 로드

- 값이 없음에는 null과 undefined가 있는데 undefined는 정의되지 않음이고 null은 아무것도 없음이란 뜻이다.

### 3.3 ECMAScript 6 추가된 데이터타입

#### 3.3.1 심벌

- 심벌은 자기 자신을 제외한 그 어떤 값과도 다른 유일무이한 값.
- 상수를 정의하겠다.
- Symbol.for()를 활용하며 문자열과 연결된 심벌 생성가능

#### 3.3.2 탬플릿 리터럴

- 일부만 변경해서 반복하거나 재사용 가능한 틀
-  ex)java에서 printf("%1$d",5) 가 그 예시이다.
- 간단한 템플릿 리터널은 역따옴표(키보드 1번옆의)
- \n 줄바꿈
- 이스케이프 시퀀스 문자를 그대로 출력하려면 String.raw 를 앞에 붙인다.

##### 보간 표현식

- ${} 안에 든 표현식이 문자열로 바뀐다.

# 5장 연산자

### 5.1연산자

#### 5.1.1표현식과 연산자

### 5.2산술연산

- **정수끼리 나누어도 결과가 부동소수점이 된다, 나머지 연산자 %의 피연산자는 부동소수점이다.** 자바와 다른점!

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
    document.write(0/0+"<Br>");
    document.write("one"+1+"<Br>");
    document.write(true+true+"<Br>");
    document.write(1+null+"<Br>");
    document.write(1+undefined+"<Br>");

    </script>
</body>
</html>
```

- 결과값
- NaN
  one1
  2
  1
  NaN

- 0/0  //NaN 계산할 수 없다.
- "one"+1  //NaN 계산할 수 없다.
- true+true //2 논리값의 타입을 숫자로 바꾸어 더한다.
- 1+null // 1  null을 0으로 바꾸어 더한다.
- 1+undefined //NaN undefined를 NaN으로 바꾸어 더한다.

#### 5.2.1증가 연산자

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
    a=1;
    b=++a;
    console.log("b="+b);
    console.log("a="+a);
    c=a++ +2;
    console.log("c="+c);
    console.log("a="+a);
    //console.log("(a++)++ =>"+(a++)++);
    </script>
</body>
</html>
```

- 결과값
- b=2
   a=2
   c=4
   a=3
- (a++)++  //ReferenceError 

#### 5.2.2 Math 객체

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
       var num= Math.round(Math.random()*5)+1;// round는 정수값만 얻기 위해서
       document.write("주사위의 숫자:"+num );
        

    </script>
    실행할때마다 주사위가 던져져서 값이 출력된다.
</body>
</html>
```

#### 5.2.3 부동소수점 정확도

- 정확도 문제 -정해진 부동소수점으로 표현하여 계산하면 오차가 발생한다. 
- 정밀도 손실

### 5.3 문자열 제어

##### 5.3.1문자열 연결

```html
<script>
document.write("1+{}==>"+(1+{})+"<br>")//{}-JSON객체는 Object 내장객체를 상속 받는다.
       document.write("true+(new date())==>"+(true+(new Date()))+"<br>");
</script> 

```

- 결과값
- 1+{}==>1[object Object]
  true+(new date())==>trueTue Jun 18 2019 13:51:15 GMT+0900 (한국 표준시)
- {}은 객체이면서 최상위 Object클래스

##### 5.3.2문자열 조작메서드

- 원시값을 객체로 변환하는 행위를 래핑(wrapping)이라고 한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <br>
    <script>
      
        var msgObj=new String("Everything is practice");
        document.write("Everything is practice"+"<br>");
        document.write("msgObj.length =>"+msgObj.length+"<Br>");
        document.write("msgObj.charAt(3) =>"+msgObj.charAt(3)+"<Br>");
        document.write("msgObj[3] =>"+msgObj[3]+"<Br>");
        document.write("msgObj.substring(7,10) =>"+msgObj.substring(7,10)+"<Br>");
        document.write("msgObj.slice(7,10) =>"+msgObj.slice(7,10)+"<Br>");
        document.write("msgObj.slice(-3) =>"+msgObj.slice(-3)+"<Br>");
        document.write("msgObj.slice(-9,-6) =>"+msgObj.slice(-9,-6)+"<Br>");
        document.write("msgObj.indexOf('t')=>"+msgObj.indexOf("t")+"<Br>");
        document.write("msgObj.indexOf('i',10)=>"+msgObj.indexOf('i'+10)+"<Br>");
        document.write("msgObj.replace('p','P')=>"+msgObj.indexOf("t")+"<Br>");
        document.write("msgObj.split(' ')=>"+msgObj.split(" ")+"<Br>");
        document.write("msgObj.includes('thing')=>"+msgObj.includes('thing')+"<Br>");
        document.write("msgObj.charCodeAt(0)=>"+msgObj.charCodeAt(0)+"<Br>");                 
        document.write("msgObj.codePointAt(0)>"+msgObj.codePointAt(0)+"<Br>");                 

</script>

</body>
</html>
```

- 결과값
- Everything is practice
  msgObj.length =>22
  msgObj.charAt(3) =>r
  msgObj[3] =>r
  msgObj.substring(7,10) =>ing
  msgObj.slice(7,10) =>ing
  msgObj.slice(-3) =>ice
  msgObj.slice(-9,-6) => pr
  msgObj.indexOf('t')=>5
  msgObj.indexOf('i',10)=>-1
  msgObj.replace('p','P')=>5
  msgObj.split(' ')=>Everything,is,practice
  msgObj.includes('thing')=>true
  msgObj.charCodeAt(0)=>69
  msgObj.codePointAt(0)>69
- 앞에서 부터 셀 때는 0부터 뒤에서 부터 셀 때는 -1부터
- 자바스크립트의 문자열은 **불변**

#### 5.3.3비교연산자

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
        document.write("null==undefined =>"+(null==undefined)+"<br>");
        document.write("1=='1' =>"+(1=='1')+"<br>");
        document.write("255=='0xff' =>"+(255== '0xff')+"<br>");
        document.write("true==1 =>"+(true==1)+"<br>");
        document.write("true=='1' =>"+(true=='1')+"<br>");
        document.write("new String('a')=='a' =>"+(new String('a')=='a')+"<br>");
        document.write("new Number(2)==2 =>"+(new Number(2)==2)+"<br>");

        document.write("null===undefined =>"+(null===undefined)+"<br>");
        document.write("1==='1' =>"+(1==='1')+"<br>");
        document.write("255=== '0xff' =>"+(255=== '0xff')+"<br>");
        document.write("true===1 =>"+(true===1)+"<br>");
        document.write("true==='1' =>"+(true==='1')+"<br>");
        document.write("new String('a')==='a' =>"+(new String('a')==='a')+"<br>");
        document.write("new Number(2)===2 =>"+(new Number(2)===2)+"<br>");
        document.write("10<20<30 =>"+(10<20<30)+"<Br>");
        document.write("10>20>30 =>"+(10>20>30)+"<Br>");
        </script>
    
</body>
</html>
```

- 결과값
- null==undefined =>true
  1=='1' =>true
  255=='0xff' =>true
  true==1 =>true
  true=='1' =>true
  new String('a')=='a' =>true
  new Number(2)==2 =>true
  null===undefined =>false
  1==='1' =>false
  255=== '0xff' =>false
  true===1 =>false
  true==='1' =>false
  new String('a')==='a' =>false
  new Number(2)===2 =>false
  10<20<30 =>true
  10>20>30 =>false
- == 는 값만 비교한다. 자바스크립트 엔진에서 자동 형변환이 수행
- === 는 값과 타입을 비교한다.

#### 5.3.4 기타연산

##### eval()

```html
<script>
var a="window.alert('eval은 문자열을 자바스크립트 코드로 실행합니다.')";
eval(a);//인수로 받은 문자열을 자바스크립트 코드로 실행
</script>
```

##### in,istanceof,typeof

```html
<Script>
  var student={"name":"Lee","ko":85, "en":90, "math":80};
        document.write("typeof(student)=>"+typeof(student)+"<br>");
    //데이터 타입 조사
        document.write("student instanceof Object=>"+(student instanceof Object)+"<br>");
    //객체 종류 확인
        document.write("ko in student =>"+('ko' in student)+"<br>");
   //ko는 과목명이기에 ' '사이에 작성해 준다., in 은 프로퍼티 포함 여부를 확인
</Script>
```

### 5.4 명시적 타입 변환

#### 5.4.1 숫자로 문자열로

- 10+"apple" //10apple
- 100+"" //"100"
- ("0000"+12).slice(-4) //"0012"

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
        var n=26;
        document.write(n.toString()+"<Br>");
        document.write(n.toString(2)+"<Br>");
        document.write( n.toString(16)+"<Br>");
        document.write((26).toString(16)+"<Br>");

        var x=1234.567;
        document.write( x.toString()+"<Br>");
        document.write(x.toString(16)+"<Br>");//숫자를 인수로 변환, 인수로 기수(2~32)넘기면 진법 바꿀 수 있다.
        document.write(x.toFixed(0)+"<Br>");//소수점 아래 자릿수 지정
        document.write( x.toFixed(2)+"<Br>");
        document.write( x.toFixed(4)+"<Br>");
        document.write(x.toExponential(3)+"<Br>");//자릿수 지정과 함께 지수와 표시
        document.write(x.toPrecision(3)+"<Br>");//유효 숫자가 문자열로 변환, 유효 숫자가 정수부 릿수보다 작을 때 지수로 표시
        document.write( x.toPrecision(6)+"<Br>");
        </script>
</body>
</html>
```

- 결과값
- 26
  11010
  1a
  1a
  1234.567
  4d2.9126e978d5
  1235
  1234.57
  1234.5670
  1.235e+3
  1.23e+3
  1234.57

##### String 함수 활용

- String 생성자 앞에 new 연산자를 붙이면 String 객체를 생성하는 함수로 사용 가능하지만 new가 없으면 일반 함수로 활용 가능하다.
- String(26)  //"26"
- String(1234.567) //"1234.567"
- String(0x1a) //"26"
- String(NaN) //"NaN"
- String(undefined) //"undefined"
- String({x:1,y:2})  // "[object Object]"
- String([1,2,3])  //"1,2,3"  

#### 5.4.2 문자열을 숫자로

- var s="2";
- s-0 //2
- +s   //2

##### window 함수를 사용

- window.parseInt() 윈도우 내장함수로 변환가능

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
        document.write(parseInt("3.14")+"<br>");
        document.write(parseFloat("3.14")+"<br>");
        document.write(parseInt("3.14 meters")+"<br>");
        document.write(parseFloat("3.14 meters")+"<br>");
        document.write(parseInt("123a")+"<br>");
        document.write(Number("123a")+"<br>");
        document.write(parseInt("0xFF")+"<br>");
        document.write(parseInt("0.5")+"<br>");
        document.write(parseInt(".5")+"<br>");
        document.write(parseInt("abc")+"<br>");
        document.write(parseInt("\100")+"<br>");
       
        

        </script>
</body>
</html>
```

- 결과값

- 3
  3.14
  3  //숫자 다음 문자열 무시
  3.14 //숫자 다음 문자열 무시

  123  //변환이 잘된다. 

  NaN //변환 안된다.

  255
  0
  NaN//문자 앞에 . 이 있어 해석 **x**
  NaN //숫자로 해석 불가능
  NaN //문자열 앞에 \가 있어 해석 **x**

##### Number함수 활용

- Number 에 new를 붙이면 객체 생성함수 사용 가능 하지만 없는 경우 일반 함수 처럼 사용
- 인수로 문자열을 넘기면 정수 또는 부동소수점으로 바꾸며 10진수만 처리 가능
- Number(123)  // 123
- Number(true) // 1
- Number(false) //0
- Number(NaN) // NaN
- Number(undefined) // NaN
- Number(null)  // 0
- Number({x:1, y:2}) // NaN
- Number([1,2,3])//NaN

##### 논리값으로 변환

!! x

Boolean (x)

- 어떤 값이든 논리값으로 바꾸는 방법은 위의 두 가지이다. ! 연산자는 논리 타입이 아닌 값의 타입을 논리 타입으로 바꾼다. 그 후 !를 하나 더 붙여 참과 거짓을 뒤바꾼다. 

```html
<Script>
	   document.write(!!"  "+"<br>");
        document.write(!!""+"<br>");
        document.write(!!null+"<br>");
        document.write(!!undefined+"<br>");
        document.write(!!NaN+"<br>");
   </Script>
```

- 결과값
- true
  false
  false
  false
  false

# 7장 제어문

### 7.1 제어문

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <Script>
        var input1=window.prompt("점수를 입력하시오",0);
        document.write(input1+typeof(input1)+"<br>");

        var input2=window.confirm("종료하시겠습니까");//확인 누르면 
        //trueboolean 취소 누르면 falseboolean
        document.write(input2+typeof(input2)+"<br>");
        </Script>
</body>
</html>
```

### 7.2 조건문

##### if 제어문

- nested if,다중 if문

##### switch문

- javascript에서는 범위 비교 연산 가능

##### 삼항 연산자

- 삼항 연산자(조건문)=> (조건식)? true일때 수행 문장: false일떄 수행하는 문장;

- 조건식 1&& 조건식2(실행문장2)=>조건식1이 true이면 조건식2(실행문장2)수행 아니면 조건식1 실행

- 조건식 1&& 조건식2(실행문장2)=>조건식1이 false이면 조건식1(실행문장1)수행 아니면 조건식 2 실행

- 조건식 1|| 조건식2(실행문장2)=>조건식1이 true이면 조건식2(실행문장2)수행 아니면 조건식 1 실행

- 조건식 1|| 조건식2(실행문장2)=>조건식1이 true이면 조건식2(실행문장2)수행 아니면 조건식 2실행

  

- 문1> if문을 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수 인지 출력
- 문2> 삼항연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수 인지
- 문3>&& ||논리연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수인지

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">

    <title>Document</title>
</head>
<body>

    <script>
//문1> if문을 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수 인지 출력
var input=window.prompt("정수를 입력하시오",0);
if(input%2==0) {
    console.log("짝수입니다.");
}else{
    console.log("홀수입니다.");
}

//문2> 삼항연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수 인지
var input=window.prompt("정수를 입력하시오.",0);
input%2==0? console.log("짝수") :console.log("홀수");
//문3>&& ||논리연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수인지
var input=window.prompt("정수를 입력하시오.",0);
if(input%2==0&&0==0){
    console.log("짝수");
}else{
    console.log("홀수");
}
//문4>switch문을 사용해서 사용자로부터 입력받은 점수에 대한 a(>=90),b(>=80),c(>=70),d(>=60),f(<60)등급 판별하는 웹 어플리케이션을 swith구문을 사용하여 구현하시오
switch(true){
    case input>=90: alert("A");break;
    case input>=80: alert("B");break;
    case input>=70: alert("C");break;
    case input>=60: alert("D");break;
    default : alert("F");

}
var sum=parseInt(input/10)
alert(sum)
switch(sum){
    case 10:
    case 9:document.write("A");break;
    case 8:document.write("B");break;
    case 7:document.write("C");break;
    case 6:document.write("D");break;
    default:document.write("F");
}
</script>
</body>
</html>
```

### 7.3 반복문



```javascript
for(var i=0;i<10;i++){
}//기본 for문

var i=0;
while(i<10){
}//기본 while문

do{
    
}while();//do~ while문
       
var nums={1,2,3,4,5,6,7,8,9,10};
for(var n in nums){
}//배열  for문
```



문>1~10까지의 홀수 출력과 구구단을 가로로!

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <script>
    for(var i=0;i<10;i++){
        if(i%2==1){
            document.write(i);
        }
    }
    document.write("<hr>")
    var i=0;
    while(i<10){
        i++;
        if(i%2==1){
           
            document.write(i);
        }
    }
    document.write("<hr>")
    i=1;
    do{
        if(i%2==1){
            document.write(i);
        }
    }while(++i<10);
    document.write("<hr>")
    var nums=[1,2,3,4,5,6,7,8,9,10];
for(var n in nums){
    if(n%2==1){
            document.write(n+"<Br>");
        }
}
document.write("<hr>")
for(var i=2;i<10;i++){
    for(var j=1;j<10;j++){
        document.write("  "+i+"x"+j+"="+i*j );
    }
    document.write("<br>")
} 
</script>
</body>
</html>
```



# 연산자

##### 삼항연산자

```javascript
if (a > b){
document.write("a가 크다");
}else {
  document.write("b가 크다")
}//를 아래의 삼항연산자를 이용하여 (조건식)? true일경우 실행:false일 경우 실행;으로 작성
a>b? document.write("a가 크다"):document.write("b가 크다");
```

##### 입력 받기

```javascript
var input=window.prompt("정수를 입력하시오",0);
// prompt(입력창에 띄울 메세지,기본값으로 들어가있을 문자열);
```

##### 출력문

```javascript

```

##### 경고장 띄우기

```javascript
alert("경고장 띄우기")
```





