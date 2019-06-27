# JSP와 서블릿(survlet)

#### 참고 

Servlet 3.1 API - Apache Tomcat 8.0.53 나 다른 것을 참고하자

#### 네트워크

1. 사전적 의미로는 망형 조직
2. 일상적으로 사용하고있는  네트워크 응용 서비스의 한 종류로  TCP/IP라고 하는 통신 프로토콜 기반
3. 일종의 규약으로 서로 다른 언어를 사용하더라도 소통 가능

#### 네트워크>>> TCP/IP

- TCP/IP(Transmission Control Prorocol/Internet Protocol)는 컴퓨터 통신을 위한 프로토콜 중 하나로 우리가 사용하는 인터넷의 기반이다.

- TCP/IP가 인터넷의 기반 프로토콜이 된 이유는 하드웨어, 운영체제, 접속 매체와 관계없이 동작할 수 있는 개방형 구조이기 떄문

- TCP/IP 는 보다 큰 네트워크 프로토콜 개념인 OSI 7 Layer 에서 유래한 것으로 복잡성을 단순화 한 4계층 구조이다.

#### 도메인 이름

- ip주소를 알기 쉬운 이름으로 바꾼 것
- DNS(Domain Name System)서버 필요

#### 인터넷

Internet -일반적으로 알고 있는 인터넷

internet-내부 네트워크 의미

| 이름   | 프로토콜       | 포트       | 기능                    |
| ------ | -------------- | ---------- | ----------------------- |
| www    | http           | 80         | 웹서비스                |
| Email  | SMTP/POP3/IMAP | 25/110/114 | 이메일 서비스           |
| FTP    | ftp            | 21         | 파일 전송 서비스        |
| telnet | telnet         | 23         | 원격 로그인             |
| DNS    | DNS            | 83         | 도메인 이름 변환 서비스 |
| News   | NNTP           | 119        | 인터넷 뉴스 서비스      |

#### 웹 서버 클라이언트

#### HTML 클라이언트 기술

- HTML으로 웹 서비스 적용시
  - 정적서비스로 동적은 처리하기 힘듬.
  - www를 통해 서비스하는 모든 내용은 HTML로 표시해야함
  - 동적요청 처리 후 결과는 html로 생성해서 응답해야한다.
- 동적 처리 위해
  - CGI,Fast CGI, PHP,ASP,JSP 등의 기술 사용
  - 가장 처음에 나온것은 CGI다.
- web Server 기능
  - http서비스 에 있는 Http Demon  의 JVM에서 요청받은 것에 맞게 servlet과 jsp로 구성하고 이는 .init()와 .service(),destory()로.........
  - 이를 통합적으로 web server기능과 application기능을 합쳤다 라고 한다.

#### CGI

- 초기 웹 프로그래밍 기술에 사용
- 프로세스 단위로 실행되기 떄문에 사용자 증가하면 성능 저하, 프로세스를 다시 사용 못하기 때문에

#### 서버스크립트 기술

- **ASP**- 웹 서버 페이지로 윈도우 운영체제 기반, 최근에는 .Net플래폼으로 변화 되면서 ASP.Net이라는 이름으로 변경되어 보다 강력해짐
- **PHP** - 오픈소스 프로젝트로 다양한 운영체제와 웹서버를 지원, 초기 서버 스크립트 기술의 대표로 주목받았으나 완전한 프로그래밍 언어가 아닌 관계로 기능확장의 한계
- **JSP**- 서블릿이라고 하는 자바 웹 프로그래밍 기술에 기반,스레드 기반으로 시스템 자원을 절약하고 효육적인 공류가 가능해**최초 요청시 서블릿**으로 컴파일 되어 이후 요청은 메모리에서 처리해 보다 빠른 처리속도 제공.자바언어의 모든 기능 사용 가능해 무한한 확장성 자랑, 효율적인 **공유**가 가능하다

#### servlet 과 jsp

##### 서블릿이란

- 자바를 기반으로 하는 웹 애플리케이션 프로그래밍
- 서블릿 기술에서는 자바 클래스 형태로 웹 애플리게이션을  작성하는데 이를 서블릿 클래스라 지칭
- 규칙을 지켜야 하는데
  1. javax.servle패키지에 속하는 Servlet인터페이스 구현하도록 한다.
  2. doGet또는 doPost라는 메서드 선언하고 호출시 해야할일 작성해야한다.
  3. 동적 HTML문서를 생성해서 웹 브라우저로 보내는 일을  하기 위해서 doGet, doPost메서드에서 파라미터를 두개 지정해야 한다.(`HttpServletRequest req,HttpServletRespons req`) 

