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

##### 서블릿(자바클래스에 웹 어플리케이션 작성)

- 자바를 기반으로 하는 웹 애플리케이션 프로그래밍
- 서블릿 기술에서는 자바 클래스 형태로 웹 애플리게이션을  작성하는데 이를 서블릿 클래스라 지칭
- 규칙을 지켜야 하는데
  1. javax.servle패키지에 속하는 Servlet인터페이스 구현하도록 한다.
  2. doGet또는 doPost라는 메서드 선언하고 호출시 해야할일 작성해야한다.
  3. 동적 HTML문서를 생성해서 웹 브라우저로 보내는 일을  하기 위해서 doGet, doPost메서드에서 파라미터를 두개 지정해야 한다.(`HttpServletRequest req,HttpServletRespons req`) 

##### jsp(html문서 안에 자바코드 삽입)

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

4. 이 상태에서 web1파일안에 index.html파일을 만들어보자. 그리고 톰캣 아래 bin폴더 아래  startup window문서를 실행하고 브라우저에서 http://localhost:8080/web1/ 을 실행하면 만들어 놓은 html파일이 자동으로 실행됨을 알 수있다.

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

### JSP Spec 만들시 준수해야하는 것

0

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

  ```java
  ServletContext sc=request.getServletContext();
  
  RequestDispatcher rd=request.getRequestDispatcher("/요청 재지정 자원 경로와 루트.html");
  
  request.setAttribute(key,value);
  
  rd.forward(request,response);
  ```

  

  - url주소 표현은 **처음** 요청한 Servlet이나 JSP

- redirect 는 클라이언트로부터 수행을 요청받은 A가 302응답 코드와 응답할 B자원에 대한 URL정보로 응답한다. 즉 클라이언트는 요청이 재지정된 사실을 알 수 있으며 동일 서버 뿐만이 아닌 다른 웹사이트의 자원으로도 요청 재지정이 가능하다.

  - `response.sendRedirect("루트.html");`

    `response.sendRedirect("http://www.naver.com");`(http:로 시작하거나 ./상대경로로 지정하거나, /인 root context로부터 시작하는)

    - 최초 요청시 컨테이너가 생성한 request와 response는 소멸되고 , 새로운 request와 response객체가 redirect된 redirect된 자원으로 get 방식으로 전달(이때는 setAttribute로 저장못함)
  
  - 동일한 웹 컨텍스트 , 웹 서버 내 공유할 정보(는 대게 상태 정보 ,클라이언트)는 전달하기 위햇 HttpSession.setAttribute(key.value) 또는 ServletContext.setAttribute(key,value)를 사용한다.
  
  - 요청 재지정 제한이 없다.
  
  -  url주소 표현은 **최종** 요청이 전달된 Servlet이나 Servlet이나 JSP또는 웹 서버의 주소

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



# 지금까지의 내용 한번 정리

- http 요청 메세지로부터 헤더정보 추출?

1. http://ip:port/web1/header 요청 => @WebServlet("/header")

2. HttpServletRequest.getHeaderName():Enumeration< String>
3. Enumeration.hasMoreElement() : boolean
4. Enumeration.nextElement():String
5. HttpServletRequest.getHeader(): header이름으로 저장된 value를 반환(String)
6. HttpServletRequest.getHeaders():header이름으로 저장된 value가 하나 이상이면 반환

- http 요청 메시지를 번송한 클라이언트 ip정보 추출?1. HttpServletRequest.getRemoteAddr()
- http 요청 메시지를 전송한 방식 정보 추출?
  1. HttpServletRequest.getMethod()
- WAS가 서비스하는 웹 컨텍스트를 생성하면 웹 컨텍스트를 추상화한 객체: Servlet
- 요청한 웹 컨텍스트의 객체를 반환하는 메서드
  - HttpServletRequest.getServletContext()
- 클라이언트가 form태그내에 data를 서버 웹 컴포넌트로 전송, 서버 웹 컴포넌트에서 클라이언트가 보낸 form데이터를 추출하려면?
  - HttpServletRequest.getParameter("input요소의 name속성값 이 와야한다.")
