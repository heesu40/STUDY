# 스프링MVC



1. 개요
   - Model- 어플리케이션 데이터와 로직을 담는 객체
   - View -  Model의 정보를 사용자에게 표시
   - Controller - Model과 View의 중계역활로 View를 선택

![1563151347845](D:\gitgithub\STUDY\javaStudy\MVC2)

2. 설정 방법

- Client( list.do, View.do, modify.do,delete.do,update.do....) 이 다음으로 요청
-  DispatcherServlet(요청 받아 HandlerMapping (채ㅜ))
  - FrontController(web.xml에 )
  - IoC Container(빈설정 파일)
    - view생성해서 응답

![1563151446425](D:\gitgithub\STUDY\javaStudy\MVC3)

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







![1563152976260](D:\gitgithub\STUDY\javaStudy\MVC4)

이미지 등은 webapp 밑에 저장해 주고 보이고 싶지 않다면 WEB-INF아래에 저장

![1563153094442](D:\gitgithub\STUDY\javaStudy\MVC5)

설정해 주자. JRE javaSE 를 edit를 눌러 그림과 같은 것으로 바꿔주고

![1563153185207](D:\gitgithub\STUDY\javaStudy\MVC6)

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



![1563157010507](D:\gitgithub\STUDY\javaStudy\MVC7)

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

![1563165140023](D:\gitgithub\STUDY\javaStudy\MVC8)

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
				<input type="text" style="width:150" name="userid" value="${userid }">
				 
			</td>
		  </tr>
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">비밀번호</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="password" style="width:150" name="userpwd" value="${userpwd }">
				 
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
		   <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">직     업  </td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="job" value="">
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
<!-- <form name="f" method="post" action="./add.do"> -->
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
 		  	 <c:forEach var="user" items="${users}" >
           <tr>
            <td>${user.userid }</td>
            <td>${user.username }</td>
            <td>${user.email }</td>
           </tr>
            <!-- 답글 -->
          </c:forEach>
	  	</table>
	  	<!-- /list -->	 

		<br><form name="f" method="get" action="./add.do">
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
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
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
//	
//	@RequestMapping(value="/add.do",method=RequestMethod.POST)
//	public ModelAndView userCreate(UserVO user) {
//		ModelAndView mav=new ModelAndView();
//		service.addUser(user);
//		
//		
//		mav.setViewName("redirect:/list.do");
//		
//		return mav;
//	}
//	@RequestMapping(value="/list.do",method=RequestMethod.GET)//애는 왜 GET이지???
//	public ModelAndView userlist() {
//		ModelAndView mav=new ModelAndView();
//		
//		List<UserVO> list=service.findUserList();
//		mav.addObject("list",list);
//		mav.setViewName("userList");//setViewName을 통해 뷰의 이름을 지정할 수 있다.
//		
//		return mav;
//		
//	}
	
	@RequestMapping(value="/add.do",method=RequestMethod.POST)
	public ModelAndView addUser(@ModelAttribute("user")UserVO vo) {
		ModelAndView mav=new ModelAndView();
		if(service.addUser(vo)>0) {
			mav.setViewName("redirect:/list.do");
		}else {
			mav.setViewName("redirect:/login.do");
		}
		return mav;
	}
	@GetMapping("/list.do")
	public ModelAndView listUser() {
		ModelAndView mav=new ModelAndView();
		List<UserVO> userList=null;
		userList=service.findUserList();
		mav.addObject("users",userList);//앞에 따옴표 있는 것을 실제 list.jsp에 불러오는 
		//c:forEach var="user" items="${users}" 에서 items안에 들어가는 값 
		mav.setViewName("userList");
		return mav;
	}
	
	
}

```









# 스프링 MVC 구조 확인(책)

이클립스에서 maven porject를 시작하고  webapp가 들어있는 것으로 만들어야 하위 폴더 구성이 자동으로 추가 된다.



index가 webapp-WEB_INF-index.jsp에 있는 것ㅇ르 확인하고

jsp인데 선언이 빠져있으므로 넣어주자

#####  index.jsp

```jsp
<%@ page contentType="text/html;charset=utf-8" %>
<html>
<body>
<meta charset="utf-8">
<h2>Spring mvc web 컨텍스트</h2>
</body>
</html>

```

chapter9장은 책대로 해보자.

#####  pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>spring_orm</groupId>
  <artifactId>spring_orm</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>spring_orm</name>
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
    
  </dependencies>
  
  
</project>

```



config 패키지 만든후

#####  MvcConfig.java

```java
package config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.DefaultServletHandlerConfigurer;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@EnableWebMvc
public class MvcConfig implements WebMvcConfigurer{

	@Override
	public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
		
		configurer.enable();
	}

	@Override
	public void configureViewResolvers(ViewResolverRegistry registry) {
		
		registry.jsp("/WEB-INF/view/",".jsp");
	}

	  
	
}

```

