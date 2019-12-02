//배열에 모든 요소에 2를 곱하여 새로우 배열로 만들기
//before
console.log("★ before")
var numbers = [1, 2, 3]
var doubleNumber = []

for (var i = 0; i < numbers.length ; i++){
	doubleNumber.push(numbers[i]*2)
}
console.log("원값 : ",numbers)
console.log("계산값 : " , doubleNumber)
// map 을 사용해 보자

console.log("★ map사용")
let NUMBERS = [2 , 4 , 6] //let으로 해서 원본을 바꾸는지 새롭게 배열을 만드는지 확인해보자~
let  doubleNum = NUMBERS.map(function (num){
	return num * 2
}) //map 알아서 배열로 만들어 주기 떄문에  push를 사용해 줄 필요가 없다!

let doubleNum2 = numbers.map(num => num * 2)

console.log("원본값:" ,NUMBERS)
console.log("새로운 값일까?: ",doubleNum)
console.log("map : ", doubleNum2)



// 실습 1
// 숫자가 담긴 배열을 받아서
// 각 숫자들의 제곱근이 들어있는 새 배열로 만들기

console.log('★ 실습1')
const newNum = [4, 9, 16]
let roots = newNum.map(num => num ** 0.5)
console.log(roots)

// 실습 2 
// images 배열 안에 Objects 들의 height만 저장되어있는 배열을 만들자.
console.log('★ 실습2')
const IMAGES = [
	{height : '34px' , width: '39px'},
	{height : '44px' , width: '79px'},
	{height : '87px' , width: '19px'}
]

let ww = IMAGES.map(w => w.height)

console.log(ww)



//실습 3
//{name : brand , movie : 영화}
console.log('★ 실습3')
const brands = ["Marvel" , "DC"]
const movies = ["Avengers" , "Batman"]

const Heroes = brands.map(function (brand, idx){
	return {name : brand , movie : movies[idx]} //인덱스로 선택을 해주면 OK
})

const Heroes2 = brands.map((brand,idx) => ({name:brand , movie:movies[idx]})) 
//인자가 두개이기 떄문에 () 생각 불가능이므로 (brand, idx) , 해 주고 {}가 있으므로 ({}) 해주어야한다.
console.log(Heroes)
console.log(Heroes2)