- checkbox input요소(여러 속성이 다양한 이름속성을 가진다. String[] 반환이다.checked된 요소가 다양하기 때문에 이 value들을 추출하려면 
  - HttpServletRequest.getParameterValues("input 요소의 name속성값")

예를 들어보자.

1. memberform.html요청(단순페이지요청:GET방식

2. HttpListener가 html페이지 응답

3. 클라이언트가 데이터 입력하고 form data전송

   < form acton="./join" method=" " encType="multipart/form-data "에 선언되는 속성값도 외워야한다.>

4. @WebServlet("/join") 선언된 서블릿이 요청받는다.

5. 파일업로드에 처리하는 서블릿에 선언한 Annotation은?

   - @MultipartConfig(location=" ",masFileSize="" 기본이 byte크기,maxRequestSize="") 

6. 업로드된 파일의 메타정보, 스트림등을 추출하기 위해 반환 객채? 

   - HttpServletRequest.getPart() : 하나의 part객체 리턴
   - HttpServletRequest.getParts(): 여러개의 part객체를 Coolection< Part>에 담아서 리턴
   - Part.getName():업로드된 파일 이름 반환
   - Part.getContenType() :업로드된 파일의 내용 유형 반환
   - Part.getSize(): 업로드된 파일 크기 반환
   - Part.write(): 업로드된 파일을 @MultipartConfig의 location에 출력(서버에 파일로 기록)을 해야 파일로 저장되는데 이때사용하는 메서드

**요청을 동일한 웹 컨텍스트의 다른 Servlet또는 jsp에 전송가능**

1. ServletContext sc=ruquest.getServletContext()*;//요청 웹 컨텍스트를 받는다.
2. RequestDispatcher rd=sc.getRequestDispacher*("/다른 servlet이나 jsp경로") 현재 웹 사이트 아래라는 뜻의 /꼭 넣어준다.다른 Servlet이나 jsp의 경로(보내기위해서)sc는 컨텍스트에 요청할 경로의 대한 정보를 가지고 있기 때문에 sc에서 불러온다.
3. rd.forward(request,response)-요청을 다른곳에 보내기위해서이며 추가적인 정보를 request에 저장할 수 있는데  HttpServletRequest.setAttribute(키로 사용될 객체, 키로 저장될 값 객체로 배열이나 값 가능)로 map구조로 여러개 저장 한다. 꺼내기 위해서는 HttpServletRequest.getAttribute(키); 이며 Object로 반환되므로 실제 저장한 타입으로 DownCasting해주어야 한다. 
4. rd.include()-

< a href="./xxx">요청전달< /a> 전송 방식은 Get방식으로 ./xxx?parmeterName=parameterValue&....의 방식으로 전달된다. url에 붙어서

**Http 특성**

1. 요청을 보낼때 Connection 되고, 응답이 전송되고 나면 disconnect된다.=비 연결형 프로토콜(protocol)
2. 상태정보를 저장할 방법
   1. 클라이언트 브라우저(key,value) - cookie, setMaxAge()로 유효기간을 지정가능, 브라우저에 저장되므로 브라우저마다 다르다.
   2. url의 쿼리 스트링으로 요청시마다 전송으로 url문자열 뒤에 추가하는 방법
   3. 요청을 전송하는 페이지에 form요소로 < input type="hidden" name="" value=""> 히든 태그로 보내기
   4. 웹 서버에 (자바기반임으로) 객체로 저장:Session , 클라이언트의 브라우저 종료되어 세션이 종료될때 까지만 정보유지

**클라이언트가 특정 웹서버로 (tomcat)로 최초 요청을 전송 하면 응답을 하게 되는데**

1. 웹서버(tomcat)가 클라이언트 요청에 대해 응답을 할때 JSessionID값을 생성해서 쿠키로 전송
2. 클라리언트가 웹 서버로 두번째, 세번째,...요청할때 마다 브라우저 자체적으로 요청웹 서버에서 보내준 쿠기 정보를 찾아서 리퀘스트시마다 전송 
3. 웹 서버의 웹 컴포넌트(서블릿)에서 요청과 함께 넘어온 쿠키정보 추출하려면  
   - HttpServletRequest.getCookies():Cookie[]로 리턴된다.(여러개로 저장된다.)

**new Cookie(key,name) 객체를 응답으로 전송하려면**

- HttpServletResponse.addCookie()를 사용해서 보낸다. 

1. http://ip:poart/web1/cookieLogin 요청(GET방식)
2. @WebServlet("/cookieLogin")서블릿의 doGet() 요청 처리
   - 쿠기 정보 추출 request.getCookies(), userid로 저장된 값 검색(쿠키 배열을 리턴한다.)
   - 추출한 쿠기 정보를 request.setAttribute("userid" 쿠키값);
   - RequestDispatcher를 사용해서 /cookie_login.jsp로 전송 
3. form태그 전송 (action="cookieLogin" method="post")
4. @WebServlet("/cookieLogin")서블릿의 doPost() 요청 처리
   - 로그인 처리
   - 아이디 저장 checkbox선택된 경우 userid를 쿠키로 저장(response에 addcookie)
   - RequestDispatcher를 사용해서 /main.jsp로 전송
5. main.jsp에서 로그아웃 (/cookiLogout) 요청(버튼인데 앵커 태그로 묶었다. GET방식)
6. @WebServlet("/cookieLogout")서블릿의 doGet()에서 요청 처리 
   - 쿠키 정보 삭제  request.getCookies(),쿠키 정보 추출해서 cookie.setMaxage(0)으로 설정(단위는 초단위이다.)
   - RequestDispatcher를 사용해서 다시 로그인 페이지로. 넘기는 방법은 두가지 1. (/cookieLogin) 이나 2.(/cookie_login.jsp)

# Session

### JSESSIONID 

- HttpSession 객체가 생성될 떄 세션 ID가 하나 부여되며 Cookie기술을 이용해서 저장하며 최대 유지 시간은 브라우저 구동 동안이며 또한 일정 시간 동안 응답이 없으면 (기본30분) 서버에 생성된 HttpSession객체는 더이상 사용 못한다.

### 상태정보 유지 과정

- Session객체는 최초 요청시에 웹 컨테이너가 HttpSession구현 객체를 생성
- HttpSession객체 생성,추출
  
- HttpSession session=request.getSession();
  
- HttpSession객체에 상태 정보 보관 객체 등록(한번만 등록한다.)
  
  - session.setAttribute("xx",new data()); 순서는(key,value)이다.
  
- HttpSession객체에 참조값을 얻어 사용(읽기,변경)
  
  - Dage ref
  
- 삭제하기 위해서

  - removeAttribute(key)

- 값을 얻어오기 위해서는

  - getAttribute()

- HttpSession객체에 저장된 JSESSION ID변환 메소드 getSession()

  - getLastAccessTime()

- 클라이언트가 요청하지 않아도 HttpSession을 웹 컨테이너의 메모리에 유지시간 설정 setMaxInactiveInterval(초단위)

- 웹 컨텐스트 전역으로 세션시간 설정은 web.xml에

  ```html
  <session-config>
  	<session-timeout>30</session-timeout>
  	</session-config>
  ```

-  세션에 저장된 상태정보를 삭제하고 세션 객체를 만료시키려면 invalidate()사용

  





### Session확인해보자

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/sessiontest")
public class SessionTestServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    
    public SessionTestServlet() {
        super();
       
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		String command=request.getParameter("comm");
		HttpSession session=request.getSession();
		String msg="";
		long time=session.getCreationTime();//객체가 생성된 시간 추축
		String id=session.getId();//객체의 세션 ID추출
		if(command.equals("view")) {
			if(session.isNew()) {
				msg="세션 객체 생성:";
				
			}else {
				msg="세션객체 추출:";
				
			}
			msg+="<br>id: "+id+"<br>time: "+new Date(time);
		}else if(command.equals("delete")) {
			session.invalidate();//객체 삭제
			msg=id+"을 id로 갖는 세션 객체 삭제";
		}else {
			msg="요청시 Query문자열로 comm=view 또는 comm=delete를"+"전달해주세요!";
		}
		out.print("<h2>"+msg+"</h2>");
		out.close();
	}

}

```

- 브라우저 마지막에 ?comm=view
- ?comm=delete를 작성해 보자 결과값확인!

### 로또 번호 

```java
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/lottolimit")
public class LottoServletLimit extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
    public LottoServletLimit() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		HttpSession session=request.getSession();//HttpSession객체의 세션ID추출
		if(session.getAttribute("lottocnt")==null) {
			session.setAttribute("lottocnt", new int[1]);
		}
		int[] count=(int[])session.getAttribute("lottocnt");
		String msg="";
		if(++count[0]>3) {
			msg="<h3>더이상 응모할 수 없습니다.브라우저를 재시작하여 응모하세요.</h3>";
		}else {
			int answer=(int)(Math.random()*10)+1;
			int input=Integer.parseInt(request.getParameter("guess"));
			if(answer==input){
				msg="<h3>축하합니다. 당첩이예요!</h3>";
				count[0]=4;
			}else {
				msg="<h3><strong>꽝</strong>입니다.</h3><a href='"+request.getHeader("referer")+"'>재도전</a>";
			}
		}
		PrintWriter out=response.getWriter();
		out.print(msg);
		out.close();
	}

}

```

### session에 저장된 아이디 비밀번호 확인

main1.jsp

```html
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<h3>회원전용 페이지</h3>
<%
String uid=null;
uid=(String)session.getAttribute("userid");//세션에 유저아이디를 저장한다.
if(uid!=null){
%>

<%= uid %>님 환영합니다.^^
<a href="cookieLogout"><button>로그아웃</button></a><br>
<img src="./images/dog.jpg"><br>
<%
}else{
%>
 <script>
	alert("회원 전용 페이지입니다.\n 로그인 페이지로 이동합니다.");
	location.href="./cookieLogin";
 </script>

<%} %>

