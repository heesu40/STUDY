# 1장 특징

### 1.1 자바스크립트

1. 인터프리터 언어
   - 한줄 씩 기계어로 번역해서 실행 하는 언어
   - 느릴 것 같지만 최근 JIT(Just in time compiler)가 내장되어 있어 실행 속도가 매우 빠르다.
2. 동적 프로토타입 기반객체 지향 언어
   - 클래스가 아닌 프로토타입을 상속하는 프로토타입 기반 객체 지향 언어
3. 동적 타입 언어
   - 타입 선언을 하지 않고, 저장되는 값에 따라 그때그때 달라진다.
4. 함수가 일급 객체(function)
   - 함수가 중심이 되며 함수가 객체다.=>함수형 프로그래밍 언어
   - 함수를 변수에 저장, 함수의 인수로 함수를 전달, 함수 내부에 함수 정의 가능, 함수에서 함수 정의를 리턴(반환 가능)
5.  클로저 정의
   - 클로저로 변수 은닉 하거나 영속성을 보장한다. 함수를 외부에서 사용가능하게도 한다.

#### 기술적 요소

1. 구성 기술 요소
   
   - ECMAScript : 코어 언어(자바스크립트 핵심 언어)
   - 웹 브라우저의 API(클라이언트 측 고유한 기술 요소)
     - Window 인터페이스 :  브라우저 최상위 객체
     - DOM  :  HTML문서의 요소 제어(document)
     - XMLHttpRequest : 서버와 비동기 통신 기능 제공
     - 그외 : jQuery,Vue.js,React.js,.....
   - HTML5에 규정된 API(서버측 자바스크트의 고유 기술 요소)
     - Node.js   =>웹 어플리케이션 만들때 가장 많이 사용
     - Rhino
     - Aptana Jaxer
     - Geolocation,webworks,Canvas,video,audio,dragndrop,....등 
   
   

### 1.2자바스크립트 역사

# 2장 프로그램의 작성과 실행

### 2.1 웹 브라우저 Node.js실행

- 크롬과 Node.js 사용한다.
- `httts://nodejs.org/ko/download/`

#### 2.1.1 텍스트 편집기 준비

- 서브라임 텍스트 `https://www.sublimetext.com/`

- 저장시
  - 파일 이름 끝에 확장자는 .js
  - 파일 문자 인코딩은 UTF-8로 설정

#### 2.1.2 저장시

- 대소문자 구별
- 유니코드 문자로 작성
- 인코딩은 utf-8권장
- .js 파일로 저장
- 한 문장 단위로 ;으로 구분

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



# 3장 변수와 값

### 3.1변수

- 변수란 값을 담기 위해 이름 붙인 상자의 이름이 변수다.
- var 선언자(키워드)
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

#### 3.1.2 전역변수(Global Object)

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

#### 3.1.3 변수 끌어올림, 중복 선언 , hoisting

- 변수와 함수 선언이 있으면 아무리 밑에 있어도 먼저 처리를 한다. hoisting 이라고 한다.(변수 선언의 끌어올림)
- 중복 선언시 오류가 뜨지 않는다. 같은 이름으로 선언된 변수는 모두 호이스팅 한 후 단 하나의 영역에만 할당.
- var 문을 사용하여 같은 이름을 가진 변수를 여러 개 선언해도 문제 발생 **x**

```javascript
//var n; 밑에 있는 선언이 호이스팅 된다. 그래서 오류 x
console.log(n);
var n;

console.log(n); //undefined
var n=5;
console.log(n); // 5 선언과 동시에 대입하는 코드는 호이스팅 안한다.

```





#### 3.1.5 명명규칙

- 자바와 동일하다
- _,$,영문자로 시작
- 두번째부터  숫자 가능
- 길이 제한 없음
- 키워드**X**, 내장함수명, 내장객체명 사용 권장 안하는데 사용하면 이름 충돌로 인해 기본 기능을 하지 못한다.

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
  - String,number,boolean,undefined,null,symbol
- reference 객체타입
  - funcion,object ,interface,inNum..? 추가되었고, 배열 Array은 객체 취급(=object 유형)이다.
- 구별해보자!
  - 선언되지 않는 변수를 참조하면 반환되는 값은?    **ReferenceError**
  - 선언만 된 변수, 초기값이 할당되지 않은 변수를 참조하면 반환되는 값은? **undefined**
  - 객체를 메모리에서 검색을 했는데, 검색되지 않으면 반환되는 값은? **null**

#### 3.2.2 문자열, 논리값

- " " or ' ' 사이는 문자열로 취급한다

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

- 값이 없음에는 null과 undefined가 있는데

  -  undefined는 정의되지 않음이며 데이터 타입이자, 값이다. 
    -  `var n;` n변수에 undefined란 값을 가진다는 것. 그렇기에 데이터 타입이다.

  -  null은 아무것도 없음이란 뜻이다. 아무것도 참조 하지 않는 다는 의미임으로 객체 변수 초기화시 많이 사용
    - null또한 값이며 데이터 타입이지만 undefined는 변수 선언만 해도 할당되지만 null은 변수 선언 후 null로 값을 바꾼다.

### 3.3 ECMAScript 6 추가된 데이터타입

#### 3.3.1 심벌

- 심벌은 자기 자신을 제외한 그 어떤 값과도 다른 유일무이한 값.
- 상수를 정의하겠다.란 의미이다.
- Symbol.for()를 활용하며 문자열과 연결된 심벌 생성가능

#### 3.3.2 탬플릿 리터럴

- 일부만 변경해서 반복하거나 재사용 가능한 틀
- 포맷형식 문자열에 실행시에 인수를 전달해서 출력할때 사용
-  ex)java에서 printf("%1$d",5) 가 그 예시이다.
- 간단한 템플릿 리터널은 역따옴표(키보드 1번옆의)
- \n 줄바꿈
- 이스케이프 시퀀스 문자를 그대로 출력하려면 String.raw 를 앞에 붙인다.

##### 보간 표현식

- ${변수} 안에 든 표현식이 문자열로 바뀐다.



# 4장 객체와 배열, 함수기초

### 4.1 함수

#### 4.1.1객체

- 객체는 이름과 값을 한쌍으로 묶은 데이터를 다양하게 모든 것(= 연관 배열, 사전), java에서는 map하고 비슷

- 객체의 데이터 하나 -**프로퍼티**

- 프로퍼티 이름- **키**

  - `var student={one :"하리오", two:"아리자"};` 의 경우 프로퍼티는 "하리오" ,"아리자", 키는 one,two이다.

- 객체 생성방법
  1. 객체 리터럴 사용 -JSON, 하나의 객체만 생성해서 사용하는 경우
  2. 생성자 함수 사용 - new 사용, 필요할때마다 생성자함수로부터 객체 생성
  
- 변수에 대입된 객체 안의 프로퍼티 값(key)을 읽거나 쓸때
  1. 마침표(.)연산자
  2. 대괄호([])연산자 사용
  
- 프로퍼티 추가,삭제

  1. 추가 

  ```
  student.value="오리카";
  console.log(student); //
  ```

  



 <문> 객체 안의 프로퍼티 값을 읽어 보자 마침표와 대괄호를 사용하고 key를 사용해서!

