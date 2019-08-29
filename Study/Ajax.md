# Ajax(Asynchronous JavaScript)

- 특징

  1. javaScript에 의한 비동기적 통신 (다른 작업 가능)
  2. 부분 갱신 , 최소한의 정보로 통신하므로 처리속도가 빠르다. 
  3. XML보다 가볍다. 최근에는 Ajax형식을 더 많이 사용한다.

  

- XMLHttpRequest메서드

| 메서드                         | 설명                               |
| ------------------------------ | ---------------------------------- |
| abort()                        | 현재 실행 중인 비동기 통신을 중단  |
| getAllResponsHeaders()         | 수신한 모든 HTTP응답 헤더 가져오기 |
| getResponseHeader(header)      | 특정 HTTP응답 헤더 가져오기        |
| open(...)                      | HTTP요청 초기화                    |
| send(data)                     | HTTp요청 보낸다                    |
| setRequestHeader(header,value) | 요청 헤더에 정보 추가              |



- XMLHttpRequest프로퍼티

| 프로퍼티           | 설명                                              | 읽기전용여부 |
| ------------------ | ------------------------------------------------- | ------------ |
| readyStateHTTP     | 통신상태가져오기(0~4)                             | 읽기         |
| response           | 응답 내용 가져오기                                | 읽기         |
| responseText       | 응답 내용을 텍스트 형식으로                       | 읽기         |
| responseType       | 응답 타입 가져오기,설정하기                       | 쓰기         |
| responseXML        | 응답 내용 XMLDocument객체로 가져오기              | 읽기         |
| status             | 요청에 대한 HTTP상태 코드                         | 읽기         |
| statusText         | 요청에 대한 보충 메시지                           | 읽기         |
| timeout            | 요청을 자동으로 끝내는데 걸리는 시간(밀리초)      | 쓰기         |
| withCredentials    | 크로스 오리진 통신에 대해 인증정보 사용 여부      | 쓰기         |
| onreadystatechange | readyState값이 바뀔 때마다 호출되는 이벤트 처리기 | 쓰기         |
| ontimeout          | 요청 시간이 초과할 떄마다 호출 되는 이벤트 처리기 | 쓰기         |

readyState프로퍼티 값

- 0   uninitizlized 객체만 생성되고 초기화 되지 않은상태(open메서드 호출안됨)
- 1   loading   open메서드가 호출되고 아직 send메서드가 불리지 않은 상태
- 2   loaded send 메서드가 불렸지만 status와 헤더는도착하지 않은 상태
- 3    interative 데이터의 일부를 받은 상태
- 4    Completed 데이터를 전부 받은 상태, 완전한 데이터 이용 가능 

### 글 읽어오기

같은 파일내에 data.txt 파일을 미리 만들어 놓아야 한다.(아무거나 써놓자)

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
<script>
window.onload=function(){           //이벤트가 발생되면
    var req=new XMLHttpRequest();//1. xmlrequest객체 생성
    req.onloadstart=function(){
        console.log("loadstart: 요청 보낼떄");
    }
    req.onload=function(){
        console.log("load: 요청 성공, 응답 가져올 수 있을 때");
    }
    req.onloadend=function(){
        console.log("loadend: 요청완료");
    }
    req.onprogress=function(){
        console.log("progress:데이터 주고 받을 때");
    }

    req.onreadystatechange=function(){//응답처리 함수를 미리 저장(콜백함수로)
        if(req.readyState==4){
            if(req.status==200){
                document.getElementById("view").innerHTML=req.responseText;
            }
        }
        
    }//응답된것을 innerHTML로 body에 넣어준다.

    //2.요청보낼 준비
    req.open("GET","data.txt");
    //같은 페이지인 경우 주소를 따로 쓰지 않는다. 원래는 주소를 다 작성해주어야한다.

    //3.요청 보내기
    req.send(null);//get방식으로 보내는 경우 body에 포함이 안되기 때문에 null지정해주자.
    
};
</script>
    <title>Document</title>
</head>
<body>
    <p id="view"></p>
</body>
</html>
```

#####  jquery로 바꾸기

```html
<!DOCTYPE html>
<html >
<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <meta charset="UTF-8">
<script>
$(document).ready(function(){
    $.ajax({
        url:"data.txt",
        success:function(data){
            $("#view").html(data);
        }
    });
});

   
</script>
    <title>Document</title>
