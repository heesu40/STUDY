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