- 또한 내장객체의 상속을 받았는지확인을 해보자 (true이면 자동으로 상속을 받는 것!)

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <h3>객체 리터럴방식으로 객체 생성</h3>
    <script>
    var employee ={};//빈 객체 생성, var emp= new Object();
    employee.ename='Scott';
    employee.job='Developer';
    employee.salary=5000;
    employee.hiredate='2013/01/01';
    employee.address='삼성동';

    document.write("emloyee.ename="+employee.ename+"<Br>");
        document.write("employee['job']="+employee['job']+"<Br>");

    for(var key in employee){
        document.write(key+" :"+employee[key]+"<br>")
    }
    document.write("employee instanceof Object =>"+(employee instanceof Object)+"<br>");
    //내장객체중 최상위 Object 상속 확인
    </script>

</body>
</html>
```

#### 4.1.2 in 연산자로 프로퍼티 있는지 확인

- for in 반복문을 통해 객체의 속성에 접근할때 사용 가능

```html
<script>
document.write("employee instanceof Object =>"+(employee instanceof Object)+"<br>");
    //내장객체중 최상위 Object 상속 확인
    console.dir(Object);
    document.write(employee+"<br>");

    employee.toString=function(){
        var output="";
        for(var key in this){
            if(key !='toString'){
                output+=key+":"+this[key]+"\n";
            }
        }
        return output;
    }
    document.write(employee+"<Br>");
    document.write(employee.toString()+"<br>");
    //toString 오버라이딩 했을떄 안했을때 비교하면 안하면 
    //document.write(employee+"<Br>"); 이 [object Object] 뜨지만
    //오버라이딩 후에는 ename:Scot job:Developer salary:5000 hiredate:2013/01/01 address:삼성동 요렇게 뜬다!


    </script>
```



문>삭제후 객체 안에 있는지 없는지 확인해 보자.

- 객체에 대해서 사용하는 in 키워드는 속성 존재 여부를 체크할 떄 사용

```html
  <script>
  delete(employee.address);
        document.write(employee+"<Br>");
            document.write("address in employee=>"+('address' in employee)+"<BR>");
                document.write("hiredate in employee=>"+('hiredate' in employee)+"<br>");
    </script>
```



<문> 총점과 평균을 구해보자

- with 를 사용하여 간략하게 작성가능하다.
- 객체의 속성을 객체.속성 대신 속성명으로만 사용할떄 with(객체){}사용

```html
  <script>
        var student={이름:'홍길동', 영어:88,국어:90,수학:77,과학:79};
        document.write(student.이름+"의 총점 :"+(student.과학+student.수학+student.국어+student.영어)+"<br>");//이름과 총점 출력
        with(student){
            document.write(이름+"의 평균 :"+(영어+국어+수학+과학)/4+"<br>");
        }
        </script>
```



객체 리터럴 방식으로 정의되는 객체는 동적으로 속성, 메소드를 추가하거나, 제거 할 수 있다.



### 4.2 함수

#### 4.2.1함수

- 함수는 일련의 처리를 하나로 모아 언제든 호출할 수 있도록 만들어 둔것
- 함수 입력값 **인수** 출력값 **반환 값**

#### 4.2.2 함수 선언문으로 함수 정의

`function square(x){return x*x;}`

- return값이 없는 경우 undefind로 출력
- var 변수=funcion(){}; //익명(anonymous) 함수
- function 이름 (){}//named function, 선언적 함수
- 사용자 정의 함수는 소스가 공개되지만, 내장함수등은 소스는 native code로 공개하지 않는다
- 자바스크립트 엔진은 실행코드보다 먼저 선언적 함수를 읽는다.(hoisting)
- 선언적 함수는 defintion전에 호출을 하더라도 실행 순서상 문제가 되지 않는다.

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>

<body>
<h3>자바스크립트 함수</h3>    
<script>
    // func1();//변수에 저장된 함수 호출 먼저 익명함수 정의 하면 오류뜬다!
     func2();//선언적 함수(named funcion)호출
var func1=function(){
        var input=Number(window.prompt("정수를 입력하시오.",0));
        (input%2==0)? alert("짝수") :alert("홀수");
}//출력안된다.
func1(); //뒤에 해야 한다. 이렇게 되면 결과 확인시 func2가 먼저 실행되고 func1이 늦게 실행된다.
function func2(){
    var input=Number(window.prompt("1~100사이의 수를 입력",0));
    (input%2==0)? alert("짝수"):alert("홀수");
}//출력된다. 얘는 호이스팅 때문에 오류가 안뜬다.
</script>
</body>
</html>
```

#### 함수 리터럴로 함수 정의

- `var student=function(num){return num*num;};`

- 함수 리터럴은 익명 함수 또는 무명 함수라고 한다.

- 전역객체에 저장

- student(5)라 하면 함수 실행 가능. 가능한 이유는 리텉럴과 함수 선언문 모두 내부적으로 square변수에 함수 객체를 참조로 저장하기 떄문. 하지만 함수 리터럴로 정의한 함수는 *끌어올리지 않기 때문에 함수 정의 후 사용*

  

##### 즉시 실행 함수

- 익명 함수를 정의하고 바로 실행하는 함수

- 한번 실행하므로 초기화 작업시 사용하며, 전역 유효 범위를 오염시키지 않는다.

  

  ```javascript
   function(x) {return x*x})(5); //즉시 실행 함수다. 
  document.write((function(x) {return x*x})(5);
  document.write((function(x) {return x*x}) (5));//값 확인시 25임을 알 수 있다. 위아래 둘다 가능
  (function square(x) {return x*x})(5) ;//이름 정의할 수 있지만 가로안에서만 소용있기때문에 굳이..? 할 필요 없다. 일회용이다.
  
  ```

  

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <script>
    var student={
        이름:'홍길동'
        ,영어:55,국어:90,수학:77,과학:75 ,
        total : function(){ //총점 반환
      return this.영어+this.국어+this.수학+this.과학

    },
    average : function(){//평균 반환
        return this.total()/4
    }}
document.write(student.total()+"<Br>");
document.write(student.average());
        </script>
    
</body>
</html>
```

##### Function 생성자로 정의 가능

` var square=new Function("x","return x*x");

square(5) // 호출

##### 화살표 함수 표현식(람다식)으로 정의

```javascript
 var square= x => x*x;
    document.write(square(5)); //결과값 25
```





##### 생성자 함수 이용

- 동일한 속성을 가지는 객체를 하나 이상 생성해야 하는 겨우 객체 리터럴 방식보다 **생성자 함수**를 정의
- 생성자 함수로부터 property값만 전달해서 객체 생성

- 생성자 함수로 생성된 객체들의 기능은 모두 동일하므로 객체 생성시마다 메모리에 객체의 메서드가 생성되는 것이 아닌  function객체로 메모리에 생성될때 프로토타입으로 메모리에 자동으로 생성 (f12클릭후 console.dir()해서 보면 프로토타입 속성객체가 생성되어 있다. 생성자를 만들면)