</head>
<body>
    <p id="view"></p>
</body>
</html>
```





### 이미지 불러오기

##### images.jsp

```jsp

<%@ page contentType="text/plain; charset=utf-8"
pageEncoding="utf-8">

{"rows":[
	{"title":"이미지1","url":"images/img1.jpg"},
	{"title":"이미지2","url":"images/img2.jpg"},
	{"title":"이미지4","url":"images/img4.jpg"},
	{"title":"이미지5","url":"images/img5.jpg"},
	{"title":"이미지3","url":"images/img3.jpg"},
	{"title":"이미지6","url":"images/img6.jpg"},
	{"title":"이미지7","url":"images/img7.jpg"},
	{"title":"이미지8","url":"images/img8.jpg"},
	{"title":"이미지10","url":"images/img10.jpg"}
]}

```

##### ajax_json.js

```js

window.onload=function () {
    document.getElementById("btn_load").onclick=function(){
        var url="images.jsp";//요청 url설정
        req= new XMLHttpRequest();//XMLHttpRequest생성
        req.onreadystatechange=createImages;
        req.open("Get",url,"true");
        req.send("null");//서버로 요청
    };
}
function createImages(){
    if(req.readyState==4){//요청객체의 상태가 모든 데이터를 받을 수
        if(req.status==200){//서버로부터 응답받는 HTTP상태가 정상인
            var obj=JSON.parse(req.responseText);
            var images=obj["rows"];
            var strDOM="";
            for(var i=0;i<images.length;i++){
                //2.n번재 이미지 정보 구하기
                var image=images[i];
                //3.n번째 이미지 패널 생성
                strDom+='<div class="image_panel">'
                strDom+='     <img src="'+image.url+'"<';
                strDom+='       <p class="title">'+image.title+'</p>';
                strDOM+='</div>';
            }
            document.querySelector("#image_container").innerHTML=strDom;

        }else{
            alert("처리중 에러가 발생했습니다.");
        }
    }
}

```

##### ajax이미지.html

```html

<!DOCTYPE html>
<html>
<head>
<meta  charset="UTF-8">
	<title></title>
	<style>
		.image_panel{
			border:1px solid eeeeee;
			text-align:center;
			margin:5px;
		}
		.image_panel .title{
			font-size:9pt;
			color:#ff0000;
			
		}
		
	</style>
	 
    <script src="ajax_json.js"></script>	
    <script>
    d
    </script> 
</head>

<body>
	<div>
		<button id="btn_load">이미지 읽어들이기</button>
	</div>
	<div id="image_container">
		<!-- 1. 이곳에 이미지를 넣어주세요-->
	</div>
	
	<!-- 2. 이 내용은 이미지 패널 템플릿입니다. -->
	<div style="display:none;" id="image_panel_template">
		<div class="image_panel">
			<img >
			<p class="title"></p>
		</div>
	</div>
</body>
</html>

```

##### jquery로 바꿔보자

```html

<!DOCTYPE html>
<html>
<head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<meta  charset="UTF-8">
	<title></title>
	<style>
		.image_panel{
			border:1px solid eeeeee;
			text-align:center;
			margin:5px;
		}
		.image_panel .title{
			font-size:9pt;
			color:#ff0000;
			
		}
		
	</style>
	 
    
    <script>
    $(document).ready(function(){
        $("#btn_load").click(function(){
            $.getJSON("images.jsp",null,createImages);
        });
    });
    function createImages(data){
        var images=data.rows;
        var strDOM="";
        for(var i=0;i<images.length;i++){
            var image=images[i];
             strDOM+='<div class="image_panel">'
                strDOM+='     <img src="'+image.url+'">';
                strDOM+='       <p class="title">'+image.title+'</p>';
               strDOM+='</div>'
        }
       
        var $imageContainer  =$('#image_container');
        $imageContainer.append(strDOM);

        $(document).ajaxComplete(function(){
            console.log("ajax event:complete");
        });
        $(document).ajaxSend(function(){
            console.log("ajax event: send");
        });
        $(document).ajaxStart(function(){
            console.log("ajax evnet: start");
        });
        $(document).ajaxSuccess(function(){
            console.log("ajax event:success");
        });
    }
    </script> 
</head>