</body>
</html>
```



LoginServlet.java

밑의 두줄을 추가한다.

`HttpSession session=request.getSession();`

`session.setAttribute("userid", uid);`

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
import javax.servlet.http.HttpSession;


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
			uidCookie.setMaxAge(60*60*24*365);
			response.addCookie(uidCookie);
		}
		HttpSession session=request.getSession();//세션에 저장하기 위해 추가했다.
		if(uid.equals("admin")&&passwd.equals("1234")) {
			session.setAttribute("userid", uid);//세션에 저장하기위해 추가했다.
			request.setAttribute("userid", uid);
			sctx=request.getServletContext();//현재 관련된 웹 컨테스트 객체가 리턴된다
			rd=sctx.getRequestDispatcher("/main1.jsp");//직접 요청을 못하고 servlet에서 경유해서 연결되게 요청을 한다.브라우저에 저 상태로 작성하면 직접 접근 못한다.
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



LogoutServlet.java

밑의 세줄을 추가한다.

`HttpSession session=request.getSession();`

`session.removeAttribute("userid");`

`session.invalidate();//세션만료시킴,세션 객체 삭제`

```html
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
import javax.servlet.http.HttpSession;


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
		HttpSession session=request.getSession();
		if(cookies!=null) {
			for(int i=0;i<cookies.length;i++) {
				if(cookies[i].getName().equals("userid")) {
					cookies[i].setMaxAge(0);
					response.addCookie(cookies[i]);
					
					
				}
			}
		}
		session.removeAttribute("userid");
		session.invalidate();//세션만료시킴,세션 객체 삭제
		sctx=request.getServletContext();
		rd=sctx.getRequestDispatcher("/logout.jsp");
		rd.forward(request, response);
		
	}

}

```



# 요청재지정(응답하기)

RequestDispatcher(forward기능으로 요청 재지정)

sendRedirect(redirect기능으로 요청 재지정) 

- ("web url path방식") 
- http://~~~
- ./~
- /web1/xxxx.jsp
- 로 주소지정..?
- 요청과 주소가 일치한다.
- 다른 웹서버,동일서버 등 재지정대상 제한 없다.
- 동일서버에 재지정하면 request,response가 새로 생성된다. 아래 예제로 비교해보자.

위치지정을 c:/testcontent/sample.html 이다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>자바스크립트</li>
        <li>21</li>
        <li>웹앱개발전용OOP언어</li>
    </ul>
</body>
</html>
```

sample.xml

```xml

<textxml>
<name>자바스크립트</name>
<age>21</age>
<kind>웹앱개발 전용 OOP언어</kind>
</textxml>
```

sample.json

```json
{"name":"자바스크립트", "age":21, "kind":"웹앱개발 전용OOP언어"}
```

sample.trans_duke.png로 하나 저장하자.

```java
package core;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet({ "/getHTML", "/getXML", "/getJSON", "/getImage" })
public class ResponseServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
    public ResponseServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	String uri =request.getRequestURI();
	String filename= "";
	String contentType="";
	if(uri.endsWith("getHTML")) {
		filename="c:/testcontent/sample.html";
		contentType="text/html;charset=utf-8";
		
	}else if(uri.endsWith("getXML")) {
		filename="c:/testcontent/sample.xml";
		contentType="text/xml;charset=utf-8";
	}else if(uri.endsWith("getJSON")){
		filename="c:/testcontent/sample.json";
		contentType="text/json;charset=utf-8";
	}else {
		filename="c:/testcontent/trans_duke.png";
		contentType="image/png";
	}
	File f=new File(filename);
	FileInputStream fis=new FileInputStream(f);
	response.setContentType(contentType);
	if(contentType.startsWith("image")) {
		byte[] content=new byte[(int)f.length()];
		ServletOutputStream sos=
				response.getOutputStream();
		fis.read(content);
		sos.write(content);
		sos.close();
	}else {
		InputStreamReader isr=new InputStreamReader(fis,"utf-8");
		BufferedReader br=new BufferedReader(isr);
		PrintWriter out=response.getWriter();
		String line=null;
		while((line=br.readLine())!=null)
			out.println(line);
		out.close();
		br.close();
		isr.close();
	}
	fis.close();
	}

}

```

확장자는 mimetype으로 검색하면 다양하게 알수 있다.

### sendRed

```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/PostServlet")
public class PostServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

    public PostServlet() {
        super();
       
    }


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out=response.getWriter();
		String msg=request.getParameter("msg");
		request.setAttribute("address", "서울시 강남구 역삼동" );//추가정보로 보내려 한다.
		//response.sendRedirect("./postResult.jsp");//이곳에 요청을 전달했따.request,response객체가 새로 생성된다.
		response.sendRedirect("http://www.daum.net");
	}

}

```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
if(request.getParameter("msg")!=null&&request.getAttribute("address")!=null){
	

%>
send.jsp에서 보낸 파라미터 메시지:<%=request.getParameter("msg") %><br>
PostServlet에서 보낸 메시지:<%=request.getAttribute("address") %><Br>
<%
}else{%>
sendRedirect()로 요청을 전달하면,
요청된 페이지에 새로운request와 response객체가 전달되므로<br>
파라미터와 Attribute를 request로부터 추출할 수 없다.<br>
<%
}%>
</body>
</html>
```



### 계산결과를 Ajax로

```html


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>calc.jsp</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
 //action="./CalcServlet"  method="post"
 $(document).ready(function(){
	 $("#f1").submit( function(event){
		 event.preventDefault();
		 var n1 = $("#num1").val();
		 var n2 = $("#num2").val();
		 var op = $("#operator option:selected").val();		 
		  $.ajax( {
			    url  : "./CalcServlet",
			    data : {"num1" : n1, "num2": n2, "operator" : op},
				  success: function(data){ 
					  console.log(data);
					  $("#result").html("<mark>"+n1+op+n2+"="+data+"</mark>");
				  }
		  });
		 
	 })
 });
 
</script>
</head>
<body>
<h3>계산기</h3>
  <form id="f1" >
   number1 :
   <input type="text"  name="num1" id="num1"  ><br>
   operator :
   <select name="operator" id="operator">
   <option value="+">+</option>
   <option value="-">-</option>
   <option value="*">*</option>
   <option value="/">/</option>
   </select>
   <br>
   number2 :
   <input type="text"  name="num2"  id="num2" ><br>
   
   <input type="submit"  value="계산">
  </form>
  <hr>
  계산결과 :  <span id="result"></span>
</body>
</html>
```



```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/CalcServlet")
public class CalcServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public CalcServlet() {
        super();

    }


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/plain;charset=UTF-8");
		PrintWriter out=response.getWriter();
		request.getParameterValues("n1");
		request.getParameter("op");
		String n13=request.getParameter("op");
		String n12[]=request.getParameterValues("n1");
		int outint=0;

		switch(n13){
			case "+": outint=(Integer.parseInt(n12[0])+Integer.parseInt(n12[1]));break;
			case "-": outint=(Integer.parseInt(n12[0])-Integer.parseInt(n12[1]));break;
			case "x": outint=(Integer.parseInt(n12[0])*Integer.parseInt(n12[1]));break;
			case "/": outint=(Integer.parseInt(n12[0])/Integer.parseInt(n12[1]));break;
			}
		out.print(outint);
	
//		ServletContext sc=request.getServletContext();
//		RequestDispatcher rd=sc.getRequestDispatcher("/calcResult.jsp");
//		request.setAttribute("outint", outint);
//		rd.forward(request, response);
//		
	}

}

```

