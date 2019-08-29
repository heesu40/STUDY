

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

![](D:\gitgithub\STUDY\javaStudy\maven1.PNG)

![](D:\gitgithub\STUDY\javaStudy\maven2.PNG)

으로 실행 처음 실행시 로딩이 길다

###### **메이븐아키타입**(참고)

## Maven Archetypes

Maven provides several archetype artifacts:

| Archetype ArtifactIds                                        | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [maven-archetype-archetype](https://maven.apache.org/archetypes/maven-archetype-archetype/) | An archetype to generate a sample archetype.                 |
| [maven-archetype-j2ee-simple](https://maven.apache.org/archetypes/maven-archetype-j2ee-simple/) | An archetype to generate a simplifed sample J2EE application. |
| [maven-archetype-plugin](https://maven.apache.org/archetypes/maven-archetype-plugin/) | An archetype to generate a sample Maven plugin.              |
| [maven-archetype-plugin-site](https://maven.apache.org/archetypes/maven-archetype-plugin-site/) | An archetype to generate a sample Maven plugin site.         |
| [maven-archetype-portlet](https://maven.apache.org/archetypes/maven-archetype-portlet/) | An archetype to generate a sample JSR-268 Portlet.           |
| [maven-archetype-quickstart](https://maven.apache.org/archetypes/maven-archetype-quickstart/) | An archetype to generate a sample Maven project.             |
| [maven-archetype-simple](https://maven.apache.org/archetypes/maven-archetype-simple/) | An archetype to generate a simple Maven project.             |
| [maven-archetype-site](https://maven.apache.org/archetypes/maven-archetype-site/) | An archetype to generate a sample Maven site which demonstrates some of the supported document types like APT, Markdown, XDoc, and FML and demonstrates how to i18n your site. |
| [maven-archetype-site-simple](https://maven.apache.org/archetypes/maven-archetype-site-simple/) | An archetype to generate a sample Maven site.                |
| [maven-archetype-site-skin](https://maven.apache.org/archetypes/maven-archetype-site-skin/) | An archetype to generate a sample Maven Site Skin.           |
| [maven-archetype-webapp](https://maven.apache.org/archetypes/maven-archetype-webapp/) | An archetype to generate a sample Maven Webapp project.      |

출처:https://maven.apache.org/archetypes/





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



src - main- resources(파일을 만들고 그 안에 bean configuration file) -application.xml을 만든다

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

<!-- <bean id="service"
		class="lab.spring.di.service.HelloServiceLifeCycle"
		p:name="Spring5.0!!!"
		p:myMessage-ref="firstMessage"
		init-method="custom_init"
		destroy-method="custom_end"/> -->
		
<bean id="oracleDBUtile"
	class="lab.spring.di.util.JdbcUtil"
	p:driver="oracle.jdbc.OracleDriver"
	p:url="jdbc:oracle:thin:@localhost:1521:orcl"
	p:user="hr"
	p:pwd="oracle"/>
	
<bean id="userDAO"
	class="lab.spring.di.persist.UserManageDAO"
	p:dbUtil-ref="oracleDBUtile"/><!-- 의존관계라 oracleDBUtil과 관계되어있다. -->
	
<bean id="loginService"
	class="lab.spring.di.service.UserServiceImpl"
	p:dao-ref="userDAO"/>

<bean id="messageSource"
	class="org.springframework.context.support.ResourceBundleMessageSource">
	
	<property name="basenames">
	<value>messages.notice</value>
	</property>
	</bean>
	


</beans>



```

userVO.java

```java
package lab.spring.di.persist;

public class userVO {
	 private String userid;
	 private String userpwd;
	 private String username;
	 private String email;
	 private String phone;
	 private String address;
	 private String job;
	public String getUserid() {
		return userid;
	}
	public void setUserid(String userid) {
		this.userid = userid;
	}
	public String getUserpwd() {
		return userpwd;
	}
	public void setUserpwd(String userpwd) {
		this.userpwd = userpwd;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getJob() {
		return job;
	}
	public void setJob(String job) {
		this.job = job;
	}
	 
}

```

UserManageDAO.java

```java
package lab.spring.di.persist;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;


import lab.spring.di.util.JdbcUtil;

public class UserManageDAO {
	private JdbcUtil dbUtil;
	
	public void setDbUtil(JdbcUtil dbUtil) {
		this.dbUtil=dbUtil;
	}
	
	public userVO loginProc(String uid,String upwd) {
		userVO user=null;
		
		Connection con=null;
		PreparedStatement stat=null;
		String sql="select*from userinfo where userid=? and userpwd=? ";
		ResultSet rs=null;
		try {
			con=dbUtil.dbCon();
			stat=con.prepareStatement(sql);
			stat.setString(1, uid);
			stat.setString(2,upwd);
			rs=stat.executeQuery();
			while(rs.next()) {
				user=new userVO();
				user.setUserid(rs.getString("userid"));
				user.setUsername(rs.getString("username"));
				user.setAddress(rs.getString("address"));
				user.setEmail(rs.getString("email"));
				user.setJob(rs.getString("job"));
				user.setPhone(rs.getString("phone"));
				user.setUserpwd(rs.getString("userpwd"));
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			dbUtil.dbClose(con,stat,rs);
		}
		return user;
	}
}

```

Message.java

```java
package lab.spring.di.persist;

public class Message {
 public String getMessage() {
	 return "bean lifeCycle";
 }
}

```

UserService.java

```java
package lab.spring.di.service;

public interface UserService {
	public String[] login(String userid,String userpwd);
	
}

```

UserServiceImpl.java

```java
package lab.spring.di.service;

import java.util.Locale;

import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;

import lab.spring.di.persist.UserManageDAO;

public class UserServiceImpl implements UserService, ApplicationContextAware {

		private UserManageDAO dao;
		private ApplicationContext context;
		
		
		public void setDao(UserManageDAO dao) {
			this.dao=dao;
		}
		public void setApplicationContext(ApplicationContext context) throws BeansException {
			this.context=context;

		}
	public String[] login(String uid,String upwd) {
		String messages[]=new String[2];
		Object[] args=new String[] {uid};
		Locale locale=Locale.getDefault();
		if(dao.loginProc(uid, upwd)!=null){
			messages[0]=context.getMessage("login.success", args,locale);
			
		}else {
			messages[0]=context.getMessage("login.fail", args,locale);
		}
		
		Locale locale_en=Locale.ENGLISH;
		if(dao.loginProc(uid, upwd)!=null) {
			messages[1]=context.getMessage("login.success", args,locale_en);
		}else {
			messages[1]=context.getMessage("login.fail", args,locale_en);
		}
		return messages;
}
}

```

UserServiceImpl.java

```java
package lab.spring.di.service;

import java.util.Locale;

import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;

import lab.spring.di.persist.UserManageDAO;

public class UserServiceImpl implements UserService, ApplicationContextAware {

		private UserManageDAO dao;
		private ApplicationContext context;
		
		
		public void setDao(UserManageDAO dao) {
			this.dao=dao;
		}
		public void setApplicationContext(ApplicationContext context) throws BeansException {
			this.context=context;

		}
	public String[] login(String uid,String upwd) {
		String messages[]=new String[2];
		Object[] args=new String[] {uid};
		Locale locale=Locale.getDefault();
		if(dao.loginProc(uid, upwd)!=null){
			messages[0]=context.getMessage("login.success", args,locale);
			
		}else {
			messages[0]=context.getMessage("login.fail", args,locale);
		}
		
		Locale locale_en=Locale.ENGLISH;
		if(dao.loginProc(uid, upwd)!=null) {
			messages[1]=context.getMessage("login.success", args,locale_en);
		}else {
			messages[1]=context.getMessage("login.fail", args,locale_en);
		}
		return messages;
}
}

```

UserServiceInterface.java

```java
package lab.spring.di.service;

import lab.spring.di.persist.userVO;

public interface UserServiceInterface {
	public userVO login(String userid,String userpwd);
	
}

```

MessageTest.java

```java
package lab.spring.di.test;

import java.util.Locale;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.UserService;

public class MessageTest {

	public static void main(String[] args) {
		ApplicationContext context=new ClassPathXmlApplicationContext("application.xml");//Spring Containner생성
		
		Locale locale=Locale.getDefault();
		String greet=context.getMessage("greeting", new Object[0],locale);//greeting에 잇는 key를 가지구 옴
		System.out.println("default locale 인삿말: "+greet);
		
		Locale locale_en=Locale.ENGLISH;
		greet=context.getMessage("greeting", new Object[0],locale_en);
		System.out.println("ENGLISH locale 인삿말: "+greet);
		
		UserService proc=context.getBean("loginService",UserService.class);
		
//		String[] results=proc.login("admin", "a1234");//등록된 아이디(성공 메시지 확인()
		String[] results=proc.login("korea","1234");//등록되지 않은 아이디(실패 메시지 확인)
		for(String m: results) {
			System.out.println(m);
		}

	}

}

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

![1562723632560](C:\Users\student\Documents\GitHub\STUDY\javaStudy\bean)



greeting=안녕~ 스프링5.0 시작!!!
login.success={0}!^^ 환영해~
login.fail=ID{0} 존재하지않거나 비밀번호가 틀렸어!! 를 각각의 파일에 한글은 한글로 영어는 영어로 저장하자







# 앞에부분 정리

##  Spring Framework특성

1. 경량 컨테이너 지원(제공)
2. IoC컨테이너는 Factory패턴이 적용된 (객체를 직접 생성하지 않고 )
3. AOP(관점지향 프로그래밍)지원- 핵심 로직과 고통 로직을 분리해서 핵심 로직 수행시 공통 로직을 적용(다양한 방법이 있는데 spring의 경우....)
4. POJO 로 Bean을 정의해서 사용가능 -특정 라이브러리에 종속되거나 .....를 방지하여 충돌방지
5. 영속성과 관련된 다양한 API(Hibernate,Mybatis,JDO.....) 지원
6. 트랜잭션 처리를 위한 일관된 방법으로 처리, 관리 지원
7. 배치 처리, 메시지 처리, ....다양한 API지원
8. Framework을 위한 Framework이라는 말을 많이 한다.



## Spring Framework 모듈

1. Spring Core 모듈 -  IoC기능 지원(Spring Container 클래스: BeanFactory)
2. Spring Context 모듈 -Core에서 지원하는 기능 외에 추가적인 기능들 지원(JNDI,EJB(망함,지금안씀 너무 무거운), (ApplicationContext Spring Container 클래스: Beanfactory을 상속받아서 국제화 메시지처리, , 이벤트)
3. Spring AOP모듈-관점 지향 프로그래밍 지원
4. Spring DAO모듈 -JDBC 보다더 쉽고, 간결하게 개발 가능 
5. Spring ORM모듈-API(Hibernate,Mybatis,JDO.....)를 일관된 방법으로 사용할 수 있으며 결합, 통합 지원
6. Spirng Web모듈-MVC 패턴이 적용된 Web App 개발 지원,  struts,Webwork와 같은 프레임워크와 통합
7. Spring web MVC모듈- 다양한 Web UI, 기술 등의 API지원 

## 의존객체를 생성, 주입 방식

1. 생성자를통해 주입
2. setxxxx메서드를 이용해서 주입



## Bean설정 방식

1. xml 설정 방식

   - bean id="" name="" class="">

   - < constructor-arg ref="빈이름" />

   - < property    type="" index="" value="문자열등" ref="빈이름" />

     

2. 자바클래스와 Annotation 

   - @Configuration  & Bean 메서드 앞에 @Bean 이라 써주어야 한다. 빈의 이름은 메서드이름
   - 소스코드에서 빈요청할때 - 컨테이너객체.getBean("빈이름",빈타입.class)

3. Spring 컨테이너의 default 빈 scopre는 singleton이다.

!!!! 참고로 디폴트 생성자는 무조건 만들어 놓자~ 쓰기 좋게





#  annoteConfig.xml(어노테이션 설정)

annoteConfig.xml을 새로 만들자!

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.0.xsd">


</beans>

```







## DB연동

먼저 tomcat.apache.org 에 다큐멘터리 9.0 에 들어가서 Oracle 8i,9i,10g 에 들어가서 

```xml
<Resource name="jdbc/myoracle" auth="Container"
              type="javax.sql.DataSource" driverClassName="oracle.jdbc.OracleDriver"
              url="jdbc:oracle:thin:@127.0.0.1:1521:mysid"
              username="scott" password="tiger" maxTotal="20" maxIdle="10"
              maxWaitMillis="-1"/>
```

복사후

![](C:\Users\student\Pictures\DB연동.PNG)

![](C:\Users\student\Pictures\DB연동1.PNG)

를 추가해준다 이것은 Servers 폴더에  Tomcat v9.0 Server at localhost-config ...파일에 있는 server.xml파일 안의 내용안에 추가하는 것이다.



DriverClass 로딩

Connection 생성

Statement 생성

sql문장의 파라미터 세팅 후에 전송

결과가 select인 경우 Domain,Entity Object 매핑

[예외 처리]

[리소스 정리 ]

### 모르는 것 추가해보자

1. ApplicationContextAware 인터페이스

   ```java
   public void setApplicationContext(ApplicationContext context) throws BeansException {
   			this.context=context;
   
   		}
   ```

   

를 구현하면  Application Context객체를 얻게 된다.

그러면 스프링 프레임 워크에서 인자값(application Context 변수)로 객체를 넘겨준다.특정 타입에 속한 빈(bean)들을 조회할 경우  getBeansOfType 을 이용하여  바로 Map 객체로 가져온다.



2. repository를 한번 삭제후 다시 하고 싶다면
   - c드라이브에 사용자 student .m2 밑에 존재하는 repository를 삭제하고 다시 이클립스를 실행하면 다시 다운로드 된다.  이곳에는 메이븐을 통해 받은 파일이 존재하게 된다. 그 후 이클립스 실행후 자신의 프로젝트 마우스 오른쪽 버튼을 누르고 maven - update Project 를 클릭한다. OK눌러준다.(기본설정대로 하자.)

##### 1.lab.spring.aop.advice

1. AnnotLoggingAdvice

```java

package lab.spring.aop.advice;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;



@Component
@Aspect
public class AnnotLoggingAdvice { 
	 
	@Pointcut("execution(* lab.spring.aop.service.*Service.*(..))")
	public void logPointcut() {}
	
	@Before("logPointcut()")
	public void beforeAdviceMethod(JoinPoint thisJoinPoint) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		// 대상 메서드에 대한 로거를 얻어 해당 로거로 현재 class, method 정보 로깅		
		System.out.println("BeforeAdvice:"+className + "." + methodName + " 핵심 메소드 호출 전에 공통 기능 수행....");
	}
	
	 @AfterReturning(pointcut="logPointcut()",returning="retVal")
	public void afterReturningAdviceMethod(JoinPoint thisJoinPoint,	Object retVal) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.println("AfterReturningAdvice:"+className + "." + methodName + " 핵심 메소드 정상 수행 후 공통 기능 수행...");
		System.out.println("return value is [" + ((Integer)retVal) + "]");
	}
	
	 @AfterThrowing(pointcut="logPointcut()",throwing="exception")
	public void afterThrowingAdviceMethod(JoinPoint thisJoinPoint,	Exception exception) 
			                                                             throws Exception{
//		Class  clazz = thisJoinPoint.getTarget().getClass();
//		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
//		String methodName = thisJoinPoint.getSignature().getName();
//		System.out.print("afterThrowingAdvice:"+className + "." + methodName);	
		System.out.println("핵심 메소드가 수행 중 예외사항을 반환하고 종료하는 경우 수행된다");
		System.err.println("에러가 발생:"+ exception.getMessage());
//			throw new Exception("에러가 발생했습니다. ", exception);
		}
    
	 @After("logPointcut()")
	public void afterAdviceMethod(JoinPoint thisJoinPoint) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.print("AfterAdvice:"+className + "." + methodName);	
		System.out.println("핵심 로직 메서드  정상 종료와 예외 발생 경우를 모두 처리 하는 Advice");
		}
	
	 @Around("logPointcut()")
	public Object aroundAdviceMethod(ProceedingJoinPoint thisJoinPoint)	throws Throwable {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.print("AroundAdvice:"+className + "." + methodName);	
		
		System.out.println("핵심 메소드 수행 전의 공통 기능 수행........");
		long time1 = System.currentTimeMillis();
		Object retVal = thisJoinPoint.proceed();//Target빈의 핵심 메소드 호출
		System.out.println("ProceedingJoinPoint executed. return value is [" + retVal + "]");
		 
		System.out.println("리턴 값 변경 ==>  [" + ((Integer)retVal) + "(modified)" + "]");
		long time2 = System.currentTimeMillis();
		System.out.println("핵심 메소드 수행 후의 공통 기능 수행........ Time("+ (time2 - time1) + ")");
		return retVal;
			}
	
	
	
	
	
	
	
	
	
	
	
	
	
}


```

2.LoggingAdvice.java

```java

package lab.spring.aop.advice;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;

public class LoggingAdvice { 
	 
	public void beforeAdviceMethod(JoinPoint thisJoinPoint) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		// 대상 메서드에 대한 로거를 얻어 해당 로거로 현재 class, method 정보 로깅		
		System.out.println("BeforeAdvice:"+className + "." + methodName + " 핵심 메소드 호출 전에 공통 기능 수행....");
	}
	
	 
	public void afterReturningAdviceMethod(JoinPoint thisJoinPoint,	Object retVal) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.println("AfterReturningAdvice:"+className + "." + methodName + " 핵심 메소드 정상 수행 후 공통 기능 수행...");
		System.out.println("return value is [" + ((Integer)retVal) + "]");
	}
	
	 
	public void afterThrowingAdviceMethod(JoinPoint thisJoinPoint,	Exception exception) 
			                                                             throws Exception{
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.print("afterThrowingAdvice:"+className + "." + methodName);	
		System.out.println("핵심 메소드가 수행 중 예외사항을 반환하고 종료하는 경우 수행된다");
		System.err.println("에러가 발생:"+ exception.getMessage());
			throw new Exception("에러가 발생했습니다. ", exception);
		}
    
	 
	public void afterAdviceMethod(JoinPoint thisJoinPoint) {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.print("AfterAdvice:"+className + "." + methodName);	
		System.out.println("핵심 로직 메서드  정상 종료와 예외 발생 경우를 모두 처리 하는 Advice");
		}
	
	 
	public Object aroundAdviceMethod(ProceedingJoinPoint thisJoinPoint)	throws Throwable {
		Class  clazz = thisJoinPoint.getTarget().getClass();
		String className = thisJoinPoint.getTarget().getClass().getSimpleName();
		String methodName = thisJoinPoint.getSignature().getName();
		System.out.print("AroundAdvice:"+className + "." + methodName);	
		
		System.out.println("핵심 메소드 수행 전의 공통 기능 수행........");
		long time1 = System.currentTimeMillis();
		Object retVal = thisJoinPoint.proceed();//Target빈의 핵심 메소드 호출
		System.out.println("ProceedingJoinPoint executed. return value is [" + retVal + "]");
		 
		System.out.println("리턴 값 변경 ==>  [" + ((Integer)retVal) + "(modified)" + "]");
		long time2 = System.currentTimeMillis();
		System.out.println("핵심 메소드 수행 후의 공통 기능 수행........ Time("+ (time2 - time1) + ")");
		return retVal;
			}
	
	
	
	
	
	
	
	
	
	
	
	
	
}


```

##### 2.lab.spring.aop.persist

1. UserManageDAO.java

```java
package lab.spring.aop.persist;



import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.PreparedStatementCreator;
import org.springframework.stereotype.Repository;



@Repository("dao")
public class UserManageDAO {
	
	private JdbcTemplate template;
	@Autowired
	public void setTemplate(JdbcTemplate template) {
		this.template=template;
	}
	
	public List<userVO> loginProc(String uid,String upwd) {
		List<userVO> lists=null;
		Object args[]=new String[]{uid,upwd};
		String sql="select*from userinfo where userid=? and userpwd=?";
		lists=template.query(sql,args,new UserRowMapper());
		return lists;
		
	}public int JoinProc(final userVO user) {
		int rows=0;
		final StringBuffer sql=new StringBuffer();
		sql.append("insert into userinfo(userid,username,userpwd,email,phone,job");
		sql.append(" values (?,?,?,?,?,?,?");
		rows=template.update(new PreparedStatementCreator() {
			
			public PreparedStatement createPreparedStatement(Connection con) throws SQLException {
				PreparedStatement pstat=con.prepareStatement(sql.toString());
				

				pstat.setString(1, user.getUserid());
				pstat.setString(2, user.getUsername());
				
				pstat.setString(3,user.getUserpwd());
				pstat.setString(4, user.getEmail());
				pstat.setString(5, user.getPhone());
				pstat.setString(6, user.getAddress());
				pstat.setString(7, user.getJob());
				return pstat;
			
			}

	});
 return rows;
}
	

	public List<userVO> findUserList(){
		List<userVO> userList=null;
		String sql="select*from userinfo";
		userList=template.query(sql,new UserRowMapper());
		return userList.isEmpty()?null:userList;
	}
	
	public userVO findUser(String userid) {
		Object vo=null;
		String sql="select*from userinfo where userid=?";
		vo=template.queryForObject(sql, new Object[] {userid},new UserRowMapper());
		return (userVO)vo;
	}
 public int updateUser(final userVO user) {
	 int rows=0;
	 final StringBuffer sql=new StringBuffer();
	 sql.append("update userinfo set email=?,phone=?,address=?,job=?");
	 sql.append(" where userid=?");
	 rows=template.update(new PreparedStatementCreator() {
		
		public PreparedStatement createPreparedStatement(Connection con) throws SQLException {
			 PreparedStatement pstat=con.prepareStatement(sql.toString());
			 
				pstat.setString(1, user.getEmail());
				pstat.setString(2, user.getPhone());
				pstat.setString(3, user.getAddress());
				pstat.setString(4, user.getJob());
				pstat.setString(5, user.getUserid());
				return pstat;
		}
	 
		
	 });
	 return rows;
 }
 
 public int removeUser(final String userid) {
	 int rows=0;
	 final String sql="delete userinfo where userid=?";
	 rows=template.update(new PreparedStatementCreator() {
		
		public PreparedStatement createPreparedStatement(Connection con) throws SQLException {
			PreparedStatement pstat=con.prepareStatement(sql);
			pstat.setString(1,userid);
			return pstat;
		}
	});
	 return rows;
 }
}

```



2.UserRowMapper.java

```java
package lab.spring.aop.persist;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public class UserRowMapper implements RowMapper<userVO> {

	public userVO mapRow(ResultSet rs,int num)throws SQLException{
		userVO vo=new userVO();
		vo.setUserid(rs.getString("userid"));
		vo.setUsername(rs.getString("username"));
		vo.setUserpwd(rs.getString("userpwd"));
		vo.setPhone(rs.getString("phone"));
		vo.setAddress(rs.getString("address"));
		vo.setEmail(rs.getString("email"));
		vo.setJob(rs.getString("job"));
		return vo;
	}

}

```



3.userVO.java

```java
package lab.spring.aop.persist;

public class userVO {
	 private String userid;
	 private String userpwd;
	 private String username;
	 private String email;
	 private String phone;
	 private String address;
	 private String job;
	public String getUserid() {
		return userid;
	}
	public void setUserid(String userid) {
		this.userid = userid;
	}
	public String getUserpwd() {
		return userpwd;
	}
	public void setUserpwd(String userpwd) {
		this.userpwd = userpwd;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getJob() {
		return job;
	}
	public void setJob(String job) {
		this.job = job;
	}
	 
}

```



##### 3.lab.spring.aop.service

1.UserService.java

```java
package lab.spring.aop.service;

import java.util.List;

import lab.spring.aop.persist.userVO;

public interface UserService {
 public int registMember(userVO user);
 public int updateUser(userVO user);
 public int removeUser(String uid);
 public userVO finUser(String uid);
 public List<userVO> login(String uid,String upwd);
 public List<userVO> findUserList();
}

```

2.UserServiceImpl.java

UserService에 넣어놓은 것을 구현해야한다.

오버라이드로 추가하고 return에 dao.로 받아주는 걸로 교체한다.

```java
package lab.spring.aop.service;

import java.util.List;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Service;

import lab.spring.aop.persist.UserManageDAO;
import lab.spring.aop.persist.userVO;


@Service("userService")
public class UserServiceImpl implements UserService {
  @Autowired
  private UserManageDAO dao;
  
	
  
	public void setDao(UserManageDAO dao) {
	this.dao = dao;
}


	

	public int updateUser(userVO user) {
		// TODO Auto-generated method stub
		return dao.updateUser(user);
	}




	public int removeUser(String uid) {
		// TODO Auto-generated method stub
		return dao.removeUser(uid);
	}




	public userVO finUser(String uid) {
		// TODO Auto-generated method stub
		return dao.findUser(uid);
	}









	public List<userVO> login(String uid, String upwd) {
		// TODO Auto-generated method stub
		return dao.loginProc(uid, upwd);
	}




	public List<userVO> findUserList() {
		// TODO Auto-generated method stub
		return dao.findUserList();
	}




	public int registMember(userVO vo) {
		int result=0;
		result=dao.JoinProc(vo);
		return result;
	}

}

```

##### 4.lab.spring.aop.test

1.DBTest

```java
package lab.spring.aop.test;

import java.util.Iterator;
import java.util.List;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.aop.persist.userVO;
import lab.spring.aop.service.UserService;

public class DBTest {

	public static void main(String[] args) {
		String[] configs =new String[] {"springDao.xml"};
		ApplicationContext context=
				new ClassPathXmlApplicationContext(configs);
		UserService service=
				context.getBean("userService", UserService.class);
		System.out.println("###############전체 목록###################");
		List<userVO> lists=service.findUserList();
		Iterator<userVO> iter=lists.iterator();
		while(iter.hasNext()) {
			userVO u=iter.next();
			System.out.println(u);
		}
		

	}

}

```



##### 5.lab.spring.aop.util

1.JdbcUtil.java

```java
package lab.spring.aop.util;

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



##### SpringDao.xam

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<context:annotation-config/>
<context:component-scan base-package="lab.spring.aop"/>

<!-- SpringDAO Framework에서 저수준 작업 JdbcTemplate 빈설정 -->

<bean id="jdbcTemplate"
	class="org.springframework.jdbc.core.JdbcTemplate"
	p:dateSource-ref="dataSource"/>
<!-- Jdbvtemplate 빈에 주입된 DataSource에 빈 설정 -->
<bean id="org.springframework.jdbc.datasource.DriverManagerDataSource"
p:drvierClassName="oracle.jdbc.OracleDriver"
p:url="jdbc:oracle:thin:@127.0.0.1:1521:orcl"
p:username="hr" p:password="oracle"/>

</beans>

```

##### pom.xml

```java
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>spring_aop</groupId>
  <artifactId>spirng_aop</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>spirng_aop</name>
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
    
    <dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
       
    </dependency>
    <dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.4</version>
       
    </dependency>
    <dependency>
    <groupId>aopalliance</groupId>
    <artifactId>aopalliance</artifactId>
    <version>1.0</version>
       
    </dependency>
    
  <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-jdbc</artifactId>
<version>${spring.maven.artifact.version}</version>

</dependency> <!-- 이게 있어야 DB연동...?-->
    

      
  
  </dependencies>
</project>

```







## 정리해보까?

```java
<bean id="targer" class=""/>
<bean id="advice" class=""/>
<aop:aspect>
<aop:pointcut ref="target">
	<aop:before ~ advice-ref..>
	<aop:after~
	..
        </aop:pointcut>
```





