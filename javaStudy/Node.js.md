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



1. 들ㅇ온