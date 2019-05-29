# Day1~8

## 자바

자바 특징

* 운영체제 독립적(but JRE필요)
* 객체지향언어
* 자동 메모리 관리(가비지컬렉터)가 자동적으로 관리
* 네트워크라 분산처리 지원
* 멀티쓰레드 지원
* 동적 로딩 지원

##  JVM

- JRE에 포함되어 있는 '자바 실행 위한  가상기계'

## 자바개발환경

- javac.exe 자바 컴파일러(자바소스코드를 바이트코드로 컴파일)
- java.exe 자바 인터프리터 해석&실행
- javadoc.exe 문서 자동생성
- jar.exe 압축프로그램

## 주석

- /* */ 범위주석
- // 한줄주석

## 변수

- 단 하나의 값을 저장할 수 있는 메모리 공간
- 자바 변수 선언or 실행 문장 한개라도 반드시 클래스 단위로 소스코드 작성
- 키워드는 식별자(변수,메소드,클래스)로 사용 못한다.

## 기본형

|        | 1byte  | 2byte | 4byte | 8byte  |
| ------ | ------ | ----- | ----- | ------ |
| 논리형 | boolen |       |       |        |
| 문자형 |        | char  |       |        |
| 정수형 | byte   | short | int   | long   |
| 실수형 |        |       | float | double |

- casting은 byte short (char) int long float double 순서이다. char의 경우 같은 2byte여도 short와 범위가 다르기 때문에(char는 문자이기에 번위에 음수가 없다.) 서로 형변환이 필요하다. 

```java
public class Test {
    //속성+기능
	int a; //멤버변수 , 인스턴스 변수
	public static void main(String[] args) {
		 int b; //로컬변수, 사용전 반드시 초기화 필요!
		 System.out.println("test");
		 System.out.println(b);//초기화 안해서 오류
		 System.out.println(a);//객체 생성없이 사용해서 오류
	}
}
```

## 연산자

- 단항연산자 : +, -, ++, --, !, ~, ()

- 이항연산자 : 산술연산자 (*, /, %, +,-) 정수/정수=>정수

  - 비교연산자 ( >, >=, <, <=, ==, !=)
  - 비트연산자 (&, |, ^)
  - 논리연산자 (&&, ||)
  - shift연산자 (<<, >>, >>>)
    - `X<<Y : X*2^Y의 결과`
    - `X>>Y : X/2^Y의 결과, 왼쪽 비트를 sign 비트로 채움`
    - `X>>>Y :왼쪽 비트는 항상 0으로 채움, 결과는 항상 양수`

  

- 삼항연산자

## 반복문

### if

```java
if(조건표현식)  문장;
if(조건표현식) {
   문장;
   ...
}else {
   문장;
   ....
}
```

```java
//다중 if문
if(카운트 변수 초기화;조건식;증감식) {
   문장;
   ...
}else if(조건표현식) {
   if(){
       //if안에 if문이 올 수 있다.반복문안에 반복문 사용 가능 하며, 반복문안에 제어문 사용 가능하다. 
   }
}else if(조건표현식){
  문장;
   ....
}else{
  문장;
   ....
}
for( ; ;){
    if(종료조건)break;//무한루프는 반드시 반복문 내부에 종료 조건을 넣어주면 좋다.
}
```

### Switch

```java
//byte, short, int, char, String 
switch(표현식) {
   case 값1 :  문장 ; break;
   case 값2 :  문장 ;
   .....
   default : 문장 ;
}//조건식 결과(=값)는 정수 또는 문자열이어야 한다. case문의 값은 정수 상수만 가능하며, 중복되지 않아야 한다.
```

### while, do~while

```java
int num=0;
while(조건표현식){
  반복 수행 문장;
    System.out.println(num);
}//while은 객체 생성시 반복문 밖에서 해야 한다..
while(true){//무한루프 방식이며
    if(조건)break;//를 작성하여 반복문 빠져나오는 조건을 만들어주자.
}

//while문은 선 조건 체크, 후 실행
//do ~ while문 선 실행, 후 조건 체크 그렇기에 do~while은 최소 한번은 무조건 실행된다.
do {
 반복 수행 문장;
 }while(조건표현식);//마감한 조건을 작성한다.
```

## 제어문

### break, continue

```java
public static void main(String[] args) {
		int num=15;
		int sum=50;
		while(true){
			if(num<50){
		 	 break; //break;를 사용하면 조건에 걸릴시 while(반복문)을 완전히 벗어난다. 
		      
		}else {
			sum+=num;
		}
		
}
		System.out.println(sum);
}
}
//결과값은 50이 나온다. if을 완전히 벗어남을 알 수 있다.
```

- continue는  break와는 다르게 블럭의 끝으로 이동하기에 반복문을 벗어나지 않는다.
- break문은 근접한 단 하나의 반복문만을 벗어나기에 중첩된 경우에는 break문으로 완전히 빠져나가기 힘들다. 이때 사용하는 것이 이름을 붙이는 것!



