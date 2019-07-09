

## Java EE

자바 엔터프라이즈 애플리케이션을 뜻한다.

웹애플리케이션과 관련된 기술의 표준사양을 정의 하는데 표준 스택만 정의한다. 



##### 어플리케이션 서버?

Web+Application Server=WAS 라 하는데 톰캣과 weblogic,AS,websphere,Jeus,Jboss등등이 포함된다. 

1. 톰캣-WebServer +WebContainer()
2. 그외에는 EJB Container 와 Tx,DNS,MOM이 포함?

##### Java EE는 

1. 컨테이너는 컴포넌트 실행환경 제공
2. 데이터베이스연결 풀링 및 캐싱같은 엔터프라이즈 환경에서 요구ㄱ되는 서비스 제공
3. 트랜잭션 관리, 보안,상태 관리, 프로세스와 스레드, 시스템 리소스 관리 등 제공
4. 서버는 웹컨테이너와 EJB컨테이너로 구성
5. 자바컨포넌트는 이제 안쓴다.
6. 웹 애플리케이션을 웹 컨테이너에 설치 또는 배포할때 웹 애플리케이션이 행위를 설정할 수 있다. 
7. JPA를 표준 퍼시스턴스을 솔루션으로 정의, 지속성이라는 의미로 프로그램의 실행이 끝나거나 컴퓨터가 종료해서 상태 지속, 일반적으로 데이터베이스에 데이터를 저장, 최근의 데이터 액세스 방법의 주류를 형성하는 ORM프로그래밍 모델 제공.



##### 아키텍처

1. JSP와 JDBC만을 사용하여 개발(Model1)
   - 개발속도가 편하고, 숙련도가 낮으며, 빠르게 적응 가능
2. Model2
   - MVC패턴을 웹 새발에 적용해 구현
   - 컨트롤러는 업무 로직을 구현하고 모델과 뷰를 통제
   - 웹서버는 정적인 웹페이지 처리를 전담 하고 동적인 웹페이지와 업무로직 등은 애플리케이션 서버에서 담당하게 한다.

### 개요

구성

1. 프레젠테이션 레이어,서비스레이어,레파지토리 레이어등으로 최소 3개의  레이어로  구분할 것이다.
2. 레파지토리 레이어는 DAO패턴을 적용하여 데이터베이스에서 데이터를 입출력하는 데이터액세스 로직 구현

DTO

1. 프레젠테이션 레이어와  서비스 레이어 사이의 데이터 전송을 담당하는 도메인 클래스
2. 프레젠테이션 레이어와 MVC패턴에 따라 모뎅,뷰, 컨트롤러 나누어지므로  데이터와 관련된 클래스는 **모델 클래스**와 *도메인 클래스,엔티티 클래스* 등 모두 3가지 유형이 있따.
3. 도메인과 엔티티 클래스는 구분되어야만한다.



### Maven

- 의존성 관리,라이브러리 관리
- 프로젝트 관리 도구로 표준화된 빌드 기능, 리포팅 및 생성기능등 제공

#### 실행

자바에서 new->

![](C:\Users\student\Documents\GitHub\STUDY\javaStudy\maven1.PNG)

![](C:\Users\student\Documents\GitHub\STUDY\javaStudy\maven2.PNG)

으로 실행 처음 실행시 로딩이 길다



도구모음에 help에 들어가 이클립스marketplace 에 들어가 Spring검색 후  spring Tool 3 add-On (aka Spring Tool Suite 3)3.9.9RELEASE를 설치한다(최신버전으로 하자)



그후 maven 프로젝트 생성후

pom.xml 로 가서 추가 기본에 `<https://mvnrepository.com/artifact/org.springframework/spring-core>`사이트의 5.0.2(버전..책에 있떤 버전이므로) 을 복사 하여 하나는 core, 하나는 context로 붙여넣어준다.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>spring_ioc</groupId>
  <artifactId>spring_ioc</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>spring_ioc</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <spring.maven.artifact.version>5.0.2.RELEASE</spring.maven.artifact.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
    
    <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-core</artifactId>
    <version>${spring.maven.artifact.version}</version>
