Node.js

Node.js(https://nodejs.org/ko/) 에서 다운받는다.

최신으로 받아도 되고 아니어도 상관없는데, node의 경우 업데이트가 이뤄지면 메서드가 안 돌아가는 경우가 생기므로 참고하자.

이클립스의 경우 node 검색후(eclipse Marketplace 에서 node검색) 다운로드 하고 다른 에디터를 이용해도 된다.(ex)서브프라임 등)

1. 크롬 v8자바스크립트 엔진으로 빌드된 자바스크립트 런타임
   - v8엔진은 자바스크립트 코드를 네이티브 코드로 바꾼 후 실행
   - v8엔진에는 필요한 기능을 병렬로 실행하는 '스레드 풀'과 이벤트 받아 처리하는 '이벤트 루프' 기본 기능 탑재
   - 그 위에는 네트워킹 기능 담당하는 소켓(Socket).http 라이브러리 들이 있다
2. 이벤트기반으로 논블로킹 I/O모델을 사용해 가볍고 효율적이다.
   - 싱글스레드, 논블로킹 의 경우 식당의 주문을 맡는 점원의 예를 들면 편하다. 모든 테이블의 주문을 받고 (싱글스레드) 각각을 서빙하는 것(논블로킹, 블로킹은 하나가 하나만 맡는 것)
3. 생태계인 npm은 세계에서 가장 큰 오픈소스 라이브러리 생태계
4. 자바스크립트 애플리케이션이 서버로서 기능하기 위한 도구를 제공하며, 서버 역할을 수행

## 특징

1. 비동기 입출력 

2. 콜백함수

3. 이벤트 기반의입출력(Event driven I/O) 모델

4. 모듈과 패키지

5. REPL (Read Eval Print Loop) 런타임 도구 제공

   - 사용자가 커맨드 입력하면 시스템이 값을 반환하는 환경
   - Ctrl+c  현재 명렁어 종료
   - Ctrl+c(2번) Node REPL종료
   - Ctrl+D Node REPL종료
   - 위/아래 키 명령어 히스토리 탐색후 명령어 수정
   - Tab 현재 입력란에 쓴 값으로 시작하는 명령어/변수 목록 확인
   - .help 모든 커맨드 목록 확인
   - .break 멀티 라인 표현식 입력 도중 입력을 종료
   - .clear .break와 같다
   - 

6. 내장 HTTP서버 라이브러리를 포함하고 있어 웹 서버에서 아파치 등의 별도 소프트웨어 없이 동작

   

## 효율성 좋은 분야

1. 입출력 잦은 어플리케이션
2. 데이터 스트리밍 어플리케이션
3. 데이터 실시간 다루는 어플리케이션
4. JSON API 기반 어플리케이션
5. 싱글페이지 어플리케이션(한가지 언어로 전체 웹 페이지를 만들 수 있게 됨)

but!

- CPU사용률이 높은 어플리케이션은 권장 안함(이미지나 비디오 처리, 대규모 데이터 처리 등)

## 실행

cmd 창 실행 후 node를 쓰면 알아서 들어가진다(설치를 끝냈기 때문에)



![1564364300702](C:\Users\student\Documents\GitHub\javaStudy\사진\노드)



```js
var a = '';    
var b = 0;    
var c = false; //boolean 
var d = null; //
var e = undefined;//  
var f = [];  //배열 이지만 object로 나온다
var g = {};//객체 정의시  
var h = function() {};//function
typeof a;  
typeof b;  
typeof c;  
typeof d;  
typeof e;  
typeof f;  
typeof g; 
typeof h;  
```



결과값 cmd 창에 확인해보자

#### 종료

.exit 를 cmd 창에 입력해주자. or ctrl +C 두번 입력

## 비동기 프로그래밍 이해

#### 동기, 블로킹 방식 syncTest.js

```js
//동기 블럭킹 방식
function lonRunningTask(){

    var hap=0
    for(var i=0;i<100000;i++){
        console.log(i)
        hap+=i;
    }
    console.log(i)
    console.log('작업 끝');
}
console.log('시작');
lonRunningTask();
console.log('다음 작업');

//비동기 non=blocking
function logRunningTask(){
    //오래 걸리는 작업 
    var hap=0;
    for(var i=0;i<100000;i++){
        hap+=i;
    }
    console.log(i)
    console.log('작업 끝');
}
console.log('시작');
setTimeout(logRunningTask,0);
console.log('다음 작업');
```

#### 순차처리

- 비동기 방식이지만 순차처리가 가능하다

  참고로 아래 코드 사용 전 빈파일 processId.txt 를 만들어 보자

```js

//동기 방식
var fs = require('fs');
var filenames = fs.readdirSync('.');  
var i;  
for (i = 0; i < filenames.length; i++) {  
    console.log(filenames[i]);
}
console.log('ready');
console.log('can process next job...'); var fs = require('fs');
var oldFilename = './processId.txt';  
var newFilename = './processIdOld.txt';

fs.chmodSync(oldFilename, 777);  
console.log('complete chmod.');  
fs.renameSync(oldFilename, newFilename);  
console.log('complete rename.');  
var isSymLink = fs.lstatSync(newFilename).isSymbolicLink();  
console.log('complete symbolic check.');  
var fs = require('fs'); 

```



```js


//비동기
var oldFilename = './processId.txt';  
var newFilename = './processIdOld.txt';
var fs=require('fs');
fs.chmod(oldFilename, 777, function (err) {  
    console.log('complete chmod.');
    fs.rename(oldFilename, newFilename, function (err) {
        console.log('complete rename.');
        fs.lstat(newFilename, function (err, stats) {
            var isSymLink = stats.isSymbolicLink();
            console.log('complete symbolic check.');
        });
    });
});

```



일반적으로는

- 'async' 라는 모듈을 사용
- waterfall API를 사용하면 Callback의  중첩을 줄이면서 로직의 순서를 보장한다.

```js
var fs = require('fs');  
var async = require('async');
var oldFilename = './processId.txt';  
var newFilename = './processIdOld.txt';
async.waterfall([  
    function (cb) {
        fs.chmod(oldFilename, 777, function (err){
            console.log('complete chmod.');
            cb(null);
        });
    },
    function (cb) {
        fs.rename(oldFilename, newFilename, function (err) {
            console.log('complete rename.');
            cb(null);
        });
    },
    function (cb) {
        fs.lstat(newFilename, function (err, stats) {
            var isSymLink = stats.isSymbolicLink();
            console.log('complete symbolic check.');
        });
    }
]);

```

#### callback 처리의 재사용

외부에 선언한 객채를 부르는 것으로 callback함수 수행

```js
var fs = require('fs');

var path1 = './';  
var path2 = '.././';  
var countCallback;

function countFiles(path, callback) {  
    fs.readdir(path, function (err, filenames) {
        callback(err, path, filenames.length);
    });
}

countCallback = function (err, path, count) {  
    console.log(count + ' files in ' + path);
};

countFiles(path1, countCallback);  
countFiles(path2, countCallback); 

```



호출 시점 확인해보자

```js
var fs = require('fs');
function executeCallbacks() {  
    fs.readdir('.', function (err, filenames) {
        var i;
        for (i = 0; i < filenames.length; i++) {
            fs.stat('./' + filenames[i], function (err, stats){
                console.log(i + ':'+stats.isFile());//is file은 true를 리턴한다.
            });//파일인지 아닌지(아니면 리퍼런스다)
        }
    });
}
executeCallbacks(); 

```

```js
var fs = require('fs');
function executeCallbacks() {  
    fs.readdir('.', function (err, filenames) {
        var i;
        for (i = 0; i < filenames.length; i++) {
            (function(){
                var j = i;//
                fs.stat('./' + filenames[i], function (err, stats){
                    console.log(j + ':'+stats.isFile());
                });
            })();
        }
    });
}
executeCallbacks(); 

```

순차적인 i값을 출력하기 위해서는 외부 Callback 실행시 i값을 어딘가에 저장해야 한다.

Closure를 생성하여 새로운 Scope, 즉시실행 함수를 만들었다.

## ES2015+

1. Node 6버전부터 ES2015문법을 사용 가능
2. const,let
   - var- 함수 스코드를 가지므로 if문의 블록과 관계없이 접근
   - const,let-블록 스코프를 가지므로 블록 밖에서 접근 못함
   - const- 상수, 초기화 시 값을 대입하지 않으면 에러 발생

```js
if (true) {
  var x = 3;
}
console.log(x); // 3

```

```js
if (true) {
  const y = 3;
}
console.log(y); // Uncaught ReferenceError: y is not defined

```

```js
const a = 0;
a = 1; // Uncaught TypeError: Assignment to constant variable.
let b = 0;
b = 1; // 1

const c; // Uncaught SyntaxError: Missing initializer in const declaration

```



1. 



## 모듈

- 독립적인 하나의 소프트웨어
- 특정한 기능을 하는 함수나 변수들의 집합
- 모듈로 만들어두면 여러 프로그램에 해당 모듈을 재사용할 수 있다.
- 보통 파일 하나가 모듈 하나가 됩니다. 파일별로 코드를 모듈화할 수 있어 관리하기 편리하다.
- 대표적인 모듈 생성 방법은 module.exports 를 사용한다

#### 모듈로 함수 메서드 생성

```js
//cal.js
function add(a, b) {
  return a + b;
}
module.exports = add;

```

```js
//main.js
const add = require('./cal.js');
console.log(add(1, 2)); // 3

```

각각을 저장하여 두개의 파일을 만든후 cmd 에서 node main 을 불러본다.(위치는 해당파일이 있는 장소에서 필자는 c아래 test파일 아래 저장)



#### 모듈 활용

1. require 함수 안에 불러올 모듈의 경로를 지정한다(파일 경로에서 js 나 json같은 확장자는 생략 가능)
2. 모듈 하나가 여러 개의 모듈 사용 가능
3. 모듈 하나가 여러 개의 모듈 사용

```js
//var.js
const odd='odd';
const even='even';

module.exports={odd,even};
```



```js
//func.js
function add(a,b){
return a+b;} 
module.exports=add;
```



```js
//index.js
const {odd,even}=require('./var.js');
const checkNumber=require('./func.js');
function checkStringOddOrEven(str){
if(str.length%2){
return odd;}
return even;}
console.log(checkNumber(10));
console.log(checkStringOddOrEven('hello'));
```



