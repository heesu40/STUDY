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
        path -> path.toString().endsWith(".java"))//path 에 문자열 추가하고 아마 클래스 추가가 안되어 있을 테니 경로 를 c 아래 workspace2아래 해당 프로젝트 아래 src아래로 지정해주어야 할것이다.
        .forEach(System.out::println);
////////////////////////////////////////////////////////////////////////////////////////////////

package open1;

import java.io.IOException;
import java.nio.file.Files;

import java.nio.file.Paths;

public class Test2 {
	 public static void main(String[] args) throws IOException {
		//List files of certain extention with Files.newDirectoryStream() 
		 Files.newDirectoryStream(Paths.get("C:\\test"),//위의 경우가 안먹힌다면 이처럼 경로 를 추가해주자. 현재 필자는 c아래 text아래 text파일과 java파일을 넣어 두었다. 넣어 둔 후 실행하고 자바만 검색하는지 알아보자.
		         path -> path.toString().endsWith(".java"))//path 에 문자열 추가하고 
		         .forEach(System.out::println);
	 }
}


```

```java
//Find all hidden files in directory 
final File[] files = new File(".").listFiles(file -> file.isHidden());
//or
final File[] files = new File(".").listFiles(File::isHidden);

```

== 이리 자바만 선택하는 것은 필터처리! 즉 중간 처리 다.

최대값, 평균값등의 집계 처리가 최종 처리이다. 그렇기에 중간처리가 약간 지연시켜두었다가 최종처리 때 그때 중간 처리를 같이 처리할...........................수있다(?)

#### Stream filter

중간 스트림이 생성될 때 요소들이 바로 중간 처리(필터링, 매핑, 정렬) 되는  것이 아니라 최종 처리가 시작되기 전까지 중간 처리는 지연(lazy)된다.



- 매개변수를 만들어 주어야 한다.

```java
package open1;

public class Member {
public static int MALE=0;
public static int FEMALI=1;

private String name;
private int sex;
private int age;


public Member(String name, int sex, int age) {
	super();
	this.name = name;
	this.sex = sex;
	this.age = age;
}
public static int getMALE() {
	return MALE;
}
public static void setMALE(int mALE) {
	MALE = mALE;
}
public static int getFEMALI() {
	return FEMALI;
}
public static void setFEMALI(int fEMALI) {
	FEMALI = fEMALI;
}
public String getName() {
	return name;
}
public void setName(String name) {
	this.name = name;
}
public int getSex() {
	return sex;
}
public void setSex(int sex) {
	this.sex = sex;
}
public int getAge() {
	return age;
}
public void setAge(int age) {
	this.age = age;
}



}

```



```java
package open1;

import java.util.Arrays;
import java.util.List;

public class test4 {

	public static void main(String[] args) {
	List<Member> list = Arrays.asList(
	         new Member("Kush", Member.MALE, 40),
	         new Member("Pierre", Member.MALE, 22),
	         new Member("Jolie", Member.FEMALI, 18),
	         new Member("Sozi", Member.FEMALI, 22)
	        );
	        
	    double ageAvg = list.stream()
	           .filter(m -> m.getSex() == Member.MALE)
	           .mapToInt(Member :: getAge)
	           .average()
	           .getAsDouble();
	        
	     System.out.println("남자 평균 나이: " + ageAvg);
	}
}

```





###### 파일로부터 스트림 얻기

```java
package open1_1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class test1 {

	public static void main(String[] args) throws IOException {
	    File file = new File("c:/test/data.txt");
	    FileReader fr = new FileReader(file);
	    BufferedReader br = new BufferedReader(fr);
	    String line;
	    while((line = br.readLine()) != null){
	        if(line.contains("password")){
	            System.out.println(line);//패스워드만 있는 라인만 출력
	        }
	    }
	    br.close();
	    fr.close();

	}



}

```

```

```



위에는 실제 돌아가는 형식이고 아래 예씨를 통해 한번 연습해 보자.

data.txt 예시; 파일

```
//data.txt
Lokesh
Gupta
Never
store
password
except
in mind.

```



```java
//Read file lazily as stream of lines 
private static void readStreamOfLinesUsingFiles() throws IOException
{
    Stream<String> lines = Files.lines(Paths.get("c:/temp", "data.txt"));//파일의 라인에 스트링을 //가져오는 또다른 방법이다
    Optional<String> hasPassword = lines.filter(s -> s.contains("password")).findFirst();//finfirst()//메서드를 이용하고 만약 패스워드가 없는 경우 
//null값이 넘겨져 널 포인트 예외가 생기므로 
//밑에 옵션을 넣어 준다. 
    if(hasPassword.isPresent()){
        System.out.println(hasPassword.get());
    }
    //Close the stream and it's underlying file as well
    lines.close();
}

