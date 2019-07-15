# 스프링MVC



1. 개요
   - Model- 어플리케이션 데이터와 로직을 담는 객체
   - View -  Model의 정보를 사용자에게 표시
   - Controller - Model과 View의 중계역활로 View를 선택

![1563151347845](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC2)

2. 설정 방법

- Client( list.do, View.do, modify.do,delete.do,update.do....) 이 다음으로 요청
-  DispatcherServlet(요청 받아 HandlerMapping (채ㅜ))
  - FrontController(web.xml에 )
  - IoC Container(빈설정 파일)
    - view생성해서 응답

![1563151446425](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC3)

```xml
<!-- ApplicationContext 빈 설정 파일-->
<context-param>
<param-name>contextConfigLocation</param-name><!--이름은 반드시 왼쪽과 같이 -->
<param-value>
/WEB-INF/config/service/easycompany-service.xml <!--서비스 빈 정의-->
/WEB-INF/config/service/easycompany-dao.xml <!--Dao 빈 정의-->
</param-value>
</context-param>
<listener>
<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
```



```xml
<!-- WebApplicationContext 빈 설정 파일-->
<servlet>
<servlet-name>servlet</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>
/WEB-INF/config/easycompany-servlet.xml <!--web layer 관련 빈 선언-->
</param-value>
</init-param>
</servlet>
<!-- WebApplicationContext 빈 설정 파일-->
<servlet>
<servlet-name>webservice</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>
/WEB-INF/config/easycompany-webservice.xml
</param-value>
</init-param>
</servlet>
```

Servlet를 지금 따로 여러개 설정하고 있다.(예를 들어 외부사용자,내부사용자를 나누어 상대하기 위해..등등 )

단순하게 만들거라 이리 만들지는 않다.(이런것은 기능 많을 때), 그렇기에 참고만 하자.





## hello를 찍어보자







![1563152976260](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC4)

이미지 등은 webapp 밑에 저장해 주고 보이고 싶지 않다면 WEB-INF아래에 저장

![1563153094442](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC5)

설정해 주자. JRE javaSE 를 edit를 눌러 그림과 같은 것으로 바꿔주고

![1563153185207](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC6)

톰캣 클릭후 apply

pom.xml에 아래를 추가

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>spring.web</groupId>
  <artifactId>spring.web</artifactId>
  <packaging>war</packaging>
  <version>0.0.1-SNAPSHOT</version>
  <name>spring.web Maven Webapp</name>
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

</dependency>

<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>3.5.1</version>
</dependency>
    
    <dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
    
    <dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis-spring</artifactId>
  <version>2.0.1</version>
</dependency>

      <dependency> <!--이것과 아래 를 추가해주자. -->
<groupId>org.springframework</groupId>
<artifactId>spring-web</artifactId>
<version>${spring.maven.artifact.version}</version>

</dependency>
  <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>${spring.maven.artifact.version}</version>

</dependency>
    
  </dependencies>
  <build>
    <finalName>spring.web</finalName>
  </build>
</project>

```



webapp-WEB-INF- web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="http://xmlns.jcp.org/xml/ns/javaee" 
 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  id="WebApp_ID" version="4.0">


  <display-name>Archetype Created Web Application</display-name>
</web-app>

```



index.jsp

```jsp
<%@ page contentType="text/html; charset=utf-8" %>
<!DOCTYPE html>
<html>
<body>
<h2>spring web 컨텍스트</h2>
</body>
</html>

```

작성후 톰캣 실행하여 실행되는지 확인





web.xml 설정하자

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="http://xmlns.jcp.org/xml/ns/javaee" 
 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  id="WebApp_ID" version="4.0">


  <display-name>Archetype Created Web Application</display-name>
  
  <!-- list.do 같은 것을 dispatcherServlet이 받도록 설정할것! -->
  
  