##### jsp

- 자바를 기반으로 하는 웹 프로그래밍 기술
- jsp페이지는 서블릿 클래스와는 반대로 HTMl문서 안에 자바 코드가 삽입 되는 구조이다.
- <%로 시작해서%>로 끝나는 태그와 <%=로 시작해서 %>로 끝나는 태그는 문법이 아니라 JSP문법에 속하는 것
- <% 자바 명령문%>
- <%=자바 식%> 작성한다.
- 서블릿 클래스와 달리 컴파일 과정이나 등록 과정이 필요없고, 텍스트 에디터로 소스 코드를 작성해 웹 서버에 속한 디렉터리에 저장하면 된다.

- servlet =java+HTML
- jsp=HTML+java 
- 앞에 것이 메인이 되는 것이라 jsp는 훨씬 쉽다.
- WEBAPP(표준구조)
  - html,js,css,image,jsp
  - WEG-INF(보안폴더,웹 내부에서만 접근가능)
    - classes : 패키지 형태, class
    - lib : 외부 라이브러리 jax파일 저장
    - src : 옵션
    - tld 
    - web.sml : WEBAPP에의 리스너 정보, servlet정보, fliter정보, 전역에러정보, 외부 참조 자원 정보 등을 설정한다. anotation방식으로 사용

- Servlet등록과 매핑이 중요한데 Servlet의 경우 파일의 종류 구분이 불가능 하다. 그렇기에 등록과 매핑 설정을 web.xml이라는 디스크립터 파일에 작성해야 한다. 웹 애플리케이션에 대한 다양한 정보를 설정하는 파일로 **디스크립터 파일**이라고도 하며 WEB-INF폴더에 만들어야 한다.그 내용은..............찾아서 넣도록 하자.(servelt프로그래밍 291page를 참고하자.)

# 시작하기

1. 톰켓 파일의 webapps파일에  web1(이름은 자유롭게)의 폴더를 생성한다

2. 그 안에 WEB-INF 폴더 생성

3. WEB_INF안에 classes 폴더와 lib폴더 생성하고 `C:\Users\student\Downloads\apache-tomcat-9.0.21\apache-tomcat-9.0.21\webapps\ROOT\WEB-INF`아래에 있는 web.xml문서를 복사하여 우리가 만들고 있는 WEB_INF폴더 안에 붙여넣기 한다.

4. 이 상태에서 web1파일안에 index.html파일을 만들어보자. 그리고 톰캣을 startup window문서를 실행하고 브라우저에서 http://localhost:8080/web1/ 을 실행하면 만들어 놓은 html파일이 자동으로 실행됨을 알 수있다.

   - 자동으로 실행되는 것은 톰캣의 conf파일의 web.xml문서를 실행하면 아래의 것을 볼수 있다.

   - <welcome-file-list>

     <welcome-file>index.html</welcome-file>

     <welcome-file>index.htm</welcome-file>

     <welcome-file>index.jsp</welcome-file>

     </welcome-file-list>

     </web-app> 

     - 그렇기에 자동으로읽는 것이다. 다른 이름으로 실행하고 싶으면 오버라이드 하여 바꾸면 된다.

- 이렇게 만드는 것은 root에서 읽는 것과 다른 서버를 만들기 위해서이다........????????????

### 서블릿 만들어보자

1. client 에서 localhost:8080/web1/hello로 요청하고 싶다. 이는 webserver 에서 webContainer.JVM에서 처리한다.그 안에는 HttpServletRequest와 HttpServletResponse가 있다.
2. 모든 정보는 HttpServletRequest에 저장되어 넘어온다.
3. 그리고 HttpServletResponse에 변환되어 응답한다.

java파일을 수동으로 만들어 보자.

```java
package lab.web.controller;
public class HelloServlet extends HttpServlet{
    public static void main(String[] args){
        public void init(){//override하지 않으면 부모의 init()수행,
        //서블릿이 요청되어서 컨테이너 메모리에 생성될떄 1번만 수행
            System.out.println("inin():초기화");
        }
        public void service(HttpServletRequest req,HttpServletRespons req)throws ServletException, IOException//오버라이드며 꼭 인수는 두개를 해주어야 한다.
        {//서블릿이 요청시마다 반복적으로 수행

        }
        public void destory(){//서블릿이 컨테이너로부터 소멸될떄 1번만 수행
        System.out.println("destroy():컨테이너 종료 또는 GC될떄 수행");

        }
    }

}
```

