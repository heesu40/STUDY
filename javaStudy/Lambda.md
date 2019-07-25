# java file programing

### java.io.file

- 파일 시스템의 파일 정보를 얻기 위한 클래스
- 파일 크기, 파일 속성, 파일 이름 등의 정보를 얻어내는 기능과 파일 생성 및 삭제 기능 제공

###### java.io.FilenameFilter 예제(파일이름 필터)

자바 파일 이름 필터다.

```java
package open1;

import java.io.File;
import java.io.FilenameFilter;

public class JavaIoFilenameFilter {
	public static void main(String[] args) {      
	      File f = null;
	      File[] paths;      
	      try {        
	         // create new file
	         f = new File("c:/test");
	         
	         // create new filename filter
	         FilenameFilter fileNameFilter = new FilenameFilter() {   //익명으로 객체 생성하면서 오버레이드하고있다.
	            @Override
	            public boolean accept(File dir, String name) {
	               if(name.lastIndexOf('.')>0) {
	               
	                  // get last index for '.' char
	                  int lastIndex = name.lastIndexOf('.');
	                  
	                  // get extension
	                  String str = name.substring(lastIndex);
	                  // match path name extension
	                  if(str.equals(".txt")) {
	                     return true;
	                  }
	               }               
	               return false;
	            }
	         };
	         
	          // returns pathnames for files and directory
	         paths = f.listFiles(fileNameFilter);         
	         // for each pathname in pathname array
	         for(File path:paths) {         
	            // prints file and directory paths
	            System.out.println(path);
	         }         
	      } catch(Exception e) {         
	         // if any error occurs
	         e.printStackTrace();
	      }
	   }


}

```

### Lambda Expressions

- 익명 함수를 생성하기 위한 식
- 자바 코드가 간결해지고, 컬렉션 요소를 필터링하거나 매핑해서 원하는 결과 쉽게 집계
- ` Runnable runnable (매개변수, ....) -> { 실행코드; ... }`
  - 매개변수가 하나인 경우 생략 가능, 실행문도 하나만 있다면 생략 가능
- 람다식으로 표현가능 한 것은 함수적 인터페이스라 한다.
  - 추상 메서드가 **하나**여야 한다!(딱 **한개**)
  - @FunctionalInterface-두 개 이상의 추상 메소드가 선언되지 않도록 컴파일러가 체킹해주는 기능
- 람다식에서 this는 내부적으로 생성되는 익명 개체의 참조가 아닌, 람다식을 실행한 객체의 참조다.**주의**
- 익명함수의 매개변 수 또는 로컬 변수는 람다식 내부에서 외부에서 변경이 불가하다(자동으로 final 처리가 된다.)



###### 함수적 인터페이스-java.util.function

Consumer- 매개값있고, 리턴값은 없어, 매개값 소비하는 역할만

Supplier-매개값은 없고, 리턴값은 있다.호출한 곳으로 데이터를 리턴 역활

Function-매개값 있고, 리턴값도 있다.매개값을 리턴값으로 매핑(타입 변환) 하는 역할

Operator-매개값도 있고, 리턴값도 있다. 매개값을 연산하고 결과를 리턴하는 역할

Predicate-필터를 하기위해 사용한다.(리턴타입은 불리언,boolean)



###### Non람다식->람다식 (코드 변화 확인)

```java
public class NonLambdaExam {
        public static void main(String[] args) {
//익명 클래스다 아래는 
            new Thread(new Runnable(){
	   public void run(){
                    for(int i = 0; i < 10; i++){
                         System.out.println("hello");
                }
            }}).start();
        }   
    }

```



```java
public class LambdaExam {  
        public static void main(String[] args) {
            new Thread( ()->{
                for(int i = 0; i < 10; i++){
                    System.out.println("hello");
                }
            } ).start();
        }   
    }

```

람다식으로 하면 좀더 코드가 간결해진다.





###### 매개변수와 리턴값이 없는 람다식

```java
package open1;

@FunctionalInterface
public interface MyFunctionalInterface {
	public void method();

}

```



```java
package open1;

public class MyFunctionalInterfaceExam {

	public static void main(String[] args) {
        MyFunctionalInterface fi; 
        fi = () -> {    //인터페이스를 타켓 타입으로 갖는 람다식
            String str = "method call1";
            System.out.println(str);
        }; 
        fi.method();                 //람다식 호출
        fi = () -> {   
            System.out.println("method call2");
        };
        fi.method(); 
        fi = () -> System.out.println("method call3");
        fi.method();
    }//2,3번 방식을 더 많이 사용 한다 

	}



```

###### 매개 변수가 있는 람다식

```java
@FunctionalInterface
public interface MyFunctionalInterface2 {
    public void method(int x);
}

```

```java
public class MyFunctionalInterfaceExam2 {
 
    public static void main(String[] args) {
        MyFunctionalInterface2 fi;
 
        fi = (x) -> {
            int result = x * 5;
            System.out.println(result);
        };
        fi.method(2);
 
        fi = x -> System.out.println(x * 5);
        fi.method(2);
    }
 
}

```



###### 리턴값이 있는 람다식



```java
@FunctionalInterface
public interface MyFunctionalInterface3 {
    public int method(int x, int y);
}

```



