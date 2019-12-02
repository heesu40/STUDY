//예전 방식
console.log("예전 방식")

var colors = ['red' , 'orange' , 'yellow']
for (var i = 0; i < colors.length; i++){
	console.log(colors[i])
}
console.log("forEach 방식")
// use forEach
const COLORS = ['red' ,'orange' , 'yellow']
COLORS.forEach(function(color){
	console.log(color)
})


//즉시실행함수로 
console.log("즉시실행함수로 ")
const result = COLORS.forEach(color=> console.log(color))
//foreach는 아무것도 리턴을 하지 않는다. 
console.log(result)  //그래서 결과는 undefined가 뜨게 된다.



//---------------------------------------------------
//실습 넘버1 
console.log("실습넘버1")
function hadlePosts(){
	const posts = [{
		id: 23,
		title: "오늘의 뉴스",

	},
	{
		id: 34,
		title: "오늘의 스포츠",
	},
	{
		id : 78,
		title : "오늘의 먹거리"
	}

	]

	console.log("예전방식")
	for (let i = 0; i < posts.length ; i++){
		console.log(posts[i])
	}
	console.log("forEach방식")
	posts.forEach(post => console.log(post))

}
//3개의 objects를 가지는 리스트 완성! 
hadlePosts()


// 실습 2
//image 배열 안에 있는 정보를 가지고 넓이를 구하고 그 값을 areas에 저장

const IMAGES = [
	{height: 10 , width: 30},
	{height: 22 , width: 37},
	{height: 54 , width: 42},
]
let areas = []

function test2(){
	const IMAGES = [
		{height: 10 , width: 30},
		{height: 22 , width: 37},
		{height: 54 , width: 42},
	]
	let areas = []
	
	IMAGES.forEach(i => areas.push(i.height * i.width))
	console.log(areas)
}
test2()