<filter>
    <filter-name>encodingFilter</filter-name>
    <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
    <init-param>
      <param-name>encoding</param-name>
      <param-value>UTF-8</param-value>
    </init-param>
  </filter>
   
  <filter-mapping>
    <filter-name>encodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>
  
  <!-- DispatcherServlet 을 FrontController로 설정 -->
    <servlet>
    <servlet-name>action</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
  </servlet>
 
  <servlet-mapping>
    <servlet-name>action</servlet-name>
    <url-pattern>*.do</url-pattern><!-- .do는 dispatcherServlet이 처리하도록 설정한 것이다. -->
  </servlet-mapping>
</web-app>



   
  


```



webapp- WEB-INF-(bean configration xml (action-servlet.xml)을 만든후 그 파일에)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
<context:annotation-config/>
<context:component-scan base-package="lab.spring.web"/>

<!--  Handler mapping bean설정( DefaultAnnotationHandlerMapping)
기본 HandlerMapping이므로 빈 설정 파일에 별도로 선언할 필요 없으나, 다른 HandlerMapping과 함께 사용한다면 선언
해야 한다. -->

<!--  ViewResolver Bean 설정 -->
<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix" value="/WEB-INF/view/"></property>
    <property name="suffix" value=".jsp"></property>
  </bean>
</beans>



<!--  Controller Bean 설정(자동으로 스캔에서 되도록 설정할것이다. 위에 context scan추가로) -->


```

추가하자.



그후 java Resources 아래 src/main/java 아래 패키지 lab.spring.web.controller; 만든후 클래스 생성

```java
package lab.spring.web.controller;

import java.util.Calendar;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloController {
	
	@RequestMapping(value="/hello.do", method=RequestMethod.GET)//get인지 post인지 요청 방식 설정 가능 여기서는 get방식
	public ModelAndView sayHello() {
		ModelAndView mav= new ModelAndView();//모델과 view를 보내겠따.라고 설정
		mav.addObject("greet", getGreeting());//request.setAttribute("key,
		mav.setViewName("hello");
		return mav;
	}

public String getGreeting() {
	long now=System.currentTimeMillis();
	int Hour=Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
	String message="";
	if(Hour < 12) {
		message="Good Morning 스프링 웹~";
		
	}else if(Hour <18) {
		message="Good Afternoon 스프링 웹~";
	}else {
		message="Good Evening 스프링 웹~";
	}
	return message;
}
}


```



![1563157010507](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC7)

