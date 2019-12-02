let heros = [
	{ name : 'Tony Stark', age: 45}, //object 를 만든다!
	{ name : 'Captin Ame', age: 82}, //object 를 만든다!
	{ name : 'Thor', age: 1500}, //object 를 만든다!
	{ name : 'Tony Stark', age: 25}, //object 를 만든다!
]


//before
console.log("★  before")
var hero = {}
for(var i = 0 ; i < heros.length ; i++){
	if(heros[i].name === 'Tony Stark'){
		hero = heros[i]
		break; //첫번째 값만 구할 것이기 떄문에 스탑!
	}
}

console.log(hero);


//find
console.log("★  find");

let hero1 = heros.find(function (hh){
	return hh.name === "Tony Stark"
})

console.log(hero1);



//실습
//잔액이 2만원 이상인 사람의 이름을 출력해 보자.

const ACCOUNTS = [
	{name: "pengsu" , money: 1200},
	{name: "bbung" , money: 24000},
	{name: "pororo" , money: 50000},
]


let pp = ACCOUNTS.find(p => p.money > 20000)
console.log(pp);