저장시 

`web1/WEB-INF/src/lab/web/controller/HelloServlet.java`로 저장한다. 중간에 없는 파일은 새로 만들어 주어야 한다. 

이것의 class 파일을 만들기 위해서는  

먼저 설정을 한다

web1 파일 밑의 WEB-INF파일 아래 web.xml 을 열고 편집을 한다

 </description>

<servlet>

  <servlet-name>Hello</servlet-name>

  <servlet-class>lab.web.controller.HelloServlet</servlet-class>

  </servlet>

  <servlet-mapping>

  <servlet-name>Hello</servlet-name>

  <url-pattern>/hello</url-pattern>

  </servlet-mapping>

</web-app>

이 내용을 마지막에 넣어주자 그 후

1. 먼저 cmd 창을 열고
2. cd 'C:\apache-tomcat-9.0.21\apache-tomcat-9.0.21\webapps\web1\WEB-INF\classes\lab\web\controller' java 파일을 저장한 위치의 경로를 입력한다
3. 엔터 후 `javac -classpath .;C:\apache-tomcat-9.0.21\apache-tomcat-9.0.21\lib\servlet-api.jar -d ../../../../classes/ HelloServlet.java ` 를 입력한다. 이것은 class파일을 만들기 위함이다. 루트는 자신의 루트를 작성하면 되며 자신에게 맞게 변형시키자.

# 

### 서블릿 이클립스로 실행해보기

1. file -swith workplace 해서 새로운 루트를 만들자(넘어가도 상관없다.)
2. file-new-Dynamic web project 클릭
3. 이름 설정 후 Target runtime은 저장한 톰캣 버전을 눌러 주는데 나는 apache tomcat v9.0이다.
4. Dynamic web module version은 최신일수록 4이다. 4.0눌러주자.
5. 이클립스로 톰캣 연결 을위해서
6. web1(만들어놓은 daynamic web project이름)에 WebContet오른쪽 버튼을 눌러 new-Html파일을 클릭 이름은 아까 만들었던 index.html로 해보자. body에 내용을 쓰고 run as - 하고 next(...?) 하고 server에 추가한다........maybe? 이러면 알아서 bulidpath생성된다.
7. 그 후 java Resources에 src에 패키지 lab.web.controller로 만든후 servlet에 내용 추가를 하자. 이름 명을 정하고 url mapping도 정할 수 있으며 생성 메서드도 만들수 있다.

```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HeeloServlet
 */
@WebServlet("/hello")
public class HeeloServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HeeloServlet() {
        super();
        System.out.println("HeeloServlet() called!");
    }

	/**
	 * @see Servlet#init(ServletConfig)
	 */
	public void init(ServletConfig config) throws ServletException {
		System.out.println("init() called! - 서브릿 초기화");
	}

	/**
	 * @see Servlet#destroy()
	 */
	public void destroy() {
		System.out.println("destory()() called! - 컨테이너로부터 서블릿 제거될때");
	}

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		  out.print("<html>");
          out.print("<head><title>HelloServlet</title></head>");
          out.print("<Body>");
          out.print("Hello요청에 대한 Servlet응답<br>");
          out.print("서블릿입니다.");
          out.print("이클립스에서 실행중입니다.");
          out.print("</body></html>");//응답할것을 일일이 작성해여한다. 
          //System.out.println("service() 메서드 호출!");
	}

}

```

`response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();` getWriter()전에 setContentType("text/html;charset=utf-8")호출이 필수다. 한글이 포함된 html사용하기 위해서

### jsp파일 만들어보기

이번에는 톰캣에 직접 파일넣어 실행해 보자.

위치는 web1아래 에 저장하고 저장명이 hello.jsp였으므로

브라우저 실행시 http://localhost:8080/web1/hello.jsp로 확인해 본다.(이클립스의 톰캣 실행은 끈다. 충돌 일어날 수 있다.)

jsp는 <%@ page로 시작한다. contentType 의 속성을 지정해 주고 좌르륵 작성해 준다.



```jsp
<%@ page contentType="text/html;charset=utf-8" %> 
<%@ page import="java.util.Date"%>
<%-- jsp주석: HTML태그 +java코드 포함 --%>
<html>
    <head>
        <meta charset="utf-8">
        
        <title>hello.jsp</title></head>
    <body>
        처음 만들어보는 jsp페이지다.
        <%
        //자바 코드 영역
        Date now=new Date();
        out.println(now);
        %>
    </body>
</html>

```