사실 잘 안됐따...한번 해보자...

### 상품 계산하기

```java


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>calc.jsp</title>
  
</script>
</head>
<body>
<h3>계산기</h3>
  <form id="f1" action="./Price" method="post">
  <table>
   <tr><td width=150> 상품명</td><td width=150> 가격</td><td width=150> 수량</td>
   <tr><td>
   <input type="hidden"  name="snak1" id="snak"  value="새우깡" >
   <br>
   <img src="./images/shimp.jpg" width=100 height=100>
   </td>
   <td>
   1500원
   <input type="hidden"  name="price1" id="price"  value="1500" >
   </td>
   <td>
   <select name="qty1" id="qty">
   <option value="0">0</option>
   <option value="1">1</option>
   <option value="2">2</option>
   <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
   </select>
  </td>
  </tr>
   <tr><td>
   <input type="hidden"  name="snak2" id="snak"  value="바나나퀵" >
   <br>
   <img src="./images/banana.jpg" width=100 height=100>
   </td>
   <td>
   1000원
   <input type="hidden"  name="price2" id="price"  value="1000" >
   </td>
   <td>
   <select name="qty2" id="qty">
   <option value="0">0</option>
   <option value="1">1</option>
   <option value="2">2</option>
   <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
   </select>
  </td>
  </tr>
   <tr><td>
   <input type="hidden"  name="snak3" id="snak"  value="칸초" >
   <br>
   <img src="./images/ccancho.JPG" width=100 height=100>
   </td>
   <td>
   1200원
   <input type="hidden"  name="price3" id="price"  value="1200" >
   </td>
   <td>
   <select name="qty3" id="qty">
   <option value="0">0</option>
   <option value="1">1</option>
   <option value="2">2</option>
   <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
   </select>
  </td>
  </tr>
   </table>
   <input type="submit"  value="계산">
  </form>
  <hr>
  계산결과 :  <span id="result"></span>
</body>
</html>
```



# MVC패턴 적용 웹 어플리케이션(JSP)

- 스크립트,HTML태그와 함께 java코드 포함 view와 로직이 분리가 안되서 재사용성이 낮다. 페이지단위기 때문에 빨리 만들 수 있다.
- Servlet->JSP->EJB(망함)-> MVC패턴 적용 웹 애플리케이션 구현(view페이지는 JSP,Controller 는 Servlet으로 만든다.,data영속성과 비지니스로직은 JavaObject로 만든다.)
- 자바코드를 직접적으로 넣는 것을 권장하지 않는다.
- JSP는  MVC구조에서 Veiw로만 제한하며, 태그와 EL(expression L)로만 생성하는 것을 권장

### JSP요소

#### 정적지시자 

- <%@ page~~~%>
  - page처리 정보 전달
  - contentType(mime타입을 설정)
  - text/plain(텍스트만)
  - text/jpeg(이미지만)
  - application/vnd.ms-word등등(워드, 파워포인트 등)
  - text/json 같은것도 있다.
  - session
  - buffer(버퍼늘리기위해 사용)
  - isThreadSafe
  - errorPage
  - isErrorPage
  - info
  - language(디폴트가 자바)
  - import
  - extends
  - isELIgnored
  - deferredSyntaxAllowedAsLiteral(참고만)
- <%@ include~~~%>
  - file <%@ include file="%>
  - 포함될 jsp페이지에서 < html> ,< head> < body>를 제외하고, < body>태그의 내용의 컨텐츠만 포함
- <%@ taglib~~~%>
  - prefix
  - uri
  - <%@ tagilb prefix="" uri="http://java.sun.com/jsp/jstl/~"%>
  - jsp페이지내에 HTML이 아닌 태그를 만나면 태그에 매핑된 javaclass 를 실행
  - JSTL(java Standard Tag Library)을 사용하기 위한 선언, core,sql,xml국제화 format처리 라이브러리 등을 사용하기 위해 선언 한다.

#### 동적 지시자

- <jsp: include ~>< /jsp:include>
- < jsp:useBean~>< jsp:getProperty ~~ >< jsp:setProperty ~~~ >< /jsp:u
- 동적인 요청을 처리하는 JSP를 요청과 응답을 처리하기 위해서 JSP 컨테이너가 서블릿으로 변환하면서 내장 객체들을 생성해서 _jspService()로 전달 추가합니다.
  JSP에서는 내장 객체를 new 로 생성하지 않고 컨테이너가 정의해놓은 이름으로 사용
- request
  - javax.servlet.http.HttpServletRequest
- response
  - javax.servlet.http.HttpServletResponse
- session
  - javax.servlet.http.HttpSession
- application
  - javax.servlet.http.ServetContext
- out
  - javax.servlet.jsp.JSPWriter
- exception
  - java.lang.Throwable
- page
  - java.lang.Object
- config
  - javax.servlet.ServletConfig
- pageContext
  - javax.servlet.jsp.PageContext

#### 내장객체들의 유효 범위(작은범위에서 큰 범위)

- 컨테이너 메모리에 유지되는 범위
- page-현재 jsp페이지가 범위,jsp가 수행되는 동안만 유지
- request- sendRedirect를 이용 get방식으로 보내기 전까지(요청전까지)<jsp:include~><jsp:forward>로 다른 jsp또는 서블릿으로 공유될때
- session- 세션만료 될떄까지, inactive상태에서는 30분
- application-웹 컨텍스트가 웹 컨테이너로부터 삭제될때까지 or 종료될때까지
- page,request,session,application에 정보를 저장, 삭제, 반환 메서드
  - setAttribute()
  - getAttribute()
  - removeAttribute()
  - getAttributeNames()
  - 위의 메서드를 공통적으로 가지고 있다.

##### 내장객체들 확인

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@page import="java.util.Date" %>


<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h2>JSP의 내장 객체들 점검</h2>

getMethod():<%=request.getMethod() %><Br>
getRequestURI() :<%=request.getRequestURI() %><Br>
getHeader("user-agent"):<%= request.getHeader("user-agent") %><Br>
[application]<br>
getContextPath():<%= application.getContextPath() %><Br>
getServletContextName(): <%= application.getServletContextName() %> <br>
getServerInfo() : <%= application.getServerInfo() %><Br>
getMajorVersion() : <%= application.getMajorVersion() %><Br>
getSessionTimeout() : <%= application.getSessionTimeout() %><Br>
[session]<Br>
getId() : <%= session.getId() %><BR>
getCreationTime() : <%= new Date(session.getCreationTime()) %><Br>
[response]<Br>
getStatus() : <%=response.getStatus() %><Br>
getContentType() : <%= response.getContentType() %><Br>
<H4>Web Application(/edu)폴더의 파일 리스트</H4>
<%
java.util.Set<String> list=application.getResourcePaths("/");
if(list !=null){
	Object obj[]=list.toArray();
	for(int i=0;i<obj.length;i++){
		out.print(obj[i]+", ");
	}
}
%>