#### 모듈 활용 2

require 을 하게 되면 객체를 통째로 가져 오기 때문에 .add .multiply 속성에 접근



```js
//cal.js
function add(a,b){
return a+b;} 

function substract(a,b){
return a-b;} 

function multiply(a,b){
return a*b;} 

function divide(a,b){
return a/b;} 

module.exports={
add: add,
substract:substract,
multiply:multiply,
divide:divide,};
```



```js
//main.js
const add=require('./cal.js').add;
const multiply=require('./cal.js').multiply;


console.log(multiply(add(1,2),add(2,3)));
```



#### 모듈 활용3

export 객체를 사용해서 모듈 생성

exports는 속성을 추가할때만 사용 (즉 위는 한번에, 이건 하나하나)

```js

//cal.js
exports.add=function(a,b){
return a+b;};

exports.substract=function(a,b){
return a-b;};

exports.multiply=function(a,b){

return a*b;};

exports.divide=function(a,b){
return a/b;};
```

```js
//main.js
const add=require('./cal.js').add;
const multiply=require('./cal.js').multiply;


console.log(multiply(add(1,2),add(2,3)));
```

위와 결과값은 동일하다



#### ES2015모듈

1. 자바스크립트 자체 모듈 시스템 문법
2. require 가 module.exports 가 import, export default 로 바뀌었다.
3. 노드에서도 9버전부터 ES2015의 모듈 시스템을 사용 가능하다
4. 파일의 확장자를 mjs 로 지정해야한다
5. 실행시 node --experimental-modules[파일명]
6. 즉 이것이 최신문법이다!

```js
//func.mjs

import { odd, even } from'./var';

function checkOddOrEven(num) {
  if (num % 2) { // 홀수면
    return odd;
  }
  return even;
}

export default checkOddOrEven;

```

허나 10버전에서는 안된다~ 참고하자 최신으로 다운 받아 해보자



#### global 객체

1. 브라우저의 window와 같은 전역 객체
2. 모든 파일에서 접근 가능
3. global도 생략 가능(require 함수는 global.require에서 global이 생략. console객체도 global.console이다.)
4. 노드에서는 DOM이나 BOM이 없어 window와 document객체 사용 안된다
5. global객체는 간단한 데이터를 파일끼리 공유시 사용

```js
module.exports=()=>global.message;
```

```js
const A=require('./globalA.js');
global.message='hello';
console.log(A());
```

#### console 객체

- console 객체는 디버깅을 위해 사용 (개발 중 변수에 값 확인, 에러 발생 시 에러 내용을 콘솔에 출력, 코드 실행 시간 확인)
- **console.time****(***레이블***)** : console.timeEnd(레이블)과 대응되어 같은 레이블을 가진 time과 timeEnd 사이의 시간을 측정
- **console.log(**내용**)** :  로그를 콘솔에 출력합니다. console.log(내용, 내용, ...)처럼 여러 내용을 동시에 표시 가능
- **console.error****(**에러 내용**) : 에러를 콘솔에 출력
- **console.dir****( **객체**,**옵션**)** : 객체를 콘솔에 출력할 때 사용합니다. 첫 번째 인자로 표시할 객체를 넣고, 두 번째 인자로 옵션을 넣어보자. 옵션의 colors를 true로 하면 콘솔에 색이 추가되어 보기가 한결 편해진다. depth는 객체 안의 객체를 몇 단계까지 보여줄지를 결정 기본값은 2이다
- **console.trace****(**레이블**)** : 에러가 어디서 발생했는지 추적할 수 있게 해주는 것으로 보통은 에러 발생 시 에러 위치를 알려주므로 자주 사용하지는 않지만, 위치가 나오지 않는다면 사용할 만하다.

```js
//console.js

const string ='abc';
const number = 1;
const boolean = true;
const obj = {
  outside: {
    inside: {
      key:'value',
    },
  },
};
console.time('전체 시간');
console.log('평범한 로그입니다 쉼표로 구분해 여러 값을 찍을 수 있습니다');
console.log(string, number, boolean);
console.error('에러 메시지는 console.error에 담아주세요');

console.dir(obj, { colors: false, depth: 2 });
console.dir(obj, { colors: true, depth: 1 });
console.time('시간 측정');
for (let i = 0; i < 100000; i++) {
  continue;
}
console.timeEnd('시간 측정');

function b() {
  console.trace('에러 위치 추적');
}
function a() {
  b();
}
a();

console.timeEnd('전체 시간');


```



#### 타이머

1. 타이머 기능을 제공하는 함수인 setTimeout, setInterval, setImmediate는 노드에서 window 대신 global 객체 안에 들어 있습니다. 
2. setTimeout(콜백 함수, 밀리초): 주어진 밀리초(1000분의 1초) 이후에 콜백 함수를 실행합니다.
3. setInterval(콜백 함수, 밀리초): 주어진 밀리초마다 콜백 함수를 반복 실행합니다.
4. setImmediate(콜백 함수): 콜백 함수를 즉시 실행합니다.
5. 타이머 함수들은 모두 id를 반환하며,  id를 사용하여 타이머를 취소할 수 있습니다.
6. clearTimeout(아이디): setTimeout을 취소합니다.
7. clearInterval(아이디): setInterval을 취소합니다.
8. clearImmediate(아이디): setImmediate를 취소합니다.  
9. setImmediate(콜백)과 setTimeout(콜백, 0)에 담긴 콜백 함수는 이벤트 루프를 거친 뒤 즉시 실행됩니다
10. 파일 시스템 접근, 네트워킹 같은 I/O 작업의 콜백 함수 안에서 타이머를 호출하는 경우 setImmediate는 setTimeout(콜백, 0)보다 먼저 실행됩니다.

```js
//timer.js
const timeout=setTimeout(()=>{
    console.log('1.5초 후 실행');
},1500);

const interval =setInterval(()=>{
    console.log('1초마다 실행');
},1000);

const timeout2=setTimeout(()=>{
    console.log('실행되지 않습니다.');
},3000);

setTimeout(()=>{
    clearTimeout(timeout2);
    clearInterval(interval);
},2500);

const immediate=setImmediate(()=>{
    console.log('즉시 실행');
});
const immediate2=setImmediate(()=>{
    console.log('실행되지 않았습니다.')
});
clearImmediate(immediate2);
```



#### _ filename,_ dirname

- 노드는 __filename, __dirname이라는 키워드로 경로에 대한 정보를 제공
- 파일에 __filename__을 넣어두면 실행 시 현재 파일명과 파일 경로로 바뀐다.

```js
//filename.js

console.log(__filename);
console.log(__dirname);

```



#### process

- 현재 실행되고 있는 노드 프로세스에 대한 정보를 담는다.
- 운영체제나 실행 환경별로 다른 동작을 하고 싶을 때 사용. 
- Node.js에만이 존재하는 객체

```js
process.argv.forEach(function (item,index){
    console.log(index+':'+typeof(item)+":",item);

    //실행 매개 변수에 --exit 가 있을 때
    if(item =='--exit'){
        //다음 실행 매개 변수를 얻습니다.
        var exitTime =Number(process.argv[index +1]);

        //일정 시간 후 프로그램 종료
        setTimeout(function(){
            process.exit();
        },exitTime);
    }
});

```

process.env 는  서비스의 중요한 키를 저장하는 공간으로 활용.

중요 비밀번호는 process.env의 속성으로 대체

```js
const secretId =process.env.SECRET_ID;
const secretCode=process.env.SECRET_CODE;
```



#### process.nextTick(롤백)

- 이벤트 루프가 다른 콜백 함수들보다 nextTick의 콜백 함수를 우선으로 처리
- process.nextTick으로 받은 콜백 함수나 resolve된 Promise는 다른 이벤트 루프에서 대기하는 콜백 함수보다도 먼저 실행
- Microtask를 재귀 호출하게 되면 이벤트 루프는 다른 콜백 함수보다 Microtask를 우선하여 처리하므로 콜백 함수들이 실행되지 않을 수도 있다

```js
//nextTick.js
setImmediate(()=>{
    console.log('immediate');
});
process.nextTick(()=>{
    console.log('nextTick');
})
setTimeout(()=>{
    console.log('timeout');
},0
);
Promise.resolve().then(()=>console.log('promise'));
```

호출 순서는 nextTick, promise, timeout, immediate 다.

#### process.exit(코드)

- 실행 중인 노드 프로세스를 종료합니다
- 서버에 이 함수를 사용하면 서버가 멈추므로 서버에는 거의 사용하지 않습니다. 
- 서버 외의 독립적인 프로그램에서는 수동으로 노드를 멈추게 하기 위해 사용합니다.
- process.exit 메서드는 인자로 코드 번호  0이면 정상 종료를 뜻하고, 1을 주면 비정상 종료를 뜻합니다. 

## Node 내장 모듈 이해와 활용

- 노드의 모듈 들은 노드 버전마다 차이가 있다!

```js
const os = require('os');
console.log('운영체제 정보---------------------------------');
console.log('os.arch():', os.arch());
console.log('os.platform():', os.platform());
console.log('os.type():', os.type());
console.log('os.uptime():', os.uptime());
console.log('os.hostname():', os.hostname());
console.log('os.release():', os.release());
console.log('경로---------------------------------');
console.log('os.homedir():', os.homedir());
console.log('os.tmpdir():', os.tmpdir());
console.log('cpu 정보---------------------------------');
console.log('os.cpus():', os.cpus());
console.log('os.cpus().length:', os.cpus().length);
console.log('메모리 정보---------------------------------');
console.log('os.freemem():', os.freemem());
console.log('os.totalmem():', os.totalmem());



```



#### path

다양한 path를 정리해준다........?