view 파일 생성 후 hello.jsp를 만들자(view용 보여주기 위한 파일 생성)

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>hello.jsp</title>
</head>
<body>
인삿말: ${greet}<Br>
from HelloControler
</body>
</html>
```

그 후 



WEB-INF-> lib 파일을 만들고 ->jstl.jar 파일과 standard.jar 파일을 추가한다 

##### @RequestMapping

요청에 대한 어떤 Controller, 어떤 메소드가 처리하지를 맵핑하기 위한 어노테이션

- value-String[] -ufl 값으로



###### 로그인 해보기

Server프로젝트에  server.xml 일부 변경점을 찾아보.........................힘들테니 중간과 마지막을 참고해보자.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
--><!-- Note:  A "Server" is not itself a "Container", so you may not
     define subcomponents such as "Valves" at this level.
     Documentation at /docs/config/server.html
 --><Server port="8005" shutdown="SHUTDOWN">
  <Listener className="org.apache.catalina.startup.VersionLoggerListener"/>
  <!-- Security listener. Documentation at /docs/config/listeners.html
  <Listener className="org.apache.catalina.security.SecurityListener" />
  -->
  <!--APR library loader. Documentation at /docs/apr.html -->
  <Listener SSLEngine="on" className="org.apache.catalina.core.AprLifecycleListener"/>
  <!-- Prevent memory leaks due to use of particular java/javax APIs-->
  <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener"/>
  <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener"/>
  <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener"/>

  <!-- Global JNDI resources
       Documentation at /docs/jndi-resources-howto.html
  -->
  <GlobalNamingResources>
    <!-- Editable user database that can also be used by
         UserDatabaseRealm to authenticate users
    -->
    <Resource auth="Container" description="User database that can be updated and saved" factory="org.apache.catalina.users.MemoryUserDatabaseFactory" name="UserDatabase" pathname="conf/tomcat-users.xml" type="org.apache.catalina.UserDatabase"/>
  
  <Resource auth="Container" driverClassName="oracle.jdbc.OracleDriver" 
  maxIdle="10" maxTotal="20" maxWaitMillis="-1" name="jdbc/oracle" 
  password="oracle" type="javax.sql.DataSource" 
  url="jdbc:oracle:thin:@127.0.0.1:1521:orcl" username="hr"/>
  
  </GlobalNamingResources>

  <!-- A "Service" is a collection of one or more "Connectors" that share
       a single "Container" Note:  A "Service" is not itself a "Container",
       so you may not define subcomponents such as "Valves" at this level.
       Documentation at /docs/config/service.html
   -->
  <Service name="Catalina">

    <!--The connectors can use a shared executor, you can define one or more named thread pools-->
    <!--
    <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"
        maxThreads="150" minSpareThreads="4"/>
    -->


    <!-- A "Connector" represents an endpoint by which requests are received
         and responses are returned. Documentation at :
         Java HTTP Connector: /docs/config/http.html
         Java AJP  Connector: /docs/config/ajp.html
         APR (HTTP/AJP) Connector: /docs/apr.html
         Define a non-SSL/TLS HTTP/1.1 Connector on port 8080
    -->
    <Connector connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443"/>
    <!-- A "Connector" using the shared thread pool-->
    <!--
    <Connector executor="tomcatThreadPool"
               port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    -->
    <!-- Define a SSL/TLS HTTP/1.1 Connector on port 8443
         This connector uses the NIO implementation. The default
         SSLImplementation will depend on the presence of the APR/native
         library and the useOpenSSL attribute of the
         AprLifecycleListener.
         Either JSSE or OpenSSL style configuration may be used regardless of
         the SSLImplementation selected. JSSE style configuration is used below.
    -->
    <!--
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="150" SSLEnabled="true">
        <SSLHostConfig>
            <Certificate certificateKeystoreFile="conf/localhost-rsa.jks"
                         type="RSA" />
        </SSLHostConfig>
    </Connector>
    -->
    <!-- Define a SSL/TLS HTTP/1.1 Connector on port 8443 with HTTP/2
         This connector uses the APR/native implementation which always uses
         OpenSSL for TLS.
         Either JSSE or OpenSSL style configuration may be used. OpenSSL style
         configuration is used below.
    -->
    <!--
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11AprProtocol"
               maxThreads="150" SSLEnabled="true" >
        <UpgradeProtocol className="org.apache.coyote.http2.Http2Protocol" />
        <SSLHostConfig>
            <Certificate certificateKeyFile="conf/localhost-rsa-key.pem"
                         certificateFile="conf/localhost-rsa-cert.pem"
                         certificateChainFile="conf/localhost-rsa-chain.pem"
                         type="RSA" />
        </SSLHostConfig>
    </Connector>
    -->

    <!-- Define an AJP 1.3 Connector on port 8009 -->
    <Connector port="8009" protocol="AJP/1.3" redirectPort="8443"/>


    <!-- An Engine represents the entry point (within Catalina) that processes
         every request.  The Engine implementation for Tomcat stand alone
         analyzes the HTTP headers included with the request, and passes them
         on to the appropriate Host (virtual host).
         Documentation at /docs/config/engine.html -->

    <!-- You should set jvmRoute to support load-balancing via AJP ie :
    <Engine name="Catalina" defaultHost="localhost" jvmRoute="jvm1">
    -->
    <Engine defaultHost="localhost" name="Catalina">

      <!--For clustering, please take a look at documentation at:
          /docs/cluster-howto.html  (simple how to)
          /docs/config/cluster.html (reference documentation) -->
      <!--
      <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>
      -->

      <!-- Use the LockOutRealm to prevent attempts to guess user passwords
           via a brute-force attack -->
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <!-- This Realm uses the UserDatabase configured in the global JNDI
             resources under the key "UserDatabase".  Any edits
             that are performed against this UserDatabase are immediately
             available for use by the Realm.  -->
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm" resourceName="UserDatabase"/>
      </Realm>

      <Host appBase="webapps" autoDeploy="true" name="localhost" unpackWARs="true">

        <!-- SingleSignOn valve, share authentication between web applications
             Documentation at: /docs/config/valve.html -->
        <!--
        <Valve className="org.apache.catalina.authenticator.SingleSignOn" />
        -->

        <!-- Access log processes all example.
             Documentation at: /docs/config/valve.html
             Note: The pattern used is equivalent to using pattern="common" -->
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log" suffix=".txt"/>

      <Context docBase="board" path="/board" reloadable="true" source="org.eclipse.jst.jee.server:board">
      
        <Resource auth="Container" driverClassName="oracle.jdbc.OracleDriver" maxIdle="10" maxTotal="20" maxWaitMillis="-1" name="jdbc/oracle" password="oracle" type="javax.sql.DataSource" url="jdbc:oracle:thin:@127.0.0.1:1521:orcl" username="hr"/>
      </Context>
      <Context docBase="spring.web" path="/spring.web" 
      reloadable="true" source="org.eclipse.jst.j2ee.server:spring.web">
      
       <Resource auth="Container" driverClassName="oracle.jdbc.OracleDriver" 
  maxIdle="10" maxTotal="20" maxWaitMillis="-1" name="jdbc/oracle" 
  password="oracle" type="javax.sql.DataSource" 
  url="jdbc:oracle:thin:@127.0.0.1:1521:orcl" username="hr"/>
  </Context>
      
      <Context docBase="bbs" path="/bbs" reloadable="true" source="org.eclipse.jst.j2ee.server:bbs"/>
      <Context docBase="web1" path="/web1" reloadable="true" source="org.eclipse.jst.jee.server:web1"/>
      </Host>
      
    </Engine>
  </Service>
</Server>
```



