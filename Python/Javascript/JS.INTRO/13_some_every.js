const NUMBERS = [1,2,3,4,5]

//some

const sresult = NUMBERS.some(function(elem){
	return elem % 2 === 0
})
console.log(sresult);

//every
const eresult = NUMBERS.every(function(elem){
	return elem % 2 === 0
})
console.log(eresult);