</dependency>
    
      <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>${spring.maven.artifact.version}</version>
</dependency>

 <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-aop</artifactId>
    <version>${spring.maven.artifact.version}</version>
</dependency>

 <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-beans</artifactId>
    <version>${spring.maven.artifact.version}</version>
</dependency>

 <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context-support</artifactId>
    <version>${spring.maven.artifact.version}</version>
</dependency>

    
  </dependencies>
</project>

```







### Framework?

 개발의 어플리케이션 구현의 있어서 뼈대에 해당

시스템 구조를 제공하고, 이미 성능이 성능이 검증된 기반이 되는 Compent ,실행환경의 container제공 



### 비교

1. 컨테이너 주입
2. annotation

###  결합도와 유지보수

##### 결합도 떨어뜨리는 방법(느슨하게 하는 방법)

1. 인터페이스로 표준화
2. Factory패턴을 이용한 결합도 떨어뜨리기 (Container ioc는 이 방식이다. 3번과 방법은 비슷~ )

3. Spring IoC를 이용한 결합도 떨어뜨리기

##### xml을 이용하여 결합도 떨어뜨려보자.

package lab.spring.di.service

```java
package lab.spring.di.service;

public interface HelloService {
 public void sayHello();
}

```

```java
package lab.spring.di.service;

import lab.spring.di.persist.Message;

public class HelloServiceImpl implements HelloService {
	private Message message;//다른 패키지게 만든 getMessage를 부르기위해 파일명 Message를 연결..?
	public void sayHello() {
	System.out.println(message.getMessage());
	}
	
	public HelloServiceImpl() {
		super();
	}
	public HelloServiceImpl(Message message) {
		super();
		this.message=message;
		System.out.println("생성자를 이용해서 Bean주입함");
	}
	
//public void setMessage(Message message) {
//	this.message=message;
//}
}

```

package lab.spring.di.persist

```java
package lab.spring.di.persist;

public class Message {
 public String getMessage() {
	 return "생성자 주입";
 }
}

```

package lab.spring.di.test

```java
package lab.spring.di.test;



import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.HelloService;

public class ContainerDITest {

	public static void main(String[] args) {
		ApplicationContext context=new ClassPathXmlApplicationContext("application.xml");
		
		String beanName="hello";
		HelloService service=context.getBean(beanName,HelloService.class);//지금 객체 생성 안했따!
		service.sayHello();

	}

}

```



src - main- resources(파일을 만들고 그 안에) -application.xml을 만든다

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">


<bean id="firstMessage" 
class="lab.spring.di.persist.Message" />

<bean id="hello" class="lab.spring.di.service.HelloServiceImpl">
<constructor-arg  ref="firstMessage"/><!-- 생성자로 할시-->
<!-- <property name="message" ref="firstMessage"/> --><!--아닐시-->
</bean>



</beans>

```

##### annotation를 이용하여 결합도 떨어뜨려보자.

AnnotationDiTest.java

```java
package lab.spring.di.test;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import lab.spring.di.service.HelloService;

public class AnnotationDITest {

	public static void main(String[] args) {
	AnnotationConfigApplicationContext context=new AnnotationConfigApplicationContext(AppConfig.class);
	
	HelloService service=context.getBean("hello",HelloService.class);
	service.sayHello();

	}

}

```



AppConfig.java

```java
package lab.spring.di.test;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import lab.spring.di.persist.Message;
import lab.spring.di.service.HelloService;
import lab.spring.di.service.HelloServiceImpl;

@Configuration
public class AppConfig {
 @Bean
 public  HelloService hello() {
	 Message msg=new Message();
	 HelloServiceImpl service=new HelloServiceImpl(msg);
	 return service;
 }
}

```