```js
//path.js
const path = require('path');
const string = __filename;
console.log('path.sep:', path.sep);
console.log('path.delimiter:', path.delimiter);
console.log('------------------------------');
console.log('path.dirname():', path.dirname(string));
console.log('path.extname():', path.extname(string));
console.log('path.basename():', path.basename(string));
console.log('path.basename():', path.basename(string, path.extname(string)));
console.log('------------------------------');
console.log('path.parse()', path.parse(string));
console.log('path.format():', path.format({
  dir:'C:\\users\\zerocho',
  name:'path',
  ext:'.js',
}));

console.log('path.normalize():', path.normalize('C://users\\\\zerocho\\\path.js'));
console.log('------------------------------');
console.log('path.isAbsolute():', path.isAbsolute('C:\\'));
console.log('path.isAbsolute():', path.isAbsolute('./home'));
console.log('------------------------------');
console.log('path.relative():', path.relative('C:\\users\\zerocho\\path.js','C:\\'));
console.log('path.join():', path.join(__dirname,'..','..','/users','.','/zerocho'));
console.log('path.resolve():', path.resolve(__dirname,'..','users','.','/zerocho'));

```

#### url Module

- http://nodejs.org/api/url.html
- url.resolve(from, to) - 매개변수를 조합하여 완전한 URL문자열을 생성해 리턴
- url.parse(주소): 주소를 **분해**한다.. WHATWG 방식과 비교하면 username과 password 대신 auth 속성이 있고, searchParams 대신 query가 있다.
- url.format(객체): WHATWG 방식의 url과 기존 노드의 url 모두 사용할 수 있다. 분해되었던 url 객체를 다시 원래 상태로 **조립**

```js

const url = require('url');     
const URL = url.URL;
const myURL = new URL('http://www.gilbut.co.kr/book/bookList.aspx?sercate1=001001000#anchor');
console.log('new URL():', myURL);
console.log('url.format():', url.format(myURL));//합치기
console.log('------------------------------');
const parsedUrl = url.parse('http://www.gilbut.co.kr/book/bookList.aspx?sercate1=001001000#anchor');
console.log('url.parse():', parsedUrl);//분해
console.log('url.format():', url.format(parsedUrl));//합치기

```



##### searchParams 객체

- URL 생성자를 통해 주소 객체를 만들면,  생성된 주소객체에 searchParams 객체가 있다.
- searchParams 객체는 search 부분을 조작하는 다양한 메서드를 지원
- getAll(키): 키에 해당하는 모든 값들을 가져오고 category 키에는 두 가지 값, 즉 nodejs와 javascript의 값이 들어 있다
- get(키): 키에 해당하는 첫 번째 값만 가져온다.
- has(키): 해당 키가 있는지 없는지를 검사
- keys(): searchParams의 모든 키를 반복기(iterator, ES2015 문법) 객체로 가져온다.
- values(): searchParams의 모든 값을 반복기 객체로 가져온다.
- append(키, 값): 해당 키를 추가합니다. 같은 키의 값이 있다면 유지하고 하나 더 추가
- set(키, 값): append와 비슷하지만 같은 키의 값들을 모두 지우고 새로 추가
- delete(키): 해당 키를 제거
- toString(): 조작한 searchParams 객체를 다시 문자열로 만들고 이 문자열을 search에 대입하면 주소 객체에 반영

```js
//searchParams.js

const { URL } = require('url');
const myURL = new URL('http://www.gilbut.co.kr/?page=3&limit=10&category=nodejs&category=javascript');
console.log('searchParams:', myURL.searchParams);
console.log('searchParams.getAll():', myURL.searchParams.getAll('category'));
console.log('searchParams.get():', myURL.searchParams.get('limit'));
console.log('searchParams.has():', myURL.searchParams.has('page'));
console.log('searchParams.keys():', myURL.searchParams.keys());
console.log('searchParams.values():', myURL.searchParams.values());
myURL.searchParams.append('filter','es3');
myURL.searchParams.append('filter','es5');
console.log(myURL.searchParams.getAll('filter'));
myURL.searchParams.set('filter','es6');
console.log(myURL.searchParams.getAll('filter'));
myURL.searchParams.delete('filter');
console.log(myURL.searchParams.getAll('filter'));
console.log('searchParams.toString():', myURL.searchParams.toString());
myURL.search = myURL.searchParams.toString();

```

#### querystring Module

- WHATWG 방식의 url 대신 기존 노드의 url을 사용할 때 search 부분을 사용하기 쉽게 객체로 만드는 모듈 
- [http](http://nodejs.org/api/querystring.html)[://nodejs.org/api/querystring.html](http://nodejs.org/api/querystring.html)
- querystring.stringify(obj, [sep], [eq]) - 쿼리 객체를 쿼리 문자열로 변환해 리턴
- querystring.parse(str, [sep], [eq], [options]) - 쿼리 문자열을 쿼리 객체로 변환해 리턴
- querystring.escape
- querystring.unescape

```js
// querystringExample.js
var querystring = require('querystring'); 
var qStr = 'where=nexearch&query=querystring&sm=top_hty&fbm=1&ie=utf8';
var qObj = querystring.parse(qStr); // 일반적인 사용
var qObj2 = querystring.parse(qStr, '&', '=', { maxKeys: 3 });
// 구분 문자열이 다를 경우 &와 = 자리에 해당 문자를 넣어 사용합니다.
// maxKeys로 3을 넘겨주면 값을 3개만 가져옵니다. 
console.log(qObj); // 쿼리의 값들을 모두 가져옴
console.log(querystring.stringify(qObj));
console.log(querystring.stringify(qObj, '; ', '->')); 
console.log(qObj2); // 쿼리의 값을 3개만 가져옴
console.log(querystring.stringify(qObj2));
console.log(querystring.stringify(qObj2, '; ', '->'));

```

#### crypto(암호화 모듈)

- 암호화를 도와주는 모듈
- 비밀번호는 단방향 암호화(복호화할 수 없는 암호화 방식) 알고리즘을 사용해서 암호화
- 복호화 - 암호화된 문자열을 원래 문자열로 되돌려놓는 것
- 단방향 암호화 알고리즘은 주로 해시 기법을 사용 
- 해시 기법 - 어떠한 문자열을 고정된 길이의 다른 문자열로 바꿔버리는 방식
- createHash(알고리즘): 사용할 해시 알고리즘을 넣어줍니다. md5, sha1, sha256, sha512 등이 가능하지만, md5와 sha1은 이미 취약점이 발견. 현재는 sha512 정도로 충분하지만, 나중에 sha512마저도 취약해지면 더 강화된 알고리즘으로 바꿔야 한다.
- update(문자열): 변환할 문자열을 넣어준다.
- digest(인코딩): 인코딩할 알고리즘을 넣어준다.. base64, hex, latin1이 주로 사용되는데, 그중 base64가 결과 문자열이 가장 짧아 애용됩니다. 결과물로 변환된 문자열을 반환.

```js
const cryto=require("crypto")
console.log('base64',cryto.createHash('sha512').update('1234').digest("base64"));
console.log('hex',cryto.createHash('sha512').update('1234').digest('hex'));
console.log('base64',cryto.createHash('sha512').update('12345').digest('base64'));
```



#### 양방향 암호화

```js
//cipher.js

const crypto = require('crypto');

const cipher = crypto.createCipher('aes-256-cbc','열쇠');
let result = cipher.update('암호화할 문장','utf8','base64');
result += cipher.final('base64');
console.log('암호화:', result);

const decipher = crypto.createDecipher('aes-256-cbc','열쇠');
let result2 = decipher.update(result,'base64','utf8');
result2 += decipher.final('utf8');
console.log('복호화:', result2);

```

#### util 모듈

- node.js의 보조적인 유용한 기능들을 모아놓은 모듈
- http://nodejs.org/api/util.html
- util.format(format, [...]) - console.log() 메소드와 비슷한 기능을 합니다. 차이점이라면 console.log()는 화면에 출력하는 역을 하지만 util.format은 문자열로 반환합니다.
- util.debug(string)
- util.error([...])
- util.puts([...])
- util.print([...])
- util.log(string)
- util.inspect(object, [options])
- Customizing util.inspect colors
- util.isArray(object)
- util.isRegExp(object)
- util.isDate(object)
- util.isError(object)
- util.pump(readableStream, writableStream, [callback])
- util.inherits(constructor, superConstructor)
- util.deprecate: 함수가 deprecated 처리되었음을 알려줍니다. 첫 번째 인자로 넣은 함수를 사용했을 때 경고 메시지가 출력됩니다. 두 번째 인자로 경고 메시지 내용을 넣으면 됩니다. 함수가 조만간 사라지거나 변경될 때 알려줄 수 있어 유용합니다.
- util.promisify: 콜백 패턴을 프로미스 패턴으로 바꿔줍니다. 바꿀 함수를 인자로 제공하면 됩니다. 이렇게 바꾸어두면 async/await 패턴까지 사용할 수 있어 좋습니다.

```js
//util.js

const util = require('util');
const crypto = require('crypto');

const dontUseMe = util.deprecate((x, y) => {
  console.log(x + y);
},'dontUseMe 함수는 deprecated되었으니 더 이상 사용하지 마세요!');
dontUseMe(1, 2);

const randomBytesPromise = util.promisify(crypto.randomBytes);
randomBytesPromise(64)
  .then((buf) => {
    console.log(buf.toString('base64'));
  })
  .catch((error) => {
    console.error(error);
  });

```



#### fs(파일 생성 , 삭제 등)

- 파일을 생성하거나 삭제하고, 읽거나 쓸 수 있습니다. 
- 폴더를 생성하거나 삭제 할 수 있습니다.
- readFile(file, encoding, callback) : 파일을 비동기적으로 읽습니다.
- readFileSync(file, encoding) : 파일을 동기적으로 읽습니다.
- writeFile(file, data, encoding, callback) : 파일을 비동기적으로 씁니다.
- writeFileSync(file, data, encoding) : 파일을 동기적으로 씁니다.
- fs.appendFile() : appends specified content to a file. If the file does not exist, the file will be created
- fs.open()  : takes a "flag" as the second argument, if the flag is "w" for "writing", the specified file is opened for writing. If the file does not exist, an empty file is created
- fs.unlink() :  deletes the specified file
- fs.rename() :  renames the specified file
- readFile의 결과물은 버퍼라는 형식으로 제공됩니다.
- 버퍼는 사람이 읽을 수 있는 형식이 아니므로 toString()을 사용해 문자열로 변환합니다



###### 특징

1. 동기의 경우 다른 일 못하고 대기
2. 비동기 다른 일 수행 가능(콜백 함수 호출로 인하여)
   - 수백개의 I/O요청이 와도 메인 스레드는 백그라운드에 요청 처리 위임하고 요청 처리 완료시 그때 콜백 함수 처리를 한다. 
3. 블로킹과 논블로킹은 백그라운드 작업 완료 여부의 차이다.
4. 동기 비동기는 바로바로 return 되는가의 차이다

```
저를 읽어주세요
```

```js
const fs=require('fs');
fs.readFile('./readme.txt',(err,data)=>{
    if(err){
        throw err;
    }
    console.log(data);
    console.log(data.toString());
})

```

Create File 실습

```js
var fs = require('fs');
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});

```

```js
var fs = require('fs');
fs.open('mynewfile2.txt', 'w', function (err, file) {
  if (err) throw err;
  console.log('Saved!');
});

```

```js
var fs = require('fs');
fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});

```



Update,Delete Files 실습

```js
var fs = require('fs');
fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
  if (err) throw err;
  console.log('Updated!');
});

```

```js
var fs = require('fs');
fs.writeFile('mynewfile3.txt', 'This is my text', function (err) {
  if (err) throw err;
  console.log('Replaced!');
});

```

```js
var fs = require('fs');
fs.unlink('mynewfile2.txt', function (err) {
  if (err) throw err;
  console.log('File deleted!');
});

```





#### fs 의 동기 비동기 확인

```

```



#### fs.access(경로 옵션, 콜백)

- fs.access(경로, 옵션, 콜백): 폴더나 파일에 접근할 수 있는지를 체크. 두 번째 인자로 상수들을 넣고, F_OK는 파일 존재 여부, R_OK는 읽기 권한 여부, W_OK는 쓰기 권한 여부를 체크한다. 파일/폴더나 권한이 없다면 에러가 발생하는데, 파일/폴더가 없을 때의 에러 코드는 ENOENT이다.
- fs.mkdir(경로, 콜백): 폴더를 만드는 메서드입니다. 이미 폴더가 있다면 에러가 발생하므로 먼저 access() 메서드를 호출해서 확인하는 것이 중요합니다.
- fs.open(경로, 옵션, 콜백): 파일의 아이디(fd 변수)를 가져오는 메서드입니다. 파일이 없다면 파일을 생성한 뒤 그 아이디를 가져옵니다. 가져온 아이디를 사용해 fs.read()나 fs.write()로 읽거나 쓸 수 있습니다. 두 번째 인자로 어떤 동작을 할 것인지 설정할 수 있습니다. 쓰려면 w, 읽으려면 r, 기존 파일에 추가하려면 a입니다. 예제에서는 w로 설정했으므로 파일이 없을 때 새로 만들 수 있었습니다. r이었다면 에러가 발생하였을 것입니다.
- fs.rename(기존 경로, 새 경로, 콜백): 파일의 이름을 바꾸는 메서드입니다. 기존 파일 위치와 새로운 파일 위치를 적어주면 됩니다. 반드시 같은 폴더를 지정할 필요는 없으므로 잘라내기 같은 기능을 할 수도 있습니다.
- fs.readdir(경로, 콜백): 폴더 안의 내용물을 확인할 수 있습니다. 배열 안에 내부 파일과 폴더명이 나옵니다.
- fs.unlink(경로, 콜백): 파일을 지울 수 있습니다. 파일이 없다면 에러가 발생하므로 먼저 파일이 있는지를 꼭 확인해야 합니다.
- fs.rmdir(경로, 콜백): 폴더를 지울 수 있습니다. 폴더 안에 파일이 있다면 에러가 발생하므로 먼저 내부 파일을 모두 지우고 호출해야 합니다.

```js
//fsCreate.js

const fs = require('fs');

fs.access('./folder', fs.constants.F_OK | fs.constants.R_OK | fs.constants.W_OK, (err) => {
  if (err) {
    if (err.code ==='ENOENT') {
      console.log('폴더 없음');
      fs.mkdir('./folder', (err) => {
        if (err) {
          throw err;
        }
        console.log('폴더 만들기 성공');
        fs.open('./folder/file.js','w', (err, fd) => {
          if (err) {
            throw err;
          }
          console.log('빈 파일 만들기 성공', fd);
 
fs.rename('./folder/file.js','./folder/newfile.js', (err) => {
            if (err) {
              throw err;
            }
            console.log('이름 바꾸기 성공');
          });
        });
      });
    } else {
      throw err;
    }
  } else {
    console.log('이미 폴더 있음');
  }
});

```

```js
//fsDelete.js

const fs = require('fs');
fs.readdir('./folder', (err, dir) => {
  if (err) {
    throw err;
  }
  console.log('폴더 내용 확인', dir);
  fs.unlink('./folder/newFile.js', (err) => {
    if (err) {
      throw err;
    }
    console.log('파일 삭제 성공');
    fs.rmdir('./folder', (err) => {
      if (err) {
        throw err;
      }
      console.log('폴더 삭제 성공');
    });
  });
});

```



#### fs 의 copyFile()  

1. node 8.5버전에서 새로 추가된 파일 복사 메서드
2. 첫번 쨰 인자로 복사할 파일을 두번째 인자로 복사될 경로를, 세번째 인자로 복사 후 실행될 콜백 함수 지정

```js
//copyFile.js

const fs=require('fs');


fs.copyFile('readme4.txt','writeme4.txt',(error)=>{
    if(error){
        return console.error(error);
    }
    console.log("복사 완료");
});
```



#### 버퍼와 스트림 이해

- 파일을 읽거나 쓰는 방식 - 버퍼를 이용하는 방식, 스트림을 이용하는 방식
- 예] 버퍼링은 데이터를 모으는 동작이고, 스트리밍은  데이터를 조금씩 전송하는 동작입니다. 
- 스트리밍하는 과정에서 버퍼링을 할 수도 있습니다. (전송이 너무 느리면   최소한의 데이터를 모아야 하고, 데이터가 처리 속도보다 빨리 전송되어도 미리 전송받은 데이터를 저장할 공간이 필요합니다)
- 노드는 파일을 읽을 때 메모리에 파일 크기만큼 공간을 마련해두며, 파일 데이터를 메모리에 저장한 뒤 사용자가 조작할 수 있도록 해줍니다. (이 경우 문제점은 파일이 메모리보다 크면 안된다)
- 메모리에 저장된 데이터가 바로 버퍼입니다.

