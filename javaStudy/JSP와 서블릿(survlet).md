# JSP와 서블릿(survlet)

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

| 이름   | 프로토콜       |      |      |
| ------ | -------------- | ---- | ---- |
| www    | http           |      |      |
| Email  | SMTP/POP3/IMAP |      |      |
| FTP    | ftp            |      |      |
| telnet | telnet         |      |      |
| DNS    | DNS            |      |      |
| News   | NNTP           |      |      |

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