##### Bean의 성질변화

```java
package lab.spring.di.test;



import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.HelloService;

public class ContainerDITest {

	public static void main(String[] args) {
		ApplicationContext context=new ClassPathXmlApplicationContext("application.xml");
		
		String beanName="hello";
		HelloService service=context.getBean(beanName,HelloService.class);//지금 객체 생성 안했따!
		service.sayHello();
		HelloService service2=context.getBean("hello",HelloService.class);
		service2.sayHello();
		System.out.println("스프링이 생성해준 빈이 singlton이라면 동일한 객첵 리턴"+(service==s
                                                                 ervice2));

	}

}

```



```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">


<bean id="firstMessage" 
class="lab.spring.di.persist.Message" />

<bean id="hello" class="lab.spring.di.service.HelloServiceImpl"
 scope="prototype">
<constructor-arg  ref="firstMessage"/>
<!-- <property name="message" ref="firstMessage"/> -->
</bean>



</beans>

```

scope="prototype"을 주면 bean값의 두개가 달라진다(false!)

bean Scope의 속성인데,  default값은 singleton이다.

1. singleton -하나의 Bean정의에 대해서 Spring loC Container내에 단 하나의 객체만 존재
2. prototype-하나의 Bean정의에 다수의 객체 존재
3. request-하나의 Bean정의에 하나의 HTTP request의 생명주기 안에 단 하나의 객체만 존재
4. session- 하나의 Bean정의에 하나의 HTTP Session의 생명주기 안에 단 하나의 객체만 존재
5. global session- 하나의 Bean정의에 하나의 HTTP Session의 생명주기 안에 단 하나의 객체만 존재



##### bean의 lifecycle



```java
package lab.spring.di.persist;

public class Message {
 public String getMessage() {
	 return "bean lifeCycle";
 }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">


<bean id="firstMessage" 
class="lab.spring.di.persist.Message" />

<bean id="hello" class="lab.spring.di.service.HelloServiceImpl"
 scope="prototype">
<constructor-arg  ref="firstMessage"/>
<!-- <property name="message" ref="firstMessage"/> -->
</bean>

<bean id="service"
		class="lab.spring.di.service.HelloServiceLifeCycle"
		p:name="Spring5.0!!!"
		p:myMessage-ref="firstMessage"
		init-method="custom_init"
		destroy-method="custom_end"/>



</beans>



```

```java
package lab.spring.di.service;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanFactoryAware;
import org.springframework.beans.factory.BeanNameAware;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

import lab.spring.di.persist.Message;

public class HelloServiceLifeCycle
		implements HelloService, BeanNameAware, BeanFactoryAware, InitializingBean, DisposableBean {

	private String name;
	private Message myMessage;
	private String beanName;
	private BeanFactory beanFactory;
	
	public HelloServiceLifeCycle(){
		super();
		System.out.println("1.default 생성자를 이용해서 빈 인스턴스 생성");
	}
	


	public void setName(String name) {
		this.name = name;
		System.out.println("2.의존성 체크후 property로 빈 인스턴스 주입");
	}



	public void setMyMessage(Message myMessage) {
		this.myMessage = myMessage;
		System.out.println("2. 의존성 체크 후 property로 빈 인스턴스 주입");
	}

	

	public BeanFactory getBeanFactory() {
		return beanFactory;
	}

	public void destroy() throws Exception {
		// TODO Auto-generated method stub
		System.out.println("8.Ioc컴테이너로부터 빈이 제거될때 정리, 종료 수행 메서드");

	}
	public void custom_end() {
		System.out.println("9.IOC컨테이너로부터 빈이 제거될때 사용자 정의 종료 및 정리 수행 메서드(컨테이너에 독립적)");
	}
	public void afterPropertiesSet() throws Exception {
		
		System.out.println("5.모든 property가 설정된 후 유효성 체크등의 수행하기 위한 용도");
	}
	
	public void custom_init() {
		System.out.println("6.사용자 정의 초기화 메서드(스프링컨테이너에 독립적......)");
	}
	public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
		System.out.println("4.스프링 컨테이너 객체 주입");
		this.beanFactory=beanFactory;

	}

	public void setBeanName(String beanFactory) {
		System.out.println("3.설정 파일에서의 빈 이름을 주입");
		this.beanName=beanFactory;
		System.out.println("주입받은 빈 이름: "+beanName);
		
				

	}
	public String getname() {
		return name;
	}

	public void sayHello() {//서비스 메서드
		System.out.println("7.빈의 서비스 메서드 호출");
		System.out.println(myMessage.getMessage()+"from "+name);
		

	}

}

```

