const numbers = [1, 2, 3, 4, 5, 6, 7]
console.log(numbers[1])
console.log(numbers[-1]) //파이썬은 되지만 여기서는 안된다! 양의 정수만 가능!
console.log(numbers.length)

console.log(numbers.reverse()) //뒤집힌다!
console.log(numbers) //한번 reverse 면 원본이 뒤집힌다! 주의**
console.log(numbers[0]) //가장 마지막 번호를 뽑아올 수 있다.  


//push 배열의 마지막에 값을 넣어 주는 것 넣어주고 끝나면 배열의 총 길이를 return 해준다.
numbers.push('peng') ///return 값은 배열의 길이가 된다. (새롭게 추가된 값까지의 길이를 알려준다.)
console.log(numbers)//맨 마지막에 추가됨을 확인 할 수 있다.
console.log(numbers.push('su'))

//pop 빼는 아이

console.log(numbers.pop()) //할때마다 값이 날아갈 것이다! 조심!
console.log(numbers) //배열에서도 지워버리는 역할

//unshift 배열의 가장 앞쪽에 요소를 추가
console.log(numbers.unshift("pengsu"))
console.log(numbers)

//shift
console.log(numbers.shift())
console.log(numbers)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//includes
console.log(numbers.includes(1)) //ture false로 나오므로 있는지 없는지 확인 가능

console.log("index", numbers.indexOf(2)) //위치를 알려준다! 어느 위치에 있는지

numbers.push('peng' , 'peng') //값 중복이면 어찌 될까?
console.log(numbers)
console.log(numbers.indexOf('peng')) //첫번쨰 오는 인덱스의 값만 반환을 해준다. 중복해도 처음 것만!

//join
console.log(numbers.join('-')) //1-2-3-4-5-6-7-peng-peng 
console.log(numbers.join()) //1,2,3,4,5,6,7,peng,peng 기본은 , 이다.
console.log(numbers.join('')) //1234567pengpeng 다 붙여서!
console.log(numbers) //(9) [1, 2, 3, 4, 5, 6, 7, "peng", "peng"] 원본은 건드리지 않는다!