</body>
</html>
```



##### request내장객체 확인

```html
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<% if(request.getMethod().equals("GET")){ %><!-- 다음페이지로 넘어가기위해? -->
<h2>원하는 컬러와 날짜를 선택하세요</h2>
<form method="post" action="./request내장객체.jsp">
컬러: <input type="color" name="fcolor"><Br>
날짜: <input type="date" name="fdate"><BR>
<input type="submit" value="전송">

</form>
<%}else{ %>
<script>
document.body.style.backgroundColor='<%=request.getParameter("fcolor")%>';
</script>
<h2>선택 날짜는 <%= request.getParameter("fdate")%>이네요..</h2>
<%} %>
</body>
</html>
```



- 자바 코드와 관련된JSP요소

  - ```jsp
    <%! 변수 선언 초기화://
    메서드 정의//
    %>
    <% 
    자바실행문장;//변환된 서블릿에 _jspService()에 포함...
    %>
    <%= 출력내용%>
    <% out.print(출력내용);%>
    ${출력내용
    ```

    
    

- declare scriptlet <%! 전역변수 또는 메서드 정의 %>

  ```jsp
  <%! 변수 선언 초기화; //변환된 서블릿의 멤버변수로 정의 
  
  	  public void method(){
  
     문장;
  
     }//변환된 서블릿의 멤버 메서드로 정의
  
  %>
  ```

  

- scriptlet <% 자바실행 문장 %>

  ```jsp
  <%
  
  		자바실행 문장;//변환된 서블릿의 _service()의 실행문장으로 
  
  ...
      %>
  ```

  

- expression <%= 출력내용 %>

  ```java
  <%= 출력내용 %> //은 <% out.println(출력내용) %>와 동일하다. ${출력내용}과도 동일
  ```

- jsp에는 구현요소가 총 4가지가 있다.
  1. 템플릿 콘텐츠 기반 구현
  2. 스크립트 기반 구현
  3. 액션태그기반 구현
  4. EL기반 구현
  5. JSTL기반 구현

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h2>첫번째 예제</h2>
<h3>Hello Guest! 방문 시간:1시 50분 30초 (시간 고정인 템플릿 콘텐츠 기반구현)</h3><br>
오늘 날짜:<%= java.time.LocalDate.now() %>( 스크립트기반구현)<br> 
<jsp:useBean id="hello" class="jspbean.TestBean"/> 
<jsp:setProperty name="hello" property="name"/>
<h3>Hello<jsp:getProperty name="hello" property="time" />이다.</h3>액션태그기반 구현 <Br>
    <h3>EL기반</h3>
<jsp:useBean id="hello" class="jspbean.TestBean"/> 
<jsp:setProperty name="hello" param="name" property="name"/>
<h3>Hello ${param.name}! 방문시간은 ${ pageScope.hello.time }이다.</h3>EL기반 구현 <Br>
</body>
</html>
```

5. JSTL기반 구현의 경우 c라는 접두어를 붙여 사용한다는 설정이 필요
   - `<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>`





### 한번 확인해보자

```jsp
<%@ page  contentType="text/html; charset=utf-8"%>
<%!
 int global=100;
	public int method(int num){
		int local=num;
		return local*global;
		
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
3+4:<%= 3+4 %><br>
"jdk"+8:<%= "jdk"+8 %><br>
global변수 :<%=global %><br>
method(3)호출 결과: <%= method(3) %>
<hr>
<%
out.print("3+4:"+(3+4)+"<br>");
out.print("'jdk'+8:"+("jdk"+8)+"<br>");
out.print("global변수 :"+(global)+"<br>");
out.print("method(3)호출 결과:"+(method(3))+"<br>");
%>
</body>
</html>
```

```java
/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.21
 * Generated at: 2019-06-28 08:40:46 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class test1_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {


 int global=100;
	public int method(int num){
		int local=num;
		return local*global;
		
	}

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = null;
  }

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    if (!javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSP들은 오직 GET, POST 또는 HEAD 메소드만을 허용합니다. Jasper는 OPTIONS 메소드 또한 허용합니다.");
        return;
      }
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=utf-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write('\r');
      out.write('\n');
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta charset=\"utf-8\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("3+4:");
      out.print( 3+4 );
      out.write("<br>\r\n");
      out.write("\"jdk\"+8:");
      out.print( "jdk"+8 );
      out.write("<br>\r\n");
      out.write("global변수 :");
      out.print(global );
      out.write("<br>\r\n");
      out.write("method(3)호출 결과: ");
      out.print( method(3) );
      out.write("\r\n");
      out.write("<hr>\r\n");

out.print("3+4:"+(3+4)+"<br>");
out.print("'jdk'+8:"+("jdk"+8)+"<br>");
out.print("global변수 :"+(global)+"<br>");
out.print("method(3)호출 결과:"+(method(3))+"<br>");

      out.write("\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}

```

아래는 직접 파일에 찾아가 연결프로그램으로 열어본 것이다. 차이점을 한번 봐보자. 허나 이방법은 권장하지 않는다!!!! 주의하자.

## page지시자

#### error

```jsp
<%@ page  contentType="text/html; charset=utf-8" errorPage="error.jsp"%>
<%!
 int global=100;
	public int method(int num){
		int local=num;
		return local*global;
		
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<%
int result=5/0;
%>
</body>
</html>
```

이렇게 만들면 에러페이지를 만들었기에 오류 메시지가 505..?가 아닌 403으로 뜨며

```jsp
<%@ page language="java" contentType="text/html; charset=utf-8" isErrorPage="true"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
out.println(exception.getMessage());
%>
</body>
</html>
```

이렇게 에러페이지를 만들어 주고 결과화면을 보면 깔끔하게 원인을 보여준다.

### 자주구현하는 기능을 태그로 정의

1. 표준 액션 태그

   < jsp:useBean~~~

   - JSP 스펙에 정의된 기능, 모든 JSP 컨테이너가 지원하므로 

2. 커스텀 액션 태크

   - 개발자가 직접 만든 태그 클래스, tld(xml형식) 파일을 정의해서 사용

3. EL(expression Language) :표현언어, JSP2.0에서 추가

   - <c:out ...> 또는 <jsp:getProperty ...>보다 간결하게 사용 가능
   - page,session,request,application 에 저장된 객체를 간결하게 표현



#### 표준액션태그

1. < jsp:useBean>
2. < jsp:setProperty>
3. < jsp:getProperty>

# 간단하게 실행하기

- 먼저 다운로드 받아보자
- jakarta-taglibs-standard-1.1.2
  - `https://tomcat.apache.org/taglibs/standard/`여기에서 받는다.
- 그후  lib에 있는 두개의 파일을 복사하여 web1의 WEB-INF의 lib에 붙여넣기 한다.

### 백(100)까지 더하기

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


@WebServlet("/total")
public class total extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
  
    public total() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		
		
		int total=0;
		for(int i=1;i<=100;i++)
			total+=i;
		request.setAttribute("result",total);
		RequestDispatcher rd=request.getRequestDispatcher("Hundred.jsp");
		rd.forward(request, response);
	}

}