오버라이드 하면 편하다! 오버라이드해서 불러오자.



##### web.xml(DispatcherServlet설정)

encoding필터의 경우 앞에 옴으로 앞에 써주고 최신버전의 web-app을 가져오자(가장 위의 설정 부분)

contextClass-?

contextConfigLocation- 경로지정?

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="http://xmlns.jcp.org/xml/ns/javaee" 
 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  id="WebApp_ID" version="4.0">


  <display-name>Archetype Created Web Application</display-name>
  
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
  
  
  <servlet>
  <servlet-name>dispatcher</servlet-name>
  <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
  	 <init-param>
  	 <param-name>contextClass</param-name>
  	 <param-value>
  	 org.springframework.web.context.support.AnnotationConfigWebApplicationContext
  	 </param-value>
  	 </init-param>
  	 
  	 
  	 <init-param>
  	 <param-name>contextConfigLocation</param-name>
  	 <param-value>
  	 config.MvcConfig
  	 config.ControllerConfig
  	 </param-value><!-- 장소 지정을 cinfig 패키지 아래 로 했기에 두개의 파일은 같은 패키지 아래에 있어야 한다.-->
  	 </init-param>
  	 <load-on-startup>1</load-on-startup>
  </servlet>
  
  <servlet-mapping>
  <servlet-name>dispatcher</servlet-name>
  <url-pattern>/</url-pattern>
  </servlet-mapping>
  
</web-app>

```



#####   HelloController.java(컨트롤러 구현)

```java
package controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {

		@GetMapping("/hello")
		public String hello(Model model,
				@RequestParam(value="name", required=false)String name) {
			model.addAttribute("greeting","안녕하세요,"+name);//요청처리결과를 뷰에 전달
			return "hello";//뷰 이름(뷰 구현을 찾아주는 것이 ViewResolver가 처리하는데 이는 다음문제에서 살펴보자.)
            //model 의 속성 greeting에 값을 설정해 주는데 그 값이 "안녕하세요"와 name파라미터 값을 연결한 문자다.
		}
}

```



##### ControllerConfig.java

```java
package config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import controller.HelloController;


@Configuration
public class ControllerConfig {

		@Bean
		public HelloController helloController() {
			return new HelloController();
		}
}

```





##### hello.jsp

WEB-INF 아래 view파일을 생성하고 hello.jsp를 만들자

```jsp
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello.jsp</title>
</head>
<body>
HelloController가 Model에 저장해서 View에 전달한 데이터:<br>
${greeting}
</body>
</html>
```



![1563240076479](D:\gitgithub\STUDY\javaStudy\MVC9)

만약 hello.jsp에 오류가 뜨면 톰켓이 없어서 이므로  buildpath d를 들어가 addLibrary...에 들어가 server runtime클릭후 톰캣을 넣어주자.

결과 확인은 /hello?name=아무거나 작성 을 해보면 알 수 있다.







# 메세지, 커맨드 객체 검증

###### 오류 메시지 준비

main 아래 resources아래 messages파일을 만드후

파일을 두개 만든다 각각 이름은

validation_ko.properties,validation.properties

validation_ko.properties

```
required=\uC791\uC131\uC744 \uD574\uC57C\uD55C\uB2E4.
required.user.userid=\uC544\uC774\uB514\uAC00 \uC5C6\uB2E4.
required.username=\uC774\uB984\uC774 \uC5C6\uB2E4!
required.user.userpwd=\uBE44\uBC00\uBC88\uD638\uAC00 \uC5C6\uB2E4!
```

validation.properties

```
required=Must be Required Item!!!
required.user.userid=Must be Required Userid!!
required.username=Must be Required Your Name!!
required.user.userpwd=Must be Required Password!!
```

위의 한글로 작성했지만 꺠진다 신경쓰지 말자(만약 저리 안나온다면 마우스 오른쪽 버튼 Properties에 들어가 Text file encoding을 Default로 선택하자.)

###### 오류 처리 루트



``` java
package lab.spring.web.model;

import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

public class UserValidator implements Validator {

	@Override
	public boolean supports(Class<?> clazz) {
	
		return UserVO.class.isAssignableFrom(clazz);
	}

	@Override
	public void validate(Object target, Errors errors) {
		UserVO vo=(UserVO)target;
		
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "userid", "required");
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "username", "required");
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "userpwd", "required");
		
	}

}

