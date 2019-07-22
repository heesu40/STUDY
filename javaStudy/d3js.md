# D3.js

http://d3js.org 공식 사이트

D3(Data-Driven Documents) 데이터 중심의 문서

## D3.js란?

	#### 특징

1. 데이터를 시각적으로 표현하는 자바스크립트 라이브러리
2. 다양한 그래프
3. 애니메이션 적용 가능
4. 스마트폰 등에 상호작용가능(기기에 따라 크기가 다르게 적용 할 수 있다는 뜻)
5. 버튼 조각에 따라 상호작용 가능
6. 특정 종류의 그래프 그리기 기능은 없음
   - HTML의 DOM요소나 SVG 요소,Canvas요소를 이용하여 그림(속성, 좌표 이용 해서)
   - 그래프를 그릴 떄는 주로 SVG(Scalable Vector Graphics)를 사용(W3 사이트 참고)
7. d3객체(모든 기능이 들어 있는 객체)
   - 중심이 되는 객체

#### 기능

1. d3(core)
   - selections 요소 조작



#### 체인

- 밑에는 예시다

```js
d3.select("#myGraph")
  .selectAll("rect")
  .data(dataSet)//배열 객체
  .enter()//연결
  .append("rect")//
  .attr("x", 10) //속성 x를 10으로 지정

```



#### js 만드는 그래프 프로그램 구조

1. 데이터 읽기
   - CSV,TSV,JSON,TEXT
2. 표시 그래프 지정
3. 필요한 SVG 도형 요소 준비
4. 요소 속성값 변경
   - attr()
   - style()
   - 주의해야 하는데 DOM같은 경우 css속성을 사용하면 되는데 SVG의 경우 그거에 맞는 속성명을 써 주어야 한다(주의하자)
5. 애니메이션 처리(선택)
   - transition()
6. 이벤트 처리(선택)
   - on()



# 실습

#### 연습

1. 다이나믹 웹 프로젝트 만들자
2. WebContent 아래 index.jsp를 만들어 실행하여 웹상태 확인
3. WebContent아래 chart1.html 만든다

###### 가로 막대 하나 그리기

chart1.hmtl

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart1.js"></script>
</head>
<body>
<h3>가로 막대 그래프</h3>
<svg id="myGraph"></svg>
</body>
</html>
```

WebContent아래 js파일 만들자

그후 javaScript 에 javaScript Source File 을 클릭후 이름은 chart1.js

######chart1.js

```js
window.addEventListener("load",function(){
	//1.데이터 준비
	var dataSet=[300,150,10,80,230];
	
	d3.select("#myGraph")
		.append("rect")
		.attr("x",0)
		.attr("y",0)
		.attr("width", dataSet[0])
		.attr("height","20px")
		
		
});
```

###### 가로막대 여러개 그리기

함수를 해서 값 리턴하게 만들면 다양하게 그릴 수 있다.

•데이터셋에 따라 자동으로 요소를 추가하고 처리해주는 기능 (메소드) - selectAll(), data(), enter()

1. 교체하거나 추가할 대상이 될 요소를 selectAll()로 선택

2. Data()로 준비한 데이터를 데이터셋으로 내부에 저장

3. enter() 이후의 처리가 적용 – 표시할 요소보다 데이터가 많을 때 사용

4. append()로 추가할 요소와 데이터 연결

5 .exit()로 요소 삭제





chart2.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart2.js"></script>
</head>
<body>
<h3>가로 막대 그래프- 데이터셋의 데이터 수만큼 그리기</h3>

<svg id="myGraph"></svg>
</body>
</html>
```

chart2.js

```js
window.addEventListener("load",function(){
	//1.데이터 준비
	var dataSet=[300,150,10,80,230];
	
	d3.select("#myGraph")
		.selectAll("rect")
		.data(dataSet)//데이터 설정(배열을 전달했따)
		.enter()//데이터 수에 따라 rect요소 생성
		.append("rect")//생성된 요소 추가
		.attr("x",0)//배열을 전달했기 떄문에 배열따라 수행한다., x값은 0으로(왜나하면 0에서 시작하므로)
		.attr("y",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return i*30; //가로 막대의 간격은 30씩 떨어진다(간격)
		})
		.attr("width", function(d,i){
			return d+"px";//단위를 붙여서 리턴해야한다. 배열의 실제 값을 리턴하는 것.
		})
		.attr("height","20px")
		
		
});
```

###### 막대그래프 스타일 적용(svg요소 적용)

chart3.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border:1px solid black;}
#myGraph rect{
	stroke:rgb(160,0,0);
	stroke-width:1px;
	fill : rgb(136,210,242);
}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart2.js"></script>
</head>
<body>
<h3>가로 막대 그래프- 스타일(svg)</h3>

<svg id="myGraph"></svg>
</body>
</html>
```

###### 이벤트 적용(on()사용)

chart4.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border:1px solid black;}
#myGraph rect{
	stroke:rgb(160,0,0);
	stroke-width:1px;
	fill : rgb(136,210,242);
}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart4.js"></script>
</head>
<body>
<h3>가로 막대 그래프- 이벤트</h3>
<svg id="myGraph"></svg>
<button id="updateButton">데이터업데이트</button>
</body>
</html>
```

chart4.js

```js
window.addEventListener("load",function(){
	//1.데이터 준비
	var dataSet=[300,150,10,80,230];
	
	d3.select("#myGraph")
		.selectAll("rect")
		.data(dataSet)//데이터 설정(배열을 전달했따)
		.enter()//데이터 수에 따라 rect요소 생성
		.append("rect")//생성된 요소 추가
		.attr("x",0)//배열을 전달했기 떄문에 배열따라 수행한다.
		.attr("y",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return i*30; //가로 막대의 간격은 30씩 떨어진다
		})
		.attr("width", function(d,i){
			return d+"px";//단위를 붙여서 리턴해야한다. 배열의 실제 값을 리턴하는 것.
		})
		.attr("height","20px")
		

		
	d3.select("#updateButton")
		.on("click", function(){
		       dataSet=[20, 230, 150,10, 20]; //새로운 데이터로 변경
		       d3.select("#myGraph")
		         .selectAll("rect")
		         .data(dataSet)
		         .attr("width", function(d, i) {
		             return d+"px";
		          });
		     });
	
		
		
});

	
```

###### 애니메이션 처리

- transition()  - 메서드 체인에 지정된 속성값에 따라 시간이 흐를수록 변화하는 처리를 수행
- delay() -  애니메이션 시작까지의 대기 시간을 지정,  파라미터에 함수를 지정하여 데이터셋의 데이터나 표시 순서를 전달,  밀리초 단위로 지정
- Duration() – 애니메이션 시간에서 종료까지의 시간 지정

