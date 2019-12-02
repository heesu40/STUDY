const pengsu = { //키와 value를 갖는다.
	name : '펭수' ,
	"phone number" : '012345678',
	profile:{
		deram : '우주대스타',
		age : '10살',
		sqpeciality : "요들송",
	}

}
console.log(pengsu.name)
console.log(pengsu['name'])
console.log(pengsu['phone number'])

console.log(pengsu.profile)
console.log(pengsu.profile.dream)


//before 

var books = ['Learning JS', 'Learning Django']
var comics = {
	DC : ['AquaMan' , 'superMan'],
	marvle : ['IronMan' , 'andMan']

}

var magazins  = null;

var bookShop = {
	books : books,
	comics : comics,
	magazines : magazines,
}
console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.boos[0])


//after
let bookShop = {
	books,
	comics,
	magazines,

}
console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.boos[0])