```

```java
//Normal IO operation till java 7
private static void readLinesUsingFileReader() throws IOException
{
    File file = new File("c:/temp/data.txt");
    FileReader fr = new FileReader(file);
    BufferedReader br = new BufferedReader(fr);
    String line;
    while((line = br.readLine()) != null){
        if(line.contains("password")){
            System.out.println(line);//패스워드만 있는 라인만 출력
        }
    }
    br.close();
    fr.close();
}
```



###### java.io.Console 를 이용하여 로그인과 비밀번호 받기

console실행//이클립스에서 콘솔은 실행되지 않으므로 cmd를 이용한다

cmd 에서 실행을 할때

클래스 이름과 메모장 이름 같이 한 후 java파일로 저장

컴파일후(javax 파일이름.java)

실행! (java 파일이름)

```java
import java.io.Console;
import java.util.Arrays;

public class text2 {

	public static void main(String[] args) {
		Console console=null;
		String inputName=null;
		char[] inputPasswd=null;
		
		try {
			//콘솔 객체 생성
			console=System.console();
			
			if(console!=null) {
				//사용자로부터 이름 이볅 받음
				inputName=console.readLine("Name: ");
				inputPasswd=console.readPassword("Password: ");
				//print
				System.out.println("Name entered: "+inputName);
				System.out.println("Password : " + inputPasswd);
			}
				
			
		}catch(Exception e) {
			e.printStackTrace();
		}

	}

}
```



확인시 이름과 패스워드는 수동으로 써보장



#### Scanner 클래스

#### printf 메소드

#### 객체 직렬화

- 메모리에 생성된 객체를 파일또는 네트워크로ㅓ 출력해야 하는데 이떄 직렬화를 해서 보내야 한다.
- 그 후 읽어 들이려면 역직렬화를 해야 한다.
- 이 떄 사용하는 것이 java.io.ObjectInputStream/ObjectOutputStream 을 이용 한다





## NIO 기반 입출력

### NIO(New Input/Output)

- 자바 7부터 비동기 채널 네트워크 지원을 대폭 강화한 NIO2 API 를 추가

#### IO와 NIO차이점

- IO

  - 스트림 방식
    - 단방향 방식(입출력 따로따로)
    - FileInputStream
    - FileOutputStream 
  - 넌버퍼(버퍼 사용 안한다 )
  - 비동기 방식 지원 안함
    - 다 읽어들일때까지 딴 작업 못한다
  - 블로킹 방식만 지원
    - 다른 작업 못하게 막는것

- NIO

  - 채널 방식
    - 하나의 채널에 입출력을 다 할 수 있다.
  - 버퍼
  - 비동기도 지원
  - 블로킹/넌 블로킹 모두 지원
  - IO보다 성능이 좋다

  

#### java.nio.file, java.nio.file.attribute 패키지

1. java.nio.file. FileSystem 인터페이스 

   운영체제의 파일 시스템을 접근한다.

   `FileSystem fileSystem=FileSystems.getDefault();`

2. | **메소드****(****매개 변수****)** | **설명**                                       |
   | --------------------------------- | ---------------------------------------------- |
   | getFileStores()                   | 드라이버 정보를 가진 FileStore 객체들을 리턴   |
   | getRootDirectories()              | 루트 디렉토리 정보를 가진 Path   객체들을 리턴 |
   | getSeparator()                    | 디렉토리 구분자 리턴                           |

```java
package NIO;


import java.nio.file.FileStore;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;

public class FileSystemExample {

	public static void main(String[] args) throws Exception {
		FileSystem fileSystem=FileSystems.getDefault();
		for(FileStore store: fileSystem.getFileStores()){
			System.out.println("드라이버명:" +store.name());
			System.out.println("파일시스템: "+store.type());
			System.out.println("전체 공간 :"+store.getTotalSpace()+"바이트");
			System.out.println("사용 중인 공간 :"+(store.getTotalSpace()-store.getUnallocatedSpace())+"바이트");
			System.out.println("사용 가능한 공간 :"+store.getUsableSpace()+"바이트");
			System.out.println();
		}
		System.out.println("파일 구분자 "+fileSystem.getSeparator());
		System.out.println();
		
		for(Path path:fileSystem.getRootDirectories()) {
			System.out.println(path.toString());
		}

	}

}