action-servelet.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:jee="http://www.springframework.org/schema/jee"
	xmlns:mvc="http://www.springframework.org/schema/mvc"
	xsi:schemaLocation="http://www.springframework.org/schema/jee http://www.springframework.org/schema/jee/spring-jee-4.3.xsd
		http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc-4.3.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
<context:annotation-config/>
<context:component-scan base-package="lab.spring.web"/>

<!--  Handler mapping bean설정( DefaultAnnotationHandlerMapping)
기본 HandlerMapping이므로 빈 설정 파일에 별도로 선언할 필요 없으나, 다른 HandlerMapping과 함께 사용한다면 선언
해야 한다. -->

<!--  ViewResolver Bean 설정 -->
<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix" value="/WEB-INF/view/"></property>
    <property name="suffix" value=".jsp"></property>
  </bean>
  <!-- db연동과 함께 sqlSessionfactory bean -> sqlSessio Templete -> sqlSession 을 UserManagerDAO에 주입 -->

<!-- jNDI 기반이 설정 설정 예시 -->
<jee:jndi-lookup jndi-name="jdbc/oracle" id="dataSource" resource-ref="true"/> 

<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
  <property name="dataSource" ref="dataSource" />
  <property name="mapperLocations" value="classpath*:lab/mybatis/mappers/*.xml" />
</bean>

<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
  <constructor-arg index="0" ref="sqlSessionFactory" />
</bean>

<mvc:annotation-driven/> <!-- 이렇게 하면 자동으로 HandlerAdaptor가 자동으로 추가된다. -->
  
</beans>



<!--  Controller Bean 설정(자동으로 스캔에서 되도록 설정할것이다. 위에 context scan추가로) -->


```

UserDAO.java

```java
package lab.spring.web.dao;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import lab.spring.web.model.UserVO;


@Repository
public class UserDAO {
	@Autowired
	SqlSession sqlSession;//?꽕?젙 application.xml?뿉?꽌 ?븳 ?꽕?젙Session?씠 ?뱾?뼱?삱寃껋씠?떎.
	
	
	