- 프로토타입에 생성되면 전역 메서드처럼 사용 가능하기에 메모리 절약이 가능.

  

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <script>
        //객체 생성을 위한 생성자 함수 정의
        function Student(name,ko,math,en,sci){//생성자 만들기(대문자로 시작)
            this.name= name; //참조 하고 싶으면 this를 사용한다
            this.ko=ko;
            this.math=math;
            this.en=en;
            this.sci=sci;
            this.total=function(){
                return this.en+this.ko+this.math+this.sci;
            },
            this.average=function(){
                return this.total()/4;
            }
        }

        //객체 생성
        var students =[new Student('장기영',87,98,88,95),
                        new Student('연하진',96,84,12,75),
                        new Student('구지연',97,44,12,75),
                        new Student('나선주',16,49,78,67),
                        new Student('윤아린',100,100,100,100),
                        new Student('윤명원',5,10,15,20),
                        new Student('김미화',65,85,25,15),
                    new Student('김연화',1,2,3,4),
                    new Student('박아현',5,6,7,8),
                    new Student('서준서',10,10,10,10),
                    new Student('10',90,90,90,90)];

        for(var idx in students){
            document.write(students[idx].name+"의 총점:"+students[idx].total()+"평균:"+students[idx].average()+"<Br>")
        }

        </script>
</body>
</html>
```

- 생성자를 average와 total을 프로토타입에 넣어서 사용 가능.

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <script>
        //객체 생성을 위한 생성자 함수 정의
        function Student(name,ko,math,en,sci){//생성자 만들기(대문자로 시작)
            this.name= name; //참조 하고 싶으면 this를 사용한다
            this.ko=ko;
            this.math=math;
            this.en=en;
            this.sci=sci;
           
        }
        Student.prototype.total=function(){
            return this.en+this.ko+this.math+this.sci;
        }
        Student.prototype.average=function(){
            return this.en+this.ko+this.math+this.sci;
        }
        console.dir(Student);

        //객체 생성
        var students =[new Student('장기영',87,98,88,95),
                        new Student('연하진',96,84,12,75),
                        new Student('구지연',97,44,12,75),
                        new Student('나선주',16,49,78,67),
                        new Student('윤아린',100,100,100,100),
                        new Student('윤명원',5,10,15,20),
                        new Student('김미화',65,85,25,15),
                    new Student('김연화',1,2,3,4),
                    new Student('박아현',5,6,7,8),
                    new Student('서준서',10,10,10,10),
                    new Student('10',90,90,90,90)];

        for(var idx in students){
            document.write(students[idx].name+"의 총점:"+students[idx].total()+"평균:"+students[idx].average()+"<Br>")
        }

        </script>
</body>
</html>
```



#### 4.2.3 함수 인수

- 모든 함수 **가변인자**를 가지는 함수로 정의
- 함수가 실행될때 실행 컨텍스트에서는 함수 내부에 arguments배열과 유사한 타입의 속성이 생성
- 함수를 호출할때 입력값인 함수의 property는  arguments에 저장된다.
  - arguments.length,arguments[index]
- 함수에 정의된 매개변수의 개수보다 많거나 적은 매개변수로 호출시 많으면 무시, 적으면 undefined로 전달

#### 4.2.4 호출

- 함수가 호출되어 실행되는 시점에 this값이 결정된다.
- 최상위 레벨의 코드에서 this는 Window객체의 참조변수 window

```javascript
 document.write((function(x) {return x*x})(5));
   document.write(this);
//25   [object Window]
```

```javascript
 document.write((function(x) {return x*x})(5));
   document.write(this);//window
    console.log(this==window);
    function f(){document.write(this);}//전역 유효 범위의 namespace 에 추가된다.
   f();//window
```



- 이벤트 핸들러 함수 내부에서 this는 이벤트 소스 객체

```javascript
window.onload=이벤트핸들러 함수(){};
window.onload=function(){
 this.....//?
};
button.onclick=function(){
this.......///클릭이벤트가 발생한 버튼
};

```

- 생성자 함수 안에서 this는 생성자 함수로부터 생성되는 객체 자신

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <script>
        function hap(a,b){
            document.write("함수의 인수개수:"+arguments.length+"<br>");//arguments는 함수의 인수 개수 확인할때
            var sum=0;
            for(var item in arguments){
                document.write("item의 인수개수:"+arguments[item]+"<br>");//arguments는 함수의 인수 개수 확인할때
                sum+= arguments[item];
            }
            document.write("함수의 a,b:"+a+" "+b+"<br>");
            return sum;
        }
    //함수 호출 해보자
    document.write("hap(3,5) 호출 :"+hap(3,5)+"<BR>");//인수 개수에 맞춰 호출
        document.write("<BR>");
         document.write("hap(1,3,5,7,9) 호출 :"+hap(1,3,5,7,9)+"<BR>");//인수 개수보다 많이
         document.write("<BR>");     
        document.write("hap(9) 호출:"+hap(9)+"<br>");//인수 개수보다 적게
        document.write("<BR>");
            var nums=[2,4,6,8,10];
            
            document.write("hap(nums) 호출 :"+hap(nums)+"<Br>"); //배열을 한번 넘겨본것 넘어갈까?  
                //0,2,4,6,8,10으로 호출되는데 0이 나오는 이유는 sum이 호출되기 때문!
                console.dir(hap);

                var arrays=[1,'hello',true,function(){},{name:'korea'},[100,200]];
                for(var index in arrays){
                    document.write(index+":"+arrays[index]+"<Br>");
                }
    </script>
</body>
</html>
```

#### 4.2.5 전역  변수,지역 범수의 유효 범위

- 함수 내부에 함수를 정의 가능=>외부 함수와 충돌이 발생되는 경우, 함수를 사용하는 내부에 정의할 수 있으며, 내부함수가 정의된 함수 내부에서만 호출 가능.

```html
<script>  
// function square(x){//인수의 제곱을 반환
    //     return x*x;
    // }
    function pythagoras(width,height){//직각삼각형의 빗변의 길이
        function square(x){//인수의 제곱을 반환 오류를 피하기 위해 내부에 넣어준다.
        return x*x;
    }
        return Math.sqrt(square(width)+square(height));
    }
    document.write("밑변3, 높이 4인 삼각형의 빗변의 길이 :"+ pythagoras(3,4)+"<Br>");

    
       
    //나중에 다른 사람이 만든 것을 가져왔다. 충돌이 일어나 값이 제대로 안나온다. 자바의 오버라이딩 같은 상태
    function square(width,height,hypotenuse){
        if(width*width+height*height==hypotenuse*hypotenuse){
        return true;
    } else {
        return false;
    }
}
    </script>
```

##### 클로저 함수

- 자기 자신이 정의된 환경에서 함수 안에 있는 자유 변수의 식별자 결정을 실행한다.

```javascript
function makeCounter(){
       var count=0;
       return g;
       function g(){ //클로저 함수
           return count++;
       }
   }
   var ct =makeCounter();
   document.write((ct()));
   document.write((ct()));
   document.write((ct()));
//결과값 0 1 2
```

<문> 클릭시 console에 버튼이 찍히는가 방법 1

```html
<!DOCTYPE html>
<html >
<head>
    <SCRipt>  
window.onload=function(){
            var buttons =document.getElementsByTagName("input");
            for(var i=0;i<buttons.length;i++)(function (_i){
                buttons[_i].onclick=function(){
                    console.log(_i);
                }
            })(i);
        };
                </SCRipt>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h3>클로저 함수를 사용해야 하는 예제</h3>
    <input type="button" value="0">
    <input type="button" value="1">
    <input type="button" value="2"> 
    <script>
        
        </script>
</body>
</html>
```

<문>방법 2

```html
<!DOCTYPE html>
<html >
<head>
    <SCRipt>
window.onload=function(){
    var buttons=document.getElementsByTagName("input");
    for(var i=0;i<buttons.length;i++){
        let _i=i;
        buttons[_i].onclick=function(){
            console.log(_i);
        }
    }
};
                </SCRipt>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h3>클로저 함수를 사용해야 하는 예제</h3>
    <input type="button" value="0">
    <input type="button" value="1">
    <input type="button" value="2"> 
    <script>
        
        </script>