```java
public class MyFunctionalInterfaceExam3 {
    public static void main(String[] args) {
        MyFunctionalInterface3 fi;
 
        fi = (x, y) -> {
            int result = x + y;
 
            return result;
        };
        System.out.println(fi.method(2, 5));
 
        fi = (x, y) -> {
            return x + y;
        };
        System.out.println(fi.method(2, 5))
              fi = (x, y) -> x + y;
        System.out.println(fi.method(2, 5));
 
        fi = (x, y) -> sum(x, y);
        System.out.println(fi.method(2, 5));
    }
 
    public static int sum(int x, int y) {
        return x + y;
    }
}

```

### 클래스 멤버와 로컬 변수 사용

1. 클래스의 멤버는 제약 사항 없이 사용 가능
2. 로컬 변수는 제약 사항이 따른다.



###### 메서드 내부에 람다식 정의 (아우터필드 정의 가능, 클래스내 제약없음)

클래스는 제약이 없음을 알 수 있는 예제이다.

```java
public class UsingThis {
    public int outterField = 10; 
    class Inner {
        int innerField = 20; 
        void method() {
            MyFunctionalInterface fi = () -> {
                System.out.println("Outter Field: " + outterField);
                System.out.println("Outter Field: " + UsingThis.this.outterField + "\n");
 
                System.out.println("Inner Field: " + innerField);
                System.out.println("Inner Field: " + this.innerField + "\n");//여기서 this는
//inner class를 의미한다!
            };            
            fi.method();
        }
    }
}

```

```java
public class UsingThisExam { 
    public static void main(String[] args) {
        UsingThis usingThis = new UsingThis();
        UsingThis.Inner inner = usingThis.new Inner();
        inner.method();
    } 
}

```

###### 메서드 내부에서 선언된 람다식에서 선언된 로컬변수는변경 불가



```java
public interface MyFunctionalInterface {
    public void method();
}

```

```java
public class UsingLocalVariable {
    void method(int  arg) {
        int localVar = 40;
 
        // arg = 31; // final 특성 때문에 수정 불가
        // localVar = 41; // final 특성 때문에 수정 불가
 
        MyFunctionalInterface fi = () -> {
            System.out.println("arg: " + arg);
            System.out.println("localVar: " + localVar);
        };
 
        fi.method();
    }
}

```

```java
public class UsingLocalVariableExam { 
    public static void main(String[] args) {
        UsingLocalVariable ulv = new UsingLocalVariable();
        ulv.method(20);
    } 
}

```



### Stream

- 자바 8부터 추가된 컬렉션(배열 포함)의 저장 요소를 하나씩 참조해서 람다식(functional-style)으로 처리할 수 있도록 해주는 반복자
- 컬렉션(java.util.Collection)의 stream() 메소드로 스트림 객체를 얻고 나서 stream.forEach (name -> System.out.println(name) ); 메소드를 통해 컬렉션의 요소를 하나씩 콘솔에 출력합니다.

```java
package open1;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class Test {
	public  static void main(String[] args) {
		List<String> list = Arrays.asList("John", "Simons", "Andy");
		Stream<String> stream = list.stream(); 
		stream.forEach( name -> System.out.println(name) );//name은 변수이름(??? 같은거라 다른걸로 바꾸어도 괜찮다
		//각각을 java api를 보고 각각의 의미를 찾아보는 것이 공부에 도움이 될 것이다.
		//하나씩 꺼내서 출력만 하겠다~란 의미(행위를 람다식으로 넘겨줄 수 있다.

	}
}

```



##### 특징

1. 내부 반복자를 사용하므로 병렬 처리 쉽다(ForkJoinPool)
2. 중간 처리에서 매핑, 필터링, 정렬을 수행하고,  최종 처리 작업에서 반복, 카운팅, 평균, 총합등의
   집계 처리를 수행한다. 
3. 이걸 사용하면 내부반복자를 이용하여 쉽게 처리 가능! 외부 반복자 로 계속 next()를 호출 할 필요가 없다.

###### 디렉토리에서 스트림 얻기

files의 정적 메소드인 list()를 이용해서 디렉토리의 내용을 스트림을 통해 읽고 콘솔에 출력

```java
//List all files and sub-directories using Files.list() 
Path path = Paths.get("C:/Users/workspace/");//C로만 쓰고 찾아보자.
        Stream<Path> stream = Files.list(path);
        stream.forEach(p -> System.out.println(p.getFileName()));

```

```java
//List only files inside directory using filter expression 
Files.list(Paths.get("."))
        .filter(Files::isRegularFile)//isRegularFile만 뽑아 오겠다 란 의미
        .forEach(System.out::println);//:: 형식을 사용하는데..

```

```java
//List files and sub-directories with Files.newDirectoryStream() 
Files.newDirectoryStream(Paths.get("."))
        .forEach(System.out::println);

```

```java
//List only files with Files.newDirectoryStream() 
Files.newDirectoryStream(Paths.get("."), path -> path.toFile().isFile())
        .forEach(System.out::println);

```

```java
//List files of certain extention with Files.newDirectoryStream() 
Files.newDirectoryStream(Paths.get("."),
        path -> path.toString().endsWith(".java"))
        .forEach(System.out::println);

```

```java
//Find all hidden files in directory 
final File[] files = new File(".").listFiles(file -> file.isHidden());
//or
final File[] files = new File(".").listFiles(File::isHidden);

```





# functional java



