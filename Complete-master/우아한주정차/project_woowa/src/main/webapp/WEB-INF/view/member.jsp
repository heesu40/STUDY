<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri = "http://java.sun.com/jsp/jstl/functions" prefix = "fn" %>

<html>
<head>  
    
  <title>Join</title>
   
  <!-- style, css 시작 -->  
  <link rel='stylesheet' href='./source/css/style.css' type='text/css' media='all'/> 
  
  <style>  
    table { width: 60%; margin: auto; padding : 10px; }
    .logo{ width:auto; height:auto; width:400px; }
    .inputbutton{ float:right; margin-left:15px; margin-top:5px; width:120px; }  
  </style>
   <!-- style, css 끝 -->
   
</head>

<!-- body 시작 -->
<body class="home page page-template page-template-template-portfolio page-template-template-portfolio-php">

<div id="page">
  <div class="container">
  
  <!-- header 시작 -->    
  <header id="masthead" class="site-header">

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
  
          <!-- 회원가입 내용시작 -->  
          <form method='post' action='./join.do' >
            <table >     
              <tr><td colspan=2 height=1 background=./source/img/dotline.gif></td></tr>              
                <tr>
                 <th style="width:100;text-align:left;"><a>이름</a></th>
                 <td><input type="text" name="username"> </td>
                </tr>                
                <tr>
                  <th style="width:100;text-align:left;"><a>이메일</a></th>
                    <td>
                      <input type='text' name="useremail"><a>&nbsp;@</a>
                      <input type='text' name="email_dns">
                        <select name="dns_Add">
                           <option value="">직접입력</option>
                           <option value="naver.com">naver.com</option>
                           <option value="nate.com">nate.com</option>                           
                           <option value="daum.net">daum.net</option>                           
                           <option value="gmail.com">gmail.com</option>
                           <option value="hanmail.net">hanmail.net</option>
                        </select>
                   </td>
               </tr>
              
               <tr>
                 <th style="width:100;text-align:left;"><a>비밀번호</a></th>
                 <td><input type="password" name="userpwd"> </td>
               </tr>              
               <tr>
                 <th><a>비밀번호 </a><a>확인</a></th>
                 <td><input type="password" name="mbpw_re"></td>
                </tr>       
               <tr><td colspan=2 height=1 background=./source/img/dotline.gif></td></tr>     
           </table>
           <br>                 
           <table>      
               <tr>
                 <td colspan="2" align="center">
                   <input type="submit" value="회원가입" class="inputbutton">
                 </td>
               </tr>           
           </table>                   
        </form>
        <!-- 회원가입 내용끝 -->

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