</body>
</html>
```



- 함수 수행이 끝나면 Garbage Collect되어야 하지만 클로저 함수를 리턴하는 함수의 실행 Context는 메모리에 계속 남아 있다.
- 함수를 매개변수로 전달하고 함수를 리턴하는 함수를 정의 가능

- var키워드를 생략한 함수 내부에 선언된 변수는 함수호출후에 전역변수로 Global실행 컨텍스트에 추가. 함수외부에서 참조가 가능해진다.

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <script>
    var globalVar='korea';
    function test(name){
        globalVar2=name;//var 키워드를 생략한 함수 내부에 선언된 변수는 함수호출후에
        //전역변수 Global 실행 컨텍스트에 생성됩니다. 함수외부에서 참조가 가능해진다.
        var localVar="Hello~"+name+"!!";//로컬변수
        return function(){
            return localVar;
        }
    }
    document.write("전역변수 globalVar :"+globalVar+"<br>");
    //document.write("전역변수 globalVar2:"+globalVar2+"<Br>");//매개변수 에러?
        test('독도');//함수 호출 후
        document.write("전역변수 globalVar2 :"+globalVar2+"<br>");
        //document.write("지역변수 localVar :"+localVar+"<Br>");오류뜬다.매개변수 에러?
            document.write("지역변수 localVar 를 클로저 함수를 통해 참조 가능"+ test('제주도')()+"<br>");
    </script>
</body>
</html>
```

#### 4.2.7 참조에 의한 호출과 값에 의한 호출

- 함수는 원시 값을 인수로 넘겼을 때와 객체를 인수로 넘겼을때 다르게 동작한다.
- 원시 값일때 -- call by value
- 객체 값일때 -- call by reference

#### 4.2.8 블록 유효 범위 

1. **let** 은 블록 유효 범위를 갖는 **지역변수** 선언
2. **const** 는 블록 유효 범위를 갖는 **상수** 선언

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <script>
        let x="outer x";
        {
            let x= "inner x";
            let y="inner y";
            document.write("블럭 내부에서 x:"+x+"<br>");
            document.write("블럭 내부에서 y:"+y+"<br>");
        }
        document.write("블럭 외부에서 x:"+x+"<br>");
       // document.write("블럭 외부에서 y:"+y+"<br>");referenceerror
    {
        const c= 3;
        document.write("블럭 내부에서 c:"+c+"<br");
       // c=5;//typeError
    }
        </script>
</body>
</html>
```

#### 4.2.9함수적 프로그래밍 특성

1. 변수에 함수를 저장 할 수 있다.
2. 배열의 요소로 함수를 저장 가능
3. 함수 내부에 함수 정의(nested function)
4. 함수에서 함수 반환 가능.
   - 내부에 함수를 정의하거나, 함수를 반환 하는 함수를 **고차 함수**
5. 함수의 인수로 함수를 전달 가능.
   - 인수로 전달되는 함수는 **콜백 함수**



### 4.4 내장객체

- 처음부터 사용 가능한 내장객체가 자바스크립트에 마련되어 있다.
- 내장객체 확인은 `console.dir(생성자이름)` 으로 확인한다.

#### 4.4.1 객체 분류

1. 네이티브 객체(내장 객체)

   - Object, String,Boolean,Number,Array,Date,Regexp,....

2. 호스트 객체(브라우저 객체)

   - 브라우저 객체를 호스트 객체라 한다.

   - **Window**- close(),open(url, name,{....}),moveBy(),moveTo(),alert(),confirm(),prompt(),

     setTimeout(function(){},time),clearTimeout(id),setInterval(function(){},time),

     clearInterval(id)

   - **document**의 원형은 Document로서 HTML요소 관련 처리 객체

     getElementById(""),getElementsByName(""), getElementsByTagName(""),getElementsByClassName(),querySelector("css의 select형식")

     querySelectorAll("css의 selector형식"),createElement(),creatComment(),createDocumentFagement(),createAttribute(),createTestNode(),setAttribute(),getAttribute(),removeAttribute(),parentNode,childNode,childNodes,body,appendChild(),NodeName()

3. 사용자 정의 객체(ECMAScript)

#### 4.4.2 객체 정의

1. 객체 리터럴로 정의

   `{속성: 값, 속성:값, 속성:function(){},....}

2. 생성자 함수를 정의하고 생성자 함수로부터 객체 생성가능

   ```javascript
    function Person(name,age){
   
   var _name=name; //private 성격의 속성(지역변수 외부에서 참조 불가능)
   var _age=age;
   return {
   getName : function(){return _name;},
   getAge : function(){return _age;},
   setAge : function(n){_age=n;}
   };
   }
   var p=new Person("kim",30);
   console.log(p._name);//오류
   console.log(p._age);//오류
   console.log(p.getName());
   console.log(p.getAge());//여기서도 클로저 사용
   ```

   

### 4.5배열

- 배열은 생성시 length프로퍼티가 자동 생성된다.
- java와 다르게 배열 추가, 삭제 가능
- 방법은 아래를 확인하자.

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <script>
        var array1=new Array();
        var array2=new Array(10);
        var array3=new Array(10,20,30,40,50);
        document.write("*array1.length :"+array1.length+"<br>");
        document.write("*array2.length :"+array2.length+"<br>");
        document.write("*array3.length :"+array3.length+"<br>");
        document.write("<hr>");
        array3[5]=60;//배열 추가 방법 1
        array3.push(70);//배열 추가 방법 2
        for(var idx in array3){
            document.write("*array3[idx]="+array3[idx]+"<br>")
        }
        document.write("<hr>");
        delete array3[1];//배열 삭제
        for(var idx in array3){
            document.write("*array3[idx]="+array3[idx]+"<br>")
        }
        </script>
</body>
</html>
```

#### 4.5.1 배열메서드()

- concat()
- `var 새로운배열이름=합칠배열1.concat(합칠배열 2,합칠배열3,...);`

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <script>
     var array1=[1,2,3,4,5,6,7,8,9];
     var array2=[3.14,"pi",true,{x:5,z:10},[5,6]];
     var array3=[9,10,11,12];
     var array4=array1.concat(array2,array3);
     for(var n in array4)   {
         document.write(array4[n]);
     }
     
        </script>
</body>
</html>
```





# 5장 연산자

### 5.1연산자

1. 산술연산자
   - *,/,%,+,-
2. 단항연산자
   - ~,!,+,-,++,--
     - ~ 비트 전환을 한다. (+은 -로 -는 +로)
3. 비교연산자
   - <.<=,>=,!=,===,!== (세개의 ===은 타입까지 비교)
4. 비트 연산자
   - &,|,^
5. 논리연산자
   - &&,||
6. shift 연산자-
   - <<,>>,>>>
7. 삼항 연산자
   - 조건? 항1:항2  조건이 참이면 항1 거짓이면 항2
8. 기타 연산자
   - typeof,in,instanceof.....

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

!! 값

Boolean (값)

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
- if문보다 가독성이 좋다.

```javascript
switch(포현식){
    case 값 : 문장; break;
        case 값 : 문장; break;
        case 값 : 문장; break;
        default : 문장;
        
}
switch(true){
    case 조건:문장;break;
    case 조건 : 문장;break;
        default : 문장;
}//java와는 다르게 조건사용이 가능
```



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