chart5.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border:1px solid black;}
#myGraph rect{
	stroke:rgb(160,0,0);
	stroke-width:1px;
	fill : rgb(255,192,203);
}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart5.js"></script>
</head>
<body>
<h3>가로 막대 그래프- 애니메이션</h3>
<svg id="myGraph"></svg>
<button id="updateButton">데이터업데이트</button>
</body>
</html>
```

chart5.js

```js
window.addEventListener("load",function(){
	//1.데이터 준비
	var dataSet=[300,150,10,80,230];
	
	d3.select("#myGraph")
		.selectAll("rect")
		.data(dataSet)//데이터 설정(배열을 전달했따)
		.enter()//데이터 수에 따라 rect요소 생성
		.append("rect")//생성된 요소 추가
		.attr("x",0)//배열을 전달했기 떄문에 배열따라 수행한다.
		.attr("y",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return i*30; //가로 막대의 간격은 30씩 떨어진다
		})
		.attr("width", "0px")
		.attr("height","20px")
		.transition()
		.delay(function(d,i){
			return i*500;
		})
		.duration(2500)//다섯개니까 500*5의 값(애니메이션 지속시간)
		.attr("width", function(d,i){
			return d+"px"; 
		})
		d3.select("#myGraph")
		.selectAll("rect")
		.on("click",function(){
			d3.select(this)
			.style("fill","cyan")
			
		});//rect가 이벤트가 발생하는 것이다. 왜냐? 죄다 rect로 받았기 때문에
		
		

		
	d3.select("#updateButton")
		.on("click", function(){
		      for(var i=0;i<dataSet.length;i++){
		    	   dataSet[i]=Math.floor(Math.random()*320);
		       }
		       d3.select("#myGraph")
		         .selectAll("rect")
		         .data(dataSet)
		         .transition()//변환
		        
		         .attr("width", function(d, i) {
		             return d+"px";
		          });
		     });
	
		
		
});

	
```

###### 외부데이터 처리

엑셀에 저장을 한다(위치는 chart6.html 과 같은 위치며 저장시 data.csv로 한다.)

| item1 | item2 | item3 |
| ----- | ----- | ----- |
| 120   | 60    | 300   |
| 60    | 50    | 80    |
| 300   | 30    | 90    |
| 80    | 10    | 40    |
| 220   | 200   | 150   |



chart6.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border:1px solid black;}
#myGraph rect{
	stroke:rgb(160,0,0);
	stroke-width:1px;
	fill : rgb(255,192,203);
}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart6.js"></script>

</head>
<body>
<h3>가로 막대 그래프- 외부데이터 불러오기</h3>
<svg id="myGraph"></svg>
<button id="updateButton">데이터업데이트</button>

</body>
</html>
```





```js
window.addEventListener("load",function(){

	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	var dataSet=[];//배열을 준비하고
	d3.csv("data.csv")//파일 불러와서
	.then(function(data){
	 console.log(data);//data 확인 가능
	for(var i=0;i<data.length;i++){//데이터의 줄 수 만큼 반복
		dataSet.push(data[i].item1);//item1 레이블의 데이터를 
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")
		.data(dataSet)//데이터 설정(배열을 전달했따)
		.enter()//데이터 수에 따라 rect요소 생성
		.append("rect")//생성된 요소 추가
		.attr("x",0)//배열을 전달했기 떄문에 배열따라 수행한다.
		.attr("y",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return i*30; //가로 막대의 간격은 30씩 떨어진다
		})//그래프 출력
		
		.attr("height","20px")
		.attr("width", function(d,i){
			return d+"px"; 
		})
	});
	
	)}
```

###### 눈금표시, 수치 표시 

chart7.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border:1px solid black;}
#myGraph rect{
	stroke:rgb(255,192,203);
	stroke-width:1px;
	fill : rgb(255,192,203);
}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/chart7.js"></script>

</head>
<body>
<h3>가로 막대 그래프- 축,눈금</h3>
<svg id="myGraph"></svg>


</body>
</html>
```

chart7.js

```js
window.addEventListener("load",function(){

	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	var dataSet=[];//데이터를 지정할 배열을 준비
	d3.csv("data.csv")
	.then(function(data){
		console.log(data);
		
	for(var i=0;i<data.length;i++){//데이터의 줄 수 만큼 반복
		dataSet.push(data[i].item1);//item1 레이블의 데이터를 
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")
		.data(dataSet)//데이터 설정(배열을 전달했따)
		.enter()//데이터 수에 따라 rect요소 생성
		.append("rect")//생성된 요소 추가
		.attr("x",0)//배열을 전달했기 떄문에 배열따라 수행한다.
		.attr("y",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return i*30; //가로 막대의 간격은 30씩 떨어진다
		})//그래프 출력
		
		.attr("height","20px")
		.attr("width", function(d,i){
			return d+"px"; 
		})
		
		var scale = d3.scaleLinear()//선형 스케일 설정
		.domain([0,300])
		.range([0,300])
		var axis=d3.axisBottom(scale);
	                   
	    
	    //눈금을 설정하고 표시
	    d3.select("#myGraph")
//	    	.attr("width", 300)
//	    	 .attr("height", 250)
	    	.append("g")//그룹화한다.
	    	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	    	.attr("transform","translate(0,"+((1+dataSet.length)*25+5)+")")
	    	.call(axis)//call()로 눈굼을 표시할 함수를 호출
	    			
	    		
			
	    
		
	})//then() end
	

	});
	

	
```

눈금표시

- translate()는 파라미터에 지정한 만큼 XY 좌표를 이동시킵니다
- scale() 확대 비율
- rotate()  회전 각도를 지정
- skewX(), skewY()  기울기를 지정

```js
.attr("transform", "translate(10, "+(1+dataSet.length) * 20+5) +")")