`C:\apache-tomcat-9.0.21\apache-tomcat-9.0.21\work\Catalina\localhost\web1\org\apache\jsp`루트에 가면 자동으로 init() server()destory()됐음을 저 루트에 있는 hello.jsp파일을 실행해 보면(visual studio code로)확인 가능하다.

### jsp를 이클립스에서

webContent파일에 new-jsp 로 만든다.

기본적으로 쓰여있기에 utf-8만 고친후

```jsp
<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello.jsp</title>
</head>
<body>
이클립스에서 만든 hello.jsp 페이지확인
<%
Date now=new Date();//오류뜨기에 util로 import하자
out.println(now);
%>
</body>
</html>
```

작성해서 run as 하면 실행된다.



오늘 배운 것은 

1. servlet생성
2. web.wml에 Servlet설정
3. @webServlet사용해서 Servlet 설정
4. jsp페이지 생성
5. 실행 결과 확인





### 지도 표시해보자

1.위도 경도 표시

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
 <script>
 function showPosition(pos){
     document.getElementById("demo").innerHTML="위도: "+pos.coords.latitude+"<br>경도: "+pos.coords.longitude
 }
 function locationEventHandler(){
     if(navigator.geolocation){
         navigator.geolocation.getCurrentPosition(showPosition);
     }else{
         document.getElementById("demo").innerHTML="브라우저가 Geolocation을 지원하지 않는다.";
     }
 }
 </script>
    <title>Document</title>
</head>
<body>
    <p>현재 위치가 궁금한가?</p>
    <button onclick="locationEventHandler()">위도/경도</button>
    <p id="demo" ></p>
</body>
</html>
```

2. 현재위치 표시해보자

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script  src="https://maps.googleapis.com/maps/api/js?key=복붙할 위치!"></script>
    <title>Document</title>
    <script>
    var myCenter=new google.maps.LatLng(37.498146,127.027557);
    function myMap(){
        var mapProp={center:myCenter, zoom:5,mapTypeId:google.maps.MapTypeId.ROADMAP};
        var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
        var marker=new google.maps.Marker({
            position:myCenter,animation:google.maps.Animation.BOUNCE
        });
        marker.setMap(map);
    }
    </script>
</head>
<body>
    <body onload="myMap()">
        <div id="googleMap" style="width:500px;height: 380px;"></div>
        
    </body>
</body>
</html>
```



3. 강남역 표시해보자.

- 구글 APi를 이용하는데 `http://console.developers.google.com`사이트에 접속한 후 로그인, "API 및 서비스사용설정 클릭"
- "MAP JavaScript API"를 선택
- "사용설정 클릭","사용자 인증 정보"에서 "사용자 인증정보 만들기 클릭", "API키 선택" 하여 붙여넣어야한다.

```html
<!DOCTYPE html>


<html lang="en">
<head>
        <script  src="https://maps.googleapis.com/maps/api/js?key=붙여넣기 할 부분!"></script>
    <meta charset="UTF-8">
    <title>Document</title>
    <script>
    function myMap()
  {  
      
      var mapCanvas =document.getElementById("myCanvas");
    var myLatlng=new google.maps.LatLng(37.498146,127.027557);
    var mapOptions={center:myLatlng,zoom:16,mapTypeId: google.maps.MapTypeId.ROADMAP};
    var map=new google.maps.Map(mapCanvas,mapOptions);console.log(map);
    var marker=new google.maps.Marker({
        position:myLatlng,
        map:map,
        draggable:true,
        title:'지하철 강남 역에서 하차'
    });
    var contentString='<div style="width:100px;height:50px;"> 여기서 만나자</div>';
    var infowindow=new google.maps.InfoWindow({
        content:contentString,
        size:new google.maps.Size(200,100)});
        
        
        google.maps.event.addListener(marker,'click',
        function(){
            console.log("aaa");
            infowindow.open(map,marker);
            if(marker.getAnimation() != null){
                marker.setAnimation(null);
            }else{
                marker.setAnimation(google.maps.Animation.BOUNCE);
            }
        });
        
        marker.setMap(map);
      
    }
    
    </script>
   
</head>
<body onload="myMap()">
    <div id="myCanvas" style="width:300px; height:300px;">
    </div></div>
    
</body>
</html>
```





### 정리해보자.

1. hello.jsp요청시 컴파일(.class) -메모리 로딩- 객체 생성- init(),한번만 수행-service()-destory()한번만 수행 하며 container에서 나갈때 . 그래서 2번쨰 요청시 service만 요청된다. (스레드 방식으로 진행되기에 속도가 굉장히 빠르다)