- **for 문**은 반복 횟수를 명확히 알때 사용한다.
- **while**문의 경우  반복 횟수를 모를때 사용한다. 조건에 따른 반복 수행 여부 결정할때 사용
- 최초 1번은 무조건 수행후에 조건에 따라 반복 수행 여부를 결정해야 할때 **do while문**을 사용
- 배열의 요소, 객체의 속성을 순차적으로 꺼내올때 사용하는 반복문은 **for(var 변수 in 배열or 객체)** 사용

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





# 13장 웹 브라우저 객체

### 13.1 클라이언트 측 자바스크립트

- 웹 브라우저에서 자바스크립트가 하는 일
  1. 웹 페이지의 document 객체 제어(HTML요소와 CSS스타일 작업)
  2. 웹페이지의 Window 객체 제어 및 브라우저 제어
  3. 웹 페이지에서 발생하는 이벤트 처리
  4. HTTP이용한 통신 제어

#### 13.1.1 window객체

##### 새창열기

```html
<!DOCTYPE html>
<html >
<head>
        <script>
                window.onload=function(){
                    var btn=document.getElementById("newOpen");
                    btn.onclick=function(){
                        window.open("웹브라우저 객체.html","","width=300 height=300");
                    }
                }
                </script>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <button id="newOpen">새창열기</button><br>
</body>
</html>
```

##### 새창에서 위아래업다운 버튼 클릭해서 움직이기

```html
<!DOCTYPE html>
<html >
<head>
        <script>
                window.onload=function(){
                    var btn=document.getElementById("newOpen");
                    btn.onclick=function(){
                        window.open("12.html","","width=300 height=300");
                    }
                }
                </script>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <button id="newOpen">새창열기</button><br>
</body>
</html>
```



```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
    <script>
        window.onload= function(){
            var upBtn=document.getElementById("up");
            var leftBtn=document.getElementById("left").onclick=function(){
                window.moveBy(-20,0);
            };
            var rightBtn=document.getElementById("right").onclick=function(){
                window.moveBy(20,0);
            };
            var downBtn=document.getElementById("down").onclick=function(){
                window.moveBy(0,20);
            };
            upBtn.onclick=function(){
                window.moveBy(0,-20);
            };
        }
           
        
        </script>
    <title>Document</title>
</head>
<body>
  <input type="button" id="up" value="              UP           "     /><br  />
  <input type="button" id="left" value="   LEFT    "     />
  <input type="button" id="right" value="  RIGHT   "     /><br />
  <input type="button" id="down" value="            DOWN         "   />
</body>
</html>
```



##### 새창 5초 후에 닫기

```html
<!DOCTYPE html>
<html >
<head>
    <script>
        window.onload=function(){
            setTimeout(function(){
                window.close();
            },5000);
        }
        </script>
    <meta charset="UTF-8">

    <title>Document</title>
</head>
<body>
    <h3>5초 후에 window창 종료됩니다.</h3>
</body>
</html>
```



```html
<!DOCTYPE html>
<html >
<head>
        <script>
                window.onload=function(){
                    var btn=document.getElementById("newOpen");
                    btn.onclick=function(){
                        window.open("13.html","","width=300 height=300");
                    }
                }
                </script>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <button id="newOpen">새창열기</button><br>
</body>
</html>
```



##### 11초동안 숫자를 하나씩 출력 하는

```html
<!DOCTYPE html>
<html >
<head>
        <script>
                window.onload=function(){
                    var con=0;
                    var intervalID=setInterval(function(){
                        
                            document.write(++con+"<br>");},1000);
                    setTimeout(function(){
                        clearInterval(intervalID);
                    },11000);
                }
                   
                
                </script>  
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
 <h3>1초 마다 숫자 출력하고 10까지 출력후 window종료</h3>
</body>
</html>
```

#####  새창에서 11까지 출력하고 창 끄기

```html
<!DOCTYPE html>
<html >
<head>
        <script>
                window.onload=function(){
                    var con=0;
                    var intervalID=setInterval(function(){
                        
                            document.write(++con+"<br>");},1000);
                    setTimeout(function(){
                        clearInterval(intervalID);
                        window.close()
                    },11000);
                    // setTimeout(function(){
                    //     window.close()},11000);
                    
                }
                    
                </script>  
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
 <h3>1초 마다 숫자 출력하고 10까지 출력후 window종료</h3>
</body>
</html>
```



##### 웹브라우저에 요소를 추가 하기

```html
<!DOCTYPE html>
<html >
<head>
    <script>
        window.onload=function(){
            var h1=document.createElement("h1");
            var text1=document.createTextNode("새 요소 추가");
            h1.appendChild(text1);
            document.body.appendChild(h1);
            
            var img1=document.createElement("img");
            img1.src="강아지.jpg";
            img1.width=300;
            img1.height=300;
            document.body.appendChild(img1);

            var img2=document.createElement("img");
            img2.setAttribute('src','고양이.jpg');
            img2.setAttribute('width',300);
            img2.setAttribute('height',300);
            console.log(img2.getAttribute("src"));
            document.body.appendChild(img2);
        }

        </script>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <h3>Document 객체를 이용한 문서 구조 변경</h3>
</body>
</html>
```

#####  요소 일일이 바꾸기

```html
<!DOCTYPE html>
<html >
<head>
    <script>
        window.onload=function(){
            var h1=document.createElement("h1");
            var text1=document.createTextNode("새 요소 추가");
            h1.appendChild(text1);
            document.body.appendChild(h1);
            
            var img1=document.createElement("img");
            img1.src="강아지.jpg";
            img1.width=300;
            img1.height=300;
            document.body.appendChild(img1);

            var img2=document.createElement("img");
            img2.setAttribute('src','고양이.jpg');
            img2.setAttribute('width',300);
            img2.setAttribute('height',300);
            console.log(img2.getAttribute("src"));
            document.body.appendChild(img2);

            console.log(document.getElementById("j1").innerHTML);
        var nodelist=document.getElementsByName("j2");
        console.log(nodelist.length);
        console.log(nodelist[0].innerHTML+","+nodelist[1].innerHTML);
        nodelist=document.getElementsByTagName("p");
        console.log(nodelist.length);
        console.log(nodelist[0].innerHTML+","+nodelist[1].innerHTML);
        var p1=document.getElementById("j1");
        p1.style.border="2px solid blue";
        p1.style.color="orange";
        p1.style.fontSize="20";
        console.log(document.getElementById("j1").parentNode.nodeName);
        }

       
    

        </script>
    <meta charset="UTF-8">
   
    <title>Document</title>
</head>
<body>
    <h3>Document 객체를 이용한 문서 구조 변경</h3>
    <p id="j1">javaScipt</p>
    <p name="j2">jQuery</p>
    <p name="j2">SencaTouch</p>
    <p>Node.js</p>
    <p>Angular.js</p>
</body>
</html>
```



getElementById()

getElementByName()

getElementTagName()

getElementByClassName()

는  귀찮기때문에 document.querySelector() 를 사용한다. querySelector()는 특정 name이나 id를 제한하지 않고 css선택자를 사용하여 요소를 찾는 것

문제는 여러가지를 선택후 클릭하면 상자안의 내용이 씌이는 것