```



파일 상태 보깅

```java
package NIO;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class test1 {

	public static void main(String[] args) throws Exception {
		Path path = Paths.get("c:/test/fileout.txt");
		System.out.println("디렉토리 여부: " + Files.isDirectory(path));
		System.out.println("파일 여부: " + Files.isRegularFile(path));
		System.out.println("마지막 수정 시간: " + Files.getLastModifiedTime(path));
		System.out.println("파일 크기: " + Files.size(path));
		System.out.println("소유자: " + Files.getOwner(path).getName());
		System.out.println("숨김 파일 여부: " + Files.isHidden(path));
		System.out.println("읽기 가능 여부: " + Files.isReadable(path));
		System.out.println("쓰기 가능 여부: " + Files.isWritable(path));

	}

}

```

java.nio.File 디렉토리와 파일을 생성하고, 디렉토리의 내용을 출력 예제

```java
package NIO;

import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class test2 {

	public static void main(String[] args) throws IOException  {
		
			Path path1 = Paths.get("C:/test/");
			Path path2 = Paths.get("C:/test/fileout.txt");		
			if(Files.notExists(path1)) {
				Files.createDirectories(path1);
			}		
			if(Files.notExists(path2)) {
				Files.createFile(path2);
			}		
			Path path3 = Paths.get("C:/test");
			DirectoryStream<Path> directoryStream = Files.newDirectoryStream(path3);
			for(Path path : directoryStream) {
			    if(Files.isDirectory(path)) {
				System.out.println("[디렉토리] " + path.getFileName());
			    }else {
				System.out.println("[파일] " + path.getFileName() + " (크기:" + Files.size(path) + ")");
			}
		    }
		   


	}

}

```



###### copy하기

밑에 처럼 쓰면 쉽게 copy를 할 수 있다.

```java
package NIO;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class FileCopyExample {

	public static void main(String[] args) throws Exception {
		Path sourceFile=Paths.get("c://test/고래.jpg");
		Path targetFile=Paths.get("c://test2/고래.jpg");
		
		try {
			Files.copy(sourceFile, targetFile,
					StandardCopyOption.REPLACE_EXISTING);
			System.out.println("copy completed!");
			
		}catch(IOException e) {
			e.printStackTrace();
			System.err.format("I/O Error when copying file");
		}

	}

}

```



###### 파일 변경사항 확인 이벤트

```java
package NIO;

import java.awt.Frame;
import java.awt.TextArea;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchEvent.Kind;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.util.List;


public class WatchEventFile extends Frame{
	class WatchServiceThread extends Thread{
	public void run() {
		try {
			WatchService watchService =FileSystems.getDefault().newWatchService();
			Path directory=Paths.get("c://test");
			directory.register(watchService, StandardWatchEventKinds.ENTRY_CREATE,StandardWatchEventKinds.ENTRY_DELETE,StandardWatchEventKinds.ENTRY_MODIFY);
			
			
			
			while(true) {
				WatchKey watchKey=watchService.take();
				List<WatchEvent<?>> list=watchKey.pollEvents();
				for(WatchEvent<?> watchEvent:list) {
					Kind<?> kind=watchEvent.kind();
					Path path=(Path) watchEvent.context();
					if(kind==StandardWatchEventKinds.ENTRY_CREATE) {
						textArea.append("파일 생성됨 ->"+path.getFileName()+"\n");
					}else if(kind==StandardWatchEventKinds.ENTRY_DELETE) {
						textArea.append("파일 삭제됨 ->"+path.getFileName()+"\n");
					}else if(kind==StandardWatchEventKinds.ENTRY_MODIFY) {
						textArea.append("파일 수정됨 ->"+path.getFileName()+"\n");
					}else if(kind==StandardWatchEventKinds.OVERFLOW) {
						
					}
							
				}
				boolean vaild=watchKey.reset();
				if(!vaild) {
					break;
				}
			}
			
			
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	}
	
	TextArea textArea;
	
	public WatchEventFile() {
		this.setSize(500,300);
		textArea=new TextArea();
		textArea.setEditable(false);
		this.add(textArea);
		this.setTitle("WatchEventFile");
		setVisible(true);
		WatchServiceThread wst=new WatchServiceThread();
		wst.start();
		
		
	}
	
	public static void main(String args[]) {
		new WatchEventFile();
	}

}

```



#### Buffer NIO

- 읽고 쓰기가 가능한 메모리 배열
- 다이렉트 버퍼
  - 한번 생성해 놓고 재사용이 적합
  - 채널 사용시 native I/O수행
  - 사용 안할시 내부적으로 JNI호출해서 native I/O수행
- 넌다이렉트 버퍼

| **구분**             | **넌다이렉트** **버퍼** | **다이렉트** **버퍼** |
| -------------------- | ----------------------- | --------------------- |
| 사용하는 메모리 공간 | JVM의 힙 메모리         | 운영체제의 메모리     |
| 버퍼 생성 시간       | 버퍼 생성이 빠르다      | 버퍼 생성이 느리다    |
| 버퍼의 크기          | 작다                    | 크다                  |
| 입출력 성능          | 낮다                    | 높다                  |



```java

```





##### 공통메서드

| **리턴타입** | **메소드****(****매개변수****)** | **설명**                                                     |
| ------------ | -------------------------------- | ------------------------------------------------------------ |
| Object       | array(   )                       | 버퍼가 래핑(wrap)한 배열을 리턴                              |
| int          | arrayOffset( )                   | 버퍼의 첫 번째 요소가 있는 내부 배열의 인덱스를 리턴         |
| int          | capacity( )                      | 버퍼의 전체 크기를 리턴                                      |
| Buffer       | clear(   )                       | 버퍼의 위치 속성을 초기화 (position=0, limit=capacity)       |
| Buffer       | flip(   )                        | limit을 position으로,   position을 0인덱스로   이동          |
| boolean      | hasArray( )                      | 버퍼가 래핑(wrap)한 배열을 가지고 있는지 여부                |
| boolean      | hasRemaining( )                  | position과 limit 사이에   요소가 있는지 여부(position   < limit) |
| boolean      | isDirect( )                      | 운영체제의 버퍼를 사용하는지 여부                            |
| boolean      | isReadOnly( )                    | 버퍼가 읽기 전용인지 여부                                    |
| int          | limit(   )                       | limit   위치를 리턴                                          |
| Buffer       | limit(int newLimit)              | newLimit으로 limit 위치를   설정                             |

| **리턴타입** | **메소드****(****매개변수****)** | **설명**                                |
| ------------ | -------------------------------- | --------------------------------------- |
| Buffer       | mark(   )                        | 현재 위치를 mark로 표시                 |
| int          | position(   )                    | position 위치를 리턴                    |
| Buffer       | position(int    newPosition )    | newPosition으로  position 위치를   리턴 |
| int          | remaining(   )                   | position과   limit사이의   요소의 개수  |
| Buffer       | reset(   )                       | position을 mark 위치로   이동           |
| Buffer       | rewind(   )                      | position을 0 인덱스로   이동            |

###### 버퍼 용량 확인\

```java
package NIO;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.IntBuffer;

public class Buffer1 {

