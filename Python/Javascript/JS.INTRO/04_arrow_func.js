// const greeting = function(name){
// 	return 'hello ${name}'
// }

// //1. function 키워드 생략
// const greeting  = (name) => {
// 	return 'hello'
// }

// //2. 인자가 1개인 경우 괄호도 생략 가능

// const greeting = name =>{
// 	return 'hello ${name}'
// }

// //3. body(괄호 안의 부분 ) 의 표현식이 1줄인 경우 
// const greeting = name => 'hello ${name}'

// // 실습
// let square = function(num){
// 	return num **2
// }

// let square = (num)=>{
// 	return num **2
// }

// const square = num => 'return num ** 2'


// let noArags = () => 'no Args'
// let noArgs = _=>'no Args'

// //object 형식으로 반환 된다면? 가로로 해주면 된다!

// let returnObj = () =>{
// 	return {key:'value'}
// }
let returnObj = () => ({key:'value'})
console.log(returnObj())

//인자에 기본값을 설정했을 경우

let sayHi = function(name="pengsu"){
	return 'hi ${name}'
}

let sayHi = (name="pengsu") => 'hi ${name}'
console.log(sayHi('bbung'))


//즉시 실행 함수
//즉시 실행 함수 는 왜 쓰나? 초기화 할 때! 

const cube = function(num){
	return num ** 3
}//(2)

//익명함수랑 같은데 왜 다른가!? 뒤에 (2) 바로 값을 넣어 줄수 있다.

console.log(cube(2))

//익명함수 즉시 실행 

console.log(function(num){return num ** 3}(2))
console.log(num => num ** 3(4))