```



###### 오류가 나타낼 위치에 코드 입력

userForm.jsp

 <font color="red">< form:errors path="user.username"/ ></font> 를 상자 옆에 넣어준다. username은 맞는 것에 따라 바꾸어 준다.

```java
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
     <%@ taglib prefix="spring" uri="http://www.springframework.org/tags"  %>
      <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"  %>
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
	  
	  
 <form:errors path="user" />
	  <!-- write Form  -->
	  <form name="f" method="post" action="/add.do">
	  
	  <table border="0" cellpadding="0" cellspacing="1" width="590" bgcolor="BBBBBB">
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">사용자 아이디</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:150" name="userid" value="">
				 <font color="red"><form:errors path="user.userid"/></font>
			</td>
		  </tr>
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">비밀번호</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="password" style="width:150" name="userpwd" value="">
				  <font color="red"><form:errors path="user.userpwd"/></font>
			</td>
		  </tr>
		   
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">이름</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:200" name="username" value="">
		  <font color="red"><form:errors path="user.username"/></font>
			</td>
		  </tr>
		  
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">이메일 주소</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="email" value="">
				 <font color="red"><form:errors path="user.email"/></font>
			</td>
		  </tr>		
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">전화 번호</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:150px" name="phone" value="">
				 <font color="red"><form:errors path="user.phone"/></font>
			</td>
		  </tr>		
		  <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">주    소</td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="address" value="">
				 <font color="red"><form:errors path="user.address"/></font>
			</td>
		  </tr>		
		   <tr>
			<td width=100 align=center bgcolor="E6ECDE" height="22">직     업  </td>
			<td width=490 bgcolor="ffffff" style="padding-left:20">
				<input type="text" style="width:340px" name="job" value="">
				 <font color="red"><form:errors path="user.job"/></font>
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







# 파일 업로드

###### 파일 설정 준비

pom.xml에

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

      <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-web</artifactId>
<version>${spring.maven.artifact.version}</version>

</dependency>
  <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>${spring.maven.artifact.version}</version>
</dependency>


<!-- 파일 업로드를 위한 추가 -->
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.2.1</version>
</dependency>

<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>1.4</version>
</dependency>
    
  </dependencies>
  <build>
    <finalName>spring.web</finalName>
  </build>
</project>

```

아래 부분을 추가!



action-servlet.xml 에(위치는 webapp 아래 WEB-INF 아래 ...)

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
  
  <bean id="messageSource"
   class="org.springframework.context.support.ResourceBundleMessageSource">
   <property name="basenames">
   <value>messages.validation</value>
   </property>
   </bean>
   
  <!-- 파일업로드 위한 multipartResolver를 이용한다. 스프링 bean이다. --> 
   <bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
    <property name="maxUploadSize" value="1000000" />
</bean>
  
</beans>



<!--  Controller Bean 설정(자동으로 스캔에서 되도록 설정할것이다. 위에 context scan추가로) -->


```



그 후 webapp-WEB-INF-view-report 를 만들고 그 아래 

reportComplete.jsp

```jsp
<%@ page contentType="text/html; charset=utf-8"%>
 

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>리포트 제출 완료</title>
</head>
<body>
리포트 제출 완료
</body>
</html>
```

reportForm.jsp

```jsp
<%@ page contentType="text/html; charset=utf-8"%>
 

<html>
<head>
<meta charset="utf-8">
<title>리포트 제출</title>
</head>
<body>
<h3>@RequestParam 사용</h3><!-- 파일 업로드 방법 1 참고로 업로드 파일은 POST로 넘겨야 한다. -->
<form action="submitReport1.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" value="제출"/>
</form>

<h3>MultipartHttpServletRequest 사용</h3><!-- 파일 업로드  방법 2 -->
<form action="submitReport2.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" value="제출"/>
</form>

<h3>커맨드 객체 사용</h3><!-- 파일  업로드 방법 3 -->
<form action="submitReport3.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" />
</form>


</body>
</html>
```



를 만든다.



###### 파일업로드 위한 객체와 컨트롤을 만들자

ReportCommand.java

```java
package lab.spring.web.model;

import org.springframework.web.multipart.MultipartFile;

public class ReportCommand {
private String studentNumber;
private MultipartFile report;
public String getStudentNumber() {
	return studentNumber;
}
public void setStudentNumber(String studentNumber) {
	this.studentNumber = studentNumber;
}
public MultipartFile getReport() {
	return report;
}
public void setReport(MultipartFile report) {
	this.report = report;
}


}

```



ReportController.java