```



Hundred.jsp

```jsp
<%@ page contentType="text/html; charset=UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
1부터 100까지 합은? = ${result}
</body>
</html>
```

결과값을 뽑아올때 힘들게 쓸 것이 아닌 ${result} 로 도 뽑아올수 있다. 이는 ${}이 전체적으로 파일을 서칭해서 맞는것을 찾아오기 때문이다.



headinfo를 간단하게 해보자.

```jsp
<%@page import="java.util.Enumeration" %>
<%@ page contentType="text/html; charset=utf-8" errorPage="error.jsp" %>
<%
Enumeration<String> headerName= request.getHeaderNames();
while(headerName.hasMoreElements()){
	String name=headerName.nextElement();
	out.print("<li>"+name+":");
	Enumeration<String> values=request.getHeaders(name);
	while(values.hasMoreElements()){
		out.print(values.nextElement()+",");
	}
	out.print("</li>");
}
%>
<li>요청 메소드:<%=request.getMethod()%></li>
<li>요청한 client의IP:<%=request.getRemoteAddr()%></li>
<li>ContextPath:<%=request.getContextPath()%></li>
<li>RequestURI:<%=request.getRequestURI()%></li>
<li>RequestURL:<%=request.getRequestURL()%></li>
<li>ServletPath:<%=request.getServletPath()%></li>

```





# DB 연동해보자

먼저 새로운 web2 생성

```html
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>


<!DOCTYPE html>
<html>
  <head>
    <meta  charset="utf-8">
    <title>login.jsp</title>     
    <link rel="stylesheet" href="partPage.css" type="text/css" />
    <script src="partPage.js"></script>
  </head>
  <body>
    <h3>MVC구조 login </h3>
    <table border="1">
      <tr><td colspan="2" align="center"><font size=15><b>우리회사</b></font></td></tr>
      <tr>
         <td><form action="Login" method="post">
               <div id="confirmed">
                 <table>
                    <tr>
                      <td>아이디</td>
                      <td><input type="text" id="userid" name="userid" size="15" maxlength="12"/></td>
                    </tr>
                    <tr>
                      <td>비밀번호</td>
                      <td><input type="password" id="userpwd" name="userpwd" size="15" maxlength="12"/></td>
                    </tr>
                    <tr><td colspan="2" align="center">
                        <input type="button" id="login" value="로그인" onclick ="startMethod()"/></td>
                    </tr>
                </table>
              </div>
             </form>
         </td>
         <td width="400"><img src="./images/dog.jpg"></td>
      </tr>
      <tr><td colspan="2" align="center">찾아오시는길 |회사소개|정보보호정책</td></tr>
    </table>
  </body>
</html>
```

images 파일을 생성했는데 이클립스의 web1의 WebContent 폴더 안에 images파일을 넣어주면 오케이!(#이미지 삽입, #이미지파일)



web2 에 만들었으며 기본 web2값을 저위의 페이지로 설정하기 위해서

web2->Webcontent->Web-INF->lib->web.xml 을 클릭하여 `defulat.html`값을 모두 `login.jsp`로 바꾸어 준다.

그러면 localhost:8080/web2 로만 접속해도 초기페이지 설정이 완료!

그 후 데이터베이스에 페이지 만들어 보자.

cmd를 이용하자

```cmd
sqlplus hr/oracle
select table_name from user_tables;

//새로운 테이블 만들기
create table userinfo()
userid varchar2(15) primary key,
userpwd varchar2(15),
username varchar2(20),
phone varchar2(15),
birth date
,address varchar2(100)
);
desc userinfo
insert into userinfo(userid,userpwd,username)values('admin','a1234','관리자');
commit;