```html

<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <title>Query Selector All Demo</title>

  <style type="text/css">
    td {
      border-style: solid;
      border-width: 1px;
      font-size: 200%;
    }


    #checkedResult {
      color: green;
      font-size: 200%;
    }
  </style>
<script>
 window.onload=function(){
     document.getElementById("findChecked").onclick=function(){
         var selected=document.querySelectorAll("*:checked");
         var result="Selected boxes are:";
         for(var i=0;i<selected.length;i++){
             result+=(selected[i].name+" ");
           
         }
         document.getElementById("checkedResult").innerHTML=result;
     }
 }
</script>
</head>

<body>

  <section>

    <table>
      <tr>
        <td><input type="checkbox" name="A1">A1</td>
        <td><input type="checkbox" name="A2">A2</td>
        <td><input type="checkbox" name="A3">A3</td>
      </tr>

      <tr>
        <td><input type="checkbox" name="B1">B1</td>
        <td><input type="checkbox" checked name="B2">B2</td>
        <td><input type="checkbox" name="B3">B3</td>
      </tr>

      <tr>
        <td><input type="checkbox" name="C1">C1</td>
        <td><input type="checkbox" name="C2">C2</td>
        <td><input type="checkbox" name="C3">C3</td>
      </tr>

    </table>
    <div>Select various checkboxes, then hit the button to identify them using querySelectorAll("*:checked").</div>
    <button type="button" id="findChecked" autofocus>Find checked boxes</button>
    <div id="checkedResult"></div>

     
  </section>

</body>

</html>
```



### 13.2 Location 객체

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
  <script>
  window.addEventListener("load",function(){
      setTimeout(function(){
          //location.href="http://www.daum.net";
          //location.assign("http://www.naver.com");
          location.replace("http://www.youtube.com");//3개다 가능
      },3000);
  },false);
  </script>
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

##### 3초후 reload



```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
  <script>
  window.addEventListener("load",function(){
      var panel=document.getElementById("panel");
      var nNum=1+Math.floor(Math.random()*100);
      panel.innerHTML=nNum;
      panel.style.fontSize=100+(Math.random()*100)+"px";
      setTimeout(function(){
//location.reload();
location.href=location.href;// reload()를 사용해도 되고 요 식을 사용해도 된다.
      },3000);
      
  },false);
  </script>
    <title>Document</title>
</head>
<body>
    <div id="panel"></div>
</body>
</html>
```



### 13.3 History객체

- 페이지 이전, 다음 이동

```html
<!DOCTYPE html>
<html >
<head>
    <script>
        window.addEventListener("load",function(){
    
        document.getElementById("back").onclick=function(){
        history.back();
      
        };
        document.getElementById("next").onclick=function(){
       history.forward();
      
            };
        document.getElementById("goBack").onclick=function(){
       history.go(-2);
       
        };
        document.getElementById("goNext").onclick=function(){
        history.go(3);
        
        };

        },false);

        </script>
    <meta charset="UTF-8">
 
    <title>Document</title>
</head>
<body>
    <button id="back">이전</button><br>
    <button id="next">다음</button><br>
    <button id="goBack">go(-2)</button><br>
    <button id="goNext">go(3)</button><br>
</body>
</html>
```

### 13.4 Navigator 객체

- 반응형 웹 컨텐츠를 위해 스크립트가 실행 중인 웹 브라우저 등의 애플리케이션 정보 관리

### 13.5 Screen 객체

- 모니터 크기와 색상 정보 관리

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
  
    <title>Document</title>
</head>
<body>
    <script>
        document.write("화면해상도:"+screen.width+"x"+screen.height);
        document.write("<br>색상수 화면해상도수(비트):"+screen.colorDepth);
        </script>
</body>
</html>
```



##### 물고기 움직이기

```html

<!DOCTYPE html >
<html>
<head>
	<meta  charset="UTF-8">
	<title></title>
	<style>
		body{
			font-size:9pt;
		
		}
		#panel{
			width:600px;
			height:300px;
			border:1px solid #999;
			position:relative;
		}
		
		#bar{
			position:absolute;
			left:50px;
			top:190px;
			width:500px;
			height:20px;
			
			background:#F30;
		}
		
		#img1{
			position:absolute;
			left:50px;
			top:120px;		
		}
		
		#nav{
			text-align:center;
			width:600px;
		}
	</style>
	
	<script>
		 // 시작위치 구하기.
		 // 마지막 위치.(시작위치 + bar의 넓이 - 이미지 넓이)
		 // 이미지의 현재 위치를 시작위치로 설정.
		 // 사용하게 될 이미지(물고기) 엘리먼트를 변수에 저장.
		 // 시작버튼 이벤트 리스너 등록.
		 // 정지버튼 이벤트 리스너 등록.
		 // 타이머 실행.
		 // 이미지 움직이기. -  2px만큼 이동합니다.
         //  위치값이 마지막 위치값을 넘어가는 순간, 
		//  시작 위치<--- 마지막 위치로 이동될수 있도록 방향을 바꿔준다.
		// 위치값이 시작위치값을 넘어가는 순간,
		// 시작위치 ---->마지막 위치로 이동될수 있도록 방향을 바꿔준다.
		// 최종적으로 조절된 위치값을 left에 적용시켜 준다.
		// 타이머 정지시키기.
	</script>
</head>

<body>	
	<div> 
		<h4>#img1을 #bar의 영역에서 계속 좌우로 움직이도록 만들어주세요.</h4>
		<div id="panel">
			<div id="bar"> </div>
			<div id="img1">
				<img src="fish.png">
			</div>
		</div>
		<div id="nav">
			<button id="btn_start">시작</button>
			<button id="btn_stop">멈춤</button>
		</div>
	</div>       
</body>
</html>

```



```html

<!DOCTYPE html  >
<html>
<head>
	<meta  charset="UTF-8">
	<title></title>
	<style>
		body{
			font-size:9pt;		
		}
		
		#panel{
			width:600px;
			height:300px;
			border:1px solid #999;
			position:relative;
		}
		
		#bar{
			position:absolute;
			left:50px;
			top:190px;
			width:500px;
			height:20px;
			
			background:#F30;
		}
		
		#img1{
			position:absolute;
			left:50px;
			top:120px;		
		}
		
		#nav{
			text-align:center;
			width:600px;
		}
	</style>
	
	<script>
		var nEndX;
		var nCurrentX;
		var nStartX;
		var nTimerID;
		var nStep;
		var objIMG;
	
		window.onload=function(){
			var objBar = document.getElementById("bar");
			
			// 시작위치 구하기.
			this.nStartX = objBar.offsetLeft;
	
			// 마지막 위치.(시작위치 + bar의 넓이 - 이미지 넓이)
			this.nEndX = objBar.clientWidth;
			this.nEndX += this.nStartX;		
			this.nEndX -= 128;
	
			// 이미지의 현재 위치를 시작위치로 설정.
			this.nCurrentX = this.nStartX;
			
			this.nStep = 2;
			this.nTimerID = 0;
			
			// 계속해서 사용하게 될 이미지 엘리먼트를 변수에 저장.
			this.objIMG = document.getElementById("img1");
		 
			// 시작버튼 이벤트 리스너 등록.
			document.getElementById("btn_start").addEventListener("click",function(){
				start();
			},false);
			
			// 정지버튼 이벤트 리스너 등록.
			document.getElementById("btn_stop").addEventListener("click",function(){
				stopMove();
			},false);
		}
		 
		
		// 타이머 실행.
		function start(){
			if(this.nTimerID==0)
				this.nTimerID = setInterval(this.startMove,30);
			
		}
		
		// 이미지 움직이기.
		function startMove(){
			// nStep만큼 이동합니다.
			this.nCurrentX += this.nStep;
			
			//  위치값이 마지막 위치값을 넘어가는 순간, 
			//  시작 위치<--- 마지막 위치로 이동될수 있도록 방향을 바꿔준다.
			if(this.nCurrentX>this.nEndX){
				this.nCurrentX=this.nEndX;
				this.nStep=-2;
			}
			// 위치값이 시작위치값을 넘어가는 순간,
			// 시작위치 ---->마지막 위치로 이동될수 있도록 방향을 바꿔준다.
			if(this.nCurrentX<this.nStartX){
				this.nCurrentX=this.nStartX;
				this.nStep=2;
			}
			
			// 최종적으로 조절된 위치값을 left에 적용시켜 준다.
			this.objIMG.style.left=this.nCurrentX+"px";		
		}
		
		// 타이머 정지시키기.
		function stopMove(){
			if(this.nTimerID!=0){
				clearInterval(this.nTimerID);
				this.nTimerID=0;
			}
		}
	</script>