```java
package lab.spring.web.controller;

import java.io.File;
import java.io.FileOutputStream;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import lab.spring.web.model.ReportCommand;

@Controller
public class ReportController {

	
	 @RequestMapping("/report/report.do")//getMapping으로 써도 가능(먼저 가져오고
	 public String form() {
		 return "report/reportForm";//폼을 불러온 후 
	 }
		 
	 @RequestMapping("/report/submitReport1.do")//postMapping으로 써도 가능
	 public String submitReport1( 
	    @RequestParam("studentNumber") String studentNumber,//파람값은 reportFrom.jsp와 같아야한다
		 @RequestParam("report") MultipartFile report){
			 printInfo(studentNumber,report);//
			 if(report.getSize()==0) 
				 throw new NullPointerException("업로드된 파일 없음");
				 return  "report/reportComplete";
			 
		 }
	 private void printInfo(String studentNumber, MultipartFile report) {
		 if(!report.isEmpty()) {
			 String filename=report.getOriginalFilename();
			 String imgExt =filename.substring(filename.lastIndexOf(".")
					 +1, filename.length());
			 try {
				 //upload처리
				 if(imgExt.equalsIgnoreCase("JPG")
						 ||imgExt.equalsIgnoreCase("JPEG")
						 ||imgExt.equalsIgnoreCase("GIF")
						 ||imgExt.equalsIgnoreCase("PNG")) {//바이너리(binary)(?)의 파일을
					 byte[] bytes=report.getBytes();//바이트에 저장을 하고
					 File lOutFile =new File("c://uploadtest/"+"_"+filename);
					 //파일이 없을시 만든다는 내용이 없기떄문에 c아래에 저장될 위치의 파일이 있어야 한다.
					 FileOutputStream lFileOutputStream =new FileOutputStream(lOutFile);
					 lFileOutputStream.write(bytes);//저장된 것을 뿌려준후
					 lFileOutputStream.close();//닫아준다............?
				 }else {
					 System.out.println("File type error! ");
				 }
				 System.out.println(studentNumber + "제출된 보고서: "
						 + report.getOriginalFilename());
			 }catch(Exception e){
				 e.printStackTrace();
			 }
		 }
	 }
	 
	 @ExceptionHandler(NullPointerException.class)//위에 에러를 넘겼기 때문에 이것이 있어야 한다!!!!
	 public String handleException(NullPointerException exception) {
		 return "common/error"; // 뷰이름 리턴 common폴더를 만들고 그 아래 error를 만들어 오류 경고 보내야한다.
	 }
	 
	 @RequestMapping("/report/submitReport2.do")
	 public String submitReport2(MultipartHttpServletRequest request) {
		 String sno=request.getParameter("studentNumber");
		 MultipartFile report=request.getFile("report");
		 printInfo(sno,report);
		 if(report.getSize()==0) 
			 throw new NullPointerException("업로드된 파일 없음");
		 return "report/reportComplete";
	 }
	 @RequestMapping("/report/submitReport3.do")
	 public String submitReport3(ReportCommand reportCommand) {
		 printInfo(reportCommand.getStudentNumber(), reportCommand.getReport());
		 if(reportCommand.getReport().getSize()==0) 
		 { throw new NullPointerException("업로드된 파일 없음");}
		 return "report/reportComplete";
	 }
	 
	 }


```

를 만들어 실행 코드 완료!

webapp 아래 view 아래 common폴더를 만들고 error.jsp를 만들자

error.jsp

오류를 검색하기 위해서...? isErrorPage="true"를 추가한다!

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR" isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>error.jsp</title>
</head>
<body>
    예외가 발생하였습니다.
<%=exception.getMessage() %>
${exception.message }<br>
</body>
</html>
```



###### 파일 실행 위해서

http://localhost:8080/spring.web/report/report.do 로 접속(루트를 중간에 추가해 주었기 때문에 길어졌다.)

그 후 확인해 보자. 파일이 없을시 오류메시지가 뜨는지, 업로드(여기서는 사진파일만 했으므로 사진만 올리도록 하자) 가 되어 파일 저장위치에 들어가는지 확인해보자.



# 로그인 처리

###### 처리 위한 준비

LoginController.java

```java
package lab.spring.web.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

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
								@RequestParam("userpwd")String upwd,
								HttpSession session){//Session 추가하고
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.login(uid, upwd);
		session.setAttribute("authInfo", vo);//session 추가했따!
		//mav.addObject("user",vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
			
		}else{
			mav.setViewName("loginFail");
			
		}
		return mav;
								}
								}
```



###### 성공시 실패시의 화면 작성

loginSuccess.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
     <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>로그인 성공</title>
</head>
<body>
<c:if test="${!empty authInfo}">
<font color="blue">${authInfo.userid}님 환영합니다.</font><br>
<a href="<c:url value='/view.do?userid=${authInfo.userid}'/>">고객 정보 리스트</a><Br>
<a href="<c:url value='/list.do'/>">고객 정보 리스트</a><br>
<a href="<c:url value='/logout.do'/>">로그아웃</a><br>

전화번호 :${user.phone }<Br>
이메일: ${user.email}<Br>
주소:${user.address }<Br>
업무:${user.job }<Br>
</c:if>

<br><form name="f" method="post" action="./modify.do">
		<!-- button -->
	  	<table border="0" cellpadding="0" cellspacing="1" width="590">
			<tr>
				<td align="right">
					<input type="submit" value="수정"/>
				</td>
			</tr>
		</table>
</body>
</html>
```