1.default 생성자를 이용해서 빈 인스턴스 생성
2. 의존성 체크 후 property로 빈 인스턴스 주입
2.의존성 체크후 property로 빈 인스턴스 주입
3.설정 파일에서의 빈 이름을 주입
주입받은 빈 이름: service
4.스프링 컨테이너 객체 주입
5.모든 property가 설정된 후 유효성 체크등의 수행하기 위한 용도
6.사용자 정의 초기화 메서드(스프링컨테이너에 독립적......)**여기까지가 빈 생성**
7.빈의 서비스 메서드 호출
bean lifeCyclefrom Spring5.0!!!
8.Ioc컴테이너로부터 빈이 제거될때 정리, 종료 수행 메서드
9.IOC컨테이너로부터 빈이 제거될때 사용자 정의 종료 및 정리 수행 메서드(컨테이너에 독립적)

##### 한국어 외국어 구분해서 가져와보자

application.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">


<bean id="firstMessage" 
class="lab.spring.di.persist.Message" />

<bean id="hello" class="lab.spring.di.service.HelloServiceImpl"
 scope="prototype">
<constructor-arg  ref="firstMessage"/>
<!-- <property name="message" ref="firstMessage"/> -->
</bean>

<bean id="service"
		class="lab.spring.di.service.HelloServiceLifeCycle"
		p:name="Spring5.0!!!"
		p:myMessage-ref="firstMessage"
		init-method="custom_init"
		destroy-method="custom_end"/>
		
<bean id="oracleDBUtile"
	class="lab.spring.di.util.JdbcUtil"
	p:driver="oracle.jdbc.OracleDriver"
	p:url="jdbc:oracle:thin:@localhost:1521:orcl"
	p:user="hr"
	p:pwd="oracle"/>
	
<bean id="dao"
	class="lab.spring.di.persist.UserManageDAO"
	p:dbUtil-ref="oracleDBUtil"/>

<bean id="messageSource"
	class="org.springframework.context.support.ResourceBundleMessageSource">
	
	<property name="basenames">
	<value></value>
	</property>
	</bean>

</beans>



```



JdbcUtil.java

```java
package lab.spring.di.util;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class JdbcUtil {
	private String driver;
	private String url;
	private String user;
	private String pwd;
	public void setDriver(String driver) {
		this.driver = driver;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public void setUser(String user) {
		this.user = user;
	}
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}
	
	public Connection dbCon() {
		 Connection con=null;
		 try{
			 Class.forName(driver);
			 con=DriverManager.getConnection(url,user,pwd);
					}catch(Exception e) {
						e.printStackTrace();
					}
					return con;
	 }
	 public void dbClose(Connection con, Statement stat,ResultSet rs) {
		 try {
			 if(rs!=null)rs.close();
			 if(stat!=null)stat.close();
			 if(con!=null)con.close();
		 }catch(Exception e) {
				e.printStackTrace();
			}
		}
}

```





이것좀 추가하자

 ![](C:\Users\student\Documents\GitHub\STUDY\javaStudy\bean.PNG)



greeting=안녕~ 스프링5.0 시작!!!
login.success={0}!^^ 환영해~
login.fail=ID{0} 존재하지않거나 비밀번호가 틀렸어!!