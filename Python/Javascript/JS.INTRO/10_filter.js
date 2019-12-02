const products = [
	{ name : 'cucumber' , type : 'vegetable'},
	{ name : 'banana' , type : 'fruit'},
	{ name : 'carrot' , type : 'vegetable'},
	{ name : 'apple' , type : 'fruit'},
]

//type이 과일이 친구만 뽑기 위해서는?

//befor
console.log("★  befor")
var selectProducts = []
for (var i = 0 ; i < products.length; i++){
	if(products[i].type === "vegetable"){
		selectProducts.push(products[i])
	}
}

console.log(selectProducts)


//filter 로
console.log("★  filter")

let selectProducts2 = products.filter(function(prod){
	return prod.type === "vegetable"

})
console.log("filter : ",selectProducts2)
console.log("원본 : " , products)


//실습 1
//80점 이상인 결과만 따로 배열로 만들기
const testResults = [90, 85, 70, 78, 100, 86, 99, 82]
let test1 = testResults.filter(score => (score>=80))
console.log(test1)
console.log(testResults)