loginFail.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
      <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>로그인 실패</title>
</head>
<body>

<c:if test="${empty authInfo}">
<font color="red">${authInfo.userid}님 아이디가 존재하지 않거나, 비밀번호 오류입니다.</font><br>

<a href="<c:url value='/login.do'/>">로그인</a><br>
<a href="<c:url value='/add.do'/>">회원</a><br>
</c:if>
</body>
</html>
```



###### 로그인 컨트롤과 유저 컨트롤 페이지를 수정

LoginController.java 

에서 일부 고쳐준다. ...

```java
package lab.spring.web.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.UserVO;
import lab.spring.web.service.UserService;

@Controller
public class LoginController {

	
	@Autowired
	UserService service;
	
	@RequestMapping(value="/login.do",method=RequestMethod.GET)
	public String form() {
		return "loginForm";//view이름만 리턴//view이름으로 리턴하므로 String으로 해도 된다.
	}
	
	@RequestMapping(value="/login.do",method=RequestMethod.POST)
	public ModelAndView login(@RequestParam("userid")String uid,
								@RequestParam("userpwd")String upwd,
								HttpSession session){//Session 추가하고
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.login(uid, upwd);
		session.setAttribute("authInfo", vo);//session 추가했따!
//		mav.addObject("user",vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
			
		}else{
			mav.setViewName("loginFail");
			
		}
		return mav;
	}
	@RequestMapping(value="/logout.do")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/login.do";
	}
//	@RequestMapping(method=RequestMethod.POST)
//	public ModelAndView login(UserVO user){
//		ModelAndView mav=new ModelAndView();
//		UserVO vo=null;
//		vo=service.login(user.getUserid(),user.getUserpwd());
//		mav.addObject("user",vo);
//		if(vo!=null) {
//			mav.setViewName("loginSuccess");
//			
//		}else{
//			mav.setViewName("loginFail");
//			
//		}
//		return mav;
//								}
//	@RequestMapping(method=RequestMethod.POST)
//	public ModelAndView login(HttpServletRequest request,HttpServletResponse response){
//		ModelAndView mav=new ModelAndView();
//		String uid=request.getParameter("userid");
//		String upwd=request.getParameter("userpwd");
//		UserVO vo=null;
//		vo=service.login(uid,upwd);
//		mav.addObject("user",vo);
//		if(vo!=null) {
//			mav.setViewName("loginSuccess");
//			
//		}else{
//			mav.setViewName("loginFail");
//			
//		}
//		return mav;
//								}
}

```

UserController.java

```java
package lab.spring.web.controller;

import java.util.ArrayList;
import java.util.List;

import javax.naming.directory.SearchControls;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.SearchVO;
import lab.spring.web.model.UserVO;
import lab.spring.web.model.UserValidator;
import lab.spring.web.service.UserService;

@Controller
public class UserController {

	
	@Autowired
	UserService service;
	
	
	
	
	@RequestMapping(value="/add.do",method=RequestMethod.GET)
		public  String form() {
			return "userForm";
		}
//	
//	@RequestMapping(value="/add.do",method=RequestMethod.POST)
//	public ModelAndView userCreate(UserVO user) {
//		ModelAndView mav=new ModelAndView();
//		service.addUser(user);
//		
//		
//		mav.setViewName("redirect:/list.do");
//		
//		return mav;
//	}
//	@RequestMapping(value="/list.do",method=RequestMethod.GET)//애는 왜 GET이지???
//	public ModelAndView userlist() {
//		ModelAndView mav=new ModelAndView();
//		
//		List<UserVO> list=service.findUserList();
//		mav.addObject("list",list);
//		mav.setViewName("userList");//setViewName을 통해 뷰의 이름을 지정할 수 있다.
//		
//		return mav;
//		
//	}
	
	@RequestMapping(value="/add.do",method=RequestMethod.POST)
	public ModelAndView addUser(@ModelAttribute("user")UserVO vo
			, BindingResult rs) {//에러를 상속받아 
		ModelAndView mav=new ModelAndView();
		new UserValidator().validate(vo, rs);
		if(rs.hasErrors()){//에러 메시지를 윗 줄에서 확인해서 만약 있다면
			mav.setViewName("userForm");
		}else if(service.addUser(vo)>0) {
			mav.setViewName("redirect:/list.do");
		}else {
			mav.setViewName("redirect:/login.do");
		}
		return mav;
	}
	