```

###### 도형그리기

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
 svg{
width:340px;
height:340px;
border:1px solid black;
}
rect {
stroke-width:4px;
stroke:black;
fill:orange;
}
circle{
opacity:0.75;
fill:blue;
} 
</style>
</head>
<body>
<svg>
<!-- <rect x="30" y="20" width="200" height="100"/>
<rect x="30" y="150" width="200" height="100" rx="20" ry="20"/>
<circle cx="190" cy="140" r="80"/> -->



<!-- <path d="M80,50 L220,90 L280,200"/> -->
<!-- <path d="M10,110 C80,-100 150, 80 300 110"/> -->

<!-- <rect x="30" y="20" width="200" height="100"
style="fill:red;stroke:blue;stroke-width:10px"/>
 -->
 
<!--  <svg width=400>
 <rect x="200" y="0" width="1" height="160" style="fill:red"/>

<text x="200" y="40"  text-anchor="short" style="fill:black">SVG 텍스트 예제</text>
<text x="200" y="80" text-anchor="middle" style="fill:black">SVG 텍스트 예제</text>
<text x="200" y="120" text-anchor="end" style="fill:black">SVG 텍스트 예제</text>
 </svg>
 -->

<!-- 그룹으로 스타일을 적용해볼까 함 -->
<h1>도형 그룹화</h1>
<svg>
<g style="opacity:0.25"><!-- 투명도 흐리게 나온다. -->
<rect x="200" y="50" width="100" height="80"/>
<text x="200" y="40" text-anchor="start" style="fill:cyan">sample Text</text>
</svg>

<!-- 도형이동 -->
<h1>도형 이동</h1>
<svg>
<g transform="translate(-200,40)"><!-- -200,40 만큼 이동한다. -->
<rect x="200" y="50" width="100" height="80"/>
<text x="200" y="40" text-anchor="start" style="fill:cyan">sample Text2</text>
</svg>

<h1>도형 회전</h1>
<svg>
<g transform="rotate(45,200,100)"><!-- (회전정도,x,y) -->
<rect x="200" y="50" width="100" height="80"/>
<text x="200" y="40" text-anchor="start" style="fill:cyan">sample Text3</text>

</svg>

<h1>도형 확대</h1>
<svg>
<g transform="scale(2.0)"><!-- 1.0이 기본이다. -->
<rect x="20" y="50" width="100" height="80"/>
<text x="200" y="40" text-anchor="start" style="fill:cyan">sample Text4</text>

</svg>

</svg>
<br>
M 절대 좌표/m 상대 좌표:이동 관련 명령<br> 
Z,z는 패스를 닫음<br>
L 절대 좌표, ㅣ 상대 좌표:그리기 관련 명령<Br>
C 곡선 절대 좌표 ,c 곡선 상대 좌표 :곡선 관련 명령
A 곡선 절대 좌표,a 곡선상대 좌표:곡선 그리기 관련 명령
</body>
</html>
```

###### tsvRead(TSV 파일) 데이터에 따라 그래프 표시