/// **스트림**은 단방향(output input 하는 방식)

- byte[] 바이트 배열을 read하고 write해서 좀더 이용가능성을 높힌다.

/// **채널**은 양방향(버퍼에 넣어 놓으면 write 할 수 있다. 포지션 지정해서 중간에 랜덤하게 액세스 가능)

##### 버퍼

- JavaScript는 유니 코드와 호환되지만 바이너리 데이터에는 적합하지 않습니다. 
- TCP 스트림이나 파일 시스템을 다루는 동안, 옥텟(octet ) 스트림을 처리해야합니다
- Node는 정수 배열과 비슷한 원시(raw) 데이터를 저장하는 인스턴스를 제공
- V8 heap 외부의 raw 메모리 할당에 해당하는 Buffer 클래스를 제공
- 전역 객체
- 새롭게 만들기 위해서는 new 키워드를 이용한다

버퍼생성

```js
//buffer 생성

var buf = new Buffer(10);
var buf = new Buffer([10, 20, 30, 40, 50]);
var buf = new Buffer("Simply Easy Learning", "utf-8");

```



buffer에 쓰기

```js
//buffer에 쓰기 buf.write(string[, offset][, length][, encoding])

buf = new Buffer(256);
len = buf.write("Simply Easy Learning");
console.log("Octets written : "+  len);

```

buffer에 읽기

```js
//buffer에서 읽기 buf.toString([encoding][, start][, end])

buf = new Buffer(26);
for (var i = 0 ; i < 26 ; i++) {
  buf[i] = i + 97;
}

console.log( buf.toString('ascii'));       // outputs: abcdefghijklmnopqrstuvwxyz
console.log( buf.toString('ascii',0,5));   // outputs: abcde
console.log( buf.toString('utf8',0,5));    // outputs: abcde
console.log( buf.toString(undefined,0,5)); // encoding defaults to 'utf8', outputs abcde

```

buffer를 json으로 변환

```js
//buffer 를 JSON으로 변환  buf.toJSON()

var buf = new Buffer('Simply Easy Learning');
var json = buf.toJSON(buf);
console.log(json);

```

buffer 연결

```js
//buffer 연결  Buffer.concat(list[, totalLength])

var buffer1 = new Buffer('TutorialsPoint ');
var buffer2 = new Buffer('Simply Easy Learning');
var buffer3 = Buffer.concat([buffer1,buffer2]);

console.log("buffer3 content: " + buffer3.toString());
```

buffer 비교

```js
//buffer 비교  buf.compare(otherBuffer);

var buffer1 = new Buffer('ABC');
var buffer2 = new Buffer('ABCD');
var result = buffer1.compare(buffer2);

if(result < 0) {
   console.log(buffer1 +" comes before " + buffer2);
} else if(result === 0) {
   console.log(buffer1 +" is same as " + buffer2);
} else {
   console.log(buffer1 +" comes after " + buffer2);
}

```

buffer복사

```js
//buffer 복사  buf.copy(targetBuffer[, targetStart][, sourceStart][, sourceEnd])

var buffer1 = new Buffer('ABC');//저장한 후 

//copy a buffer
var buffer2 = new Buffer(3);//사이즈만 생성
buffer1.copy(buffer2);//타켓(buffer2)에 소스(buffer1를 )를 저장
console.log("buffer2 content: " + buffer2.toString());//buffer2를 읽어 복사 확인

```

buffer slice, slicing a buffer, lenth of the buffer

```js
//buffer slice  buf.slice([start][, end])
//일부만 가져오고 싶을때
var buffer1 = new Buffer('TutorialsPoint');

//slicing a buffer
var buffer2 = buffer1.slice(0,9);
console.log("buffer2 content: " + buffer2.toString());

var buffer = new Buffer('TutorialsPoint');

//length of the buffer
console.log("buffer length: " + buffer.length); //버퍼의 길이

```

 ##### 스트림(stream)

원본에서 데이터를 읽거나 데이터를 대상에 연속적으로 쓸 수있게 해주는 개체 

1. Node.js 스트림 유형 

