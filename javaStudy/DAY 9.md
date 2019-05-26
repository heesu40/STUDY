

# DAY 9

## 7장 수업내용

- 인터페이스

  - 용도 : 사용자(User)와 제공자(Provider) 중간 매개체(연결) 역활

    - 사용자와 제공자 간의 상속이 없음에도 가능.

  - 구성요소 : public static final 상수 속성 ,abstract 메서드 , static 메서드 ,default 메서드

    - abstract 메서드는 구현 body 없다.

      '~();'

    - static과 default는 구현 body있다.

    - '~(){}'

  - 설계시, 서로 다른 시스템을 통합할때 표준화를 위해서 활용

  - 클래스는 일원화된 구조(선언+구현)

  - 인터페이스는 이원화된 구조(선언) , 그래서 구현 클래스가 있어야 한다.

  - public interface 이름 [extends 인터페이스, 인터페이스.....] (인터페이스는 인터페이스만 상속 가능,다중상속 가능)

    - public class 이름 implements 인터페이스, 인터페이스....{}

  - 인터페이스는 reference 변수(객체명) 타입으로 선언 가능하다.

  - 인터페이스는 new를 사용해서 객체 생성 가능하려면 구현한 클래스로 객체 생성해야한다.

    (다형성객체)

- abstract 

  - (추상, 구현이 없고, 선언만 존재한다.)-클래스, 메서드
  - 일반적으로 abstract메서드는 클래스 설계시 모든 자식 클래스의 공통 기능을
  - abstract 메서드는 상속 받은 자식 클래스에서 반드시 override해서 구현 body를 정의해야만 객체 생성이 가능하다.
  - abstract 클래스는 new 사용해서 인스턴스(객체) 생성 불가능 .
    - abstract메서드가 선언되어 있는 클래스 또는 객체 생성 못하게 클래스 설계할 때 사용
  - abstract 메서드가 정의되어 있지 않아도 클래스를 abstract 라고 선언할 수 있다. (객체생성 못하게 하기 위해서)

​	

## 8장 예외처리

프로그램 오류는 컴파일 에러와 런타임 에러가 있다.

컴파일 에러- 컴파일 할때 나타나는 에러

- Checked Exeception -범위 이상의 에러 임으로 미리 알려준다.(처리 가능 외의 오류, I/o, network,DB등)

런타임 에러- 실행중 발생하는 에러

- 논리적 에러-실행은 되지만 의도와 다르게 동작.

- 런타임 에러는 또 에러와 예외 두가지로 구분

  1.에러- 수습될 수 없는 심각한 오류

  2.예외- 다소 미약한 오류

  - 예외중 Exception클래스 -사용자의 실수와 같은 외적 요인에 의한 예외
  - 예외중 RuntimeException클래스-프로그램의 실수로 발생하는 예외

예외처리 방법 (declare,handle)

- 예외 발생-declare,handle
- 예외 발생 -throw new 발생시킬예외클래스 생성자()
- 사용자 정의 Exception 정의, 생성, 사용
  1. 예외 처리(declare)-throw
  2. 예외 처리(handle)- try~catch~finally

예외클래스의 상속 계층 구조

- catch가 여러번 선언될 경우, 예외 클래스의  상속 계층구조의 역순으로 구체적인 예외클래스타입부터 선언해준다. 즉 큰 오류부터 작성하면 작은 오류를 잡지 못한다.

```
try~catch~finally
try~finally
try~catch(0or M)

try{
예외 발생 가능성 문장;
문장;
}catch(예외클래스타입 객체){
	예외처리 문장;
}catch(예외클래스타입 객체){
	예외처리 문장
}finally{
	예외 발생과 무관한 반드시 수행해야 할 문장;
	ex)사용했었던 resource들의 정리(close())코드문장
}
```



```java
public class 짝수홀수 {

	public static void main(String[] args) {
		System.out.println("main start");
		int num =-1;
		try {
		num =Integer.parseInt(args[0]);
		System.out.println("other statement processing...");
		}catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("배열관련예외처리");
		}catch(NumberFormatException e) {
			System.out.println("숫자 형식관련 예외 처리");
		}catch(Exception e) {
			e.printStackTrace();//보안관련 실제로는 삭제하는게 좋다
			System.out.println(e.getMessage());
		}finally {
			System.out.println("resource 정리");
		}
		if(num%2==0&& num>0) {
			System.out.println(args[0]+"짝수입니다.");
		}else if(num%2==1 && num>0){
			System.out.println(args[0]+"홀수입니다.");
		}

		System.out.println("main end");
	}

```

Run configuation 하고 'a'를 넣게 되면 숫자 형식 관련 예외 처리에 걸리므로 "숫자형식 관련 예외"가 출력되어야 하며 finally는 무조건 실행이므로'' resource정리'' 가 나오고 if, else if 구문은 해당이 없기에 넘어간다.

결과는 

`main start
숫자 형식관련 예외 처리
resource 정리
main end`

사용자정의 예외 클래스

- 사용자 정의 예외 클래스를 정의할때는 구체적인 예외 처리 관련 API의 Excetion  속성과 메서드를 추가해서 만든다.

- 사용자 정의 예외 클래스를 정의할때 Eeception을 상속을 받아서 예외처리에 필요한 속성과 메서드를 추가해서 만든다.

```java
public class XXXException extends Exception {
    //속성
    //생성자
    //멤버 메서드
}
```

```java
public class ExceptionHandleTest {
    
	public void checkTall(double tall) throws AbnormalValueException {
		//중학생 키 범위가 140이상 180이하 여부를 체크해서
		//범위가 아니면예외를 던집니다
        
		if(tall<140) throw new AbnormalValueException("140보다 작습니다");
		if(tall>180) throw new AbnormalValueException("180보다 큽니다");
	}
	
	public static void main(String[] args) {
		double[] talls = new double[] { 155.5,163.2,170.4,149.5,
				128,168,189.5,166,172,169,158,173};
		ExceptionHandleTest  test = new ExceptionHandleTest();
        //키값의 범위를 체크해서
		//예외 발생하면 예외처리합니다. => 작년도 키 평균값으로 보정합니다.
		//올해의 중학생 평균 키값을 출력합니다.
		for(int i=0;i<talls.length;i++) {
			try {
			     test.checkTall(talls[i]);
			}catch(AbnormalValueException e) {
				System.out.println(e.getMessage()+", 작년도 키값으로 보정합니다.");
				talls[i] = e.getOldTall();				
			}
		}
		double hap = 0.0;
		for(double tall : talls)
			hap += tall;
		System.out.println("올해 중학생 평균 키는 "+(hap/talls.length)+"cm입니다.");
		
		}//main end

}//class 
```

```java
public class AbnormalValueException extends Exception {
	private double oldTall = 161.2;

	public AbnormalValueException(String message) {
		super(message);
	}
	public double getOldTall() {
		return oldTall;
	}
	}
```

위의 문제로 복습해 보자.