tsvRead.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/tsvRead.js"></script>
</head>
<body>
<h1>(TSV 파일)데이터에 따라 그래프 표시</h1>
<svg id="myGraph"></svg>
</body>
</html>
```

tsvRead.js

```js
window.addEventListener("load",function(){

	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.tsv("data.tsv")
	.then(function(data){
		var dataSet=[];
		
		
	for(var i=0;i<data.length;i++){//데이터의 줄 수 만큼 반복
		dataSet.push(data[i].item1);//item1 레이블의 데이터를 
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		
		var scale = d3.scaleLinear()//선형 스케일 설정
		.domain([0,300])
		.range([0,300])
		var axis=d3.axisBottom(scale);
	                   
	    
	    //눈금을 설정하고 표시
	    d3.select("#myGraph")
//	    	.attr("width", 300)
//	    	 .attr("height", 250)
	    	.append("g")//그룹화한다.
	    	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	    	.attr("transform","translate(0,"+((1+dataSet.length)*25+5)+")")
	    	.call(axis)//call()로 눈굼을 표시할 함수를 호출
	    			
	    		
			
	    
		
	})//then() end
	

	});
	

	
```

data.tsv가 필요하다.........................알아서 찾길 바란다.

###### JSON파일 )데이터에 따라 그래프 표시

data.json(파일인데 이름을 이리 저장해 주자)

```json
[
	{ "item" : "상품A", "sales" : [ 150, 90, 300 ] },
	{ "item" : "상품B", "sales" : [ 70, 260, 110 ] },
	{ "item" : "상품C", "sales" : [ 20, 40, 280 ] },
	{ "item" : "상품D", "sales" : [ 80, 100, 50 ] },
	{ "item" : "상품E", "sales" : [ 190, 100, 220 ] }
]
```

dataJson.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>

#myGraph rect{
	stroke:rgb(255,192,203);
	stroke-width:1px;
	fill : rgb(255,192,203);
}
.axis text{
			font-family:sans-serif;
			font-size: 11px;
			}
.axis path,
.axis line(
			fill:none;
			stroke:black;
	)	
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://d3js.org/d3-axis.v1.min.js"></script>
<script src="./js/dataJson.js"></script>

</head>
<body>
<h3>(json)데이터에 따라 그래프표시- dataJson</h3>
<svg id="myGraph"></svg>


</body>
</html>
```

dataJson.js

```js
window.addEventListener("load",function(){

	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.json("data.json")
	.then(function(data){
		var dataSet=[];
		
		
	for(var i=0;i<data.length;i++){//데이터의 줄 수 만큼 반복
		dataSet.push(data[i].sales[0]);//item1 레이블의 데이터를 
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		

	})//then() end
	

	});
	

	
```

###### html 파일 )데이터에 따라 그래프 표시

data.html

```html

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>매출 데이터</title>
		<style>
			table, th, td { border: 1px solid gray; }
		</style>
	</head>
	<body>
		<h1>매출 데이터</h1>
		<table>
			<tr><th>상품A</th><th>상품B</th><th>상품C</th></tr>
			<tr><td>90</td><td>60</td><td>200</td></tr>
			<tr><td>130</td><td>160</td><td>250</td></tr>
			<tr><td>200</td><td>90</td><td>40</td></tr>
			<tr><td>160</td><td>40</td><td>90</td></tr>
			<tr><td>290</td><td>150</td><td>200</td></tr>
		</table>
	</body>
</html>

```

htmlRead.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/htmlRead.js"></script>
</head>
<body>
<h1>(html 파일)데이터에 따라 그래프 표시</h1>
<svg id="myGraph"></svg>
</body>
</html>



```

htmlRead.js

```js
window.addEventListener("load",function(){

	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.html("data.html").then(function(docFragment){
		var tr=docFragment.querySelectorAll("table tr");//
		var dataSet=[ ];//데이터를 저장할 배열을 준비
		
		
	for(var i=1;i<tr.length;i++){//데이터의 줄 수 만큼 반복
		var d = tr[i].querySelectorAll("td")[0].firstChild.nodeValue;//tr요소의 줄 수 -1만큼 반복(1번째
		dataSet.push(d);//상품 A의 데이터만 추출
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		
	
	    
		
	})//then() end
	

	});
	

	
```

###### xml파일)데이터에 따라 그래프 표시

data.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>

<datalist>
<data>
<item>상품A</item>
<sales>150</sales>
<sales>90</sales>
<sales>300</sales>
<sales>200</sales>
<sales>120</sales>
</data>
<data>
<item>상품B</item>
<sales>70</sales>
<sales>260</sales>
<sales>110</sales>
<sales>30</sales>
<sales>90</sales>
</data>
<data>
<item>상품C</item>
<sales>20</sales>
<sales>40</sales>
<sales>280</sales>
<sales>80</sales>
<sales>190</sales>
</data>
<data>
<item>상품D</item>
<sales>80</sales>
<sales>100</sales>
<sales>50</sales>
<sales>150</sales>
<sales>120</sales>
</data>
<data>
<item>상품E</item>
<sales>190</sales>
<sales>100</sales>
<sales>220</sales>
<sales>280</sales>
<sales>300</sales>
</data>
</datalist>
```



xmlRead.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/xmlRead.js"></script>
</head>
<body>
<h1>(xml파일)데이터에 따라 그래프 표시</h1>
<svg id="myGraph"></svg>
</body>
</html>
```

xmlRead.js

```js
window.addEventListener("load",function(){

	var dataSet=[];
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.xml("data.xml")
	.then(function(xmlRoot){
		var xmlData=xmlRoot.querySelectorAll("data");//data 요소를 추출
		var salesRoot=xmlData[0];//상품 A의 테이터만 추출
		var salesData=salesRoot.querySelectorAll("sales");//sales요소를
		
		
	for(var i=0;i<salesData.length;i++){//데이터의 줄 수 만큼 반복
		var d=salesData[i].firstChild.nodeValue;//데이터 읽어들이기
		dataSet.push(d);
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		
		var scale = d3.scaleLinear()//선형 스케일 설정
		.domain([0,300])
		.range([0,300])
		var axis=d3.axisBottom(scale);
	                   
	    
	    //눈금을 설정하고 표시
	    d3.select("#myGraph")
//	    	.attr("width", 300)
//	    	 .attr("height", 250)
	    	.append("g")//그룹화한다.
	    	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	    	.attr("transform","translate(0,"+((1+dataSet.length)*25+5)+")")
	    	.call(axis)//call()로 눈굼을 표시할 함수를 호출
	    			
	    		
			
	    
		
	})//then() end
	

	});
	

	
```



###### text파일)데이터에 따라 그래프 표시

data.txt

```file
�곹뭹A/10/90/120/60/300
�곹뭹B/70/260/110/90/180
�곹뭹C/20/40/280/240/220
�곹뭹D/80/100/50/90/130
�곹뭹E/120/100/22/66/160/300
```

textRead.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/textRead.js"></script>
</head>
<body>
<h1>(txt파일)데이터에 따라 그래프 표시</h1>
<svg id="myGraph"></svg>
</body>
</html>
```



textReat.js

```js
window.addEventListener("load",function(){

	var dataSet=[];
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.text("data.txt")
	.then(function(plainText){
		
		var Data=plainText.split("\x0a");//\oxoa는 줄바꿈 코드
		var sales=Data[0].split("/");//처음 1줄을 /rnqnswkfh sksndj xpdlxjfh
		
		
		
	for(var i=0;i<sales.length;i++){//데이터의 줄 수 만큼 반복
		
		dataSet.push(sales[i]);
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		
		var scale = d3.scaleLinear()//선형 스케일 설정
		.domain([0,300])
		.range([0,300])
		var axis=d3.axisBottom(scale);
	                   
	    
	    //눈금을 설정하고 표시
	    d3.select("#myGraph")
//	    	.attr("width", 300)
//	    	 .attr("height", 250)
	    	.append("g")//그룹화한다.
	    	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	    	.attr("transform","translate(0,"+((1+dataSet.length)*25+5)+")")
	    	.call(axis)//call()로 눈굼을 표시할 함수를 호출
	    			
	    		
			
	    
		
	})//then() end
	

	});
	

	
```

###### 데이터에 따라 그래프 표시



mydata.txt

```
상품A|상품B|상품C|상품D|상품E|상품F
120|90|120|90|200|130
90|160|110|90|190|50
20|80|280|240|200|60
10|20|80|40|140|160
30|40|50|220|150|80
50|120|30|85|100|260
60|180|210|200|220|190
```

mydataRead.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="./js/mytextRead.js"></script>
</head>
<body>
<h1>(txt파일)데이터에 따라 그래프 표시</h1>
<svg id="myGraph"></svg>
</body>
</html>
```

mydataRead.js

```js
window.addEventListener("load",function(){

	var dataSet=[];
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.dsv("|","mydata.txt")
	.then(function(data){
		
	console.log(data);
		
		
		
	for(var i=1;i<data.length;i++){//데이터의 줄 수 만큼 반복
		
		dataSet.push(data[i]["상품A"]);
		
	}//dataSet에 저장을 한후
	
	
	d3.select("#myGraph")
		.selectAll("rect")//rect요소 지정
		.data(dataSet)//데이터 설정(배열을 전달했따) 데이터를 요소에 연결
		.enter()//데이터 수에 따라 rect요소 생성 데이터 개수만큼 반복
		.append("rect")//데이터 개수만큼 rect요소가 추가
		.attr("class","bar")//CSS클래스를 지정
		.attr("width",function(d,i){//d 는 배열의 값이고 i는 배열의 인덱스 파라미터가 넘어간다.
			return d; 
		})
		
		.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		
		var scale = d3.scaleLinear()//선형 스케일 설정
		.domain([0,300])
		.range([0,300])
		var axis=d3.axisBottom(scale);
	                   
	    
	    //눈금을 설정하고 표시
	    d3.select("#myGraph")
//	    	.attr("width", 300)
//	    	 .attr("height", 250)
	    	.append("g")//그룹화한다.
	    	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	    	.attr("transform","translate(0,"+((1+dataSet.length)*25+5)+")")
	    	.call(axis)//call()로 눈굼을 표시할 함수를 호출
	    			
	    		
			
	    
		
	})//then() end
	

	});
	

	
```

###### 테이터 추가/ 갱신에 따라 그래프 표시

WebContent 아래 datas파일을 만든다.

그 후 선생님이 주신 mydata4,5,6를 넣어준다.

modify1.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg{width: 320px; height: 240px; border:1px solid black;}
.bar{fill:orange;}
</style>
<script src="https://d3js.org/d3-dsv.v1.min.js"></script>
<script src="https://d3js.org/d3-fetch.v1.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://d3js.org/d3-axis.v1.min.js"></script>
<script src="./js/modify1.js"></script>
</head>
<body>
<h1>데이터 추가/갱신에 따라 그래프 표시</h1>
<div>

<button data-src="./datas/mydata4.csv">mydata4.csv불러오기</button>
<button data-src="./datas/mydata5.csv">mydata5.csv불러오기</button>
<button data-src="./datas/mydata6.csv">mydata6.csv불러오기</button>

</div>
<svg id="myGraph"></svg>
</body>
</html>
```

modify1.js

```js
window.addEventListener("load",function(){

	var barElements; // 막대그래프의 막대 요소를 저장할 변수
	
	//1. 데이터 준비-csv파일을 불러와 그래프 그리기
	//데이터를 지정할 배열을 준비
	d3.selectAll("button").on("click",function(){
		var csvFile=this.getAttribute("data-src"); //data-src 속성을 읽어
		var dataSet=[];
		
		d3.csv(csvFile).then(function(data){
			for(var i=0;i<data.length;i++){//데이터 줄 수 만큼 반복
				dataSet.push(data[i]["상품A"]);//상품 Adml 레이블 테이터만
				
			}
			
			barElements=d3.select("#myGraph")
			.selectAll("rect")//rect 요소 지정
			.data(dataSet)//데이터를 요소에 연결
			
			barElements.enter()//데이터 개수만ㅋ늠 반복
			.append("rect")
			.attr("class","bar")//css클래스를 지정
			.attr("width",function(d,i){//넓이 지정, 2번째 파라미터에 함수
				return d;//테이터 값을 그대로 넓이로 반환
			})
			.attr("height",20)//높이 지정
		.attr("x",0)//x좌표를 0으로 함
		.attr("y", function(d,i){//Y좌표를 지정함
			return i*25;//표시 순서에 25를 곱해 위치를 계산
		})
		.attr("width",function(d,i){//넓이를 지정, 2번째 파라미터에 함수
			return d;//데이터 값을 그대로 넓이로 변환
		})
		barElements
		.exit()//삭제 대상 요소 추출
		.remove()//요소 삭제
	
	
	});
		
		

	    		
			
	    
		
	})//then() end
	

	});
	

	
```



## 복습

1. 객체 선택은 

```js
	d3.select("#myGraph")            //SVG 요소를 지정
		.selectAll("rect")               //SVG로 사각형을 표시할 요소를 지정(객체 선택)
		.data(dataSet)                   //SVG 사각형 생성
		.enter()                         //데이터 수에 따라 rect 요소 생성(생성)
		.append("rect")
		.attr("x", 0)                    //가로형 막대그래프이므로 X 좌표를 0으로 설정()
		.attr("y",  function(d, i) {     //Y 좌표를 배열의 순서에 따라 계산    
	              return  i*30;})   //막대그래프의 높이를 30px 단위로 계산
	     .attr("width", function(d, i){
	    	return d+"px";
	    })						   //데이터의 값을 그대로 넓이로 함                
	    .attr("height", "20px")
```

2. D3.js로 만들 그래프의 프로그램 구조  

- 데이터 읽어들이기 
  - CSV(점으로 구분짓는 파일명의 경우), TSV, XML, JSON, TEXT(어떤 파일의 경우 어떤 속성을 쓰는지)
- 표시할 그래프 지정
  - D3.js의 레이아웃 객체를 지정하여 데이터로부터 그래프를 표시해야 할 좌표를 계산하여 반환
- 그래프를 그리는 데 필요한 SVG 도형 요소 준비
  - DOM 요소나 Canavs 요소 생성 가능
- 요소의 속성값 변경
  - attr()
  - style()
- 필요하다면 애니메이션 처리
  - transition()
- 필요하다면 이벤트에 따른 처리
  - on()

### 세로막대그래프

###### 세로막대그래프&텍스트 설정

bar1.html

data값이 =height 임으로 y 좌표는 svgheight-height를 해주면 OK

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border: 1px solid black;}
.bar{fill : orange;}
.barNum{
font-size:9pt;
text-anchor:middle;})
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/bar1.js"></script>
</head>
<body>
<h3>세로형 막대그래프에 값을 표시</h3>
<svg id = "myGraph"></svg>
</body>
</html>
```

bar1.js

```js
window.addEventListener("load",function(){
	

//1. 데이터 준비
var dataSet = [120, 150, 10, 80, 230];
var svgHeight=240;//SVG의 요소의 높이
var barElements;//막대그래프의 막대 요소를 저장할 변수


barElements=d3.select("#myGraph")
  .selectAll("rect")//rect요소 지정
  .data(dataSet)//데이터를 요소에 연결
    
  barElements.enter()//데이터 수만큼 반복
	  			.append("rect")//데이터 수만큼 rect요소가 추가
	  			.attr("class","bar")//css 클래스 설정
	  			.attr("height", function(d,i){//높이 설정. 
	  				return d;//데이터 값 그대로 높이로 지정
	  			})
	  			.attr("width", 20)
	  			
	  			.attr("x",function(d,i){
	  				return i*25;
	  			})
	  			.attr("y", function(d,i){
	  				return svgHeight -d;
	  			})
	  			
	  			
barElements.enter()
.append("text")
.attr("class","barNum")
.attr("x",function(d,i){
	return i*25+10;
})
.attr("y",function(d,i){
	return svgHeight-d-5;
	})//y 좌표 설정 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
.text(function(d,i){
	return d;
})

});
```

###### 세로형 막대 그래프 눈금 표시



bar2.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border: 1px solid black;}
.bar{fill : cyan;}
.barNum{
font-size:9pt;
text-anchor:middle;})
.axis text{
font-family:sans-serif;
font-size:11px;}
.axis path,
.axis line{
fill:none;
stroke:black;}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/bar2.js"></script>
</head>
<body>
<h3>세로형 막대그래프에 눈금 표시</h3>
<svg id = "myGraph"></svg>
</body>
</html>
```

bar2.js

```js
window.addEventListener("load",function(){
	

//1. 데이터 준비
var dataSet = [120, 150, 10, 80, 220];
var offsetX=30;//x좌표의 오프셋(어긋남의 정도 총체적으로 이동?
var offsetY=10;//y좌표의 오프셋(어긋남의 정도 총체적 이동?
var svgHeight=240;//SVG의 요소의 높이
var barElements;//막대그래프의 막대 요소를 저장할 변수


barElements=d3.select("#myGraph")
  .selectAll("rect")//rect요소 지정
  .data(dataSet)//데이터를 요소에 연결
    
  barElements.enter()//데이터 수만큼 반복
	  			.append("rect")//데이터 수만큼 rect요소가 추가
	  			
	  			.attr("class","bar")//css 클래스 설정
	  			.attr("height", function(d,i){//높이 설정. 
	  				return d;//데이터 값 그대로 높이로 지정
	  			})
	  			.attr("width", 20)
	  			
	  			.attr("x",function(d,i){
	  				return i*25+offsetX;
	  			})
	  			.attr("y", function(d,i){
	  				return svgHeight -d-offsetY;
	  			})
	  			
	  			
barElements.enter()
.append("text")
.attr("class","barNum")
.attr("x",function(d,i){
	return i*25+10+offsetX;//offsetx추가
})
.attr("y",function(d,i){
	return svgHeight-d-offsetY;;
	})//y 좌표 설정 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
.text(function(d,i){
	return d;
})

    var yScale=d3.scaleLinear()
    .domain([0,300])//원래 크기
    .range([300,0]);//실제 출력 크기

var axis= d3.axisLeft(yScale);

d3.select("#myGraph").append("g")//g는 그룹핑 해주는 것?
.attr("class","axis")
.attr("transform",
		"translate("+offsetX+","+((svgHeight-300)-offsetY)+")")//눈금 표시위치를 했으므로 
//위에서 x 좌표의 값들을 30씩 옮겨주자.(그래프 값과 text값 모두 보내주어야 한다)
.call(axis)//표현하려고~

});
```

전체적으로 이동하기 위해서 var offsetX=30;  var offsetY=10;를 지정

###### 눈금간격 조정

bar3.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border: 1px solid black;}
.bar{fill : cyan;}
.barNum{
font-size:9pt;
text-anchor:middle;})
.axis text{
font-family:sans-serif;
font-size:11px;}
.axis path,
.axis line{
fill:none;
stroke:black;}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/bar3.js"></script>
</head>
<body>
<h3>눈금간격 조정</h3>
<svg id = "myGraph"></svg>
<hr>
<Br>
ticks()=눈금 간격 지정, 기본값10<br>
ticks()는 모두가 지정한 값과 같은 간격이 된다.<br>
tickValues()는 서로 다른 간격으로 표시<Br>
tickFormat()는 눈금에 표시할 숫자에 서식 지정<br>
</body>
</html>
```

ticks()=눈금 간격 지정, 기본값10<br>
ticks()는 모두가 지정한 값과 같은 간격이 된다.<br>
tickValues()는 서로 다른 간격으로 표시<Br>
tickFormat()는 눈금에 표시할 숫자에 서식 지정<br>

참고하자~~~

bar3.js

```js
window.addEventListener("load",function(){
	

//1. 데이터 준비
var dataSet = [120, 150, 10, 80, 220];
var offsetX=30;//x좌표의 오프셋(어긋남의 정도 총체적으로 이동?
var offsetY=10;//y좌표의 오프셋(어긋남의 정도 총체적 이동?
var svgHeight=240;//SVG의 요소의 높이
var barElements;//막대그래프의 막대 요소를 저장할 변수


barElements=d3.select("#myGraph")
  .selectAll("rect")//rect요소 지정
  .data(dataSet)//데이터를 요소에 연결
    
  barElements.enter()//데이터 수만큼 반복
	  			.append("rect")//데이터 수만큼 rect요소가 추가
	  			
	  			.attr("class","bar")//css 클래스 설정
	  			.attr("height", function(d,i){//높이 설정. 
	  				return d;//데이터 값 그대로 높이로 지정
	  			})
	  			.attr("width", 20)
	  			
	  			.attr("x",function(d,i){
	  				return i*25+offsetX;
	  			})
	  			.attr("y", function(d,i){
	  				return svgHeight -d-offsetY;
	  			})
	  			
	  			
barElements.enter()
.append("text")
.attr("class","barNum")
.attr("x",function(d,i){
	return i*25+10+offsetX;//offsetx추가
})
.attr("y",svgHeight-5-offsetY)
//y 좌표 설정 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
.text(function(d,i){
	return d;
})

    var yScale=d3.scaleLinear()
    .domain([0,300])//원래 크기
    .range([300,0]);//실제 출력 크기

var axis= d3.axisLeft(yScale)
			.ticks(10)//눈금간격
			.tickValues([10,20,30,50,100,150,200])
//		.tickFormat(d3.format(",2f"))

d3.select("#myGraph").append("g")//g는 그룹핑 해주는 것?
.attr("class","axis")
.attr("transform",
		"translate("+offsetX+","+((svgHeight-300)-offsetY)+")")//눈금 표시위치 조정과 함께 좌표선 그리기?
//위에서 x 좌표의 값들을 30씩 옮겨주자.(그래프 값과 text값 모두 보내주어야 한다)
.call(axis)//표현하려고~

d3.select("#myGraph")
.append("rect")
.attr("class","axis_x")
.attr("width",320)
.attr("height",1)
.attr("transform","translate("+offsetX+","+(svgHeight-offsetY)+")")//X 좌표선 그리기


barElements.enter()
.append("text")
.attr("class","barNum")
.attr("x",function(d,i){
	return i*25+10+offsetX;
})

.attr("y",svgHeight-offsetY+15)
	//y 좌표 설정 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
.text(function(d,i){
	return ["A","B","C","D","E"][i];//x축 라벨
})


});
```



###### 애니메이션



###### call

바로 앞에 호출된 객체를 매개변수로 넘겨주는 역활(좌표의 축을 그리거나, 등등)

##### pie(원 그래프 그리기)

pie2.html

```html

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sample</title>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/pie2.js"></script>
<style>
svg { width: 320px; height: 240px; border: 1px solid black; }
.pie{fill:cyan;stroke:black;}
</style>
	</head>
	<body>
		<h1>원 그래프 표시</h1>
		<svg id="myGraph"></svg>
		<br>
   <br>
		 
	</body>