- Readable - 읽기 작업에 사용되는 스트림
- Writable - 쓰기 작업에 사용되는 스트림
- Duplex - 읽기 및 쓰기 작업에 모두 사용할 수있는 스트림
- Transform - 입력을 기반으로 출력이 계산되는 양방향 스트림
- 각 유형의 Stream은 EventEmitter 인스턴스이며 서로 다른 시간에 여러 이벤트를 발생

2. 이벤트

- data이벤트 - 읽을 수있는 데이터가있는 경우 시작
- end이벤트 - 읽을 데이터가 더 이상 없을 때 시작
- error이벤트 - 데이터 수신 또는 쓰기 오류가 발생하면 시작
- finish 이벤트 - 모든 데이터가 기본 시스템으로 플러시 된 경우 시작

```
//input.txt
Streams are objects that let you read data from a source or write data to a destination in continuous fashion

```



stream 읽기

```js
//  stream으로부터 읽기
var fs = require("fs");
var data = '';
var readerStream = fs.createReadStream('input.txt');
// Set the encoding to be utf8. 
readerStream.setEncoding('UTF8');//인코딩 해야하다.
// Handle stream events --> data, end, and error 핸들러 이벤트 다 지정
readerStream.on('data', function(chunk) {
   data += chunk;
});
readerStream.on('end',function() {
   console.log(data);
});
readerStream.on('error', function(err) {
   console.log(err.stack);
});
console.log("Program Ended");
```



strea 쓰기

```js
//  stream에 쓰기
var fs = require("fs");
var data = 'Simply Easy Learning';
// writable stream 생성
var writerStream = fs.createWriteStream('output.txt');
// utf8로 인코딩한 data를 stream 에 쓰기
writerStream.write(data,'UTF8');
// Mark the end of file
writerStream.end();
// Handle stream events --> finish, and error
writerStream.on('finish', function() {
   console.log("Write completed.");
});
writerStream.on('error', function(err) {
   console.log(err.stack);
});
console.log("Program Ended");

```



Stream Piping

​	한 스트림의 출력을 다른 스트림의 입력으로 제공

```js
var fs = require("fs");
// Create a readable stream
var readerStream = fs.createReadStream('input.txt');
// Create a writable stream
var writerStream = fs.createWriteStream('output.txt');
// Pipe the read and write operations
// read input.txt and write data to output.txt
readerStream.pipe(writerStream);

console.log("Program Ended");

```

Stream Chaining

- 한 스트림의 출력을 다른 스트림에 연결하고 여러 스트림 작업 체인을 만드는 메커니즘

```js
var fs = require("fs");
var zlib = require('zlib');//압출해주는 모듈이다.
// input.txt가 압축되어 현재 디렉토리에 input.txt.gz라는 파일이 생성
fs.createReadStream('input.txt')
   .pipe(zlib.createGzip())//pipe 메서드가 있어서  압축을 한다.
   .pipe(fs.createWriteStream('input.txt.gz'));//압축파일로 생성
  
console.log("File Compressed."); 

```



```js
var fs = require("fs");
var zlib = require('zlib');
//input.txt.gz을  input.txt로 압축풀기
fs.createReadStream('input.txt.gz')//압출 풀 대상
   .pipe(zlib.createGunzip())
   .pipe(fs.createWriteStream('input2.txt'));//다른 이름으로 압출파일 푼다
  
console.log("File Decompressed.");

```



##### 버퍼와 스트림의 이해 (각종 메서드)

- Buffer - 버퍼를 직접 다룰 수 있는 객체
- from(문자열): 문자열을 버퍼로 바꿀 수 있습니다. length 속성은 버퍼의 크기를 알려줍니다. 바이트 단위입니다.
- toString(버퍼): 버퍼를 다시 문자열로 바꿀 수 있습니다. 이때 base64나 hex를 인자로 넣으면 해당 인코딩으로도 변환할 수 있습니다.
- concat(배열): 배열 안에 든 버퍼들을 하나로 합칩니다.
- alloc(바이트): 빈 버퍼를 생성합니다. 바이트를 인자로 지정해주면 해당 크기의 버퍼가 생성됩니다.



```js
//buffer.js

const buffer = Buffer.from('저를 버퍼로 바꿔보세요');
console.log('from():', buffer);
console.log('length:', buffer.length);
console.log('toString():', buffer.toString());

const array = [Buffer.from('띄엄'), Buffer.from('띄엄'), Buffer.from('띄어쓰기')];//3개의 버퍼가 생긴것이다.
const buffer2 = Buffer.concat(array);//이것을 컴캣해서
console.log('concat():', buffer2.toString());

const buffer3 = Buffer.alloc(5);//결과 찍는 것
console.log('alloc():', buffer3);

```

- 모든 내용을 버퍼에 다 쓴 후에야 다음 동작으로 넘어가므로 파일 읽기, 압축, 파일 쓰기 등의 조작을 연달아 할 때 매번 전체 용량을 버퍼로 처리해야 다음 단계로 넘어갈 수 있다.
- 버퍼의 크기를 작게 만들어서 여러 번에 나눠서 보내는 방식 **스트림**이라 한다. 
  - 예] 버퍼 1MB를 만든 후 100MB 파일을 백 번에 걸쳐 보내는 것(그래서 버퍼랑 스트림을 같이 써야 한다.)

- createReadStream - 파일을 읽는 스트림 메서드
- 첫 번째 인자로 읽을 파일 경로를 넣습니다. 
- 두 번째 인자는 옵션로서 highWaterMark 는  버퍼의 크기(바이트 단위)를 정할 수 있습니다.(기본값은 64KB) 
- readStream은 이벤트 리스너 (data, end, error 이벤트)를 붙여서 사용합니다. 

 ```js
//createReadStream.js

const fs = require('fs');
const readStream = fs.createReadStream('./readme3.txt', { highWaterMark: 16 });
const data = [];
readStream.on('data', (chunk) => {
  data.push(chunk);
  console.log('data :', chunk, chunk.length);
});
readStream.on('end', () => {
  console.log('end :', Buffer.concat(data).toString());
});
readStream.on('error', (err) => {
  console.log('error :', err);
});

 ```

- 쓰기 스트림 메서드 - createWriteStream() 
- finish 이벤트 리스너 - 파일 쓰기가 종료되면 콜백 함수가 호출됩니다.
- writeStream에서 제공하는 write() 메서드로 넣을 데이터를 씁니다.
- 데이터를 다 썼다면 end() 메서드로 종료를 알려줍니다. 이때 finish 이벤트가 발생합니다.
- createReadStream으로 파일을 읽고 그 스트림을 전달받아 createWriteStream으로 파일을 쓸 수도 있습니다. 





- 읽기 스트림과 쓰기 스트림을 만들어둔 후 두 개의 스트림 사이를 pipe 메서드로 연결해주면 자동으로 데이터가 writeStream으로 넘어갑니다.
- pipe는 스트림 사이에 연결할 수 있습니다
- zlib 모듈 - 파일 압축 모듈
- createGzip() - 스트림을 지원, readStream과 writeStream 중간에서 파이핑을 할 수 있습니다. 버퍼 데이터가 전달되다가 gzip 압축을 거친 후 파일로 쓰여집니다.







##### Events Module

1. Node.js는 이벤트에 10개가 넘는 이벤트 핸들러를 연결한 경우 오류로 간주합니다.
2. setMaxListeners(limit) : 이벤트 핸들러 연결 개수를 limit 만큼 조절합니다.
   - 제한할 수 있다. 제한 가능
3. removeListener(eventName, handler) : 특정 이벤트의 이벤트 핸들러를 제거합니다.
4. removeAllListener([eventName]) : 모든 이벤트 핸들러를 제거합니다.
5. once(eventName, eventHandler) : 이벤트 핸들러를 한 번만 연결합니다.
6. on(이벤트명, 콜백): 이벤트 이름과 이벤트 발생 시의 콜백을 연결해줍니다. (이벤트 리스닝)이벤트 하나에 이벤트 여러 개를 연결 할 수 있습니다.
7. addListener(이벤트명, 콜백): on과 기능이 동일
   - 일반적으로는 ON 과 ADD를 사용한다.
8. emit(이벤트명): 이벤트를 호출하는 메서드입니다. 이벤트 이름을 인자로 넣어주면 미리 등록해뒀던 이벤트 콜백이 실행됩니다. 
   - 인수로 이벤트를 지정하면 이벤트 핸드러를 호출하는 결과가 나타난다.
9. off(이벤트명, 콜백): Node 10 버전에서 추가된 메서드로, removeListener와 기능이 동일
10. listenerCount(이벤트명): 현재 리스너가 몇 개 연결되어 있는지 확인합니다.

```js
process.once('uncaughtException', function(error) {
    console.log('예외 발생');
});
 
setInterval(function () {
    error.error.error('^ ^');//에러를 발생시킨 것이다.에러 객체의 에러 속성의 에러를 말생한다.허나 위에 process.once를 지정했기에 한번만 나타날 것이다.
}, 3000);

```

Events-이벤트 생성, 연결, 제거 코드 예제

```js
const EventEmitter = require('events');

const myEvent = new EventEmitter();//이벤트 에밋객체 생성한다.
myEvent.addListener('event1', () => {
  console.log('이벤트 1');
});//우리가 지정하는 이벤트이다.
myEvent.on('event2', () => {
  console.log('이벤트 2');
});//on 메서드로 핸들러 하나 더 추가
myEvent.on('event2', () => {
  console.log('이벤트 2 추가');
});

myEvent.emit('event1'); //이벤트 발생시킨것
myEvent.emit('event2');

myEvent.once('event3', () => {
  console.log('이벤트 3');
});//이벤트 한번만되도록 once
myEvent.emit('event3');
myEvent.emit('event3');

myEvent.on('event4', () => {
  console.log('이벤트 4');
});
myEvent.removeAllListeners('event4');//이벤트 4제거
myEvent.emit('event4');//이벤트4 실행해도 제거되엇 나오는거 없다.

const listener = () => {
  console.log('이벤트 5');
};
myEvent.on('event5', listener);
myEvent.removeListener('event5', listener);//이벤트5제거
myEvent.emit('event5');//이벤트 5실행해도 제거 안된다.
 
console.log(myEvent.listenerCount('event2'));//이벤트 몇개있나 확인해보자
//이벤트 3은 한번만이었으므로 없어졌고 4,5는 삭제했다. 결국 남은 건 2개

```



