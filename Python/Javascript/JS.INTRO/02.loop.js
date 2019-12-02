let i = 0;

// while (i < 10) {
// 	console.log(i)
// 	i++;
// }

// for (let j = 10; j > 0; j--) {
// 	console.log(j)
// }

const numbers = [1,2,3,4,5,6,7]

for( let num of numbers){
	console.log();
}


let sampleObj = {
	a: 1,
	b: "hello",
	c: [3,4]
}

for ( let obj in sampleObj){
	console.log(obj);
	console.log(sampleObj[obj])
}