	/*
	 * @ModelAttribute("searchConditionList")//requestMapping보다 먼저 수행된다
	 * ModelAttribute 보다. public ArrayList<SearchVO> makeSearchConditionList(){
	 * ArrayList<SearchVO> searchConditionList = new ArrayList<SearchVO>();
	 * searchConditionList.add(new SearchVO("userid","아이디"));
	 * searchConditionList.add(new SearchVO("username","이름"));
	 * searchConditionList.add(new SearchVO("email","이메일")); return
	 * searchConditionList;
	 * 
	 * 
	 * 
	 * 
	 * }
	 */
	@ModelAttribute("searchConditionList")

	public ArrayList<SearchVO> makeSearchConditionList() {

		ArrayList<SearchVO> searchConditionList = new ArrayList<SearchVO>();

		searchConditionList.add(new SearchVO("userid", "아이디"));

		searchConditionList.add(new SearchVO("username", "이름"));

		searchConditionList.add(new SearchVO("email", "이메일"));

		return searchConditionList;

	}
	
	
	
	@RequestMapping("/list.do")
	public ModelAndView listUser(HttpSession session) {
		ModelAndView mav=new ModelAndView();
		List<UserVO> userList=null;
		if(session.getAttribute("authInfo")!=null) {
		userList=service.findUserList();
		mav.addObject("users",userList);//앞에 따옴표 있는 것을 실제 list.jsp에 불러오는 
		//c:forEach var="user" items="${users}" 에서 items안에 들어가는 값 
		mav.setViewName("userList");
		}else {
			mav.setViewName("redirect:/login.do");
		}
		return mav;
	}
	
	@RequestMapping(value="/search.do",method=RequestMethod.GET)
	public ModelAndView search(@RequestParam("searchCondition")String condition,
								@RequestParam("searchKeyword")String keyword) {
		ModelAndView mav=new ModelAndView();
		List<UserVO> userList=null;
		userList=service.findUser(condition,keyword);
		mav.addObject("users",userList);
		mav.setViewName("userList");
		return mav;
	}
	
//	@RequestMapping(value="/modify.do",method=RequestMethod.GET)
//	public  String modify() {
//		return "user_modify";
//	}
	
	
	
	@RequestMapping("/view.do")
	public ModelAndView updateUser(@RequestParam("userid")String uid) {
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.findUser(uid);
		mav.addObject("user",vo);
		mav.setViewName("user_modify");
		return mav;
		
		
	}
	
	@RequestMapping("/update.do")
	public ModelAndView updateUser(@ModelAttribute("user")UserVO user) {
		ModelAndView mav=new ModelAndView();
		int vo=0;
		vo=service.updateUser(user);
		if(vo>0) {
			mav.setViewName("redirect:list.do");
		}else {
			mav.setViewName("redirect:login.do");
		}
		return mav;
	 
	}
	
	@RequestMapping("/remove.do")
	public ModelAndView dropUser(@RequestParam("userid")String uid) {
		ModelAndView mav=new ModelAndView();
		if(service.removeUser(uid)>0) {//버튼의 이름 onclick=과 같은 이름
			mav.setViewName("redirect:list.do");
		}else {
			mav.setViewName("redirect:login.do");
		}
		return mav;
	}
	
	
	
}

```



###### 인터셉터 사용하기(HandlerInterceptor)

HandlerInterceptor 인터페이스 는 Dispatcher에서 controller로 가기 전, 그 후, view실행 이후 사이에 낚아채서(?)기능을 수행한다.

1. 컨트롤러 실행전(preHandle)
2. 실행후, 뷰 실행 전(postHandle)
3. 뷰 실 행 이후(afterCompletion)

```java
package lab.spring.web.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

@Component//스캔이 되어야 하기 때문에 이걸 사용
public class AuthoCheckInterceptor implements HandlerInterceptor {

	@Override
	public boolean preHandle(HttpServletRequest request,
			HttpServletResponse response, 
			Object handler)
			throws Exception {
		
		HttpSession session =request.getSession(false);
		if(session!=null) {
			Object authInfo=session.getAttribute("authInfo");
			if(authInfo!=null) {
			return true;
			}
		}
		response.sendRedirect(request.getContextPath()+"/login.do");
		return false;
	}

}

```



UserController.java에서 

```java
	@RequestMapping("/list.do")
	public ModelAndView listUser(HttpSession session) {
		ModelAndView mav=new ModelAndView();
		List<UserVO> userList=null;
		//if(session.getAttribute("authInfo")!=null) {
		userList=service.findUserList();
		mav.addObject("users",userList);//앞에 따옴표 있는 것을 실제 list.jsp에 불러오는 
		//c:forEach var="user" items="${users}" 에서 items안에 들어가는 값 
		mav.setViewName("userList");
//		}else {
//			mav.setViewName("redirect:/login.do");
//		}HnandlerIntercepter설정시 이 부분은 필요없다
		return mav;
	}