	public UserVO login(String uid,String upwd) {
		
		Object vo=null;
		HashMap<String,String> hm=new HashMap<String,String>();
		hm.put("uid", uid);
		hm.put("upwd",upwd);
		vo= sqlSession.selectOne("lab.mybatis.user.UserMapper.login",hm);
		return (UserVO)vo;
		
	}
	public int addUser(UserVO user) {
		
		return sqlSession.insert("lab.mybatis.user.UserMapper.addUser",user);
	}
	public List<UserVO> findUserList(){
		
		return sqlSession.selectList("lab.mybatis.user.UserMapper.getUserList");
	}
	public int updateUser(UserVO user) {
		
		return sqlSession.update("lab.mybatis.user.UserMapper.modifyUser",user);
	}
	public int removeuser(final String uid) {
		
		return sqlSession.delete("lab.mybatis.user.UserMapper.removeUser",uid);
	}
	public UserVO findUser(String uid) {
		
		return sqlSession.selectOne("lab.mybatis.user.UserMapper.getUser",uid);
	}
}

```

UserVO.java

```xml
package lab.spring.web.model;

public class UserVO {
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
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		 return "userid:" + getUserid() + "\n" +
        "userpwd:" + getUserpwd() + "\n" +
        "username:" + getUsername() + "\n" +
        "phone:" + getPhone() + "\n" +
        "email:" + getEmail() + "\n" +
        "address:" + getAddress() + "\n" +
        "job:"+ getJob() + "\n";
				
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

![1563165140023](C:\Users\student\Documents\GitHub\STUDY\javaStudy\MVC8)

전에 만든것 붙여넣기 한후 참고로

LoginController.java

```java
package lab.spring.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.UserVO;
import lab.spring.web.service.UserService;

@Controller("/login.do")
public class LoginController {

	
	@Autowired
	UserService service;
	
	@RequestMapping(method=RequestMethod.GET)
	public String form() {
		return "loginForm";//view이름만 리턴//view이름으로 리턴하므로 String으로 해도 된다.
	}
	
	@RequestMapping(method=RequestMethod.POST)
	public ModelAndView login(@RequestParam("userid")String uid,
								@RequestParam("userpwd")String upwd){
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.login(uid, upwd);
		mav.addObject("user",vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
			
		}else{
			mav.setViewName("loginFail");
			
		}
		return mav;
								}
    
}

```

혹은

```java
	@RequestMapping(method=RequestMethod.POST)
	public ModelAndView login(UserVO user){
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.login(user.getUserid(),user.getUserpwd());
		mav.addObject("user",vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
			
		}else{
			mav.setViewName("loginFail");
			
		}
		return mav;
								}
```

로 해도 가능하다.

```java
	@RequestMapping(method=RequestMethod.POST)
	public ModelAndView login(HttpServletRequest request,HttpServletResponse response){
		ModelAndView mav=new ModelAndView();
		String uid=request.getParameter("userid");
		String upwd=request.getParameter("userpwd");
		UserVO vo=null;
		vo=service.login(uid,upwd);
		mav.addObject("user",vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
			
		}else{
			mav.setViewName("loginFail");
			
		}
		return mav;
								}
```

이리해도 가능! 



##### UserLIst와 UserForm추가

userForm.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta   charset="utf-8">
<TITLE>개인 정보 입력 화면</TITLE>
<link rel=stylesheet href="../css/user.css" type="text/css">
<script type="text/javascript">
function userCreate(){		
	f.action="./add.do";
	f.submit();	
}
function userList(){
	f.action="./list.do";
	f.submit();
}
</script>
</head>
<body bgcolor=#FFFFFF text=#000000 leftmargin=0 topmargin=0 marginwidth=0 marginheight=0>
<br>
<table width=780 border=0 cellpadding=0 cellspacing=0>
	<tr>
	  <td width="20"></td>
	  <td>
  <!--contents-->
	  <table width=590 border=0 cellpadding=0 cellspacing=0>
		  <tr>
			<td bgcolor="f4f4f4" height="22">&nbsp;&nbsp;<b>사용자 관리 - 개인 정보 입력</b></td>
		  </tr>
	  </table>  
	  <br>
	  
	  
 
	  <!-- write Form  -->
	  <form name="f" method="post" action="/add.do">
	  