### servlet spec 만들시 준수해야하는 것

1. 패키지 선언

2. 실행을 container가 하기 떄문에 외부에서 접근 가능하게 하기위해서 public class로 선언

3. (자바는 객체지향이기에 상속받으면 된다) HttpServlet 상속 받고

4. life cycle 메서드 override (필요한것만)  반드시 해야하는 것은 service(),doGet(),doPost(),doPut()등 ㄴservice,get,post,put 등 은 방식이기에  하나가 반드시 들어가야 한다. 

   `service(HttpServletRequest request, HttpServletRespose respose) throws ServletException,IOException{}` 을 반드시 선언해주어야 한다.

##### JSP Spec 만들시 준수해야하는 것

1. 정적 페이지 선언 <와 %@은 반드시 붙여 쓰여야 한다. `<%@ page .......%> `



# Servlet

### 개요

1. 프로그램에서 HTML핸들링시 개발과 관리가 어려웠다.
2. JSP스트립팅 기술은 핸들링이 가능하게 했으며 컨텐츠 관리가 쉬워졌지만 관리는 이전보다 어려워졌다.
3. 그래서 MVC패턴이 주목받기 시작했다.
   - 모델 자바클래스(DAO,DO)
   - 뷰(JSP,JSPT)
   - 컨트롤러(서블릿)
4. 장점
   - 자바API모두 사용 가능

### 서블릿 컨테이너

- 서블릿 컨테이너는 ....

### 서블릿 구조

### HttpServleRequest 클래스

- doGet

### header에 포함된 것을 확인해보자(이클립스에서)

`response.setContentType("text/html;charset=utf-8");//응답 받기
		PrintWriter out=response.getWriter();`  응답 받고 불러내기(?)위해서 이 두줄을 꼭 작성해준다.

web Server- Http listner-servlet COntainer JVM -headerinfo 를 가져와서 뽑아내는 것이 밑의 결과이다.

```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Headerinfo
 */
@WebServlet("/header")
public class Headerinfo extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
    public Headerinfo() {
        super();
        // TODO Auto-generated constructor stub
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");//응답 받기
		PrintWriter out=response.getWriter();
		  out.print("<html>");
          out.print("<head><title>Headerinfo </title></head>");
          out.print("<body>");
          out.print("<h3>Request Header정보</h3>");
          out.print("<ul>");
          Enumeration<String> headerName=request.getHeaderNames();
         while(headerName.hasMoreElements()) {
        	 String name= headerName.nextElement();
        	 out.print("<li>"+name+":");
        	 Enumeration<String> values=request.getHeaders(name);
        	 while(values.hasMoreElements()) {
        		 out.print(values.nextElement()+",");
        	 }
        	 out.print("</li>");
         }
         out.print("<li>요청 메소드 :"+request.getMethod() +"</il>");
         out.print("<li>요청한 client의 IP:"+ request.getRemoteAddr()+"</li>");
         out.print("<li>conTextpath:"+request.getContextPath()+"</li>");
         out.print("<li> requestURI"+request.getRequestURI()+"</li>");
         out.print("<li>requestURL"+request.getRequestURL()+"</li>");
         out.print("<li>servlet"+request.getServletPath()+"</li>");
         out.print("</body></html>");
	}

}

```

### post,get 방식으로 아이디와 비밀번호, 그 외를 뽑아와 보자.



우선 html 구성 (이름은 login.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Document</title>
</head>
<body>
    <h3>회원가입 페이지</h3>
    <form id="f1" action="./response" method="post">
    userid:<input type="text" name="userid" ><br>
    password: <input type="password" name="userpwd"><br>
    <input type="hidden" name="address" value="서울"><br>
    관심사항 : <input type="checkbox" name="interest" value="영화">영화 
    <input type="checkbox" name="interest" value="게임">게임 
    <input type="checkbox" name="interest" value="경제">경제 
    <input type="checkbox" name="interest" value="여행">여행 
    <input type="checkbox" name="interest" value="낚시">낚시 
    <input type="checkbox" name="interest" value="등산">등산 <br>

    <input type="submit" value="회원가입">
    <input type="reset"  value="취미"><br>
    
    
    </form>
</body>
</html>
```

 이클립스로 만든 servlet구성(이름은 response.java)

```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/response")
public class response extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
    public response() {
        super();
        // TODO Auto-generated constructor stub
    }

	


	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");//다시 인코딩 위해서 이것을 안하면 깨진다.
		response.setContentType("text/html;charset=utf-8");//응답 받기
		PrintWriter out=response.getWriter();
		  out.print("<html>");
          out.print("<head><title>Headerinfo </title></head>");
          out.print("<body>");
          out.print("<h3>Request로 파라미터 처리</h3>");
          out.print("<ul>");
          out.print("<li> userid:"+request.getParameter("userid")+"</li>");
          out.print("<li> userpwd:"+request.getParameter("userpwd")+"</li>");
          out.print("<li> address:"+request.getParameter("address")+"</li>");
          String interest[]=request.getParameterValues("interest");
          out.print("<li> 관심사항: ");
          for(String inter: interest) {
        	  out.print(inter+", ");
          }
          out.println("</li>");
          out.print("</body>/</html>");
          
		
	}

}