```

바꾼 뒤 logout 상태에서 list로 가면 자동으로 login.do로 가는 것을 확인한다



# Json 응답과 요청 처리

http://www.json.org/json-ko.html

를 참고하면 정확한 문법을 알 수 있다.

사용 전 pom.xml 에 json core 2.9.4를 추가하자

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

      <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-web</artifactId>
<version>${spring.maven.artifact.version}</version>

</dependency>
  <dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>${spring.maven.artifact.version}</version>
</dependency>


<!-- 파일 업로드를 위한 추가 -->
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.2.1</version>
</dependency>

<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>1.4</version>
</dependency>
<!-- Json 사용 위한 추가 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
    <version>2.9.4</version>
</dependency>

<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
<artifactId>jackson-databind</artifactId>
<version>2.9.4</version>
</dependency>

    
  </dependencies>
  <build>
    <finalName>spring.web</finalName>
  </build>
</project>

```

action-servlet.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:jee="http://www.springframework.org/schema/jee"
	xmlns:mvc="http://www.springframework.org/schema/mvc"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xsi:schemaLocation="http://www.springframework.org/schema/jee http://www.springframework.org/schema/jee/spring-jee-4.3.xsd
		http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc-4.3.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
<context:annotation-config/>
<context:component-scan base-package="lab.spring.web"/>

<!--  Handler mapping bean설정( DefaultAnnotationHandlerMapping)
기본 HandlerMapping이므로 빈 설정 파일에 별도로 선언할 필요 없으나, 다른 HandlerMapping과 함께 사용한다면 선언
해야 한다. -->

<!--  ViewResolver Bean 설정 -->
<beans:bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <beans:property name="prefix" value="/WEB-INF/view/"></beans:property>
    <beans:property name="suffix" value=".jsp"></beans:property>
  </beans:bean>
  <!-- db연동과 함께 sqlSessionfactory bean -> sqlSessio Templete -> sqlSession 을 UserManagerDAO에 주입 -->

<!-- jNDI 기반이 설정 설정 예시 -->
<jee:jndi-lookup jndi-name="jdbc/oracle" id="dataSource" resource-ref="true"/> 

<beans:bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
  <beans:property name="dataSource" ref="dataSource" />
  <beans:property name="mapperLocations" value="classpath*:lab/mybatis/mappers/*.xml" />
</beans:bean>

<beans:bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
  <beans:constructor-arg index="0" ref="sqlSessionFactory" />
</beans:bean>

<mvc:annotation-driven> <!-- 이렇게 하면 자동으로 HandlerAdaptor가 자동으로 추가된다. -->
  
  <mvc:message-converters>
  <beans:bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"/>
  </mvc:message-converters>
  </mvc:annotation-driven>
  
  <beans:bean id="messageSource"
   class="org.springframework.context.support.ResourceBundleMessageSource">
   <beans:property name="basenames">
   <beans:value>messages.validation</beans:value>
   </beans:property>
   </beans:bean>
   
  <!-- 파일업로드 위한 multipartResolver를 이용한다. 스프링 bean이다. --> 
   <beans:bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
    <beans:property name="maxUploadSize" value="1000000" />
</beans:bean>
  
  <mvc:interceptors>
  <mvc:interceptor>
   <mvc:mapping path="/list.do"/>
   <beans:bean id="authCheckInterceptor" class="lab.spring.web.interceptor.AuthoCheckInterceptor"></beans:bean>
  </mvc:interceptor>
  </mvc:interceptors>
  
</beans:beans>



<!--  Controller Bean 설정(자동으로 스캔에서 되도록 설정할것이다. 위에 context scan추가로) -->


```

이 곳에 모든 앞에 beans 를 붙여주자 (namespaces 에서 beans추가)





@Controller 를 @RestController로 바꿔준다 UserController.java에서

```java
package lab.spring.web.controller;

import java.util.ArrayList;
import java.util.List;

import javax.naming.directory.SearchControls;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.SearchVO;
import lab.spring.web.model.UserVO;
import lab.spring.web.model.UserValidator;
import lab.spring.web.service.UserService;

