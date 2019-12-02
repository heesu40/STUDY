const userName = prompt("니 이름이 뭐니?")
let message = ""

if (userName === "pengsu"){
	message = "우주 대스타";
}else if (userName === "그렇구나"){
	message = "끄덕끄덕";
}else{
	message = "<h1>어서오세요. ${userName}</h1>"
}

message;
document.write(message)