```

실행하기 위해서 이클립스에서

1. webContent 에 html 파일을 붙여넣기해서 넣어주고
2. src안에 java파일의 이름은 ` <form id="f1" action="./response" method="post">` html파일에 미리 저장된 action의 이름으로 지정해 주며 method가 포스트 이므로 post로 해준다. action의 이름으로 mapping을 바꾸어도 된다.

### upload 

1번째 업로드

multipart.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Multi partition 실습</title>
<style>
input{
margin:2px;}
</style>

</head>
<body>
<h2>mutipart/form-data 실습</h2>
<form action="./part" method="post" enctype="multipart/form-data">
<label>작성자 이름: <input type="text" name="nyname"/></label><Br>
<label>작성자 폰 번호: <input type="text name="myphone"/></label><br>
<label>첨부파일 : <input type="file" name="myfile" multiple/></label><br>
<input type="submit" value="전송" />
</form>
</body>
</html>
```



```java
package core;

import java.io.IOException;
import java.util.Collection;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;


@WebServlet("/part")
@MultipartConfig
public class part extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
 
    public part() {
        super();
        // TODO Auto-generated constructor stub
    }


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Collection<Part>parts=request.getParts();
		System.out.println("===========요청 받음==========");
		for(Part part:parts) {
			System.out.print("name: ");
			System.out.println(part.getName());
			System.out.println("[헤더 정보]");
			for(String headerName : part.getHeaderNames()) {
				System.out.println(headerName+":");
				System.out.println(part.getHeader(headerName));
			}
		System.out.println("size: ");
		System.out.println(part.getSize());
		System.out.println("--------------------------");
		}
	}

}

```

System.out.print로 빼는 경우 이클립스 안에서 결과창이 뜬다.

2번째

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>fileupload 실습</title>
<style>
input{
margin:2px;}
</style>
</head>
<body>
<h2>
Fileupload실습
</h2>
<form method="post" action="./load" enctype="multipart/form-data">
작성자<input type="text" name="theAuthor"><br>
나이<input type="text" name="theAge"><Br>
파일<input type="file" name="theFile" multiple><br>
<input type="submit" value="업로드">
</form>
</body>
</html>
```



```java
package core;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collection;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;


@WebServlet("/load")
@MultipartConfig (location ="c:/uploadtest",maxFileSize=1024*1024*5,maxRequestSize=1024*1024*5*5)
public class load extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    
    public load() {
        super();
       
    }

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		request.setCharacterEncoding("utf-8");
        //인코딩시 글자가 깨지는 것을 방지해준다.
		String path="C:/uploadtest";
		File isDir= new File(path);
		if(!isDir.isDirectory()) {
			isDir.mkdirs();
		}
		Collection<Part>parts=request.getParts();
		for(Part part : parts) {
			if(part.getContentType() != null) {
				String fileName=part.getSubmittedFileName();
				if(fileName !=null) {
					part.write(fileName.substring(0,fileName.lastIndexOf("."))+"_"+System.currentTimeMillis()+fileName.substring(fileName.lastIndexOf(".")));
					out.print("<br>업로드한 파일 이름:"+fileName);
					out.print("<br>크기:"+part.getSize());
				}
			}else {
				String partName=part.getName();
				String fieldValue=request.getParameter(partName);
				out.print("<Br>"+partName+":"+fieldValue);
			}
		}
		out.close();
	}

}