	public static void main(String[] args) {
		ByteBuffer byteBuffer = ByteBuffer.allocateDirect(100);
		System.out.println("byte 저장 용량: " + byteBuffer.capacity());
		 
		CharBuffer charBuffer = ByteBuffer.allocateDirect(100).asCharBuffer();
		System.out.println("char 저장 용량: " + charBuffer.capacity());
		        
		IntBuffer intBuffer = ByteBuffer.allocateDirect(100).asIntBuffer();
		System.out.println("int 저장 용량: " + intBuffer.capacity());


	}

}

```

기본 바이트 해석 순서 예제

```java
import java.nio.ByteOrder;
 
public class ComputerByteOrderExample {
 
    public static void main(String[] args) {
        System.out.println("운영체제: " + System.getProperty("os.name"));
        System.out.println("네이티브의 바이트 해석 순서: " + ByteOrder.nativeOrder());
    } 
}

```

Buffer의 위치 속성값 예제

``` java
package NIO;

import java.nio.ByteBuffer;

public class Buffer2 {

	public static void main(String[] args) {
		System.out.println("[7바이트 크기로 버퍼 생성]"); 
		ByteBuffer buffer = ByteBuffer.allocateDirect(7);
		printState(buffer);
		buffer.put((byte) 10);
		buffer.put((byte) 11);
		System.out.println("[2바이트 저장후]");
		printState(buffer); 
		buffer.put((byte) 12);
		buffer.put((byte) 13);
		buffer.put((byte) 14);
		System.out.println("[3바이트 저장후]");
		printState(buffer); 
		buffer.flip();
		System.out.println("[filp 실행후]");
		printState(buffer);

		buffer.get(new byte[3]);
		System.out.println("[3바이트 읽은후]");
		printState(buffer);         
		
		buffer.mark();
		System.out.println("[현재 위치 mark 해놓음");
		 
		buffer.get(new byte[2]);
		System.out.println("[2바이트 읽은 후]");
		printState(buffer);
		 
		buffer.reset();
		System.out.println("[position 을 마크 위치로 옮김]");
		printState(buffer);
		 
		buffer.rewind();
		System.out.println("[rewind 실행 후]");
		printState(buffer);
		 
		buffer.clear();
		System.out.println("[clear 실행 후]");
		printState(buffer);

		

	}

	private static void printState(ByteBuffer buffer) {
		System.out.println("\tposition: "+buffer.position()+", ");
		System.out.println("\tlimit: "+buffer.limit()+", ");
		System.out.println("\tcapacity: "+buffer.capacity());
		
	}

	

}

```





# functional java



