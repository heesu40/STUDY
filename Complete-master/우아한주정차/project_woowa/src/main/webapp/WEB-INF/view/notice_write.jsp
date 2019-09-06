<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri = "http://java.sun.com/jsp/jstl/functions" prefix = "fn" %>

<html>
<head>  
    
  <title>Write</title>
   
  <!-- style, css 시작 -->  
  <link rel='stylesheet' href='./source/css/style.css' type='text/css' media='all'/> 
  
  <style>  
    table { width: 60%; margin: auto; padding : 10px; }
    .logo { width:auto; height:auto; width:400px; }   
    .listbutton { float:right; margin-left:15px; margin-top:5px; width:80px; }
  </style>
   <!-- style, css 끝 -->
   
</head>

<!-- body 시작 -->
<body class="home page page-template page-template-template-portfolio page-template-template-portfolio-php">

<div id="page">
  <div class="container">
  
  <!-- header 시작 -->    
  <header id="masthead" class="site-header">
	<div style='text-align:right'>
    		${user.username}님 공지사항 작성 중 &nbsp;&nbsp;
	</div>
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
  
  </header>
  <!-- header 끝 -->
  
  <!-- Main Content 시작 -->     
    <div id="content" class="site-content">
      <div id="primary" class="content-area column full">
        <main id="main" class="site-main">
        
          <!-- article 시작 -->    
          <article id="post-39" class="post-39 page type-page status-publish hentry">
  
          <!-- 글쓰기 시작 -->
		<form id='notice' method='post' action='./notice_write.do' enctype="multipart/form-data">
          <!--  enctype="multipart/form-data" xxxxx-->
           <table width='100%'>
            <tr><td>작성자</td><td><input type='text' name='managername' value='${user.username}' size="10"></td></tr>
              <tr><td>제목</td><td><input type='text' name='subject' size="50"></td></tr> 
              <tr><td>파일 첨부</td><td><input type='file' name='filename' rows='20'></td></tr>              
              <tr><td>내용</td><td><textarea cols='30' name='contents' id='contents' rows='10'></textarea></td></tr>
              <tr><td colspan='2'>         
   	  		<input type='submit' value="글쓰기" class="listbutton"> 
			<a href="./notice.do" ><input type='button' value="목록" class="listbutton"></a>
              </td></tr>
            </table>
              
          </form>
          <!-- 글쓰기 끝 -->

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