```

`PrintWriter out=response.getWriter();` 를 작성후 out.print() 내용을 작성하면 다음 페이지로 넘어갈때 body에 내용이 출력된다.

### Request Dispatcher(요청재지정)

- 클라이언트에서 응답 대신 다른 자원(Servlet,JSP,HTML등)의 수행 결과를 클라이언트 대신에 응답하는 기능으로 redirect방법과 forward방법으로 나뉜다. 

- forword는 동일 서버에서도 동일 웹 애플리케이션의 자원으로만 요청 재지정 가능하다. 클라이언트에서는 요청 재지정됐는지 모른다. 

  - RequestDispatcher 객체의 forward()메서드 사용
  - `RequestDispatcher rd=request.getRequestDispatcher("/루트.html"); rd.forward(request,response);` 

- redirect 는 클라이언트로부터 수행을 요청받은 A가 302응답 코드와 응답할 B자원에 대한 URL정보로 응답한다. 즉 클라이언트는 요청이 재지정된 사실을 알 수 있으며 동일 서버 뿐만이 아닌 다른 웹사이트의 자원으로도 요청 재지정이 가능하다.

  - `response.sendRedirect("루트.html");`

    response.sendRedirect("http://www.naver.com");`

  -  요청 재지정 제한이 없다.

파라미터 추출 해서 request.setAttribute("key",value)에 저장해서 다른 jsp나 다른 subject에 보낼 수 있다.그래서 우리는 응답 내용이 처음에 보낸 메세지와 중간에 추가된 메세지가 합쳐진 것이 나오는지 확인해보자! 

WEBContent가 아닌 WEB-INF아래의 view파일을 하나 생성하고

그 안에 message.jsp와 result.jsp두가지를 만들어 보자.

직접 브라우저에 작성해서 두 파일을 읽으려 하면 보안 문서이기에 읽히지 않지만 불러 오고 싶으므로 그 방법은 아래와 같다.

message.jsp

```java
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>message.jsp</title>
</head>
<body>
<form id ="f1" action="./message" method="post" >
메세지 입력하세요<br>
<input type="text" name="msg" size=100><br>
<input type="submit" value="전송">
</form>
</body>
</html>
```

result.jsp

```java
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>result.jsp</title>
<style>
#blue{color:blue;
font-size:20px;}
#green{color:green;
font-size:20px;}
</style>
</head>
<body>
<h3>전송결과</h3>
message.jsp에서 보낸 파라미터 메시지:
<p id="blue">
<%
out.println(request.getParameter("msg")+"<Br>" );
%></p>
MessageServlet에서 보낸 추가 정보:
<p id="green">
<% 
 String msg2=(String)request.getAttribute("msg2");
out.println(msg2+"<Br>");
%>
</body>
</html>
```



forwardServlet.java

```java
package lab.web.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/message")
public class ForwardServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
   ServletContext sctx;    
   RequestDispatcher rd;
    public ForwardServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다. 파일업로드의 절대경로. 
		rd=sctx.getRequestDispatcher("/WEB-INF/view/message.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
		rd.forward(request, response);
		
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		//추가 정보를 request한거다.
		request.setAttribute("msg2", "akasha.park@gmail.com");
		sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다
		rd=sctx.getRequestDispatcher("/WEB-INF/view/result.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
		rd.forward(request, response);
		
	}

}

```

send.java

```java
package lab.web.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/send")
public class send extends HttpServlet {
	private static final long serialVersionUID = 1L;
	ServletContext sctx;    
	   RequestDispatcher rd;
    
    public send() {
        super();
        // TODO Auto-generated constructor stub
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		//추가 정보를 request에 저장
		request.setAttribute("msg2", "thdusin@naver.com");
		sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다
		rd=sctx.getRequestDispatcher("/WEB-INF/view/result.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
		rd.forward(request, response);
		
		
	}


	

}

```

forwardServlet.java와 send.java는 다른 페이지이지만 결과페이지는 result로 보아진다. 이를 확인해 보자. 또한 추가되는 내용도 다르게 된다. 그 다름또한 확인해보자.





#### 상태정보 관리

웹의 통신 프로토콜은 요청-응답 프로토콜인데 웹브라우저에서 웹서버에 정보를 요청하면서 만들어진 결과물을 **상태 정보**라 한다.예를 들어 로그인 할때의 사용된 회원 아이디 , 비밀번호 등이다. HTTP프로토콜은 기본적으로 Stateless라 정보를 저장하지않지만 유지해야하는 정보가 필요한 경우가 있다. 상태 정보 유지가 필요한데 방법은 총 4가지로

1. Cookie기술을 이용한 방법
2. HttpSession기술 이용
3. URL문자열 뒤에 추가하는 방법-정보유지 일회
4. < form>태그의 hidden타입을 사용하는 방법-정보유지 일회