Node.js에서 이벤트를 연결할 수 있는 모든 객체는 EventEmitter 객체의 상속을 받는다.

EventEmitter : node.js 의 모든 이벤트처리가 정의된 기본객체로, 이벤트를 사용하기 위해서는 이 객체를 재정의해서 사용해야할 수 있다.

on( ) : 이벤트를 연결하는 함수다.   on( ) 함수를 이용해서  이벤트를 캐치 , 모든 이벤트처리는 이런 동일한 루틴을 거쳐서 사용하게 된다.

emit( ) : 이벤트를 발생시키는 함수이고,   emit('data') 의 형태로 이벤트를 발생시켜야 한다.

```js
// 1. 이벤트가 정의되 있는 events 모듈 생성. 이전 버전의 process.EventEmitter() 는 deprecated!
var EventEmitter = require('events');
// 2. 생성된 이벤트 모듈을 사용하기 위해 custom_object로 초기화
var custom_object = new EventEmitter();
// 3. events 모듈에 선언되어 있는 on( ) 함수를 재정의 하여 'call' 이벤트를 처리 
custom_object.on('call', ()=> {//call 이벤트를 등록한다. on 은 이벤트를 연결한다.
    console.log('called events!');
});
// 4. call 이벤트를 강제로 발생 emit으로 이벤트를 호출한다.
custom_object.emit('call');

```



Events 

- 이벤트를 이용해서 매초 콘솔창에 주기적으로 현재시간을 출력하는 타이머 모듈 생성

```js
//custom_module_timer.js
var EventEmitter = require('events');
// 1. setInterval 함수가 동작하는 interval 값을 설정합니다. 1초에 한번씩 호출
var sec = 1;

// 2. timer변수를 EventEmitter 로 초기화
exports.timer = new EventEmitter();

// 3. javascript 내장함수인 setInterval 을 사용해서 1초에 한번씩 timer 객체에 tick 이벤트 발생
setInterval(function(){
    exports.timer.emit('tick');
}, sec*1000);

```



```js
//call_timer.js
var module = require('./custom_module_timer');

// 1. module 내부에 선언된 timer객체를 통해 tick 이벤트를 캐치하고, 이벤트 발생시마다 현재시간을 출력
module.timer.on('tick', function(time){
    var time = new Date(); // 2. 현재 시간을 가져오기 위한 Date 객체 생성
    console.log('now:'+time);
});//1초마다 tick이벤트를 발생하면 콘솔에 현재시간 출력

```



try~catch

- 하나뿐인 스레드(싱글 스레드)가 에러로 인해 멈춘다는 것은 전체 서버가 멈춘다.

```js
//error1.js

setInterval(() => {
  console.log('시작');
  try {
    throw new Error('서버를 고장내주마!');
  } catch (err) {
    console.error(err);//에러를 콘솔에 출력
  }
}, 1000)//에러를 강제 발생

```

- 노드 자체에서 잡아주는 에러
- 노드 내장 모듈의 에러는 실행 중인 프로세스를 멈추지 않는다.
- 에러 로그를 기록해두고 나중에 원인을 찾아 수정한다.
- throw를 하는 경우에는 반드시 try catch문으로 throw한 에러를 잡아주어야 합니다.

```js
//error2.js  - fs.unlink()로 없는 파일을 삭제
// try catch가 없는 상태 임에도 에러를 잡을까?
//노드 자체적으로 예외 처리를 해준다는 것 
const fs = require('fs');

setInterval(() => {
  fs.unlink('./abcdefg.js', (err) => {
    if (err) {
      console.error(err);
    }
  });
}, 1000);

```

예측 불가능한 에러를 처리하는 방법

- process 객체에 uncaughtException 이벤트 리스너 연결 - 처리하지 못한 에러가 발생했을 때 이벤트 리스너가 실행되고 프로세스가 유지됩니다. 
- 단순히 에러 내용을 기록하는 정도로 사용하고 process.exit()로 프로세스를 종료하는 것이 좋습니다. 
- 노드는 uncaughException 이벤트 발생 후 다음 동작이 제대로 동작하는지를 보증하지 않습니다

```js
//error3.js

process.on('uncaughtException', (err) => {
  console.error('예기치 못한 에러', err);
});

setInterval(() => {
  throw new Error('서버를 고장내주마!');
}, 1000);//1초 지나서 에러발생

setTimeout(() => {
  console.log('실행됩니다');
}, 2000);

```



#### Net 모듈

- TCP 프로토콜 기반의 소켓 프로그래밍을 지원하는 코어 모듈
- Node.js에서 소켓은 Stream이면서 EventEmitter이다. (기존이 이벤트 뿐만 아니라 사용자 정의 이벤트를 만들어 사용자 정의 프로토콜을 설계할 수 있다) 

