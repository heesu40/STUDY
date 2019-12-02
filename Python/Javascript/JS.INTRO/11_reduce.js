//배열의 총합을 구하기
const numbers = [1, 2, 3, 4]

// before
console.log("★  before")
let total = 0;
for (let i = 0 ; i< numbers.length ; i++){
	total += numbers[i]
}
console.log(total)

//reduce
console.log("★  reduce")
let sum = numbers.reduce(function(total, num){ //total로 이전값을 분류 (total=이전값이 된다.)
	return total += num //이전값에 현재값을 계속 더해주면!!! 총합이 된다.
}, 0) //마지막에는 
console.log("총합 : ",sum)
console.log("이전값  :  " , numbers)



//실습 1
//평균 구하기

const testResults = [90, 85, 70, 78, 58, 86, 99, 82]
let avg = testResults.reduce((aa,aaa) => (aa += aaa),0)/testResults.length


console.log(avg)


// 실습 2
// 배열에 담긴  이름이 중복되면 {이름: 중복 횟수} 로 반환 해보자.
const names = ['pengsu' , 'bbung', 'pororo' , 'bbung' , 'bungaeman' , 'pengsu']
let count = 0
let nameResults = names.reduce(function(allNames, name){ //allNames에 계속 값을 들고 있게 된다.
	if (name in allNames){ //object안에 값을 확인 하는 것!
		allNames[name] += 1
	}else{
		allNames[name] = 1
	}
	return allNames
},{})

console.log(nameResults)