- 쿠기 정보는 각 클라이언트별 상태 정보를 브라우저 안에 저장하는 것으로 중요 정보는 저장하면 안된다. 저장위치가 클라이언트이므로 웹서버에 부담이 없다



### 쿠기 정보를 확인하자

CookieLoginServlet.java

```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/cookieLogin")
public class CookieLoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	String uid=null,passwd=null;
	ServletContext sctx=null;
	RequestDispatcher rd=null;
	
    public CookieLoginServlet() {
        super();
        // TODO Auto-generated constructor stub
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		//get 방식으로 접근하는 경우에 쿠키를 체크한다.
		Cookie cookies[]=request.getCookies();
		if(cookies!=null) {
			for(int i=0;i<cookies.length;i++) {
				String name=cookies[i].getName();
				if(name.equals("userid")) {
					uid=cookies[i].getValue();
					//System.out.println(uid);
				}
				
			}
			request.setAttribute("userid", uid);
		}
		sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다
		rd=sctx.getRequestDispatcher("/cookie_login.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
		rd.forward(request, response);
	
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		uid =request.getParameter("userid");
		passwd=request.getParameter("passwd");
		String useCookie=request.getParameter("cookie");
		
		if(useCookie!=null) {
			Cookie uidCookie=new Cookie("userid",uid);
			uidCookie.setMaxAge(60*60*24*365);//365일 동안 저장한다는 뜻
			response.addCookie(uidCookie);
		}
		if(uid.equals("admin")&&passwd.equals("1234")) {//DB연결을 안했기 때문에 강제적으로 정해주었다. 로그인 가능 아이디와 비밀번호를 
			request.setAttribute("userid", uid);
			sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다
			rd=sctx.getRequestDispatcher("/main.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
			rd.forward(request, response);
		}else {
			out.println("<script>");
			out.println("alert(\'아이디 또는 비밀번호 오류입니다.\')");
			out.println("location.href=\"./cookie_login.jsp\"");
			out.println("</script>");
		}
	}

}

```

cookie_login.jsp 

```
<%@ page contentType="text/html; charset=utf-8" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>사용자 로그인</title>
</head>
	
	<body><h3 id='header'>사용자 로그인</h3>
	<div id='main' style='text-align:center'>
		<br><br> 
		<form method=post action="cookieLogin">
		<table style='border:1px #0000FF dotted;text-align:center'>
		  <tr><td>사용자 ID </td>
		     <%
		     if(request.getAttribute("userid")==null){
		    %>
		    <td><input type=text name=userid></td></tr>
		    <%}else{
		    String uid=(String)request.getAttribute("userid");
		   %>
		    <td><input type=text name=userid value="<%=uid%>"></td></tr> 
		     <%} %>
		  
		    
		  <tr><td>사용자 암호 </td>
		    <td><input type=password name=passwd></td></tr>
		  <tr><td>아이디 저장 사용 </td>
		    <td><input type=checkbox name=cookie></td></tr>			
		  <tr><td colspan=2 style='text-align:right'>
			<input type=submit value='로그인'>
			<input type=reset value='취소'></td></tr>
		</table>
	</form></div></body></html>
```

main.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<%=request.getAttribute("userid") %>님 환영합니다.<br>
<a href="cookieLogout"><button>로그아웃</button></a><br>
</body>
</html>
```

CookieLogoutServlet.java

쿠기 정보를 삭제하는 것을 작성해 보았다.



```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/cookieLogout")
public class CookieLogoutServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
      ServletContext sctx=null;
      RequestDispatcher rd=null;
   
    public CookieLogoutServlet() {
        super();
        
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html);charset=utf-8");
		PrintWriter out=response.getWriter();
		Cookie[] cookies=request.getCookies();
		if(cookies!=null) {//쿠기 값이 있다면
			for(int i=0;i<cookies.length;i++) {
				if(cookies[i].getName().equals("userid")) {
					cookies[i].setMaxAge(0);//이것은 쿠키값을 삭제하는 것!!
					response.addCookie(cookies[i]);//삭제된 쿠키값 돌려놓기
					
				}
			}
		}
		sctx=request.getServletContext();
		rd=sctx.getRequestDispatcher("/logout.jsp");
		rd.forward(request, response);
		
	}

}

```

logout.jsp

```java
<%@ page contentType="text/html; charset=utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<script>
alert("로그아웃 되었습니다. \n 쿠기 정보 삭제되었다/.")
location.href="./cookie_login.jsp";
</script>
</body>
</html>
```