| net.createServer([options],   [connectionListener])          | •TCP   서버를 생성   •서버에   새로운 요청이 올 때마다 connection   이벤트가 발생   •'connectionListener'   매개 변수는 자동으로 'connection'이벤트의 리스너로 추가된다   •‘options’는 {allowHalfOpen: false}가 기본값이며 true를 지정하면 소켓이 FIN   패킷을 받았을 때 FIN   패킷을 자동으로 보내지 않습니다.   (*FIN 패킷은 소켓을 더 이상 사용하지 않겠다는 의미로서,   ‘allowHalfOpen’은   한쪽에서 연결을 종료했을 때 반대쪽도 종료할 것인지를 결정 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| net.connect(options,   [connectionListener])   net.connect(port,   [host], [connectionListener])   net.connect(path,   [connectionListener]) | •새로운   소켓 객체를 생성하고 해당 위치로 소켓을 연다.    •소켓이   설정되면‘connection’   이벤트가 발생되고,   ‘connectionListener’ 매개   변수는‘connection’   이벤트에 대한 리스너로서 추가된다.   •host’를 생략하면 IPv4에 맞는 모든 주소로부터 연결을 받습니다.   •‘port’에 0을   넣으면 임의의 포트를 선택   •비동기   함수 |
| server.listen(port,   [host], [backlog], [callback])   server.listen(path,   [callback])   server.listen(handle,   [callback]) | •지정된   서버(port,   host, path, …)의   커넥션 연결을 시작한다.(대기상태로 기다린다)      •서버가   실행되면 ‘listening’   이벤트가 발생되고,   ‘callback’ 매개 변수는 ‘listening’   이벤트에 대한 리스너로서 추가된다. |

| server.address()         | 서버에 호스트와 포트에 대한 정보가 담겨 있습니다   IP 주소와 포트 번호와 같은 서버 정보를 운영체제로부터 가져온다.    ‘listening’   이벤트가 발생한 후에만 메소드 호출이 가능하다. |
| ------------------------ | ------------------------------------------------------------ |
| server.pause(msec)       | 서버가 밀리세컨드 동안 새 요청을 받지 않습니다.         서버에 부하가 심한 경우 유용하게 사용할 수 있습니다. |
| server.close([callback]) | 새로운 커넥션 연결을 중단하고 기존의 커넥션만 유지한다.         비동기로 실행됨 모든 커넥션이 종료되었을 때 서버를 닫는다.    서버는 ‘close’ 이벤트를 발생시키고 선택적으로 ‘close’   이벤트를 받을 수 있는 콜백을 매개 변수로 정할 수 있다. |
| server.maxConnections    | 서버가 최대로 받아들일 수 있는 연결 수를 지정                |
| server.connections       | 서버의 동시 연결 connection수를 알 수 있음                   |



```js
// createServer.js 
var net = require('net'); 
var server = net.createServer(function(socket) {
	console.log('createServer()');  // 연결이 되면 서버 로그에 남는 메시지
	socket.on('end', function() {//넘어온 소켓객체에 on 으로 이벤틍 ㅕㄴ결
		console.log('socket end');  // 연결이 끊어지면 서버 로그에 남는 메시지
	});
	socket.write('Hello World\r\n');  // 클라이언트에게 보여지는 메시지
}); 
server.listen(8124, function() {//아무거나 지정해도 된다(8000번도 오케이 범위가 무엇이었는지는 까묵..)
	console.log('서버가 %d 포트에 연결되었습니다.', server.address().port);  // 서버가 실행되면 서버 로그에 남는 메시지
});

```

노드로 실행한 후 아래 를 진행해야 한다.

허나 telnet 이 비실행사태라면 실행을 해주어야 하는데 제어판에서

프로그램 및 기능에서 윈도우 기능 사용/사용안함에서 talnet 기능을 사용함으로 바꿔주면 된다.

텔렛 클라리언트 체크 후 저장! 확인을 눌러주자.

윈도 커맨드 창은 시작프로그램 눌렀을 때 나오는 검색창을 말한다.

```js
// 윈도 커맨드창에서
 
telnet localhost 8124 

```



##### net.Server의 이벤트

| listening   이벤트  | server.listen()이 호출될 때 발생                             |
| ------------------- | ------------------------------------------------------------ |
| connection   이벤트 | 새 연결이 생겼을 때 발생   function(socket)   {} , 파라미터인 socket은 연결된 소켓으로 net.Socket의 객체 |
| error   이벤트      | 서버에서 에러가 날 때 발,   error 이벤트 발생 후에는 close   이벤트가 발생함 |
| close   이벤트      | 서버가 닫혔을 때 발생                                        |



##### net.Socket

- net.Socket은 TCP나 유닉스 소켓의 추상객체로써 이중 통신 방식의 스트림 인터페이스를 구현

| socket.setEncoding(encoding)                 | 소켓으로 받는 데이터의 인코딩을 지정    ascii, utf8, base64를 사용할 수 있ek. |
| -------------------------------------------- | ------------------------------------------------------------ |
| socket.write(data,   [encoding], [callback]) | 소켓에 데이터를 보내기 위해 사용   encoding은 data가   문자열일 때 사용하고 기본값을 UTF-8      커널 버퍼로 모든 데이터를 보내면 true를, 아직   큐에 쌓여있다면 false를 리턴   퍼가 비워져서 다시 쓸 수 있는 상태가 되면 drain   이벤트가 발생   콜백함수는 데이터가 모두 쓰여졌을 때 호출됨 |
| socket.end([data],   [encoding])             | FIN   패킷을 보내 소켓을 닫기 때문에 서버 쪽에서는 데이터를 계속해서   보낼 수 있습니다.    end()   함수에 data,   encoding 파라미터를 주면 socket.write() 를 하고 sockec.end() 를 한 것과 동일합니다. |
| socket.pause()                               | 소켓에서 데이터를 읽는 것을 멈추기 때문에 data   이벤트가 더 이상 발생하지 않습니다.  다시   데이터를 받기 위해서는 socket.resume()을 실행합니다. |
| socket.remoteAddress                         | 접속한 클라이언트의 원격 IP를 돌려줍니다                     |
| socket.write()                               | 소켓으로 데이터를 보내는데 만약 보낼 수 없을 때는 데이터를 큐에 넣고   추후에 다시 전송합니다. |
| socket.bufferSize                            | 현재 버퍼의 문자 수를 나타내는 프로퍼티(버퍼에   존재하는 문자열은 실제 데이터를 보낼 때 인코딩되기 때문에 socket.bufferSize가 알려주는 크기는 인코딩되기 전의 문자 크기) |



| socket.connect(port,   [host], [connectListener])   socket.connect(path,   [connectListener]) | •일반적으로   net.connect 래핑 함수를 호출하여 소켓을 열기 때문에 사용자 정의 소켓을 구현해야 할   경우에만 사용한다.    •   ‘connectListener’ 매개 변수는 ‘connect’ 이벤트에 대한 리스너로서 추가된다. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| socket.destroy()                                             | •소켓의   I/O   활동을 발생하지 않게 하는 메소드이며, 에러가   발생했을 경우에필요하다. |
| socket.resume()                                              | •데이터   읽기를 재개한다                                    |
| socket.setTimeout(timeout,   [callback])                     | •소켓에   설정된 초과 시간이 지나면 ’timeout’   이벤트가 발생하며,   ‘callback’ 매개 변수는 ‘timeout’   이벤트의 리스너로서 추가된다.   •‘timeout’   이벤트가발생하여도 커넥션은 유지된다.    •커넥션을   끊기 위해서는 사용자가 end   메소드나 destroy 메소드를 호출해야 한다. |
| socket.setNoDelay([noDelay])                                 | •Nagle   알고리즘을 비활성화하고, 기본적으로 TCP 연결은 Nagle 알고리즘을사용하므로 데이터를 보내기 전에 이를 버퍼에 저장한다.   •‘noDelay’ 매개 변수를 설정하면 write   메소드가 호출될 때마다 곧바로 데이터를 전송한다 |
| socket.setKeepAlive([enable],   [initialDelay])              | •Keep-Alive   기능의 활성화 유무를 설정하는 메소드이다. 기본적으로   비활성화 되어있으며 지연 시간을 설정할 수 있다. |



| socket.address()    | •IP   주소와 포트 번호와 같은 서버 정보를 운영체제로부터 가져온다. |
| ------------------- | ------------------------------------------------------------ |
| socket.remotePort   | •원격   포트를 가지는 프로퍼티                               |
| socket.bytesRead    | •소켓이   받은 총 바이트 수를 가지는 프로퍼티                |
| socket.bytesWritten | •소켓에   보낸 총 바이트 수를 가지는 프로퍼티                |

socket.on(event,listener)

| connect   이벤트 | 소켓 연결이 되면 발생                                        |
| ---------------- | ------------------------------------------------------------ |
| data   이벤트    | 소켓에서 데이터를 받으면 발생                                |
| end   이벤트     | 소켓으로 FIN 받았을 때 발생                                  |
| drain   이벤트   | 쓰기 버퍼가 비워졌을 때 발생                                 |
| timeout이벤트    | 시간이 초과된 경우 발생                                      |
| error   이벤트   | 에러가 나면 발생, error 이벤트 발생 후에는 close   이벤트가 발생함 |
| close   이벤트   | 소켓이 완전히 닫혔을 때 발생                                 |



```js
// tcpserver.js
var net = require('net');
//서버를 생성
var server = net.createServer(function(socket){
   console.log(socket.address().address +" connected");
   //client로부터 오는 data를 화면에 출력
   socket.on('data', function(data) {
      console.log('rcv:'+data);
   });
   //client와 접속이 끊기는 메시지 출력
   socket.on('close', function() {
      console.log('client disconnected');
   });
   //client가 접속하면 화면에 출력해주는 메시지
   socket.write('welcome to server');
   });
//에러가 발생할 경우 화면에 에러메시지 출력
server.on('error', function(err) {
    console.log('err' + err);
});
//Port 5000으로 접속이 가능하도록 대기
server.listen(5000, function(){
    console.log('listening on 5000...');
});//listen 5000번 포트를 부르고 대기하고 있다고 콘솔로 찍었따.

```



```js
// tcpclient.js
var net = require('net');
//서버 5000번 포트로 접속
var socket = net.connect( { port: 5000} );
socket.on('connect', function( ){
   console.log("connected to server!");
    setInterval(function() {  //1000ms의 간격으로 hello korea를 서버로 요청
         socket.write('hello korea!');
      }, 1000);
    socket.on('data', function(chunk) {  //서버로부터 받은 데이터를 화면에 출력
      console.log('recv : ' + chunk);
   });
   socket.on('end', function( ) {   //접속이 종료되었을 때 메시지 출력
      console.log('disconnected');
   });
   socket.on('error', function(err) {   //에러가 발생할 경우 화면에 에러메시지 출력
       console.log('err : ' + err);
});
socket.on('timeout', function(){   ////connection에서 timeout이 발생하면 메시지 출력
    console.log('connection timeout');
});
});

```

cmd 두개를 열어서 해보자. 세개 열어서 또 연결해도 된다.





## NPM 패키지 매니저

#### npm

- Node Package Manager

- package.json 으로 패키지를 관리한다.

- 자바스크립트 프로그램은 패키지라는 이름으로 npm에 등록되어 있으므로 특정 기능을 하는 패키지가 필요하다면 npm에서 찾아 설치합니다

- npm에 업로드된 노드 모듈을 패키지라고 부릅니다. 

- 패키지가 다른 패키지를 사용할 수도 있습니다. (의존관계)

- Node.js에서는 자주 쓰이고 재사용되는 자바스크립트 코드들을 패키지로 만들어서 사용할 수 있습니다. 

- 패키지를 모아놓은 저장소를 npm이라 한다.

- https://npmjs.com/ 이곳에 등록되어 있는 패키지 모듈 확인 가능

- Node.js를 설치하면 자동으로 npm이 설치된다.

- `npm -v`로 버전을 체크(cmd 창에서 앞에것을 쳐준다.)

- 1npm update -g` npm 최신버전으로 업데이트

- npm은 package.json (패키지 관리)을 만드는 명령어를 제공합니다.

  

- package name: 패키지의 이름입니다. package.json의 name 속성에 저장됩니다.
- version: 패키지의 버전입니다. npm의 버전은 다소 엄격하게 관리됩니다.  
- entry point: 자바스크립트 실행 파일 진입점입니다. 보통 마지막으로 module.exports를 하는 파일을 지정합니다. package.json의 main 속성에 저장됩니다.
- test command: 코드를 테스트할 때 입력할 명령어를 의미합니다. package.json scripts 속성 안의 test 속성에 저장됩니다.
- git repository: 코드를 저장해둔 Git 저장소 주소를 의미합니다. 나중에 소스에 문제가 생겼을 때 사용자들이 이 저장소에 방문해 문제를 제기할 수도 있고, 코드 수정본을 올릴 수도 있습니다. package.json의 repository 속성에 저장됩니다.
- keywords: 키워드는 npm 공식 홈페이지([https://npmjs.com](https://npmjs.com/))
   에서 패키지를 쉽게 찾을 수 있게 해줍니다. package.json의 
   keywords 속성에 저장됩니다.
- license: 해당 패키지의 라이선스를 넣어주면 됩니다. 

```js
$ npm init
....
package name : (폴더명) [프로젝트 이름 입력]
version : (1.0.0) [프로젝트 버전 입력]
description : [프로젝트 설명 입력]
entry point : index.js
test command : [엔터 키 클릭]
git repository : [엔터 키 클릭]
keywords : [엔터 키 클릭]
author : [여러분의 이름 입력]
license : (ISC) [엔터 키 클릭]

```

cmd 를 들어가서 test파일위치에서 npm init 를 친다

그 후 엔터엔터~

그러면 package.json파일 생성된것을 확인 할 수 있다. 각각은 바꿀 수 있다. 저 위의 내용을 정보로서 알고 있어야 한다.

##### npm 명령

- npm install 패키지@버전 :  특정한 버전을 설치
- npm install 주소 : 특정한 저장소에 있는 패키지를 설치 
- npm update : 설치한 패키지를 업데이트
- npm dedupe :  npm의 중복된 패키지들을 정리할 때 사용
- npm docs :  패키지에 대한 설명을 보여줍니다.
- npm root :  node_modules의 위치를 알려줍니다.
- npm outdated :  오래된 패키지가 있는지 알려줍니다
- npm ls :  패키지를 조회하는 명령어, 현재 설치된 패키지의 버전과 dependencies를 트리 구조로 표현합니다. 
- npm ll  더 자세한 정보를 줍니다. 
- npm ls [패키지명] :  해당 패키지가 있는지와, 해당 패키지가 어떤 패키지의 dependencies인지 보여줍니다.
- npm search : npm 저장소에서 패키지를 검색하는 명령어
- npm owner : 키지의 주인이 누군지 알려주는 명령어
- npm bugs : 버그가 발생했을 때 어떻게 패키지의 주인에게 연락을 취할지 알려줍니다. 
- npm [start | stop | restart | test | run ]
- npm cache :  npm 내의 cache를 보여줍니다.
- npm rebuild : npm을 다시 설치하는 명령어 
- npm config : npm의 설정을 조작하는 명령어
- npm uninstall [패키지명] :  해당 패키지를 제거하는 명령어
- npm info [패키지명]은 패키지의 세부 정보를 파악하고자 할 때 사용하는 명령어입니다. package.json의 내용과 의존 관계, 설치 가능한 버전 정보 등이 표시됩니다. 

##### package.json

- 프로젝트에서 필요로 하는 패키지명과 함께 패키지 버전관리에 사용됨  
- npm init 명령어로 package.json 생성 (프로젝트 폴더 안으로 cmd를 통해서 이동한 후 입력)
- 노드 어플리케이션 / 모듈의 경로에 위치
- 패키지의 속성을 정의
- scripts 부분은 npm 명령어를 저장해두는 부분

```js
$npm run [스크립트 명령어]//아래에 명령어 두개를 등록했다. test랑 start
$npm run test
$npm run  start


```



```js
//package.json  형식
{
  "name": “akasha",
  "version": "1.0.0",
  "description": "npm description",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "keywords": [//키워드는 임의로 작성
    “akasha",
    "npm",
    "nodejs",
    "lecture"
 ],
  "author": “Akasha.Park",
  "license": “ "
}

```



만들어둔 package.json파일을 열고 (편집) start에 "node tcp.js" 라 쓰자(아까 만든 server파일)

그후 저장후 cmd 창에서 위의 명령어 중 npm run start를 작성하면 node tcp 실행됨을 알 수 있다.





- npm install 명령어에 --save 옵션은  dependencies에 패키지 이름을 추가하는 옵션이지만 npm@5부터는 기본값으로 설정되어 있으므로 생략가능
- node_modules폴더가 생성되고 의존하는  다른 패키지들이 저장됩니다
- 설치한 패키지들이 dependencies 속성에 기록됩니다.
-  node_modules는 언제든지 npm install로 설치할 수 있으므로 node_modules는 
   보관할 필요가 없다



참고로 이것은 package.json형식을 설치했떤 test 파일내에서 계속 해야한다.

```js
//package.json  형식

{
  "name": "npmtest",
  // 생략
  "license": "ISC",
  "dependencies": {
    "express": "^4.16.3"
 }
}

```

```js
$npm install [패키지 이름]
$ npm install express 
```

그러면 package-lock파일이 생긴다(보면 설치된 모듈들을 확인 가능)



##### 개발용 패키지를 설치

실제 배포 시에는 사용되지 않고, 개발 중에만 사용되는 패키지들

npm install --save-dev [패키지] [...]로 설치

ackage.json에 새로운 속성  

```js
$ npm install --save-dev nodemon

```



```js
//package.json  형식

{
  ...
  "devDependencies": {
    "nodemon": "^1.17.3"
 }
}

```

추가 확인해보자.

##### 전역 설치

- 패키지를 현재 폴더의 node_modules에 설치하는 것이 아니라 npm이 설치되어 있는 폴더(윈도의 경우 기본 경로는 C:\Users\사용자이름\AppData\Roamng\npm)에 설치합니다. 
- 전역 설치한 패키지는 콘솔의 커맨드로 사용할 수 있습니다.
- rimraf는 리눅스나 macOS의 rm -rf 명령어를 윈도에서도 사용할 수 있게 해주는 패키지입니다. rm -rf는 지정한 파일이나 폴더를 지우는 명령어)
- 전역 설치했으므로 rimraf 명령어를 콘솔에서 사용할 수 있습니다. 
- 전역 설치한 패키지는 package.json에 기록되지 않습니다.

```js
$ npm install --global rimraf 
$ rimraf node_modules

```

- rimraf 모듈을 package.json의 devDependencies 속성에 기록한 후, 앞에 npx 명령어를 붙여 실행하면 됩니다. 패키지를 전역 설치한 것과 같은 효과를 얻을 수 있습니다.



```js
$ npm install --save-dev rimraf

$ npx rimraf node_modules
```





- 모든 패키지가 npm에 등록되어 있는 것은 아닙니다. 일부 패키지는 오픈 소스가 아니거나 개발 중인 패키지라서 GitHub나 nexus 등의 저장소에 보관되어 있을 수도 있습니다. 

- npm install [저장소 주소] 명령어를 통해 설치

##### 패키지 배포

![1564546407720](C:\Users\student\Documents\GitHub\javaStudy\사진\npm)

- npm adduser :  npm 로그인을 위한 명령어( npm 공식 사이트에서 가입한 계정으로 로그인) 패키지를 배포할 때 로그인이 필요합니다. 
- npm whoami는 로그인한 사용자가 누구인지 알려줍니다. 로그인된 상태가 아니라면 에러가 발생
- §npm logout은 npm adduser로 로그인한 계정을 로그아웃할 때 사용합니다.
- npm version [버전] 명령어를 사용하면 package.json의 버전을 올려줍니다. 
- npm deprecate [패키지명][버전] [메시지] : 해당 패키지를 설치할 때 경고 메시지를 띄우게 하는 명령어
- npm publish : 자신이 만든 패키지를 배포할 때 사용
- npm unpublish는 배포한 패키지를 제거할 때 사용 (24시간 이내에 배포한 패키지만 제거할 수 있습니다.)
- npm 공식 문서(https://docs.npmjs.com/)의 CLI Commands에서 명령어 확인

- 패키지로 만들 코드는 package.json의 main 부분의 파일명과 일치해야 합니다. 
- npm에서 이 파일이 패키지의 진입점임을 알 수 있습니다.
- npm은 패키지의 이름이 겹치는 것을 허용하지 않습니다.
- 패키지 이름 사용 확인 - npm info [패키지명]

```js
//index.js

module.exports = () => {
  return'hello package';
};

```



```js
$ npm publish npmtest-1234
$ npm unpublish npmtest-1234 --force
$ npm info npmtest-1234

```



## http 모듈로 웹 서버 만들기

#### HTTP Module

- 클라이언트에서 서버로 요청(request)을 보내고, 서버에서는 요청의 내용을 읽고 처리한 뒤 클라이언트에게 응답(response)을 보냅니다.
- 서버에는 요청을 받는 부분과 응답을 보내는 부분이 있어야 합니다.
- 요청과 응답은 이벤트 방식으로 클라이언트로부터 요청이 왔을 때 어떤 작업을 수행할지 이벤트 리스너를 미리 등록해두어야 합니다. 

```jade
//createServer.js

const http = require('http');

http.createServer((req, res) => {
  // 여기에 어떻게 응답할지 적어줍니다.
});

```



##### HTML 파일 읽어 전송

```html
<!--demofile1.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Node.js 웹 서버</title>
</head>
<body>
    <h1>Node.js 웹 서버</h1>
    <p>만들 준비되셨나요?</p>
</body>
</html>

```

```js
//httpServer2.js

const http = require('http');
const fs = require('fs');

http.createServer((req, res) => {
  fs.readFile('./demofile1.html', (err, data) => {
    if (err) {
      throw err;
    }
    res.end(data);
  });
}).listen(8080, () => {
  console.log('8080번 포트에서 서버 대기 중입니다!');
});

```

cmd 창에서 실행후 브라우저에서 http://localhost:8080 를 입력시 자동으로 html 파일을 읽어 온다.

##### Http, File System Module (이미지와 음악 파일 제공)

```js
var fs = require('fs');
var http = require('http'); 
http.createServer(function (request, response) {
    // Image File Read
    fs.readFile('lion.jpeg', function(error, data) {
        response.writeHead(200, {'Content-Type': 'image/jpeg'});
        response.end(data);
    });    
}).listen(30000, function() {
    console.log('Server running at http://127.0.0.1:8081');
 });  
http.createServer(function (request, response) {
    // Music File Read
    fs.readFile('Sam Smith.mp3', function(error, data) {
        response.writeHead(200, {'Content-Type': 'audio/mp3'});
        response.end(data);
    });    
}).listen(30000, function() {
    console.log('Server running at http://127.0.0.1:8081');
});

```



##### 쿠키와 세션

- 쿠키는 키와 값이 들어 있는 작은 데이터 조각으로, 이름, 값, 파기 날짜와 경로 정보를 가지고 있습니다. 
- 쿠키는 서버와 클라이언트에서 모두 저장하고 사용할 수 있습니다. 
- 쿠키는 일정 기간 동안 데이터를 저장할 수 있으므로 일정 기간 동안 로그인을 유지하는 데 사용됩니다.
- response 객체를 사용하면 클라이언트에게 쿠키를 할당할 수 있습니다. 
- 쿠키를 할당할 때 응답 헤더의 Set-Cookie 속성을 사용합니다. Set-Cookie 속성에는 쿠키의 배열을 넣습니다.

``` js
//server3.js

const http = require('http');
const parseCookies = (cookie ='') =>
  cookie
    .split(';')
    .map(v => v.split('='))
    .map(([k, ...vs]) => [k, vs.join('=')])
    .reduce((acc, [k, v]) => {
      acc[k.trim()] = decodeURIComponent(v);
      return acc;
    }, {});
http.createServer((req, res) => {
  const cookies = parseCookies(req.headers.cookie);
  console.log(req.url, cookies);
  res.writeHead(200, {'Set-Cookie':'mycookie=test' });//set-Cookie는 브라우저한테 값을 쿠키로 저장하라는 의미
  res.end('Hello Cookie');
})
  .listen(8082, () => {
    console.log('8082번 포트에서 서버 대기 중입니다!');
  });

```

쿠키는 req.headers.cookie에 들어 있습니다

- 쿠키명=쿠키값: 기본적인 쿠키의 값입니다. mycookie=test 또는 name=zerocho 같이 설정합니다.
- Expires=날짜: 만료 기한입니다. 이 기한이 지나면 쿠키가 제거됩니다. 기본값은 클라이언트가 종료될 때까지입니다.
- Max-age=초: Expires와 비슷하지만 날짜 대신 초를 입력할 수 있습니다. 해당 초가 지나면 쿠기가 제거됩니다. Expires보다 우선합니다.
- Domain=도메인명: 쿠키가 전송될 도메인을 특정할 수 있습니다. 기본값은 현재 도메인입니다.
- Path=URL: 쿠키가 전송될 URL을 특정할 수 있습니다. 기본값은 ‘/’이고 이 경우 모든 URL에서 쿠키를 전송할 수 있습니다.
- Secure: HTTPS일 경우에만 쿠키가 전송됩니다.
- HttpOnly: 설정 시 자바스크립트에서 쿠키에 접근할 수 없습니다. 쿠키 조작을 방지하기 위해 설정하는 것이 좋습니다. 