</head>

	<div> 
		<h4>#img1을 #bar의 영역에서 계속 좌우로 움직이도록 만들어주세요.</h4>
		<div id="panel">
			<div id="bar"> </div>
			<div id="img1">
				<img src="fish.png">
			</div>
		</div>
		<div id="nav">
			<button id="btn_start">시작</button>
			<button id="btn_stop">멈춤</button>
		</div>
	</div>       
</body>
</html>

```



# 14장 문서제어

### 14.4 HTML요소 내용 읽고 쓰기

1. innerHTML 프로퍼티

2. textContedt와  innerText프로퍼티

   

### 14.5 노드 생성/삽입/삭제

1. 노드생성

   ```javascript
   var el=document.createElment(요소 이름);//노드 생성
   var textnode=document.createTextNode(텍스트);//새로운 텍스트 생성
   ```

2. 노드 삽입

   ```javascript
   요소 노드.appendChild(삽입할 노드)
   ```

<문>중간에 불독을 삽입해 보기

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
  <script>
  
  </script>
    <title>Document</title>
</head>
<body>
    <ul id="doglist">
        <li>포메라이안</li>
        <li>달라미안</li>
    </ul>
    <script>
        var doglist=document.getElementById("doglist");
        var e1=document.createElement("li");
        var te=document.createTextNode("불독");
        doglist.insertBefore(e1,doglist.children[1]);
         e1.appendChild(te);
     
    </script>
</body>
</html>
```





### 14.6 HTML요소의 위치

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
 <style>
   .box{
       display :inline-block;
       padding:100px;
       margin:100px;
       margin-left:0;
       background-color:yellow;}
 </style>

    <title>Document</title>
</head>
<body>
    <div class="box" id="sec1">#sec1</div>
    <br/>
    <div class="box" id="sce2">#sec2</div>
    <br/>
    <div class="box" id="sec3">#sec3</div>
    <script>
            function getScrollTop(){
                if(window.pageYOffset !== undefined){
                    return window.pageYOffset;
                }else{
                    return document.documentElement.scrollTop || document.body.scrollTop;
                }
            }
            function getScrollLeft(){
                if(window.pageXOffset !== undefined){
                    return   window.pageXOffset;
                    
    }else{
        return document.documentElement.scrollLeft || document.body.scrollLeft;
    }
}
if('scrollRestoration' in history){
    history.scrollRestoration='manual';
}
var element=document.getElementById("sec3");
var rect =element.getBoundingClientRect();
scrollTo(rect.left+getScrollLeft(),rect.top+getScrollTop());
</script>
</body>


</html>
```





### 14.7HTML 폼

<문>비밀번호 확인

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>폼 태그</title>
<script>
 function whenSubmit(){
     //변수 선언
     var pass=document.getElementById('pass').value;
     var pass_check=document.getElementById('pass_check').value;
     //비밀번호 같은지 확인
     if(pass ==pass_check){
         alert('성공');
     }else{
         alert('다시입력해주세요');
         return false;
     }
 }
</script>
</head>
<body>
<form id="my_form" action="data.jsp" method="" onsubmit="return whenSubmit()">
        <label for="name">이름</label><br/>
        <input type="text" name="name" id="name"/><br/>
        <label for="pass">비밀번호</label><br/>
        <input type="password" name="pass" id="pass"/><br/>
        <label for="pass_check">비밀번호 확인</label><br/>
        <input type="password" id="pass_check"/><br/>
        <input type="submit" value="제출"/>
    </form>

</body>
</html>
```

# 15장 이벤트

- DOM level 0 이벤트 모델 : on 이벤트명=function(){} =>이벤트당 하나의 이벤트 핸들러만 연결

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
   <script>
   window.onload=function(){
       alert("load event harler1")
   }
   window.onload=function(){
       alert("load event harler2")
   }
   window.onload=function(){
       alert("load event harler3")
   }//얘만 실행


   </script>
    <title>Document</title>
</head>
<body>
    
    
</body>
</html>
```

- DOM Level 2 이벤트 모델:

  - 이벤트 소스(태그객체).addEventListener("이벤트명",function(){},이벤트캡처여부)-이벤트 캡처여부값은 기본이 false

     이벤트당 하나 이상의 이벤트 핸들러 연결

```html
 <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
   <script>
window.addEventListener("load",function(){
     alert("load event handler1");
 },false);
 window.addEventListener("load",function(){
     alert("load event handler2");
 },false);
 window.addEventListener("load",function(){
     alert("load event handler3");
 },false);

   </script>
    <title>Document</title>
</head>
<body>
    
    
</body>
</html>
```

- 이벤트 대한 이벤트 핸들러가 한번만 수행후 이벤트 핸들러 취소하려면
  - 이벤트 소스.on이벤트속성=null;
- 이벤트 핸들러 함수 내부에서 이벤트 객체의 속성들을 핸들링할때 이벤트 소스 객체를 this참조한다.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
   <script>
 window.addEventListener("load", function(){
	  var h3 = document.querySelector("#evt");	 
	  h3.onclick =function(){
		   alert("까꿍");
		   //h3.onclick =null;
		  this.onclick = null;
	 } ; 
	 document.querySelector("#evt2").onclick = function(){
	   this.style.color = 'blue';
	   this.style.backgroundColor = 'orange';
	};

}, false);

   </script>
    <title>Document</title>
</head>
<body>
        <h3 id="evt"> 이벤트 핸들러 한번만 </h3>
        <h3 id="evt2"> 클릭이벤트가 발생하면 배경색은 오렌지색, 글자색상은 파란색으로 변경하는 핸들러 실행 </h3>
       
        
        
    
</body>
</html>
```



<문제>강제이벤트 버튼을 누르면 숫자를 카운트 한다.

``` html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
<script>
window.onload=function(){
    document.getElementById("btn1").onclick=function(){
        var n1=document.getElementById("count1");
        n1.innerHTML=Number(n1.innerHTML)+1;
    }
    var count=0;
    document.getElementById("btn2").onclick=function(){
        var n1=document.getElementById("count2");
       count++;
        n1.innerHTML=count;
        document.querySelector("#btn1").onclick();//강제이벤트 발생

    }
}
</script>
    <title>Document</title>
</head>
<body>
<button id="btn1">Button 1</button>
<button id="btn2">Button 2</button>
<h3>Button 1 Click Count:<span id="count1">0</span></h3>
<h3>Button 2 Click Count:<span id="count2">0</span></h3>
    
</body>
</html>
```