@RestController
public class UserController {

	
	@Autowired
	UserService service;
	
	
	
	
	@RequestMapping(value="/add.do",method=RequestMethod.GET)
		public  String form() {
			return "userForm";
		}
//	
//	@RequestMapping(value="/add.do",method=RequestMethod.POST)
//	public ModelAndView userCreate(UserVO user) {
//		ModelAndView mav=new ModelAndView();
//		service.addUser(user);
//		
//		
//		mav.setViewName("redirect:/list.do");
//		
//		return mav;
//	}
//	@RequestMapping(value="/list.do",method=RequestMethod.GET)//애는 왜 GET이지???
//	public ModelAndView userlist() {
//		ModelAndView mav=new ModelAndView();
//		
//		List<UserVO> list=service.findUserList();
//		mav.addObject("list",list);
//		mav.setViewName("userList");//setViewName을 통해 뷰의 이름을 지정할 수 있다.
//		
//		return mav;
//		
//	}
	
	@RequestMapping(value="/add.do",method=RequestMethod.POST)
	public ModelAndView addUser(@ModelAttribute("user")UserVO vo
			, BindingResult rs) {//에러를 상속받아 
		ModelAndView mav=new ModelAndView();
		new UserValidator().validate(vo, rs);
		if(rs.hasErrors()){//에러 메시지를 윗 줄에서 확인해서 만약 있다면
			mav.setViewName("userForm");
		}else if(service.addUser(vo)>0) {
			mav.setViewName("redirect:/list.do");
		}else {
			mav.setViewName("redirect:/login.do");
		}
		return mav;
	}
	
	/*
	 * @ModelAttribute("searchConditionList")//requestMapping보다 먼저 수행된다
	 * ModelAttribute 보다. public ArrayList<SearchVO> makeSearchConditionList(){
	 * ArrayList<SearchVO> searchConditionList = new ArrayList<SearchVO>();
	 * searchConditionList.add(new SearchVO("userid","아이디"));
	 * searchConditionList.add(new SearchVO("username","이름"));
	 * searchConditionList.add(new SearchVO("email","이메일")); return
	 * searchConditionList;
	 * 
	 * 
	 * 
	 * 
	 * }
	 */
	@ModelAttribute("searchConditionList")

	public ArrayList<SearchVO> makeSearchConditionList() {

		ArrayList<SearchVO> searchConditionList = new ArrayList<SearchVO>();

		searchConditionList.add(new SearchVO("userid", "아이디"));

		searchConditionList.add(new SearchVO("username", "이름"));

		searchConditionList.add(new SearchVO("email", "이메일"));

		return searchConditionList;

	}
	
	
	
	@RequestMapping("/listJson.do")
	public ArrayList<UserVO> listUser() {
//		ModelAndView mav=new ModelAndView();
		ArrayList<UserVO> userList=null;
		//if(session.getAttribute("authInfo")!=null) {
		userList=(ArrayList)service.findUserList();
//		mav.addObject("users",userList);//앞에 따옴표 있는 것을 실제 list.jsp에 불러오는 
		//c:forEach var="user" items="${users}"  에서 items안에 들어가는 값 
//		mav.setViewName("userList");
//		}else {
//			mav.setViewName("redirect:/login.do");
//		}HnandlerIntercepter설정시 이 부분은 필요없다
//		return mav;
		return userList;
	}
	
	@RequestMapping(value="/search.do",method=RequestMethod.GET)
	public ModelAndView search(@RequestParam("searchCondition")String condition,
								@RequestParam("searchKeyword")String keyword) {
		ModelAndView mav=new ModelAndView();
		List<UserVO> userList=null;
		userList=service.findUser(condition,keyword);
		mav.addObject("users",userList);
		mav.setViewName("userList");
		return mav;
	}
	
//	@RequestMapping(value="/modify.do",method=RequestMethod.GET)
//	public  String modify() {
//		return "user_modify";
//	}
	
	
	
	@RequestMapping("/view.do")
	public ModelAndView updateUser(@RequestParam("userid")String uid) {
		ModelAndView mav=new ModelAndView();
		UserVO vo=null;
		vo=service.findUser(uid);
		mav.addObject("user",vo);
		mav.setViewName("user_modify");
		return mav;
		
		
	}
	
	@RequestMapping("/update.do")
	public ModelAndView updateUser(@ModelAttribute("user")UserVO user) {
		ModelAndView mav=new ModelAndView();
		int vo=0;
		vo=service.updateUser(user);
		if(vo>0) {
			mav.setViewName("redirect:list.do");
		}else {
			mav.setViewName("redirect:login.do");
		}
		return mav;
	 
	}
	
	@RequestMapping("/remove.do")
	public ModelAndView dropUser(@RequestParam("userid")String uid) {
		ModelAndView mav=new ModelAndView();
		if(service.removeUser(uid)>0) {//버튼의 이름 onclick=과 같은 이름
			mav.setViewName("redirect:list.do");
		}else {
			mav.setViewName("redirect:login.do");
		}
		return mav;
	}
	
	
	
}

```

list.do부분을 listJson.do로 바꾸어 주자.



# Transaction 처리