<body>
	<div>
		<button id="btn_load">이미지 읽어들이기</button>
	</div>
	<div id="image_container">
		<!-- 1. 이곳에 이미지를 넣어주세요-->
	</div>
	
	<!-- 2. 이 내용은 이미지 패널 템플릿입니다. -->
	<div style="display:none;" id="image_panel_template">
		<div class="image_panel">
			<img >
			<p class="title"></p>
		</div>
	</div>
</body>
</html>

```



### 부분페이지갱신,POST요청, XML응답

로그인을 해보자

jsp 파일

```jsp
<%@ page   contentType="text/xml; charset=utf-8"     %>
<%
    request.setCharacterEncoding("utf-8"); 
    //반드시 응답되는 내용의  Content-type을 "text/xml;charset=utf-8"해야함, 생략시 결과가 표시되지 않을 수 있음
   // response.setContentType("text/xml;charset=utf-8");//응답되는 내용의 Content-type을 설정

    String outString = ""; // 요청한 페이지인 partPageDBUse.js로 리턴할  결과를 저장
    int result = 0 ;
    String id = request.getParameter("userid"); 
    String passwd = request.getParameter("userpwd"); 
     
    if(id.equals("admin")&&passwd.equals("1234")){
    	result = 1;
    }else if(id.equals("admin")){
    	result = 0;
    }else{
    	result = 2;
    }
     
    
    //userCheck()메소드의 수행후 리턴되는 결과 값에 따라 처리
    if(result==1){//사용자 인증에 성공시
		session.setAttribute("id",id);
		outString="<response><result>"+ result + "</result><id>"+ id 
				+"</id></response>";
	}else if(result==0){//사용자 인증에 실패시 - 비밀번호 틀림
		outString="<response><result>"+ result + "</result><id>"+ id 
		+"</id></response>";
    }else{//사용자 인증에 실패시 - 아이디 틀림
    	outString="<response><result>"+ result + "</result><id>"+ id 
    	+"</id></response>";
    }	
    
    out.println(outString); // outString의 내용을 요청한 페이지인 partPageDBUse.js로 응답함
    