### 15.4 버블링과 캡처링

- 이벤트 **버블링**은 자식 태그객체에서 발생된 이벤트가 부모 태그 객체로 이벤트 전파되는 것
- 이벤트 **캡처링**은 부모 태그객체에서 발생된 이벤트가 자식 태그 객체로 이벤트 전파되는 것
- 이벤트 버블링을 막으려면

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>이벤트</title>
<style>
div, h1, p { border:2px solid black;
             padding : 10px;
             margin : 10px; }
</style>
<script>
 window.addEventListener("load", function(){
	document.getElementById("outerDiv").onclick= function(){
		this.style.backgroundColor='gray';
	}
	document.getElementById("innerDiv").onclick= function(){
		this.style.backgroundColor='cyan';
	}
	document.getElementById("header1").onclick= function(){
		this.style.backgroundColor='magenta';
	}
    document.getElementById("p1").onclick= function(evt){	//이벤트 객체를 사용하기 위해서 이름 지정
        var event= evt //|| window.event; 비교는 IE일때만 
       // event.cancelBubble=true;//IE의 이벤트 전파 취소 함수
        if(event.stopPropagation){
            event.stopPropagation();//w3c 표준 이벤트 전파 취소 함수, 뭐가 작동할지 몰라 두개 다 작성
        }	 //크롬의 경우 if를 안 사용해도 된다.
		this.style.backgroundColor='orange';
	}
}, false);
</script>
</head>
<body>
 <h3> 자바스크립트 버블링과 캡처링 </h3>
자바스크립트 버블링 : html문서내에서 자식 태그객체에서 발생된 이벤트가 부모 태그 객체로 이벤트 전파되는 것 <br>
자바스크립트 캡처링 : html문서내에서 부모 태그객체에서 발생된 이벤트가 자식 태그 객체로 이벤트 전파되는 것 <br>
<div id="outerDiv">
  <div id="innerDiv">
    <h1 id="header1">
       <p id="p1">이벤트 전파</p>
    </h1>
  </div>
</div>
</body>
</html>
```

### 15.5 이벤트 취소

- 브라우저에서 제공하는 기본 취소

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>이벤트</title>
<script>
window.addEventListener("load", function(){
 //브라우저 기본 이벤트 핸들러 취소
 document.getElementById("searchForm").onsubmit=function(){
    return false;
    //event.preventDefault();
 }//sumit 될때 false를 리턴하여 이벤트 실행취소시킨다.
 document.getElementById("link1").onclick=function(){
    // return false;
    event.preventDefault();//표준 권장 취소 메서드
}
}, false);
</script>
</head>
<body>
 <h3> 브라우저에 정의된 기본 이벤트 취소 </h3>
 브라우저에서 자동으로 처리해주는 기본 이벤트 핸들러를 취소하려면 이벤트 핸들러 함수를  override해서 false를 리턴합니다.<br>
<a id="link1" href="http://www.google.com">구글</a><br>
<form id="searchForm" action="data.jsp" method="GET">
찾기 <input type="search">
<input type="submit" value="검색">
</form>
</body>
</html>
```



##### 경품추천기 

- 초기화는 한번만 돌게 하기 위해서 와 if문을 실행하기 위해서.......?

```html

<!DOCTYPE html >
<html>
<head>
	<meta charset="UTF-8">
	<title></title>
	<style>
		body{
			font-size:9pt;
		}
		#panel1{
			border:1px #000000 solid;
			line-height:400px;
			font-size:100px;
			width:400px;
			height:400px;
			text-align:center;
			vertical-align:middle;		
		}
	
	</style>
	<script>
		 
		var panel1;//숫자 출력할 영역 div객체
		var nTimerID;//반복수행될 intervalId값 저장 변수
		var labTotal;//참여 인원수 입력input태그 객체 저장할 변수
		var nTotalMember;
		window.onload=function(){
			// 숫자가 출력될 #panel1을 찾아 전역변수에 담아둡니다.
			panel1 = document.getElementById("panel1");
			nTimerID = 0;
			// 참여인원 정보가 입력된 패널을 찾아 전역변수에 담아둡니다.
			labTotal = document.getElementById("lab_total");//input 태그 객체
			nTotalMember = 0;
			// 이벤트 초기화 실행.
			var btnStart = document.getElementById("btn_start");
			btnStart.addEventListener("click", function(){
				if(nTimerID==0){
					//입력된 참여인원수를 구해옵니다.
					nTotalMember = Number(labTotal.value);
					// 타이머 시작시 #panel1의 글자색을 초기화 시켜 줍니다.
					panel1.style.color = "#000000";	//검은색		
					nTimerID = setInterval(createNumber,20);	
				}
			}
			,false);
			var btnStop = document.getElementById("btn_stop");
			btnStop.addEventListener("click",function(){
				if(nTimerID){
					clearInterval(nTimerID);
					nTimerID = 0;
					//출력효과 추가.
					panel1.style.color = "#ff0000";	
					panel1.style.fontSize = "200px";
				}
			},false);
		}		
		 
		
		// 랜덤하게 1에서 참여인원수 사이의 숫자를 만들어 냅니다.
		function createNumber(){	
			var nNum = 1+Math.floor(Math.random()*this.nTotalMember);
			//만들어진 숫자를 innerHTML에 대입시켜 줍니다.
			panel1.innerHTML = nNum;
			// 폰트 크기를 100~200으로 랜덤하게 설정해줍니다.
			panel1.style.fontSize = 100+(Math.random()*100)+"px";//font size는 199...?까지?
		}
			
		 
		
		 
	</script>
</head>

<body>
	<div> 
		<h4>경품추첨기-ver 0.1</h4>
	
		<div id="panel1" > 1
			<!-- 이곳에 숫자가 출력됩니다. -->
		</div>
	
		<div id="nav">
			참여인원 : <input type="text" id="lab_total" value="100">
			<button id="btn_start">시작</button>
			<button id="btn_stop">멈춤</button>
		</div>
	</div>
</body>
</html>

```



# 모르는 것 자세하게!

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
//반환 타입은 문자열
window.confirm("메세지") //반환타입은 boolean
```

##### 출력 하기

```javascript
document.write(), document.writeln() // html 문서의 body영역 출력
console.log(), console.dir()//dir 은 내부의 계층 구조를 볼때, 브라우저 or node같은 자바스크립트 실행환경에서 제공하는 콘솔창에 출력
window.alert("메세지")
```

##### 경고장 띄우기

```javascript
alert("경고장 띄우기")
```

##### 배열

- 자바스크립트에서 배열은 모든 타입을 요소로 저장가능

```html
<script>
var arrays=[1,'hello',true,function(){},{name:'korea'},[100,200]];
                for(var index in arrays){
                    document.write(index+":"+arrays[index]+"<Br>");
                }
        </script>
```

##### 함수적 프로그래밍 특성

1. 변수에 함수를 저장 할 수 있다.
2. 배열의 요소로 함수를 저장 가능
3. 함수 내부에 함수 정의(nested function)
4. 함수에서 함수 반환 가능.
   - 내부에 함수를 정의하거나, 함수를 반환 하는 함수를 **고차 함수**
5. 함수의 인수로 함수를 전달 가능.
   - 인수로 전달되는 함수는 **콜백 함수**