```

만든 후 

WEB-INF -> lib 에

db.properties 파일을 만든다.(File이다.)

```file
driver=oracle.jdbc.OracleDriver
url=jdbc:oracle:thin:@localhost:1521:orcl
user=hr
pwd=oracle
```



loginDAO.java

```java
package lab.web.model;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class loginDAO {
	public Connection dbCon() {
		Connection con=null;
		try {
			Properties prop=new Properties();
			prop.load(new FileInputStream("C:/workspace2/web2/WebContent/WEB-INF/db.properties"));
			Class.forName(prop.getProperty("driver"));
			con =DriverManager.getConnection(prop.getProperty("url"),
			prop.getProperty("user"),prop.getProperty("pwd"));
		}catch(Exception e) {
			e.printStackTrace();
		}
		return con;
	}
		
		public void dbClose(Connection con,Statement stat, ResultSet rs) {
			try {
				if(rs!=null)rs.close();
				if(stat!=null)stat.close();
				if(con!=null)con.close();
				
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
		
	
public boolean loginProc(String uid,String upwd) {
	boolean success=false;
	Connection con=null;
	PreparedStatement stat=null;
	String sql="select*from userinfo where userid=? and userpwd=?";
	ResultSet rs=null;
	try {
		con=dbCon();
		stat=con.prepareStatement(sql);
		stat.setString(1, uid);
		stat.setString(2,upwd);
		rs=stat.executeQuery();
		if(rs.next()) {
			success=true;
		}
		
	}catch(Exception e) {
		e.printStackTrace();
	}finally {
		dbClose(con,stat,rs);
	}
	return success;
}
}



```

loginsu.jsp

```jsp
<%@ page  contentType="text/html; charset=utf-8" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>loginsu.jsp</title>
<style>
p{
color:blue;}
</style>
</head>
<body>
<p> ${userid}님 환영합니다.</p>
<br>
</body>
</html>
```



loginfail.jsp

```jsp
<%@ page  contentType="text/html; charset=utf-8" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>loginfail.jsp</title>
<style>
p{
color:red;}
</style>
</head>
<body>
<p> 아이디가 존재하지 않거나 비밀번호가 일치하지 않습니다.</p>
<a href="./Login">다시 로그인 페이지로</a>
</body>
</html>
```

Login.java(lab.web.controller 패키지에 만들었다.)

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

import lab.web.model.loginDAO;

/**
 * Servlet implementation class Login
 */
@WebServlet("/Login")
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

    public Login() {
        super();
        // TODO Auto-generated constructor stub
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		response.sendRedirect("./login.jsp");
		
		
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		String uid=request.getParameter("userid");
		String upwd=request.getParameter("userpwd");
		ServletContext sc=request.getServletContext();
		RequestDispatcher rd=null;
		loginDAO dao=new loginDAO();
		if(dao.loginProc(uid,upwd)) {
			rd=sc.getRequestDispatcher("/loginsu.jsp");
			rd.forward(request, response);
			
		}else {
			rd=sc.getRequestDispatcher("/loginfail.jsp");
			rd.forward(request, response);
		}
		
	}

}

```



### 회원가입 내용 저장

userVO.java

```java
package lab.web.controller;

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

join.java

```java
package lab.web.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/Join")
public class Join extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
 
    public Join() {
        super();
        // TODO Auto-generated constructor stub
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			response.setContentType("text/html;charset=utf-8");
			response.sendRedirect("./member.html");
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		String uid=request.getParameter("userid");
		String upwd=request.getParameter("userpwd");
		String nm=request.getParameter("username");
		String ph=request.getParameter("phone");
		String em=request.getParameter("email");
		String[] em2=request.getParameterValues("email_dns");
		String em3=em+"@"+em2;
		String[] jb=request.getParameterValues("job");
		String ad=request.getParameter("address");
		ServletContext sc=request.getServletContext();
		RequestDispatcher rd=null;
		if()
		
		
		
		
	}

}

```

loginDAO.java

```java
package lab.web.model;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

import lab.web.controller.userVO;

public class loginDAO {
	public Connection dbCon() {
		Connection con=null;
		try {
			Properties prop=new Properties();
			prop.load(new FileInputStream("C:/workspace2/web2/WebContent/WEB-INF/db.properties"));
			Class.forName(prop.getProperty("driver"));
			con =DriverManager.getConnection(prop.getProperty("url"),
			prop.getProperty("user"),prop.getProperty("pwd"));
		}catch(Exception e) {
			e.printStackTrace();
		}
		return con;
	}
		
		public void dbClose(Connection con,Statement stat, ResultSet rs) {
			try {
				if(rs!=null)rs.close();
				if(stat!=null)stat.close();
				if(con!=null)con.close();
				
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
		
	
public boolean loginProc(String uid,String upwd) {
	boolean success=false;
	Connection con=null;
	PreparedStatement stat=null;
	String sql="select*from userinfo where userid=? and userpwd=?";
	ResultSet rs=null;
	try {
		con=dbCon();
		stat=con.prepareStatement(sql);
		stat.setString(1, uid);
		stat.setString(2,upwd);
		rs=stat.executeQuery();
		if(rs.next()) {
			success=true;
		}
		
	}catch(Exception e) {
		e.printStackTrace();
	}finally {
		dbClose(con,stat,rs);
	}
	return success;
}
public int JoinProc(userVO user) {
	int rows=0;
	Connection con=null;
	PreparedStatement stat=null;
	String sql="insert into userinfo(userid,username,userpwd,userpwd,email,phone,address,job)values (?,?,?,?,?,?,?)";
	try {
		con=dbCon();
		stat=con.prepareStatement(sql);
		stat.setString(1, user.getUserid());
		stat.setString(2, user.getUsername());
		
		stat.setString(3,user.getUserpwd());
		stat.setString(4, user.getEmail());
		stat.setString(5, user.getPhone());
		stat.setString(6, user.getAddress());
		stat.setString(7, user.getJob());
		rows=stat.executeUpdate();
	}catch(Exception e) {
		e.printStackTrace();
	}finally {
		dbClose(con,stat,null);
	}
	return rows;
}
}



```

member.html

```html

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <style>
   h3 { width: 740px; 
       text-align : center; }
      
  </style>
  <title>회원 가입</title>
 </head>
 <body>
 <h3> 회원가입 정보 입력</h3>
 <form name="write_form_member" method="post" action="memberOK2.jsp">
   <table width="740" style="padding:5px 0 5px 0; ">
      <tr height="2" bgcolor="#FFC8C3"><td colspan="2"></td></tr>
      <tr>
         <th> 아이디 </th>
         <td><input type="text" name="userid" id="userid"></td>
      </tr>
      <tr>
         <th>이 름</th>
         <td><input type="text" name="username" id="username">  </td>
       </tr>        
       <tr>
         <th>비밀번호</th>
         <td><input type="password" name="userpwd" id="userpwd"> 영문/숫자포함 6자 이상</td>
       </tr>   
      
        <tr>
        </td>
           <th>연락처</th>
           <td><input type='text' name='phone' id="phone"></td>
        </tr>
        <tr>
          <th>이메일</th>
          <td>
            <input type='text' name="email" id="email">@
            <input type='text' name="email_dns" id="email_dns">
              <select name="emailaddr">
                 <option value="">직접입력</option>
                 <option value="daum.net">daum.net</option>
                 <option value="empal.com">empal.com</option>
                 <option value="gmail.com">gmail.com</option>
                 <option value="hanmail.net">hanmail.net</option>
                 <option value="msn.com">msn.com</option>
                 <option value="naver.com">naver.com</option>
                 <option value="nate.com">nate.com</option>
              </select>
            </td>
         </tr>
         
         <tr>
           <th>직업</th>
           <td>
           <select name='job' size='1' id="job">
                 <option value=''>선택하세요</option>
                 <option value='39'>학생</option>
                 <option value='40'>컴퓨터/인터넷</option>
                 <option value='41'>언론</option>
                 <option value='42'>공무원</option>
                 <option value='43'>군인</option>
                 <option value='44'>서비스업</option>
                 <option value='45'>교육</option>
                 <option value='46'>금융/증권/보험업</option>
                 <option value='47'>유통업</option>
                 <option value='48'>예술</option>
                 <option value='49'>의료</option>
           </select>
          </td>
        </tr>
       <tr>
         <th>주소 </th>
           <td class="s">
               <input type="text" name="address" id="address" >  
            </td>
         </tr>
         
 
           <tr height="2" bgcolor="#FFC8C3"><td colspan="2"></td></tr>
           <tr>
             <td colspan="2" align="center">
               <input type="submit" value="회원가입" id="Join">
               <input type="reset" value="취소" id="userVO">
            </td>
           </tr>
           </table>
          </td>
          </tr>
          </form>
 </body>
</html>
 
```

memberOK.jsp

```html
<%@page import="lab.web.model.loginDAO"%>
<%@page import="lab.web.controller.userVO"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    <% request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>memberOK.jsp</title>
</head>
<body>
<%
userVO user=new userVO();
user.setUserid(request.getParameter("userid"));
user.setUserpwd(request.getParameter("userpwd"));
user.setUsername(request.getParameter("username"));
user.setEmail(request.getParameter("email"));
user.setPhone(request.getParameter("phone"));
user.setAddress(request.getParameter("address"));
user.setJob(request.getParameter("job"));
loginDAO dao=new loginDAO();
if(dao.JoinProc(user)>0){

%>
아이디: <%= user.getUserid() %><Br>
이름: <%=user.getUsername() %><br>
비밀번호:<%=user.getUserpwd() %><Br>
전화번호:<%= user.getPhone() %><Br>
이메일:<%=user.getEmail() %><Br>
주소:<%=user.getAddress() %><Br>
직업:<%=user.getJob() %><br>

<%
}else{
%>
회원가입 처리 실패
<%
}
%>
</body>
</html>
```

이번에는 액션태그로 해보자

memberOK2.jsp

```html
<%@page import="lab.web.model.loginDAO"%>
<%@page import="lab.web.controller.userVO"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"%>
<% request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>memberOK.jsp</title>
</head>
<body>
<jsp:useBean id="user" class="lab.web.controller.userVO">
<jsp:setProperty name="user" property="*"/>
</jsp:useBean>

<jsp:useBean id="dao" class="lab.web.model.loginDAO" />
<% 
	if(dao.JoinProc(user)>0){ 
%>

아이디: <jsp:getProperty name="user" property="userid"/><Br>
이름: <jsp:getProperty name="user" property="username"/><br>
비밀번호:<jsp:getProperty name="user" property="userpwd"/><Br>
전화번호:<jsp:getProperty name="user" property="phone"/><Br>
이메일:<jsp:getProperty name="user" property="email"/><Br>
주소:<jsp:getProperty name="user" property="address"/><Br>
직업:<jsp:getProperty name="user" property="job"/><br>

<%
}else{
%>
회원가입 처리 실패
<%
}
%>
</body>
</html>
```



##### EL 연산자 

```html
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>EL테스트</title>
</head>
<body>
<h2>EL의 연산자들</h2>
<hr>
\${200+100} :${200+100}<Br>
\${200-100} :${200-100}<Br>
\${200/100} :${200/100}<Br>
\${200>100} :${200>100}<br>
\${200==100} :${200==100}<br>
\${200!=100} :${200!=100}<br>
\${'10'-10} : ${'10'-10}<br>
\${10-"10"} : ${10-"10"}<br>
\${40 div 5} : ${40 div 5}<br>
\${40 mod 5}: ${40 mod 5}<Br>
\${10 eq 10 } : ${10 eq 10 }<br>
\${10 lt 10 } : ${10 lt 10 }<br>
\${10 gt 10 } : ${10 gt 10 }<br>
\${10 le 10 } : ${10 le 10 }<br>
\${10 ge 10 } : ${10 ge 10 }<br>
\${10>5? 'A':'B' } :${10>5? 'A':'B' }<br>
\${100+200+300} :${100+200+300 }<Br>
\${100+=200+=300} :${100+=200+=300 }<Br>
\${"EL"+=12+=34+="문자열 결합연산" }:
${"EL"+=12+=34+="문자열 결합연산" }

</body>
</html>
```

결과값

${200+100} :300
${200-100} :100
${200/100} :2.0
${200>100} :true
${200==100} :false
${200!=100} :true
${'10'-10} : 0
${10-"10"} : 0
${40 div 5} : 8.0
${40 mod 5}: 0
${10 eq 10 } : true
${10 lt 10 } : false
${10 gt 10 } : false
${10 le 10 } : true
${10 ge 10 } : true
${10>5? 'A':'B' } :A
${100+200+300} :600
${100+=200+=300} :100200300
${"EL"+=12+=34+="문자열 결합연산" }: EL1234문자열 결합연산



##### JSTL 점검

```html
<%@page import="java.util.ArrayList"%>
<%@page import="lab.web.model.Product"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<%
	request.setCharacterEncoding("utf-8");
	Product p1= new Product("체리",10000,"과일");
	Product p2= new Product("에어컨",10000,"전자");
	Product p3= new Product("베스킨라빈스",400,"빙과");
	ArrayList<Product> alist=new ArrayList();
	alist.add(p1);
	alist.add(p2);
	alist.add(p3);

	request.setAttribute("product",alist);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>jstlTest.jsp</title>
</head>
<body>
	<c:set var="username" value="korea" scope="request" />
	<c:if test="${username != null}">
username 변수 값: <c:out value="${username}" /><Br>
	</c:if>
	<c:out value="${username}" />
	<c:remove var="username" />
	<c:out value="${username}" />
	<!-- 삭제했기때문에 null point exception -->

	<c:if test="${username ==  null}">
		<c:out value="username 변수가 삭제되었습니다." />
		<Br>
	</c:if>

	<c:set var="jumsu" value="${parm.jumsu}" scope="request" />
	<c:out value="${jumsu+=\"점은\" }" /><Br>
	<c:choose>
		<c:when test="${jumsu>=90}">
			<c:out value="A" />
		</c:when>
		<c:when test="${jumsu>=80 }">
			<c:out value="B" />
		</c:when>
		<c:when test="${jumsu>=70 }">
			<c:out value="C" />
		</c:when>
		<c:when test="${jumsu>=60 }">
			<c:out value="D" />
		</c:when>

		<c:otherwise>
			<c:out value="F" />
		</c:otherwise>
	</c:choose>
	
	<c:forEach var="count" begin="1" end="10" step="2">
	${count}<Br>
	</c:forEach>
	
	#상품 정보 리스트<br>
	<table>
	
	<tr><th>상품명</th><th>가격</th><th>분류</th></tr>
	<c:forEach var="product" items="${products}">
	<tr><td>${product.name}</td><td>${product.price }</td><td>${product.category }</td></tr>
	</c:forEach>
	
	</table>
	
</body>
</html>
```



##### 로그인 JSTL로 해보기

member.html

```html

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <style>
   h3 { width: 740px; 
       text-align : center; }
      
  </style>
  <title>회원 가입</title>
 </head>
 <body>
 <h3> 회원가입 정보 입력</h3>
 <form name="write_form_member" method="post" action="memberOK3.jsp">
   <table width="740" style="padding:5px 0 5px 0; ">
      <tr height="2" bgcolor="#FFC8C3"><td colspan="2"></td></tr>
      <tr>
         <th> 아이디 </th>
         <td><input type="text" name="userid" id="userid"></td>
      </tr>
      <tr>
         <th>이 름</th>
         <td><input type="text" name="username" id="username">  </td>
       </tr>        
       <tr>
         <th>비밀번호</th>
         <td><input type="password" name="userpwd" id="userpwd"> 영문/숫자포함 6자 이상</td>
       </tr>   
      
        <tr>
        </td>
           <th>연락처</th>
           <td><input type='text' name='phone' id="phone"></td>
        </tr>
        <tr>
          <th>이메일</th>
          <td>
            <input type='text' name="email" id="email">@
            <input type='text' name="email_dns" id="email_dns">
              <select name="emailaddr">
                 <option value="">직접입력</option>
                 <option value="daum.net">daum.net</option>
                 <option value="empal.com">empal.com</option>
                 <option value="gmail.com">gmail.com</option>
                 <option value="hanmail.net">hanmail.net</option>
                 <option value="msn.com">msn.com</option>
                 <option value="naver.com">naver.com</option>
                 <option value="nate.com">nate.com</option>
              </select>
            </td>
         </tr>
         
         <tr>
           <th>직업</th>
           <td>
           <select name='job' size='1' id="job">
                 <option value=''>선택하세요</option>
                 <option value='39'>학생</option>
                 <option value='40'>컴퓨터/인터넷</option>
                 <option value='41'>언론</option>
                 <option value='42'>공무원</option>
                 <option value='43'>군인</option>
                 <option value='44'>서비스업</option>
                 <option value='45'>교육</option>
                 <option value='46'>금융/증권/보험업</option>
                 <option value='47'>유통업</option>
                 <option value='48'>예술</option>
                 <option value='49'>의료</option>
           </select>
          </td>
        </tr>
       <tr>
         <th>주소 </th>
           <td class="s">
               <input type="text" name="address" id="address" >  
            </td>
         </tr>
         
 
           <tr height="2" bgcolor="#FFC8C3"><td colspan="2"></td></tr>
           <tr>
             <td colspan="2" align="center">
               <input type="submit" value="회원가입" id="Join">
               <input type="reset" value="취소" id="userVO">
            </td>
           </tr>
           </table>
          </td>
          </tr>
          </form>
 </body>
</html>
 
```