	  <table border="0" cellpadding="0" cellspacing="1" width="590" bgcolor="BBBBBB">
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">사용자 아이디</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:150" name="userid" value="">
				 
			</td>
		  </tr>
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">비밀번호</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="password" style="width:150" name="userpwd" value="">
				 
			</td>
		  </tr>
		   
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">이름</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:200" name="username" value="">
		 
			</td>
		  </tr>
		  
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">이메일 주소</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="email" value="">
			</td>
		  </tr>		
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">전화 번호</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:150px" name="phone" value="">
			</td>
		  </tr>		
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">주    소</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="address" value="">
			</td>
		  </tr>		
	  </table>
	  
	  <br>
	  
	  <table width=590 border=0 cellpadding=0 cellspacing=0>
		  <tr>
			<td align=center>
			<input type="button" value="회원 가입" onClick="userCreate()"> &nbsp;
			<input type="button" value="목록" onClick="userList()">
			</td>
		  </tr>
	  </table>

	  </td>
	</tr>
</table>  
 </form>
</body>
</html>
```



userList.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>   
<!DOCTYPE html >
<html>
<head>
<meta   charset=utf-8">
<title>user_list.jsp(사용자 관리)</title> 
<link rel=stylesheet href="../css/user.css" type="text/css">
</head>
<body bgcolor=#FFFFFF text=#000000 leftmargin=0 topmargin=0 marginwidth=0 marginheight=0>
<br>
<form name="f" method="post" action="./add.do">
<table width=780 border=0 cellpadding=0 cellspacing=0>
<tr>
	<td width="20"></td>
	<td>
	  	<!--contents-->
	  	<table width=590 border=0 cellpadding=0 cellspacing=0>
		  	<tr>
				<td bgcolor="f4f4f4" height="22">&nbsp;&nbsp;<b>사용자 관리 - 리스트</b></td>
		  	</tr>
	  	</table>  
	  	<br>
	  
	  	<!-- list -->
	  	<table border="0" cellpadding="0" cellspacing="1" width="590" bgcolor="BBBBBB">
		  	<tr>
				<td width=190 align=center bgcolor="E6ECDE" height="22">사용자 아이디</td>
				<td width=200 align=center bgcolor="E6ECDE">이름</td>
				<td width=200 align=center bgcolor="E6ECDE">이메일</td>
		  	</tr>
 
 	<!-- 사용자 리스트를 클라이언트에게 보여주기 위하여 출력. -->
 		  	 <c:forEach var="user" items="${list}">
           <tr>
            <td>${user.userid }</td>
            <td>${user.username }</td>
            <td>${user.email }</td>
           </tr>
            <!-- 답글 -->
          </c:forEach>
	  	</table>
	  	<!-- /list -->	 

		<br>
		<!-- button -->
	  	<table border="0" cellpadding="0" cellspacing="1" width="590">
			<tr>
				<td align="right">
					<input type="submit" value="사용자 추가"/>
				</td>
			</tr>
		</table>		
	</td>
</tr>
</table>  
</form>
</body>
</body>
</html>
```



UserController.java

```java
package lab.spring.web.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.UserVO;
import lab.spring.web.service.UserService;

@Controller
public class UserController {

	
	@Autowired
	UserService service;
	
	@RequestMapping(value="/add.do",method=RequestMethod.GET)
		public  String form() {
			return "userForm";
		}
	
	@RequestMapping(value="/add.do",method=RequestMethod.POST)
	public ModelAndView userCreate(UserVO user) {
		ModelAndView mav=new ModelAndView();
		service.addUser(user);
		
		
		mav.setViewName("redirect:/list.do");
		
		return mav;
	}
	@RequestMapping(value="/list.do",method=RequestMethod.GET)//애는 왜 GET이지???
	public ModelAndView userlist() {
		ModelAndView mav=new ModelAndView();
		
		List<UserVO> list=service.findUserList();
		mav.addObject("list",list);
		mav.setViewName("userList");//setViewName을 통해 뷰의 이름을 지정할 수 있다.
		
		return mav;
		
	}
	
	
	
}

```