%>
```

js 파일

```js
var req;//XMLHttpRequest 객체를 저장할 변수로 전역변수로 선언
window.onload=function(){
    req=new XMLHttpRequest();
    document.getElementById("login").onclick=startMethod;
};
function startMethod(){
    var uid=document.getElementById("userid").value;
    var upwd=document.querySelector("#userpwd").value;
    var url="partPage.jsp";//요청 url설정
    req.onreadystatechange=resultProcess;//응답 결과를 처리메소드인
    req.open("post",url,"true");//서버 요청 설정, url변수에 설정된
    req.setRequestHeader("content-type","application/x-www-form-urlencoded");
    req.send("userid="+uid+"&userpwd"+upwd); //서버로 요청을 보냄 서버 요청시 ?userid=값&userpwd=값로 보내지므로 이 형식을 맞춰준다

}
function resultProcess(){
    if(req.readyState==4){
        if(req.status==200){
            cofirmedProcess();//cofirmedProcess()메소드 호출
        }
    }
}
function cofirmedProcess(){//로그인의 성공과 실패에 따라 표시되는 내용을 결정하는 메소드
    var result =req.responseXML.getElementsByTagName("result")[0].firstChild.data;
    var name = req.responseXML.getElementsByTagName("id")[0].firstChild.data;
     
    if (result == 1){//사용자 인증성공시
      var str="<table><tr><td align='center'><b>"+name+"</b> 님 오셨구려..</td></tr>"
      str+="<tr><td align='center'><input type='button' id='logout' value='로그아웃' onclick ='logoutMethod()'/></td></tr></table>"
    	  document.getElementById("confirmed").innerHTML = str;
    }else if(result==0){//사용자 인증실패시 - 비밀번호가 틀림
      alert("비밀번호가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value=name;
      document.getElementById("userpwd").value="";
      document.getElementById("userpwd").focus();
    }else{//사용자 인증실패시 - 아이디가가 틀림
      alert("아이디가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value="";
      document.getElementById("userpwd").value="";
      document.getElementById("userid").focus();
    }
}

```

##### jQUery로 하는 경우

```js
$(document).ready(function(){
    $("#login").click(function(){
         var uid = $("#userid").val();  
         var upwd = $("#userpwd").val();  
         $.ajax({
             url: "partPage.jsp",
             data: {userid: uid, userpwd:upwd},
             success : function(data) {	    		
                 var result = $(data).find("result").text();	    		 
                 var name = $(data).find("id").text();	    	 
                 if (result == "1"){//사용자 인증성공시
                       var str="<table><tr><td align='center'><b>"+name+"</b> 님 오셨구려..</td></tr>"
                       str+="<tr><td align='center'><input type='button' id='logout' value='로그아웃' onclick ='logoutMethod()'/></td></tr></table>"
                           $("#confirmed").html( str );
                 }else if(result=="0"){//사용자 인증실패시 - 비밀번호가 틀림
                       alert("비밀번호가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
                       $("#userid").val(name);
                       $("#userpwd").val("");
                       $("#userpwd").focus();
                 }else{//사용자 인증실패시 - 아이디가가 틀림
                       alert("아이디가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
                       $("#userid").val("");
                       $("#userpwd").val("");
                       $("#userid").focus();
                 }
             }
         });
         
     });
 });
  /*
  
 function logoutMethod(){	 
     var url = "partPagelogout.jsp?timestamp="+ new Date().getTime(); //요청 URL설정
     xhr.onreadystatechange = logoutProcess; //응답결과를 처리메소드인 logoutProcess()메소드 설정 
     xhr.open("Get", url, "true");//서버의 요청설정 - url변수에 설정된 리소스를 요청할 준비
     xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded"); 
     xhr.send(null);//서버로 요청을 보냄
 }
 
  
      
     
  
  
 
 function logoutProcess(){//partPageDBUselogout.jsp페이지에서 응답결과가 오면 자동으로 실행
     if(xhr.readyState == 4){ //요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
       if(xhr.status == 200){ //서버로부터 응답받는 HTTP상태가 정상인 경우 수행
            
          var str="<table><tr><td>아이디</td><td><input type='text' id='id' size='15' maxlength='12'/></td></tr>";
          str+="<tr><td>비밀번호</td><td><input type='password' id='passwd' size='15' maxlength='12'/></td></tr>";
          str+="<tr><td colspan='2' align='center'><input type='button' id='login' value='로그인' onclick ='startMethod()'/></td></tr></table>" ;          
          
          document.getElementById("confirmed").innerHTML = str;
       }
     }
 }
 */
```



parPage.css

```css
@CHARSET "utf-8";
div#confirmed{
  width            : 250px;
  height           : 100px;
  background-color : #e0ffff;
  border-color     : #b0e0e6;
  border-style     : dotted;
}
```

html파일

```html

<!DOCTYPE html>
<html>
  <head>
    <meta  charset="utf-8">
    <title>부분페이지 동적 갱신</title>     
    <link rel="stylesheet" href="partpage.css" type="text/css" />
    <script src="partPage.js"></script>
  </head>
  <body>
    <h3>부분페이지 갱신, POST요청, XML응답처리</h3>
    <table border="1">
      <tr><td colspan="2" align="center"><font size=15><b>우리회사</b></font></td></tr>
      <tr>
         <td><form action="#">
               <div id="confirmed">
                 <table>
                    <tr>
                      <td>아이디</td>
                      <td><input type="text" id="userid" size="15" maxlength="12"/></td>
                    </tr>
                    <tr>
                      <td>비밀번호</td>
                      <td><input type="password" id="userpwd" size="15" maxlength="12"/></td>
                    </tr>
                    <tr><td colspan="2" align="center">
                        <input type="button" id="login" value="로그인" /></td>
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

### 크로스오리진 통신망

- 두가지의 html과 다른 jp를 불러와서 작성해본다.

```html
<!DOCTYPE html>
<html \>
<head>
    <meta charset="UTF-8">
 
 <script>
 function show(data){
     console.log("name: "+data.name);
     console.log("price: "+data.price);
 }
 window.onload=function(){
     var url="http://70.12.50.130:9000/jsonp.js";
     var script=document.createElement("script");
     script.setAttribute("src",url);
     document.getElementsByTagName("head")[0].appendChild(script);
 }
 </script>
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

```js
show({"name":"apple","price":100});
```

url를 따올 시 다른 포트의 주소에서 따왔기에 만약 자신의 컴퓨터 내에서 활용하기 위해서는

` var url="http://70.12.50.130:9000/jsonp.js";`를

`var url="jsnop.js"`로 하고 같은 파일내 jsnop.js로 저장한다.

다른 서버와 연결되는지 확인을 보기위한 연습이다.

### CORS

위의 했던 크로스통신을 하기 위해서는 헤더를 추가해야 한다.

`Access-Control-Allow-Origin`이라는 hTTP헤더 추가가 필요

```html
<!DOCTYPE html>
<html >
<head>
    <meta charset="UTF-8">
    <script >//type="text/javascript"
    window.onload=function(){
        setInterval(send,1000);
        //1초마다 IFrame에 메시지를 보냄.
    }
    function send(){
        var ifrm=document.getElementById("ifrm");
        var MyOrigin=location.protocol+"//"+location.host;
        var date=new Date();
        var dateStr=date.getFullYear()+"/"+(date.getMonth()+1)+date.getMinutes()+" "+date.getHours+":"
        +date.getMinutes()+":"+date.getSeconds();
        var number=Math.floor(Math.random()*100);

        ifram.contentWindow.postMessage({date:dateStr,number:number},"http://70.12.50.130:9000");
        document.getElementById("msg").innerHTML=dateStr+"생성된 값은'"+number+"' 입니다.<br/>MyOrigin:"+MyOrigin;
    }
    </script>
    <title>Document</title>
</head>
<body>
    <div id="msg">8000<br>MyOrigin</div>
    <iframe id="ifrm" src="http://70.12.50.130:9000/receive.html" width=500 height=200></iframe>
</body>
</html>
```

여기까찌 했으나 연결 오류로.............완료는 못함

### 현재 경료 표시

location.protocol : http:
location.host : [www.test.com](http://www.test.com/) (주소)
location.pathname : /6.25/cross1.html (경로)
location.search : ?wr_id=4&bbs=free (파라미터)

# 문제풀어보자

### 리스트박스 만들기

기본적인 구조

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title> </title>
<style>
 
</style>
<script>
 
</script>
</head>
<body>
 <form name="form1">
		listbox에서 항목 이동 예제<br />

		나만의 메뉴를 고르시오.<br /><br />
		<table><tr><td>
		메뉴</td><td></td><td>나만의 메뉴</td></tr> 
		<tr><td> <select name="menu" size="8">
		<option value="파일">파일</option>
		<option value="편집">편집</option>
		<option value="보기" >보기</option>
		<option value="서식">서식</option>
		<option value="삽입">삽입</option>
		<option value="도구">도구</option>
		<option value="디자인">디자인</option>
		</select></td>
		<td align="center" valign="middle">
		<input type="button" value=">>" onclick="moveR(this.form);" /><br />
		<input type="button" value="<<"onclick="moveL(this.form);" /> </td>
		<td> <select name="my" size="8"> 
		</select> </td></tr></table>
	</form>

</body>
</html>
```

html의 경우

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title> </title>
<style>
 
</style>
<script>
    function moveR(fr){
        add=new Option(fr.menu[fr.menu.selectedIndex].value,fr.menu[fr.menu.selecedIndex].value);
        fr.my.options[fr.my.length]=add;
        fr.menu.options[fr.menu.selectedIndex]=null;
    }
    function moveL(fr){
        add= new Option(fr.my[fr.my.selectedIndex].value,fr.my[fr.my.selectedIndex].value);
        fr.menu.options[fr.menu.length]=add;
        fr.my.options[fr.my.selectedIndex]=null;
    }
</script>
</head>
<body>
 <form name="form1">
		listbox에서 항목 이동 예제<br />

		나만의 메뉴를 고르시오.<br /><br />
		<table><tr><td>
		메뉴</td><td></td><td>나만의 메뉴</td></tr> 
		<tr><td> <select name="menu" size="8">
		<option value="파일">파일</option>
		<option value="편집">편집</option>
		<option value="보기" >보기</option>
		<option value="서식">서식</option>
		<option value="삽입">삽입</option>
		<option value="도구">도구</option>
		<option value="디자인">디자인</option>
		</select></td>
		<td align="center" valign="middle">
		<input type="button" value=">>" onclick="moveR(this.form);" /><br />
		<input type="button" value="<<"onclick="moveL(this.form);" /> </td>
		<td> <select name="my" size="8"> 
		</select> </td></tr></table>
	</form>

</body>
</html>
```

