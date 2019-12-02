//JSOn=> object
let jsonStr = JSON.parse('{"name" : "pengsu" , "age" : "10"}')
console.log(typeof jsonStr)


//object=> JSON
let obj = {
	name: 'pengsu',
	age : '10',

}

console.log(typeof obj)  //아직은 JSON이 아니고

let jsonObj = JSON.stringify(obj);
console.log(typeof jsonObj) //JSON 으로 바뀜! string으로 찍힌다!!