</html>

```

pie2.js

```js
window.addEventListener("load",function(){
	

//1. 데이터 준비
var dataSet = [20,50, 30, 10, 20];
var svgHeight=240;
var svgWidth=320;
var color=d3.scaleOrdinal(d3.schemeCategory10);//d3.js가 준비한 표준 색상




//원 그래프의 좌표값을 계산하는 메서드
var pie=d3.pie()//원 그래프 레이아웃
//원 그래프 외경, 내경 설정: outerRadius(0) 반지름    innerRaidus(100) 안쪽 반지름
var arc=d3.arc().innerRadius(0).outerRadius(100);

//원 그래프 그리기
//원그래프의 부채꼴은 path의 좌표로 구성되므로 path요소 지정

var pieElements=d3.select("#myGraph")
.selectAll("path")//path요소 지정
//데이터를 요소에 연결, d3,pie()함수는 데어터의 부채꼴의 좌표를 계산해서 리턴
.data(pie(dataSet))

//데이터 추가
pieElements.enter()//데이터 수만큼 반복
.append("path")//데이터 수만큼 path요소 추가
.attr("class","pie")//css클래스 지정
.attr("d",arc)//부채꼴 지정
.attr("transform","translate("+svgWidth/2+", "+svgHeight/2+")")//한가운데에 나와야 함으로 1/2값으로 지정
//.style("fill",function(d,i){
//	return ["red","orange","yellow","cyan","#3f3"][i]
//})//이렇게 색상 지정 위해서는 위이 var color=d3.scaleOrdinal(d3.schemeCategory10)을 지워야 한다. d3.js가 준비한 표준 색상
.style("fill",function(d,i){
	return color(i);//표준 10색 중 색을 반환
})

.transition()
.duration(1000)
.delay(function(d,i){// 원 그래프 나타나는 시간 다르게
	return i*1000;
})
.ease(d3.easeLinear)//직선적인 움직임으로 변경(애니메이션의 움직임이다!!!!!!
//시간에 따라 도형을 변형시키기 위해 시간에 따라 속성값 변화
.attrTween("d",function(d,i){//보간 처리?????새로운 점을 만들기 위해 수많은 점들을 평균화시키는 것

	
	var interpolate =d3.interpolate(
			{startAngle : d.startAngle, endAngle: d.startAngle},//각 부분의 시작 각도
			{startAngle : d.startAngle, endAngle: d.endAngle});//각 부분의 종료 각도
	return function(t){//여기서 t는 시간이다
		return arc(interpolate(t));//시간에 따라 처리
	}
	

})

//합계와 수와 문자를 표시
var textElements=d3.select("#myGraph")
.append("text")
.attr("class","total")
.attr("transform","translate("+svgWidth/2+","+(svgHeight/2+5)+")")
.text("합계:" +d3.sum(dataSet))//합계 표시




});
```

###### 색 표현

```js
.style("fill",function(d,i){
	return ["red","orange","yellow","cyan","#3f3"][i]

//혹은

var color=d3.scaleOrdinal(d3.schemeCategory10);//d3.js가 준비한 표준 색상

.style("fill",function(d,i){
	return color(i);//표준 10색 중 색을 반환
})
```



을 이용 한다.

###### 애니메이션 움직임

```js
.ease(d3.easeLinear) //직선적인 움직임을 표현(애니메이션의 움직임 표현)
```



###### 텍스트 추가

```js
//합계와 수와 문자를 표시
var textElements=d3.select("#myGraph")
.append("text")
.attr("class","total")
.attr("transform","translate("+svgWidth/2+","+(svgHeight/2+5)+")")
.text("합계:" +d3.sum(dataSet))//합계 표시
```

###### 원 두개 그리기

pie3.html

```html

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sample</title>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/pie3.js"></script>
<style>
svg { width: 320px; height: 240px; border: 1px solid black; }
.pie{fill:cyan;stroke:black;}
.total{font-size:9pt;text-anchor:middle;}
.pieNum{font-size:10pt;text-anchor:middle;}
</style>
	</head>
	<body>
		<h1>원 그래프 표시</h1>
		<svg id="myGraph"></svg>
		<br>
   <br>
		 
	</body>
</html>

```

pie3.js

```js
window.addEventListener("load",function(){
	

//1. 데이터 준비
var dataSet = [10,20, 30, 40, 50];
var svgHeight=240;
var svgWidth=320;
var color=d3.scaleOrdinal(d3.schemeCategory10);//d3.js가 준비한 표준 색상




//원 그래프의 좌표값을 계산하는 메서드
var pie=d3.pie().value(function(d,i){return d;})//데이터셋의 

//원 그래프 외경, 내경 설정: outerRadius(0) 반지름    innerRaidus(100) 안쪽 반지름
var arc=d3.arc().innerRadius(30).outerRadius(100);

//원 그래프 그리기
//원그래프의 부채꼴은 path의 좌표로 구성되므로 path요소 지정


var pieElements=d3.select("#myGraph")
.selectAll("g")//g요소 지정
//데이터를 요소에 연결, d3,pie()함수는 데어터의 부채꼴의 좌표를 계산해서 리턴
.data(pie(dataSet))
.enter()
.append("g")//중심 계산을 위해 그룹화하기
.attr("transform","translate("+svgWidth/2+","+svgHeight/2+")")//





//데이터 추가
pieElements//데이터 수만큼 반복
.append("path")//데이터 수만큼 path요소 추가

.attr("class","pie")//css클래스 지정
.style("fill",function(d,i){
	return color(i);//표준 10색 중 색을 반환
})

.transition()
.duration(200)
.delay(function(d,i){// 원 그래프 나타나는 시간 다르게
	return i*200;
})
.ease(d3.easeLinear)//직선적인 움직임으로 변경(애니메이션의 움직임이다!!!!!!
//시간에 따라 도형을 변형시키기 위해 시간에 따라 속성값 변화
.attrTween("d",function(d,i){//보간 처리?????새로운 점을 만들기 위해 수많은 점들을 평균화시키는 것

	
	var interpolate =d3.interpolate(
			{startAngle : d.startAngle, endAngle: d.startAngle},//각 부분의 시작 각도
			{startAngle : d.startAngle, endAngle: d.endAngle});//각 부분의 종료 각도
	return function(t){//여기서 t는 시간이다
		return arc(interpolate(t));//시간에 따라 처리
	}
	

})

//합계와 수와 문자를 표시
var textElements=d3.select("#myGraph")
.append("text")
.attr("class","total")
.attr("transform","translate("+svgWidth/2+","+(svgHeight/2+5)+")")
.text("합계:" +d3.sum(dataSet))//합계 표시

pieElements
.append("text")
.attr("class","pieNum")
.attr("transform",function(d,i){
	return "translate("+arc.centroid(d)+")";
})
.text(function(d,i){
	return d.value;//값 표시
});



});
```

###### csv 파일 데이터 표시(select박스에서 선택한 값이 나오게)

pie4.html

```html

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sample</title>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/pie3.js"></script>
<style>
svg { width: 320px; height: 240px; border: 1px solid black; }
.pie{fill:cyan;stroke:black;}
.total{font-size:9pt;text-anchor:middle;}
.pieNum{font-size:10pt;text-anchor:middle;}
</style>
	</head>
	<body>
		<h1>원 그래프 표시-csv파일 데이터 표시</h1>
		<svg id="myGraph"></svg>
		<form>
		<select id="year">
		<option value="2008">2008년</option>
		<option value="2009">2009년</option>
		<option value="2010">2010년</option>
		<option value="2011">2011년</option>
		<option value="2012">2012년</option>
		<option value="2013">2013년</option>
		<option value="2014">2014년</option>
		
		</select>
		
		</form>
   <br>
		 
	</body>
</html>

```

pie4.js

```js
window.addEventListener("load",function(){
	

//처음에는 2008년 데이터를 표시해둠
	drawPie("./pie_data/mydata2008.csv");
	//선택 메뉴가 선택되었을 떄의 처리
	d3.select("#year").on("change",function(){
		d3.select("#myGraph").selectAll("*").remove();//호출전 지우기
		drawPie("./pie_data/mydata"+this.value+".csv",this.value);//다시 호출
		
	});//파일 불러오기
	
	function drawPie(filename){
		//데이터셋은 csv파일
		d3.csv(filename)
		.then(function(data){
			var dataSet=[];//데이터를 저장할 배열 변수
		for(var i in data[0]){//최초 데이터를 처리
			dataSet.push(data[0][i]);//가로 한 줄 모두를 한꺼번에 
		}
		
		//SVG요소의 넓이와 높이를 구함
		var svgEle=document.getElementById("myGraph");
		var svgWidth=window.getComputedStyle(svgEle,null)
			.getPropertyValue("width");
		var svgHeight=window.getComputedStyle(svgEle,null)
			.getPropertyValue("height");
			svgWidth=parseFloat(svgWidth);//값에는 단위가 붙어 있으면 안된다
			svgHeight=parseFloat(svgHeight);//값에는 단위가 붙어 있으면 안된다
			
			var color=d3.scaleOrdinal(d3.schemeCategory10);
		
		
	



//원 그래프의 좌표값을 계산하는 메서드
var pie=d3.pie().value(function(d,i){return d;})//데이터셋의 

//원 그래프 외경, 내경 설정: outerRadius(0) 반지름    innerRaidus(100) 안쪽 반지름
var arc=d3.arc().innerRadius(30).outerRadius(100);

//원 그래프 그리기
//원그래프의 부채꼴은 path의 좌표로 구성되므로 path요소 지정


var pieElements=d3.select("#myGraph")
.selectAll("g")//g요소 지정
//데이터를 요소에 연결, d3,pie()함수는 데어터의 부채꼴의 좌표를 계산해서 리턴
.data(pie(dataSet))
.enter()
.append("g")//중심 계산을 위해 그룹화하기
.attr("transform","translate("+svgWidth/2+","+svgHeight/2+")")//





//데이터 추가
pieElements//데이터 수만큼 반복
.append("path")//데이터 수만큼 path요소 추가

.attr("class","pie")//css클래스 지정
.style("fill",function(d,i){
	return color(i);//표준 10색 중 색을 반환
})

.transition()
.duration(200)
.delay(function(d,i){// 원 그래프 나타나는 시간 다르게
	return i*200;
})
.ease(d3.easeLinear)//직선적인 움직임으로 변경(애니메이션의 움직임이다!!!!!!
//시간에 따라 도형을 변형시키기 위해 시간에 따라 속성값 변화
.attrTween("d",function(d,i){//보간 처리?????새로운 점을 만들기 위해 수많은 점들을 평균화시키는 것

	
	var interpolate =d3.interpolate(
			{startAngle : d.startAngle, endAngle: d.startAngle},//각 부분의 시작 각도
			{startAngle : d.startAngle, endAngle: d.endAngle});//각 부분의 종료 각도
	return function(t){//여기서 t는 시간이다
		return arc(interpolate(t));//시간에 따라 처리
	}
	

})

//합계와 수와 문자를 표시
var textElements=d3.select("#myGraph")
.append("text")
.attr("class","total")
.attr("transform","translate("+svgWidth/2+","+(svgHeight/2+5)+")")
.text("점유율:" +d3.sum(dataSet))//합계 표시

pieElements
.append("text")
.attr("class","pieNum")
.attr("transform",function(d,i){
	return "translate("+arc.centroid(d)+")";
})
.text(function(d,i){
	return d.value;//값 표시
});
});
}



});
```

##### 꺽은선 그래프

line1.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border: 1px solid black;}
.line {fill:none;stroke:black;}</style>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/line1.js"></script>
</head>
<body>
<h3>꺽은선 그래프 표시</h3>
<svg id = "myGraph"></svg>
</body>
</html>
```

line1.js

```js
window.addEventListener("load",function(){
	

var svgWidth=320;//SVG요소의 넓이
var svgHeight=240;//SVG요소의 높이
var dataSet=[10,47,65,8,64,99,75,22,63,80];//데이터셋
var margin=svgWidth/(dataSet.length-1);//꺽은선 그래프 간격
//꺽은선 그래프의 좌표 계산 메서드
var line=d3.line()//svg의 선
.x(function(d,i){
	return i*margin;//x좌표는 표시 순서 x간격
})
.y(function(d,i){
	return svgHeight -d;//데이터로부터 Y좌표 빼기
})
//꺽은ㅅ ㅓㄴ 그래프 그리기
var lineElements=d3.select("#myGraph")
.append("path")//데이터 수만큼 path요소가 추가
.attr("d",line(dataSet))//연속선 지정



});
```

###### 눈금 표시

line2.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
svg {width:320px; height:240px; border: 1px solid black;}
.line {fill:none;stroke:black;}
.axis text{
font-family:sans-serif;
font-size:11px;}
.axis path,
.axis line{
fill:none;
stroke:cyan;
}
.axis_x line{
fill:none;
stroke:red;
}
</style>
<script src="https://d3js.org/d3.v5.min.js"></script>

<script src="./js/line1.js"></script>
</head>
<body>
<h3>꺽은선 그래프 표시-눈금 표시</h3>
<svg id = "myGraph"></svg>
</body>
</html>
```

line2.js

```js
window.addEventListener("load",function(){
var offsetX=30;
var offsetY=20;

var svgWidth=320;//SVG요소의 넓이
var svgHeight=240;//SVG요소의 높이
var dataSet=[10,47,65,8,64,99,75,22,63,80];//데이터셋
var margin=svgWidth/(dataSet.length-1);//꺽은선 그래프 간격
//꺽은선 그래프의 좌표 계산 메서드
var line=d3.line()//svg의 선
.x(function(d,i){
	return i*margin+offsetX;//x좌표는 표시 순서 x간격
})
.y(function(d,i){
	return svgHeight -d-offsetY;//데이터로부터 Y좌표 빼기
})
//꺽은선 그래프 그리기
var lineElements=d3.select("#myGraph")
.append("path")//데이터 수만큼 path요소가 추가
.attr("class","line")
.attr("d",line(dataSet))//연속선 지정



  var yScale=d3.scaleLinear()
    .domain([0,100])//원래 크기
    .range([200,0]);//실제 출력 크기

var axis= d3.axisLeft(yScale)
			.ticks(20)//눈금간격
d3.select("#myGraph")

	.append("g")//그룹화한다.
	.attr("class","axis")//클래스 속성 추가 스타일시트 클래스 설정
	.attr("transform","translate("+offsetX+","+(offsetY)+")")
	.call(axis)//call()로 눈굼을 표시할 함수를 호출
			



//눈금을 설정하고 표시

	
d3.select("#myGraph")
.append("rect")
.attr("class","axis_x")
.attr("width",svgWidth)
.attr("height",1)
.attr("transform","translate("+offsetX+","+(svgHeight-offsetY)+")")//X 좌표선 그리기
});
```

