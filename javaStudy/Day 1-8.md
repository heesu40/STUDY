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

### 상수

- 변하지 않는 변수

#### 리터럴

- 변수의 값이 변하지 않는 데이터

#### 키워드

- 특정 용도로 사용하기 위해서 미리 예약 된 언어

## 기본형

|        | 1byte  | 2byte | 4byte | 8byte  |
| ------ | ------ | ----- | ----- | ------ |
| 논리형 | boolen |       |       |        |
| 문자형 |        | char  |       |        |
| 정수형 | byte   | short | int   | long   |
| 실수형 |        |       | float | double |

- casting은 byte short (char) int long float double 순서이다. char의 경우 같은 2byte여도 short와 범위가 다르기 때문에(char는 문자이기에 번위에 음수가 없다.) 서로 형변환이 필요하다. 

```java
byte b=20;
char n='A';
int i=100;
long pi=200000L; 

b=i;//error byte(1byte)<- int(4byte)
n=b;//error  char(2byte)<-byte(1byte)이지만 범위가 다르다.char는 음수 가 없다.
short s=n;//error  short(2byte)<-char(2byte)지만 범위가 다르다.
float d=pi;
i=n; 
```

- byte-> shrot -> int -> long->  float->  double (자동 변환 가능)

- char->int(자동 변환 가능)

- 접미사가 있는 자료형은  long, float,double , 접미사는 대소문자 구별 **X**

  ```java
  byte a= 300;//범위 초과
  char ch='';//적어도 한개의 문자 필요
  char ch1='ch';//두개 이상 안됨
  float f=1.12;//f붙이거나 형변환 필요
  double dl= 3.5e3f;
  ```

- 기본값
  - boolean - true, false
  - char - '\u0000'
  - float- 0.0f or 0.0F
  - int -0
  - long -0L or 0l
  - String- null( 참조형은 기본값이 null이다.)

## 참조형

- 크기는 4byte
- class, interface,enum,배열(array)

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

```java
public static void main(String[] args) {
	System.out.println("2"+"4");//24
	System.out.println("["+true+""+"]");//[true]
	System.out.println('A'+'C');//132(A=65,C=67)
	System.out.println('1'+6);//55
	System.out.println('1'+'6');//103(1=49 6=55)
	System.out.println('H'+"ello");//Hello
	//System.out.println(true+null); 오류 발생
     //문자의 합의 결과는 int 정수값인데 byte,char,short의 경우 자동casting  후 더해지기 때문이다.
}
```

```java
//System.out.println(3&&4); 오류난다.
System.out.println(3&4);//0
System.out.println(true && false);//false
System.out.println(true &false);//false
```
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

## 배열

- 특징
  - 배열은 Reference Type, 객체로 취급한다.
  - new 키워드로 생성한다.
  - new 키워드로 생성할 경우 heap메모리에 생성된다.
  - 배열은 타입에 따라서 요소(element)값을  기본값으로 저장한다.
  - 배열은 객체로 생성되면 자동으로 length 속성(멤버필드)에 요소 개수 size가 저장된다.
- 1차원 배열
  - 하나의 변수로 동일한 타입의 1개이상의 값을 저장하고,참조할 수 있는 집합 유형
  - 배열은 생성후 size조정이 불가하다.	

```java
int[]  array1;   //배열 선언
String[]  array2;
array1 = new int[5];  //배열은 생성시 size 선언해야 한다.
//명시적으로 배열의 요소값을 초기화하시 않으면 정수, 실수 타입은 자동 0으로 초기화 된다.
int[]  array3 = new int[10]; //선언과 생성을 동시에..
int[]  array4 = new int[]{'A', 'B', 'C'};//선언, 생성, 명시적 초기화, 이경우 size 정의 안한다.
```

- 2차원 배열
  - 1차원 배열이 여러개 구성된 집합 구조

```java
int[][] nums; //배열 선언
int nums2[][];
int[] nums3[];
nums = new int[5][5]; //배열 생성, 자동 0으로 초기화 
nums2 = new int[5][]; //배열 생성, 1차원 배열이 5개 저장, 1차원 배열의 저장될 요소 개수는 동적이다.
 
nums2 = new int[ ][5]; //컴파일 에러
```



## 클래스 

특징

- 클래스는 Reference Type 
- 클래스는 객체를 생성하기 위한 객체의 속성과기능을 설계한 설계도로 메모리에 객체로 생성해야 사용 가능.

```java
Scanner input = new Scanner(System.in); //객체를 생성
int num = input.nextInt()
String name = input.next();
```

객체

- 인스턴스
- 인스턴스화 한다= 클래스를 메모리에 객체로 생성하는 동적 개념.

클래스선언 

-  자바는 클래스대 클래스 상속은 단일 상속만 지원
- 명시적으로 상속받지 않으면 자동으로 java.lang.Object클래스를 상속받는다..(컴파일시에 JDK가 자동으로 )

| AccessModifier   | [Modifier]     | class | 이름 | [extends 부모클래스] | [implements 인터페이스,인터페이스.....] | {}   |
| ---------------- | -------------- | ----- | ---- | -------------------- | --------------------------------------- | ---- |
| public (default) | final abstract |       |      |                      |                                         |      |

멤버변수 선언(속성)

- 객체(인스턴스)의 멤버변수는 명시적으로 초기화하지 않으면 JVM이 객체를 생성할때 default초기값으로 초기화를 한다.

| AccessModifier | [Modifier] | 타입 변수 이름=초기값 |
| -------------- | ---------- | --------------------- |
| public         | final      |                       |
| protected      | static     |                       |
| (defalut)      | volatile   |                       |
| private        | transient  |                       |

메서드 선언(기능)

- final 선언된 상수는 반드시 명시적 초기화가 필요
-  static 선언된 변수는 객체 생성없이 클래스이름으로 사용 가능=> 클래스 변수
- static 변수는 동일한 클래스로부터 생성되는 객체들로부터 공유해야 하는 값을 설계할 때 사용한다.

| AccessModifier | [Modifier]  | 리턴타입     | 메서드이름()                  |
| -------------- | ----------- | ------------ | ----------------------------- |
| public         | final       | void         | ()안에 [타입변수,타입변수...] |
| protected      | abstract    | 모든타입가능 |                               |
| (defalut)      | static      |              |                               |
| private        | sychronized |              |                               |



## 메서드

### Random 난수 생성 메서드

```java
Random  r = new Random();
int num = r.nextInt( );//-2^31~2^31-1
```

