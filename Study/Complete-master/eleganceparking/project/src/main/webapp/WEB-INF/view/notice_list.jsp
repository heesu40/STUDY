<%@ page contentType="text/html;charset=utf-8" %> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri = "http://java.sun.com/jsp/jstl/functions" prefix = "fn" %>
<%!  
  int numPerPage = 10;
  int numPerBlock = 10;   
%>
<html>
<head>
  
  <title>Notice</title>
   
  <!-- style, css 시작 -->
  <link rel='stylesheet' href='./source/css/style.css' type='text/css' media='all'/>
    
  <style>
   .logo{ width:400px; }    
    
    #loginbutton { margin-top:3px; width:90px  }
    #joinbutton { margin-top:3px; width:90px; }   
     
    @media screen and (min-width:400px) { .img{ width:300px} 
    .parkingicon { text-align:center } .stopicon { text-align:center }
    .loginicon{text-align:right}
    .joinicon{text-align:right}   
    }
    
    @media screen and (min-width:800px) { .img{ width:400px} 
    .parkingicon { float:left; margin-left:30px; }
    .stopicon { display:inline-block; float:right; margin-right:30px; }
    .mom {display:-webkit-box; -webkit-box-orient:horizontal; float:right;}
    .loginicon { margin-left:10px; -webkit-box-ordinal-group:1;}
    .joinicon { margin-left:10px; -webkit-box-ordinal-group:2;}         
    }
        
    .w3-content{margin-left:auto;margin-right:auto;max-width:980px;}
    .w3-modal{z-index:3;display:none;padding-top:100px;position:fixed;left:0;top:0;width:100%;height:100%;overflow:auto;background-color:rgb(0,0,0);background-color:rgba(0,0,0,0.4)}
    .w3-modal-content{margin:auto;background-color:#fff;position:relative;padding:0;outline:0;width:600px}
    
    @media (max-width:600px){.w3-modal-content{margin:0 10px;width:auto!important}.w3-modal{padding-top:30px}
    .w3-dropdown-hover.w3-mobile .w3-dropdown-content,.w3-dropdown-click.w3-mobile .w3-dropdown-content{position:relative}  
    .w3-hide-small{display:none!important}.w3-mobile{display:block;width:100%!important}.w3-bar-item.w3-mobile,.w3-dropdown-hover.w3-mobile,.w3-dropdown-click.w3-mobile{text-align:center}
    .w3-dropdown-hover.w3-mobile,.w3-dropdown-hover.w3-mobile .w3-btn,.w3-dropdown-hover.w3-mobile .w3-button,.w3-dropdown-click.w3-mobile,.w3-dropdown-click.w3-mobile .w3-btn,.w3-dropdown-click.w3-mobile .w3-button{width:100%}} 
    @media (max-width:768px){.w3-modal-content{width:500px}.w3-modal{padding-top:50px}}
    @media (min-width:993px){.w3-modal-content{width:900px}.w3-hide-large{display:none!important}.w3-sidebar.w3-collapse{display:block!important}}       
  
    #xbutton { float:right; margin-right:10px; margin-top:5px; }
    #closebutton { float:right; }
    #infonote { padding-left:40px; padding-top:10px; }       
  </style>

  <!-- style, css 끝 -->
    
  <script>
    function userLogout() { location.href = "logout.do" }  
  </script>
  <script src='./source/js/non_user_alert.js'></script>
  
</head>

<!-- body 시작 -->
<body class="home page page-template page-template-template-portfolio page-template-template-portfolio-php">

  <div id="page">
    <div class="container">  
    
    <!-- header 시작 -->		
    <header id="masthead" class="site-header">
 
      <c:if test='${empty user}'>
       <div class="mom">
        <div class='loginicon'>
          <form action="./login.do" method="post">          
        	 <a>아이디 : </a><input type="text" name="useremail" size="15" maxlength="30"/>
        	 <a>비밀번호 : </a><input type="password" name="userpwd" size="15" maxlength="12"/>
        	 <input type="submit" id="loginbutton" value="로그인" />
           </form>
        </div>
        <div class='joinicon'>  
          <a href="./join.do"><input type="button" id='joinbutton' value="회원가입"></a>
        </div>   
       </div>
      </c:if>

	  <c:if test='${not empty user}'>
		<div style='text-align:right'>
    		${user.username}님 로그인 중 &nbsp;&nbsp;
    		<input type="submit" id="logout" onClick="userLogout()" value="로그아웃" />
		</div>
	 </c:if> 
      
      <br>
      <br>
      <br>
      <br>
 
 
       <!-- 제목 시작 -->            
      <div class="site-branding">       
        <a href="./main.do"><img src="./source/img/logo.jpg" class="logo" /></a>
        <br>
      	<h2 class="site-description"><a>위치기반 &nbsp;&nbsp;&nbsp;주차장 / 주정차 &nbsp;&nbsp;&nbsp;정보</a></h2>
      </div>
      <!-- 제목 끝 -->  
      
      <!-- 네비, nav 시작 -->    
      <nav id="site-navigation" class="main-navigation">        
          <div class="menu-container">
            <ul id="menu-1" class="menu">               
              <li><a href="./parking.do"><img src="./source/img/parking.png" width="45px"/>&nbsp;&nbsp;</a></li>
              <li><a href="./stop.do"><img src="./source/img/stop.png" width="45px"/></a>&nbsp;&nbsp;</a></li>
              <li><a onclick="document.getElementById('info').style.display='block'"><img src="./source/img/information.png" width="45px"/>&nbsp;&nbsp;</a></li>                
              <li><a href="./notice.do"><img src="./source/img/notice.png" width="45px"/></a></li>                
            </ul>
           </div>
      </nav>
      <!-- 네비, nav 끝 -->
     
     
  <!-- 이용안내 시작 -->
  <div id="info" class="w3-modal">
    
    <div class="w3-modal-content w3-animate-top w3-card-4">
      <header class="w3-container w3-teal w3-center w3-padding-32"> 
        <span onclick="document.getElementById('info').style.display='none'" 
              class="w3-button" id="xbutton">&times;</span>
      </header>
      
      <div class="w3-container" >
      
        <div id="infonote">          
          <h3>이용 안내</h3>
          <p>&nbsp;</p>
          <h4>본 프로젝트는 </h4>
          <h4>오픈API를 활용하여 주차장 및 주정차 정보를 제공하는 웹페이지이며</h4>
          <h4>누구나 자유롭게 사용가능합니다.</h4>
          <p>&nbsp;</p>
          <p>&nbsp;</p>
          <h4>공공데이터 활용 현황</h4>
          <p>&nbsp;</p>
          <p>주차장 정보</p>
          <p>주정차 금지(지정)구역</p>  
          <p>불법주정차 단속현황</p>
          <p>거주자우선 주차정보</p>         
          <p>&nbsp;</p>
          <p>&nbsp;</p>
        </div>
        
       <button class="w3-button w3-red w3-section" onclick="document.getElementById('info').style.display='none'" id="closebutton" > Close <i class="fa fa-remove"></i></button>       
      </div>
    </div>
    
  </div>
  <!-- 이용안내 시작 끝 -->      
  
  <!-- 이용안내 함수 -->    
  <script>  
  var modal = document.getElementById('info');
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  } 
  </script>
            
    </header>
    <!-- header 끝 --> 
          
  <!-- Main Content 시작 -->     
  <div id="content" class="site-content">
    <div id="primary" class="content-area column full">
      <main id="main" class="site-main">
      
      <!-- article 시작 -->    
      <article id="post-39" class="post-39 page type-page status-publish hentry">
         
      <!-- 게시판 시작 -->
      <table width=100%>
      <tr><th>번호</th><th>제목</th><th>작성자</th>
        <th>작성일</th><th>조회수</th></tr>
  
      <c:forEach var="row" items="${list}">
        <tr><td colspan=5 height=1 background=./soure/img/dotline.gif></td></tr>
        <tr><td>${row.bid}</td><td>     
        <a href="./notice_view.do?bid=${row.bid}">${row.subject}</a>
        </td>
          <td>${row.managername}</td>
          <td>${row.idate}</td>
          <td style='text-align:right'>${row.rcount}</td>

      <!-- 공지글작성 --> 
      </c:forEach>
        <tr><td colspan=5 height=1 background=./soure/img/dotline.gif></td></tr>
      </table>
      
      <div style='text-align:right'><br><br>
      <c:if test='${empty user}'>
        <input type="button" value="글작성" onclick="non_user()">
      </c:if>
      
      <c:if test='${not empty user }'>
      <a href=./notice_write.do><input type="button" value="글작성"></a>
      </c:if>
      </div>
      
      <div style='text-align:center'> 
         <form method='post' action='./notice_search.do'>
          <input type="hidden" name="page" value="1">
          <select name='searchKey'>
            <option value='subject'>제목</option>   
          </select>
            <input type="search" name="searchWord" >
            <input type="submit" value="검색">
         </form>
      </div>
   
          </article>         
    
    </main>     
  </div>
</div>
<!-- Main Content 끝 --> 
      
      <br>
      <br>
      <br>
      <br>                     
 
 </div>
      
 <!-- footer 시작 -->  
  <footer id="colophon" class="site-footer">
    <div class="container">
      <div class="site-info">
      <br>
      <h3 style="font-family:'';color: #ccc;font-weight:300;text-align: center;margin-bottom:0;margin-top:0;line-height:1.4;font-size: 20px;">코.하.친 (코딩하는친구들)</h3><br>
      <a>Training for the 4th Industrial Revolution.</a><br>
      <a>Open API를 활용한 빅데이터 전처리·시각화(B반), </a>
      <a>2019</a>
    </div>
  </div>
  </footer> 
 <!-- footer 끝 -->
 
</div>

</body>
</html>