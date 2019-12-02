//선언식

function add(num1 , num2){
	return num1 + num2
}
//미리 선언해 두고 필요할때 사용

let sum = add(5,7)

// 표현식
const sub = function(num1, num2){
	return num1 - num2
}

let val = sub(12, 5)
console.log(val)
console.log(typeof sub)
console.log(typeof add)
