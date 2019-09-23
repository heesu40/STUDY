R

- 데이터 분석을 위한 통계및 시각화를 지원하는 자유 소프트웨어 환경
- R은 컴퓨터 언어이자 다양한 패키지 집합
- **객체지향 프로그래밍 언어**
- data의 시각화를 위한 다양한 그래픽 도구 제공
- 모든 객체는 메모리로 로딩되어 고속으로 처리

R의 DataType -> numeric, character,logical, complex(복소수),



## 설치

[다운로드](http://cran.seoul.go.kr/) 후 설치하면 완료!

```r
#백터는 r에서 배열과 같은데 이를 생성하는 위해서 C를 사용
x <- c(1,2,3,4,5)
y <- c(10,20,30,40,50)
x+y
#결과
[1] 11 22 33 44 55
```

편하게 사용하기 위해 [r studio다운로드](https://www.rstudio.com/products/rstudio/download/#download)한다. 실행한후

```r
a <- 10
b <- 3
print(a*b)
#ctrl +enter해서 실행!
```

- 인터페이스가 마음에 안든다면 Tools -> global options--> pane layout 에서 바꾸고
- global Code에서 saving에서 utf-8로 저장
- General에서 Default directory 또한 지정해 놓자.

### 패키지

##### 패키지 개수 확인

```r
#패키지 개수 확인
dim(available.packages())
available.packages()
```

##### 설치 정보 확인

- R session은 사용자가 R 프로그램을 시작 한 후 R 콘솔 시작~ 종료까지의 수행된 정보

```r
sessioninfo()
#os, 설치 정보 , 다국어 정보, 등등 알수 있다.
R version 3.6.1 (2019-07-05)
Platform: x86_64-w64-mingw32/x64 (64-bit)
Running under: Windows 7 x64 (build 7601) Service Pack 1

# 등등
#패키지 다운되는 경로 확인
> .libPaths()
[1] "C:/Program Files/R/R-3.6.1/library"

```

##### 설치된 R패키지 목록 확인

- 설치된 R패키지 목록 확인

```r
> installed.packages()
             Package       
askpass      "askpass"     
assertthat   "assertthat"  
backports    "backports"   
base         "base"        
BH           "BH"          

#등등 무진장 많다.
```

##### 패키지 설치

```ㄱ
install.packages("stringr")
//update.packages("stringr")
remove.packages("stringr")
```

##### 설치된 패키지 사용하기 위해서 메모리에 로드

```r
library(stringr) #또는
require(stringr)

```

##### 메모리에 로드된 패키지 검색

```r
search()

```



### 처음

##### 기본 데이터 셋 보기

```r
data()
```

##### 빈도수 히스토그램

```r
hist(Nile)
```

##### 밀도 기준 히스토그램

```r
hist(Nile,freq=F)
```



##### 분포 곡선 그리기

```r
lines(density(Nile))
```

##### plots영역에 표시할 그래프 개수 설정

```r
par(mfrow=c(1,1))
```

##### 파일 출력 경로

```r
pdf("c:workspaceR/sample.pdf")
```

##### 정규분포 따르는 난수 20개 생성해서 히스토그램 생성

```r
hist(rnorm(20))# 정규분포를 따르는 난수 20개 새엇ㅇ해서 히스토그램 생성
```



##### 출력 파일 닫기

```r
dev.off()
```



## 계산

##### 변수 선언

1. 첫문자는 영문자로 시작과 첫글자가 .로 시작하면 뒤에 숫자 못온다.
2. 두번쨰 문자부터 숫자, _, . 사용가능
3. 대소문자 구분
4. 예약어 사용 불가
5. 카멜표기법
6. 변수에 저장된 값은 불변

```r
x<-3
tracemem(x)
x<- 'a'
tracemem(x) 

> x<-3
> tracemem(x)
[1] "<000000001594FAB8>"
> x<- 'a'
> tracemem(X) 
Error: object 'X' not found
> tracemem(x) 
[1] "<0000000015913450>"

> mean(x<-c(1,2,3))
[1] 2
> x
[1] 1 2 3
> mean(x=c(1,2,3,))
Error in c(1, 2, 3, ) : argument 4 is empty
> x
[1] 1 2 3

```

- **R은 변수를 선언할 때 자료형(type)을 선언하지 않는다.**

  

###### 데이터 타입

Scalar 변수-하나의 값을 저장하는 변수(scala 변수) - numeric,character,logical

```r
age <- 30
#age변수는 하나의 값을 저장한고 있는 벡터 타입
#하나 이상의 자료를 저장할 수 있는 1차원의 선형 자료 구조
class (age)
[1] "numeric"

age<-"29"
class(age)
[1] "character"

age <-  TURE #상수 객체(true,false)
class(Age)
[1] "logical"

age <- F # false
class(age)
[1] "logical"

> age <- NA #결측치(Not Available)
> class(age+10)
[1] "numeric"
> age+10
[1] NA

> age <- null
Error: object 'null' not found
> class(age+10)
[1] "numeric"
```

##### ##### ?

```r
> sum(10,20,30)
[1] 60
> sum(10,20,30,NA)
[1] NA
> sum(10,20,30,NA,na.rm=T)
[1] 60
```

##### R  Session 에서 생성한 변수 목록 확인

```r
> ls()
 [1] "a"          "age"        "b"          "dongdaemun"
 [5] "gangnam"    "p"          "police"     "seoul"     
 [9] "total"      "x"  
```

##### 자료형 확인

```r
is.numeric(변수)
is.logical(변수)
is.character(변수)
is.na(변수)
is.list(객체)
is.data.frame(객체)
is.array(객체)
is.matrix(객체)
           
```

##### 자료형 형변환

```r
as.numeric(변수)
as.logical(변수)
as.character(변수)
as.na(변수)
as.list(객체)
as.data.frame(객체)
as.array(객체)
as.matrix(객체)
as.integer(변수)
as.double(변수)
as.complex(변수)#복소수 형변환
as.factor(객체) #범주 자료형
as.Date(객체)

```

##### 형변환 확인

```r
> x <- c("1","2","3")
> result<-x*3
Error in x * 3 : non-numeric argument to binary operator
> print(result)
[1]  3 12 27
> result<-as.numeric(x)*3
> print(result)
[1] 3 6 9
> result<-as.integer(x)*#
+   print(result)
[1] 3 6 9
#복소수
> z<-5.3-3i
> class(z)
[1] "complex"
> Re(z)
[1] 5.3
> Im(z)
[1] -3
> is.complex(z)
[1] TRUE
> as.complex(5.3)
[1] 5.3+0i
```

##### class(변수)는 자료구조의 Type 반환

```r
> age <-29.5
> mode(age)
[1] "numeric"
> age<-TRUE
> age<-F
> mode(age)
[1] "logical"


> age <-29.5
> mode(age)
[1] "numeric"
> age<-TRUE
> mode(age)
[1] "logical"
> age<-F
> mode(age)
[1] "logical"
```



##### mode(변수)는 자료의 Type 반환

```r

```



##### 작업디렉토리 설정

```r
> getwd()
[1] "C:/Users/student/Documents/map"
> setwd("c:/workspace")
> getwd()
[1] "c:/workspace"
```

### 연산자

- print() 함수는 1번에 1가지만 출력, cat() 함수는 숫자와 문자 여러 개를 한번에 출력
- 여러 개의 명령을 연속적으로 실행하고 싶을 경우에 세미콜론(;)을 사용

```r
> print(3,4)
[1] 3
> cat(1,'a',2,'b')
1 a 2 b> 1+2;3*2;4/2
[1] 3
[1] 6
[1] 2
```

##### 산술연산자

- / 나누기 (실수 가능)
-  %/% 정수 나누기
-  %% 나머지 구하기
-  ^, ** 승수 구하기

##### 데이터 타입 확인시 class 함수 사용

```r
> class('1')
[1] "character"
> class(1)
[1] "numeric"
```

##### Null

- is.null은 변수에 null이 있는지 확인

```r
> x<-null
Error: object 'null' not found
> is.null(x)
[1] FALSE
> is.null(1)
[1] FALSE
> is.null(NA)
[1] FALSE
> is.na(NULL)
logical(0)


is_even <- NULL
if (a 가 짝수면) {
is_even <- TRUE
} else {
is_even <- FALSE
}
```

##### 진리값(논리값)

```r
> TRUE & TRUE
[1] TRUE
>  TRUE & FALSE
[1] FALSE
>  TRUE | TRUE
[1] TRUE
>  TRUE | FALSE
[1] TRUE
>  !TRUE
[1] FALSE
>  !FALSE
[1] TRUE
>  T <- FALSE
>  TRUE <- FALSE
Error in TRUE <- FALSE : invalid (do_set) left-hand side to assignment
>  c(TRUE, TRUE) & c(TRUE, FALSE)
[1]  TRUE FALSE
>  c(TRUE, TRUE) && c(TRUE, FALSE)
[1] TRUE #앞에것만 비교하기때문에 TRUE)

> x<-TRUE; y<-FALSE
> xor(x,y)
[1] TRUE
```

##### 날짜와 시간

- %d 일자를 숫자로 인식
-  %m 월 을 숫자로 인식
-  %b 월을 영어 약어로 인식
-  %B 월을 전체 이릉으로 인식
-  %y 년도를 숫자 두 자리로 인식
-  %Y 년도를 숫자 네 자리로 인식

```r
> Sys.Date() # 날짜만 보여주는 함수
[1] "2019-09-05"
>  Sys.time() # 날짜와 시간을 보여주는 함수
[1] "2019-09-05 16:36:13 KST"
>  date() # 미국식 날짜와 시간을 출력하는 함수
[1] "Thu Sep 05 16:36:13 2019"
>  as.Date("2017-12-01") # 문자형태의 날짜를 날짜타입으로 변환해주는 함수
[1] "2017-12-01"
>  as.Date("2017/07/04")
[1] "2017-07-04"
>  as.Date("04-07-2017") #오류
[1] "0004-07-20"
>  as.Date("01-12-2017" , format='%d-%m-%Y')
[1] "2017-12-01"
>  as.Date(10, origin="2017-12-01") #주어진 날짜 기준으로 10일후의 날짜
[1] "2017-12-11"
>  as.Date(-10, origin="2017-12-01") #주어진 날짜 기준으로 10일 이전 날짜
[1] "2017-11-21"
```

##### 날짜 산술 연산

```r
>  as.Date("2017-07-04 20:00:00")-as.Date("2017-07-04 18:30")
Time difference of 0 days
> as.POSIXct("2017-07-04 20:00:00")-as.POSIXct("2017-07-04 18:30")
Time difference of 1.5 hours

```

##### lubridate 패키지로 날짜 시간 제어

```r
> install.packages("lubridate")
Error in install.packages : Updating loaded packages
> library(lubridate)
> date<-now() #현재 날짜와 시간 넣기
> date
[1] "2019-09-05 16:41:19 KST"
> year(date) #년도만 출력
[1] 2019
> month(date,label=T) #월을 영문으로 출력
[1] 9
> month(date,label=F) #월을 숫자로 출력
[1] 9
> day(date)
[1] 5
> library(lubridate)
> date<-now() #현재 날짜와 시간 넣기


wday(date, label=T) # 요일을 영문으로 출력
wday(date, label=F) # 요일을 가중치 숫자로 출력 , 일요일 1 시작
date<-date-days(2) #2일전 날짜 출력
date
month(date)<-2 #2개월 더한 날짜 출력
date
date+years(1) #1년 추가
date+months(1) #1개월 추가
date+hours(1) #1시간 추가
date+minutes(1) #1분 추가
date+seconds(1) #1초 추가
date<-hm("22:30") ; date #시간 분 지정
date<-hms("22:30:15") ; date #시간 분 초 지정
```

##### 변수 확인 & 삭제

```r
> objects( ) # 생성한 모든 변수 확인
> rm(list=ls()) # 모든 변수들을 삭제
> rm(var3) # 변수 삭제
```



##### 현재 로케일 정보 전체 확인

```r
>   Sys.setlocale(category="LC_ALL",locale="")
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"
> Sys.getlocale()
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"
> Sys.setlocale(category = "LC_ALL",locale="English_US")
[1] "LC_COLLATE=English_United States.1252;LC_CTYPE=English_United States.1252;LC_MONETARY=English_United States.1252;LC_NUMERIC=C;LC_TIME=English_United States.1252"
> Sys.getlocale()
[1] "LC_COLLATE=English_United States.1252;LC_CTYPE=English_United States.1252;LC_MONETARY=English_United States.1252;LC_NUMERIC=C;LC_TIME=English_United States.1252"
> Sys.setlocale(category = "LC_ALL",locale = "Japanese_Japan")
[1] "LC_COLLATE=Japanese_Japan.932;LC_CTYPE=Japanese_Japan.932;LC_MONETARY=Japanese_Japan.932;LC_NUMERIC=C;LC_TIME=Japanese_Japan.932"
> Sys.getlocale()
[1] "LC_COLLATE=Japanese_Japan.932;LC_CTYPE=Japanese_Japan.932;LC_MONETARY=Japanese_Japan.932;LC_NUMERIC=C;LC_TIME=Japanese_Japan.932"
```



##### R에서 제공하는 기본 함수 사용 예제 보기

```r
> example(seq)

seq> seq(0, 1, length.out = 11)
 [1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

seq> seq(stats::rnorm(20)) # effectively 'along'
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

seq> seq(1, 9, by = 2)     # matches 'end'
[1] 1 3 5 7 9

seq> seq(1, 9, by = pi)    # stays below 'end'
[1] 1.000000 4.141593 7.283185

seq> seq(1, 6, by = 3)
[1] 1 4

seq> seq(1.575, 5.125, by = 0.05)
 [1] 1.575 1.625 1.675 1.725 1.775 1.825 1.875 1.925 1.975 2.025
[11] 2.075 2.125 2.175 2.225 2.275 2.325 2.375 2.425 2.475 2.525
[21] 2.575 2.625 2.675 2.725 2.775 2.825 2.875 2.925 2.975 3.025
[31] 3.075 3.125 3.175 3.225 3.275 3.325 3.375 3.425 3.475 3.525
[41] 3.575 3.625 3.675 3.725 3.775 3.825 3.875 3.925 3.975 4.025
[51] 4.075 4.125 4.175 4.225 4.275 4.325 4.375 4.425 4.475 4.525
[61] 4.575 4.625 4.675 4.725 4.775 4.825 4.875 4.925 4.975 5.025
[71] 5.075 5.125

seq> seq(17) # same as 1:17, or even better seq_len(17)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
```

##### R에서 제공하는 함수의 파라미터 형식 보기

```r
> args(max)
function (..., na.rm = FALSE) 
NULL
```

##### help(mean)

```r
help(mean)
?sum 
??mean #각각의 설명을 help탭에서 확인 가능
```



##### Factor 형

- 여러 번 중복으로 나오는 데이터들을 각 값으로 모아서 대표 값을 출력해 주는 형태
-  stringsAsFactors=FALSE 옵션은 대표값으로 정리하지 않고 중복되는 상태 그대로 사용하게 해 줍
  니다.
-  범주형Categorical 데이터(자료)를 표현하기 위한 데이터 타입
-  범주형 데이터 - 데이터가 사전에 정해진 특정 유형으로만 분류되는 경우
-  범주형 데이터는 또 다시 명목형Nominal과 순서형Ordinal으로 구분
-  ***명목형 데이터***는 값들 간에 **크기 비교가 불가능**한 경우
- * **순서형 데이터***는 대, 중, 소와 같이 값에 **순서**를 둘 수 있는 경우

1. `nlevels(x #팩터 값)` 반환 값은 팩터 값의 레벨 개수
2. `ordered(x # 팩터로 표현하고자 하는 값(주로 문자열 벡터로 지정))` 순서형 팩터 생성
3. `levels(x # 팩터 값)`반환 값은 팩터에서 레벨의 목록
4. `is.ordered(x #R 객체)` 반환 값은 x가 순서형 팩터면 TURE,아니면 FALSE

```r
> gender <- c("man","woman","woman","man","man")
> plot(gender)#차트는 수치 데이터만 가능하므로 오류발생 
Error in plot.window(...) : need finite 'ylim' values
In addition: Warning messages:
1: In xy.coords(x, y, xlabel, ylabel, log) : NAs introduced by coercion
2: In min(x) : no non-missing arguments to min; returning Inf
3: In max(x) : no non-missing arguments to max; returning -Inf

> class(gender)
[1] "character"
> mode(gender)
[1] "character"
> ngender<-as.factor(gender)
> class(ngender)
[1] "factor"
> mode(ngender)
[1] "numeric"
> table(gender) #빈도수 반환
gender
  man woman 
    3     2 
plot(ngender)
#아래 그림 확인
> is.factor(ngender)
[1] TRUE
> ngender # Levels속성에서 범주를 확인(알파벳 순서?인지 보자)
[1] man   woman woman man   man  
Levels: man woman
```

![1567671955486](R.assets/1567671955486.png)



```r
> args(factor) #factor()함수의 매개 변수 확인
function (x = character(), levels, labels = levels, exclude = NA, 
    ordered = is.ordered(x), nmax = NA) 
NULL
> ogender<-factor(gender,levels=c("woman","man"),ordered=T)
> ogender #범주의 순서 확인
[1] man   woman woman man   man  
Levels: woman < man
> par(mfrow=c(1,2))
> plot(ngender)
> plot(ogender)
```

![1567672327323](R.assets/1567672327323.png)

## Vector

- R에서 가장 기본이 되는 자료 구조로, 1차원, 선형 구조로 배열과 비슷하다.
- 요소의 접근 변수[index첨자]로 접근, 프로그램에서는 첨자가 0부터 시작하는데, 여기서는 첨자 index가 1부터 시작한다. 
- 동일한 데이터타입만 저장 가능하다.
- 벡터 생성 함수 : c(),seq(),rep()
- 벡터 자료 처리 함수: union(),setdiff(),intersect()......

```r
> c(1:20)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
> 1:20
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
> c(1,1,2,3,3,3,4,5,5,5,5)
 [1] 1 1 2 3 3 3 4 5 5 5 5
> seq(1, 20)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
> seq(1, 20, 2)  #순차적으로 값을 증감시켜서 벡터 자료 구조 생성
 [1]  1  3  5  7  9 11 13 15 17 19
> rep(1:3,3) #반복
[1] 1 2 3 1 2 3 1 2 3
> rep(1:3,each=3)#각각 반복
[1] 1 1 1 2 2 2 3 3 3

```

```r
> a<-c(1:5)
> b<-a+1
> c<-a*2
> d<-rep(1:3,3)
> union(a,d)
[1] 1 2 3 4 5
> setdiff(a,d)
[1] 4 5
> intersect(a,d)
[1] 1 2 3
> f <- c(33, -5, "4", 5:9 ) #벡터 중간에 문자가 있어도 오류가 없다
> class(f)# 형변환 확인해보자
[1] "character"
> mode(f)#자체적으로 형변환 발생
[1] "character"
```



```r
> a<-c(1:20)
> a[3:10]   #벡터의 요소에 접근
[1]  3  4  5  6  7  8  9 10
> a[c(3, 10)]  #벡터의 요소에 접근
[1]  3 10
> a[-c(2:18)]# 제외하고! 현재 a 는 (1:20)까지 이다.
[1]  1 19 20
> a[-c(2:18)]
[1]  1 19 20
> a[-c(1:20)]
integer(0)
> a[-c(5:20)]
[1] 1 2 3 4
> a[-c(6:20)]
[1] 1 2 3 4 5
> a[-c(2:20)]
[1] 1
> a[-c(2:18)]
[1]  1 19 20
```



##### 복습 (벡터의 다양한 처리)

```r
[1] "Sum"
> print(t[7])
[1] NA
> u<-t(c[2,3,6])
Error in c[2, 3, 6] : object of type 'builtin' is not subsettable
> u<-t[c(2,3,6)]
> print(u)
[1] "Mon" "Wed" "Sat"
> v<-t[c(TRUE,FALSE,TRUE,FALSE,FALSE,TRUE)]
> print(v)
[1] "Sum" "Wed" "Sat"
> v<t[c(-2,-5)]
[1] FALSE FALSE  TRUE FALSE
Warning message:
In v < t[c(-2, -5)] :
  longer object length is not a multiple of shorter object length
> v<-t[c(-2,-5)]

> print(v)
[1] "Sum"   "Wed"   "Thurs" "Sat"  
> y<-t[c(0,0,0,0,0,1)]
> print(y)
[1] "Sum"
> y<-t[c(0,0,1,0,0,1)]
> print(y)
[1] "Sum" "Sum"
```

##### 덧셈길이 다를때의 결과는?

```r
> v1<-c(5,7,5,1,20)
> v2<-c(3,4,6)
> v3<-c(1,2,3,4,5,6)
> v4<-c(1,2,3)
> 
> print(v1+v2)
[1]  8 11 11  4 24
Warning message:
In v1 + v2 :
  longer object length is not a multiple of shorter object length
> print(v3+v4)
[1] 2 4 6 5 7 9
```

#####  배열에서 일부 값만 출력

```r
> nums<-c(3/2,3%/%2,5%%3,2^10,2**10)
> print(nums)
[1]    1.5    1.0    2.0 1024.0 1024.0
> print((0%in%nums))
[1] FALSE
> 
> print((1024%in%nums))
[1] TRUE
> 
> print(nums[nums>10])
[1] 1024 1024
> 
> print(nums[nums%%2==0])
[1]    2 1024 1024
```

##### 배열 각각의 값에 이름을 추가, sort

```r
> loc<-c("02","031","032","052")
> str(loc)
 chr [1:4] "02" "031" "032" "052"
> names(loc)<-c("서울","경기","광주","부산")
> str(loc)
 Named chr [1:4] "02" "031" "032" "052"
 - attr(*, "names")= chr [1:4] "서울" "경기" "광주" "부산"
> 
> v<-c(3,8,4,5,0,11,-9,304)
> sort.result<-sort(v)
> print(sort.result)
[1]  -9   0   3   4   5   8  11 304
> 
> revsort.result<-sort(v,decreasing=TRUE)
> print(revsort.result)
[1] 304  11   8   5   4   3   0  -9
> v<-c("RED","BLUE","YELLOW","VIOLET")
> sort.result<-sort(v)
> print(sort.result)
[1] "BLUE"   "RED"    "VIOLET" "YELLOW"
```

##### 집합연산함수(교집합,합집합,차집합,부분집합..)

```r
##집합연산함수(교집합, 합집합, 차집합, 부분집합, ..)
#identical( 객체1, 객체2) 두객체의 데이터 갯수, 순서도 일치 하는지  반환값 FALSE,TRUE
#union( 객체1, 객체2) 중복을 뺀 모든 값
#intersect(객체1, 객체2) 교집합
#setdiff(객체1, 객체2) 객체 1와 2를 비교해 객체 1에만 있는 값을 반환
#setequal(객체1, 객체2) 값이 일치한 것을 찾는다 반환값은 False, TRUE

> vec1 <- c(1, 2, 3, 4, 5)
> vec2 <- c(10, 9, 8, 4, 5)
> vec3 <- c(1, 2, 3, 4, 5)
> print(identical(vec1,vec3))
[1] TRUE
> print(identical(vec1,vec2))
[1] FALSE
> vec4 <- c(5,3,4,1,2)
> print(setequal(vec1,vec4))  #순서는 일치하지 않아도 요소들만 일치하면 true리턴
[1] TRUE
> print(setequal(vec1,vec3))
[1] TRUE
> print(union(vec1,vec2))
[1]  1  2  3  4  5 10  9  8
> print(intersect(vec1,vec2))
[1] 4 5
> print(setdiff(vec1,vec2))
[1] 1 2 3
> print(setdiff(vec3,vec4))
numeric(0)
> print(intersect(vec3,vec4))
[1] 1 2 3 4 5
```

##### Matrix(벡터를 여러개 합친 것!  2차원)

1. 동일한 데이터 유형만 저장
2. **rbind()**로 행을 추가 가능
3. **cbind()**로 컬럼 추가 가능
4. 컬럼 이름을 지정, 조회하려면 **colnames()**사용
5. 행이름 지정, 조회하려면 **rownames()**사용

```r
matrix(
data,
nrow=1,
ncol=1, #nrow와 ncol은 default가 1
byrow=FALSE, #default가 FALSE임으로 열기준으로 데이터 저장,TRUE는 행기준
dimnames=NULL #행렬의 각 차원에 부여할 이름
)
#반환값을 행렬!
```

##### 생성실습

```r
> M <- matrix(c(3:14)) # 열 기준 2차원 데이터 구조
> print(M)
      [,1]
 [1,]    3
 [2,]    4
 [3,]    5
 [4,]    6
 [5,]    7
 [6,]    8
 [7,]    9
 [8,]   10
 [9,]   11
[10,]   12
[11,]   13
[12,]   14
> str(M)
 int [1:12, 1] 3 4 5 6 7 8 9 10 11 12 ...
> 
> M1 <- matrix(c(3:14), nrow=3) # 열 기준 2차원 데이터 구조
> print(M1)
     [,1] [,2] [,3] [,4]
[1,]    3    6    9   12
[2,]    4    7   10   13
[3,]    5    8   11   14
> str(M1)
 int [1:3, 1:4] 3 4 5 6 7 8 9 10 11 12 ...
> 
> M2 <- matrix(c(3:14), nrow = 4, byrow = TRUE) #행기준 2차원 데이터 구조
> print(M2)
     [,1] [,2] [,3]
[1,]    3    4    5
[2,]    6    7    8
[3,]    9   10   11
[4,]   12   13   14
> str(M2)
 int [1:4, 1:3] 3 6 9 12 4 7 10 13 5 8 ...
> 
> x1 <- c(5, 40, 50:52)
> x2 <-c(30, 5, 6:8)
> M3 <- rbind(x1, x2)
> print(M3)
   [,1] [,2] [,3] [,4] [,5]
x1    5   40   50   51   52
x2   30    5    6    7    8
> str(M3)
 num [1:2, 1:5] 5 30 40 5 50 6 51 7 52 8
 - attr(*, "dimnames")=List of 2
  ..$ : chr [1:2] "x1" "x2"
  ..$ : NULL
> 
> M4 <- cbind(x1, x2)
> print(M4)
     x1 x2
[1,]  5 30
[2,] 40  5
[3,] 50  6
[4,] 51  7
[5,] 52  8
> str(M4)
 num [1:5, 1:2] 5 40 50 51 52 30 5 6 7 8
 - attr(*, "dimnames")=List of 2
  ..$ : NULL
  ..$ : chr [1:2] "x1" "x2"
> 
> M <- matrix(10:19, 2)  
> print(M)
     [,1] [,2] [,3] [,4] [,5]
[1,]   10   12   14   16   18
[2,]   11   13   15   17   19
> str(M)
 int [1:2, 1:5] 10 11 12 13 14 15 16 17 18 19
#배열 개수가 맞지 않는 경우 적은 쪽이 반복되면서 채워진다.
> M<-matrix(10:20,2)
Warning message:
In matrix(10:20, 2) :
  data length [11] is not a sub-multiple or multiple of the number of rows [2]
> print(M)
     [,1] [,2] [,3] [,4] [,5] [,6]
[1,]   10   12   14   16   18   20
[2,]   11   13   15   17   19   10
```

##### 행렬 객체 생성시 데이터의 길이는 행과 열의 행렬 수에 일치 되어야 한다.

```r
> rownames <- c("row1", "row2", "row3", "row4")
> colnames <- c("col1", "col2", "col3")
> 
> M5 <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))
> print(M5)
     col1 col2 col3
row1    3    4    5
row2    6    7    8
row3    9   10   11
row4   12   13   14
> 
> 
> P1<-cbind(M5,c(13,14,15,16))
> print(P1)
     col1 col2 col3   
row1    3    4    5 13
row2    6    7    8 14
row3    9   10   11 15
row4   12   13   14 16
> P2<-rbind(M5,c(13,14,15))
> print(P2)
     col1 col2 col3
row1    3    4    5
row2    6    7    8
row3    9   10   11
row4   12   13   14
       13   14   15
> print(M5+P1)
Error in M5 + P1 : non-conformable arrays
> print(M5+P2)
Error in M5 + P2 : non-conformable arrays

```

##### Matrix요소에 접근-변수[첨자,첨자]

```r
> print(M5[1,3])
[1] 5
> print(M5[2,]) #열만 나열
col1 col2 col3 
   6    7    8 
> print(M5[,3]) #행만 나열
row1 row2 row3 row4 
   5    8   11   14 
> print(M5["row1",])  #1행 전체 요소에 접근
col1 col2 col3 
   3    4    5 
> print(M5[,"col3"])   #3열 전체 요소에 접근
row1 row2 row3 row4 
   5    8   11   14 

```

##### Matrix 연산&함수적 언어의 특징

```r
> matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
> matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)
> result <- matrix1 + matrix2
> cat("Result of addition","\n")
Result of addition 
> print(result)
     [,1] [,2] [,3]
[1,]    8   -1    5
[2,]   11   13   10
> result <- matrix1 + 10
> print(result)
     [,1] [,2] [,3]
[1,]   13    9   12
[2,]   19   14   16
> print(length(result))  #전체 원소 개수 반환
[1] 6
> print(nrow(result))  #행 수 반환
[1] 2
> print(ncol(result))  #열 수 반환
[1] 3
#apply apply(X, MARGIN, FUN, ...) (행렬객체, margin(1:행,2:열),function...)
> f<-function(x){x*c(1,2,3)} #사용자정의 함수
> result<-apply(matrix1,1,f)
> print(result)
     [,1] [,2]
[1,]    3    9
[2,]   -2    8
[3,]    6   18
> result<-apply(matrix(1:9,ncol=3),2,f)
> print(result)
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    4   10   16
[3,]    9   18   27
> print(dim(M5))   #matrix의 차원을 리턴
[1] 4 3
> 
> 
> m1 <- matrix(c(1:9), ncol=3, byrow=TRUE)
> print(m1)
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
> print(t(m1))  #전치행렬 리턴 함수
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
> 
> m2 <- matrix(rep(1:3, times=3), nrow=3)
> print(m2)
     [,1] [,2] [,3]
[1,]    1    1    1
[2,]    2    2    2
[3,]    3    3    3
> print(m1 %*% m2)   ##행렬의 곱 
     [,1] [,2] [,3]
[1,]   14   14   14
[2,]   32   32   32
[3,]   50   50   50


#문> P2 matrix객체에서 2행과 4행을 제외하고 출력
 
> print(P2[-c(2,4),])
     col1 col2 col3
row1    3    4    5
row3    9   10   11
       13   14   15

#문> P2 matrix객체에서 1열과 3열을 제외하고 출력
> print(P2[,-c(1,3)])
row1 row2 row3 row4      
   4    7   10   13   14 

> m3<-m1[, -c(1,3)] # matrix에서 하나의 열만 남겨놓고 모든 열 제거
> print(m3)
[1] 2 5 8
> str(m3)
 int [1:3] 2 5 8
> m3<-m1[, -c(1,3),drop=FALSE] #벡터로 변환되지 않도록 matrix의 drop요소 false로 지정
> print(m3)
     [,1]
[1,]    2
[2,]    5
[3,]    8
> str(m3)
 int [1:3, 1] 2 5 8
> rownames(M5)
[1] "row1" "row2" "row3" "row4"
> colnames(M5)
[1] "col1" "col2" "col3"


```

##### 역행렬

- 행렬과 역행렬을 곱하면 대각선이 1이고 나머지가 0인 행렬이 된다.

```r
#역행렬
> m4<-matrix(c(1,2,3,4,5,4,3,2,1),ncol=3)
> result<-solve(m4)
> print(m4 %*% result)
              [,1]          [,2]          [,3]
[1,]  1.000000e+00 -4.440892e-16  0.000000e+00
[2,]  2.220446e-16  1.000000e+00 -1.110223e-16
[3,] -1.110223e-16 -4.440892e-16  1.000000e+00
```

### Array 

- 동일한 자료형을 갖는 다차원 배열 구조 (3차원!)

- array()-행, 열, 면의 3차원 배열 형태의 객체를 생성, 첨자로 접근, 다른 자료 구조에 비해 상대적으로 활용도가 낮다.

```r
> vector1<-c(5,9,3)
> vector2<-c(10,11,12,13,14,15)
> result<-array(c(vector1, vector2),dim=c(3,3,2))
> print(result)
, , 1

     [,1] [,2] [,3]
[1,]    5   10   13
[2,]    9   11   14
[3,]    3   12   15

, , 2

     [,1] [,2] [,3]
[1,]    5   10   13
[2,]    9   11   14
[3,]    3   12   15

> str(result)
 num [1:3, 1:3, 1:2] 5 9 3 10 11 12 13 14 15 5 ...



```

##### 3차원 행렬에 이름 붙여주기(각행 각 열, 각 층 마다)

```r
#행열에 이름 붙여주기
> column.names<-c("COL1","COL2","COL3")
> row.names<-c("ROW1","ROW2","ROW3")
> matrix.names<-c("Matrix1","Matrix2")
> result<-array(c(vector1,vector2),dim=c(3,3,2),dimnames = list(column.names,row.names,matrix.names))
> print(result)
, , Matrix1

     ROW1 ROW2 ROW3
COL1    5   10   13
COL2    9   11   14
COL3    3   12   15

, , Matrix2

     ROW1 ROW2 ROW3
COL1    5   10   13
COL2    9   11   14
COL3    3   12   15
```



##### Array요소 접근

```r
> print(result[3, ,2])
ROW1 ROW2 ROW3 
   3   12   15 
> print(result[1,3,1])
[1] 13
> print(result[ , ,2])
     ROW1 ROW2 ROW3
COL1    5   10   13
COL2    9   11   14
COL3    3   12   15
> vector3<-c(9,1,0)
> vector4<-c(6,0,11,3,14,1,2,6,9)
> array2<-array(c(vector3,vector4),dim=c(3,3,2))
> print(array2)
, , 1

     [,1] [,2] [,3]
[1,]    9    6    3
[2,]    1    0   14
[3,]    0   11    1

, , 2

     [,1] [,2] [,3]
[1,]    2    9    6
[2,]    6    1    0
[3,]    9    0   11

> matrix1<-result[,,2]
> matrix2<-array2[,,2]
> print(matrix1+matrix2)
     ROW1 ROW2 ROW3
COL1    7   19   19
COL2   15   12   14
COL3   12   12   26
#apply(data 객체, margin,function)
> rs1<-apply(array2,c(1),sum) #c(1)각 행을 margin 1은 행이므로 이를 배열 로 하여 더했다는 뜻 
> print(rs1)
[1] 35 22 32
> rs1<-apply(array2,c(2),sum)#c(2)는 margin 2가 열이므로 이를 배열로 더했다는 뜻
> print(rs1)
[1] 27 27 35

```

### List

1. 서로 다른 자료구조(벡터, 행렬, 리스트, 데이터 프레임 등)을 객체로 구성 하며 key와 value의 한쌍으로 저장
2. c 언어의 구조체,python의 dict 자료구조, java의 map컬렉션과 비슷하며 value에 저장되는 자료 구조는 벡터, 행렬, 리스트, 데이터프레임 등 대부분의 R객체 저장 가능
3. 함수 내에서 여러 값을 하나의 키로 묶어서 반환시 유용
4. `list(key1=value1,key2=value2....)

```r
#키가 생략되고 값만 저장된 상태
#한개의 값이 vaetor형식으로 저장
> list1<-list("lee","이순신",95)
> print(list1)
[[1]]
[1] "lee"

[[2]]
[1] "이순신"

[[3]]
[1] 95

> str(list1)
List of 3
 $ : chr "lee"
 $ : chr "이순신"
 $ : num 95
> #키가 생략되고 값만 저장된 상태
> #한개의 값이 vaetor형식으로 저장장
> emp1<-list(name='kim',address='seoul',age=30,hiredate=as.Date)
> print(emp1)
$name
[1] "kim"

$address
[1] "seoul"

$age
[1] 30

$hiredate
function (x, ...) 
UseMethod("as.Date")
<bytecode: 0x000000000edad868>
<environment: namespace:base>

> str(emp1)
List of 4
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ age     : num 30
 $ hiredate:function (x, ...)  
> 
> list_data<-list(k1="Red",k2="Green",k3=c(21,32,11),k4=TRUE,k5=51.23,k6=119.1)
> print(list_data)
$k1
[1] "Red"

$k2
[1] "Green"

$k3
[1] 21 32 11

$k4
[1] TRUE

$k5
[1] 51.23

$k6
[1] 119.1

> str(list_data)
List of 6
 $ k1: chr "Red"
 $ k2: chr "Green"
 $ k3: num [1:3] 21 32 11
 $ k4: logi TRUE
 $ k5: num 51.2
 $ k6: num 119
> print(emp1[1:2])
$name
[1] "kim"

$address
[1] "seoul"

> print(emp1$age)
[1] 30

#문)list_data리스트의 요소중에서 k3에 저장된 세번째 요소만 출력!
> print(list_data$k3)
[1] 21 32 11 #k3의 요소들을 보여주는 것
> print(list_data$k3[3]) #k3의 3번째 요소만!
[1] 11
```

##### 리스트 내에 값의 타입을 리스트 저장 가능

```r
> nums<-c(1,2,3,4,5)
> tracemem(nums)
[1] "<000000000FD17A60>"
> str(nums)
 num [1:5] 1 2 3 4 5
> nums[6]<-10
tracemem[0x000000000fd17a60 -> 0x00000000104b30b0]: 
> str(nums)
 num [1:6] 1 2 3 4 5 10
> tracemem(nums)
[1] "<00000000104B3040>"
> newValue<-append(nums,99,after=3)
> print(nums)
[1]  1  2  3  4  5 10
> print(newValue)
[1]  1  2  3 99  4  5 10
> emp1$age
[1] 30
> str(emp1)
List of 4
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ age     : num 30
 $ hiredate:function (x, ...)  
> emp1$age<-Null
Error: object 'Null' not found
> emp1$age<-NULL
> str(emp1)
List of 3
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ hiredate:function (x, ...) 


> lst2<-list(cost=list(val=c(100,150,200)),price=list(val=c(200,250,300)))
> str(lst2)
List of 2
 $ cost :List of 1
  ..$ val: num [1:3] 100 150 200
 $ price:List of 1
  ..$ val: num [1:3] 200 250 300
> print(lst2)
$cost
$cost$val
[1] 100 150 200


$price
$price$val
[1] 200 250 300


> print(lst2$cost$val[2])
[1] 150
> print(lst2$price$val[3])
[1] 300
> lis<-list()
> str(lst)
Error in str(lst) : object 'lst' not found
> lst[[1]]<-0.5
Error in lst[[1]] <- 0.5 : object 'lst' not found
> lst[[2]]<-c("a","c","f")
Error in lst[[2]] <- c("a", "c", "f") : object 'lst' not found
> lst<-list()
> str(lst)
 list()
> lst[[1]]<-0.5
> lst[[2]]<-c("a","c","f")
> str(lst)
List of 2
 $ : num 0.5
 $ : chr [1:3] "a" "c" "f"
> lst[["price"]]<-c(100,200,300)
> str(lst)
List of 3
 $      : num 0.5
 $      : chr [1:3] "a" "c" "f"
 $ price: num [1:3] 100 200 300
```

##### unlist 함수

1. 기본적인 통계 함수들은 벡터에서는 동작하지만  리스트에는 동작하지 않는 경우,
    리스트 구조를 제거하고, 벡터로 만들어주는 함수

   ```r
   > vec_emp1<-unlist(emp1)  #서로 다른 데이터 타입의 값들이 chracter로 변환되어 named 벡터로 생성됨
   > str(vec_emp1)
   List of 3
    $ name    : chr "kim"
    $ address : chr "seoul"
    $ hiredate:function (x, ...)  
        
   #문  exam1<- list(1,0, 2,0, -3, 4, -5, 6, 7, -8, 9, 10)
   #exam1로부터 음수를 제거한 리스트 출력
   > print(exam1[exam1>0])# 또는 exam1(exam1[exam1<0]<-NULL print(exam1)
   [[1]]
   [1] 1
   
   [[2]]
   [1] 2
   
   [[3]]
   [1] 4
   
   [[4]]
   [1] 6
   
   [[5]]
   [1] 7
   
   [[6]]
   [1] 9
   
   [[7]]
   [1] 10
   #exam1로부터 0를 제거한 리스트 출력
   > print(exam1[exam1!=0]) #또는 exam1[exam1==0]<-NULL print(exam1)
   [[1]]
   [1] 1
   
   [[2]]
   [1] 2
   
   [[3]]
   [1] -3
   
   [[4]]
   [1] 4
   
   [[5]]
   [1] -5
   
   [[6]]
   [1] 6
   
   [[7]]
   [1] 7
   
   [[8]]
   [1] -8
   
   [[9]]
   [1] 9
   
   [[10]]
   [1] 10
   ```

##### lapply함수는 데이터 객체에 함수를 적용한 결과를 list형태로 반환

```r
> a<-list(c(1:5))
> b<-list(6:10)
> result<-lapply(c(a,b),max)
> print(result)
[[1]]
[1] 5

[[2]]
[1] 10

> str(result)
List of 2
 $ : int 5
 $ : int 10
```

##### sapply 함수는 데이터 객체에 함수를 적용한 결과를 벡터 형식으로

```r
> result<-sapply(c(a,b),max)
> print(result)
[1]  5 10
> str(result)
 int [1:2] 5 10
```

##### 다차원(중첩) 리스트

- 리스트 자료구조에 다른 리스트가 중첩된 자료구조

```r
> multi_list<-list(c1=list(1,2,3),
+                  c2=list(10,20,30),
+                  c3=list(100,200,300))
> print(multi_list)
$c1
$c1[[1]]
[1] 1

$c1[[2]]
[1] 2

$c1[[3]]
[1] 3


$c2
$c2[[1]]
[1] 10

$c2[[2]]
[1] 20

$c2[[3]]
[1] 30


$c3
$c3[[1]]
[1] 100

$c3[[2]]
[1] 200

$c3[[3]]
[1] 300
```

##### 다차원 리스트를 열단위로 바인딩

```r
> do.call(cbind,multi_list)
     c1 c2 c3 
[1,] 1  10 100
[2,] 2  20 200
[3,] 3  30 300
```

## DataFrame

1. 데이터베이스의 테이블 구조와 비슷
2. R에서 가장 많이 사용하는 자료구조
3. 칼럼 단위로 서로 다른 데이터로 저장 가능
4. 리스트와 벡터의 혼합형으로 컬럼은 리스트, 컬럼 내의 데이터는 백터 자료
5. DataFrame 생성 함수-data.frame(),read.table(),read.csv(),txt,excel,csv 파일로부터 DataFrame생성
6. data.Frame(컬럼1=자료, 컬럼2=자료,.....,컬럼n=자료)
7. 즉 리스트와 컬럼의 혼합형!
8. 여러개의 백터 객체를 이용하여 데이터프레임 생성 가능
9. 이떄 모든 컬럼은 길이가 같아야 하며, 컬럼의 길이가 다르면 오류가 생길 수 있다.

```r
> d1<-data.frame(no=c(1,2,3,4,5),
+                name=c('kim','park','lee','song','hong'),
+                gender=c('F','W','M','W','M'))
> str(d1)               
'data.frame':	5 obs. of  3 variables:
 $ no    : num  1 2 3 4 5
 $ name  : Factor w/ 5 levels "hong","kim","lee",..: 2 4 3 5 1 #알파벳순
 $ gender: Factor w/ 3 levels "F","M","W": 1 3 2 3 2 #알파벳순
> print(d1)               
  no name gender
1  1  kim      F
2  2 park      W
3  3  lee      M
4  4 song      W
5  5 hong      M
> no<-c(1,2,3)
> name<-c("hong","lee","kim")
> pay<-c(150,250,300)
> vemp<-data.frame(NO=no,Name=name,Pay=pay)
> str(vemp)
'data.frame':	3 obs. of  3 variables:
 $ NO  : num  1 2 3
 $ Name: Factor w/ 3 levels "hong","kim","lee": 1 3 2
 $ Pay : num  150 250 300
> print(vemp)
  NO Name Pay
1  1 hong 150
2  2  lee 250
3  3  kim 300
> 
> sales1<-matrix(c(1,'Apple',500,5,
+                  2,'Peach',200,2,
+                  3,'Grape',50,7,
+                  4,'Banana',100,4),nrow=4,byrow=T)
> str(sales1)
 chr [1:4, 1:4] "1" "2" "3" "4" "Apple" "Peach" "Grape" ...
> df1<-data.frame(sales1)
> str(df1)
'data.frame':	4 obs. of  4 variables:
 $ X1: Factor w/ 4 levels "1","2","3","4": 1 2 3 4
 $ X2: Factor w/ 4 levels "Apple","Banana",..: 1 4 3 2
 $ X3: Factor w/ 4 levels "100","200","50",..: 4 2 3 1
 $ X4: Factor w/ 4 levels "2","4","5","7": 3 1 4 2


```

##### as.numeric()함수는 numeric변환

- matrix로 만드는 경우 모든 컬럼이 factor로 만들어 지므로 이를 방지하기 위해서 stringAsFactors라 한다.

```r
> df1<-data.frame(sales1,stringsAsFactors = FALSE)
> str(df1)
'data.frame':	4 obs. of  4 variables:
 $ X1: chr  "1" "2" "3" "4"
 $ X2: chr  "Apple" "Peach" "Grape" "Banana"
 $ X3: chr  "500" "200" "50" "100"
 $ X4: chr  "5" "2" "7" "4"
> names(df1)<-c('No','Fruit','Price','Qty')
> str(df1)
'data.frame':	4 obs. of  4 variables:
 $ No   : chr  "1" "2" "3" "4"
 $ Fruit: chr  "Apple" "Peach" "Grape" "Banana"
 $ Price: chr  "500" "200" "50" "100"
 $ Qty  : chr  "5" "2" "7" "4"

> df1$Qty <-as.numeric(df1$Qty)
> df1$Price <-as.numeric(df1$Price)
> str(df1)
'data.frame':	4 obs. of  4 variables:
 $ No   : chr  "1" "2" "3" "4"
 $ Fruit: chr  "Apple" "Peach" "Grape" "Banana"
 $ Price: num  500 200 50 100
 $ Qty  : num  5 2 7 4
```

##### data.frame 요소에 접근 

- 변수명$컬럼명 형식으로 접근, 결과는 벡터

```r
> print(d1$name) #컬럼이름으로 data.frame의 특정 칼럼 데이터 모두 access
[1] kim  park lee  song hong
Levels: hong kim lee park song
```

##### 데이터 프레임에 새로운 열 추가

```r
> d1$age<-c(30,31,32,33,34)
> str(d1)
'data.frame':	5 obs. of  4 variables:
 $ no    : num  1 2 3 4 5
 $ name  : Factor w/ 5 levels "hong","kim","lee",..: 2 4 3 5 1
 $ gender: Factor w/ 3 levels "F","M","W": 1 3 2 3 2
 $ age   : num  30 31 32 33 34
```

##### 조건에 맞는 데이터만 추출 subset(데이터프레임 객체, 조건)

- 조건에 만족하는 행을 추출하여 독립된 객체를 생성

```r
> # df1 데이터 프레임에서 수량이 5보다 큰 추출 출력
> subset.df1 <- subset(df1, Qty>5) 
> print(subset.df1)
  No Fruit Price Qty
3  3 Grape    50   7
> str(subset.df1)
'data.frame':	1 obs. of  4 variables:
 $ No   : chr "3"
 $ Fruit: chr "Grape"
 $ Price: num 50
 $ Qty  : num 7

# 문)df1 데이터 프레임에서 가격이 150보다 작은 데이터들 출력
 > subset.df1<-subset(df1,Price<150)
> print(subset.df1)
  No  Fruit Price Qty
3  3  Grape    50   7
4  4 Banana   100   4

# 문)df1 데이터 프레임에서 과일명이 바나나인것만  data.frame 구조로  출력
> subset.df1<-subset(df1,Fruit=="Banana")
> print(subset.df1)
  No  Fruit Price Qty
4  4 Banana   100   4
> str(subset.df1)
'data.frame':	1 obs. of  4 variables:
 $ No   : chr "4"
 $ Fruit: chr "Banana"
 $ Price: num 100
 $ Qty  : num 4

df2<-data.frame(x=c(1:5), 
                y=seq(2, 10, 2), 
                z=c('a', 'b', 'c', 'd', 'e'))
#문) df2 데이터프레임객체의 x컬럼의 값이 2이상이고  y컬럼은 6이하인 데이터들로 구성된 데이터프레임 부분집합 생성
> subset.df2<-subset(df2,x>=2 & y<=6)
> print(subset.df2)
  x y z
2 2 4 b
3 3 6 c

#문> df2 데이터프레임객체의 x컬럼의 값이 2이상 또는  y컬럼은 6이하인 데이터들로 구성된 데이터프레임 부분집합 생성
> subset.df2<-subset(df2,x>=2 | y<=6)
> print(subset.df2)
  x  y z
1 1  2 a
2 2  4 b
3 3  6 c
4 4  8 d
5 5 10 e

```

#####  데이터 프레임에서 특정 컬럼만 추출해서 새로운 형태의 데이터 프레임 생성

```r
> df5<-subset(df1,select=c(Fruit,Price,Qty))
> str(df5)
'data.frame':	4 obs. of  3 variables:
 $ Fruit: chr  "Apple" "Peach" "Grape" "Banana"
 $ Price: num  500 200 50 100
 $ Qty  : num  5 2 7 4
> print(df5)
   Fruit Price Qty
1  Apple   500   5
2  Peach   200   2
3  Grape    50   7
4 Banana   100   4
#----------------------------------------------------------------------
> df6<-subset(df1,select=-No)
> str(df6)
'data.frame':	4 obs. of  3 variables:
 $ Fruit: chr  "Apple" "Peach" "Grape" "Banana"
 $ Price: num  500 200 50 100
 $ Qty  : num  5 2 7 4
> print(df6)
   Fruit Price Qty
1  Apple   500   5
2  Peach   200   2
3  Grape    50   7
4 Banana   100   4

##----------------------------------------------------------------------
> emp.data <- data.frame(
+   emp_id = c (1:5), 
+   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
+   salary = c(623.3,515.2,611.0,729.0,843.25), 
+   
+   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
+                          "2015-03-27")),
+   stringsAsFactors = FALSE
+ )
> print(emp.data) 
  emp_id emp_name salary start_date
1      1     Rick 623.30 2012-01-01
2      2      Dan 515.20 2013-09-23
3      3 Michelle 611.00 2014-11-15
4      4     Ryan 729.00 2014-05-11
5      5     Gary 843.25 2015-03-27
> str(emp.data)
'data.frame':	5 obs. of  4 variables:
 $ emp_id    : int  1 2 3 4 5
 $ emp_name  : chr  "Rick" "Dan" "Michelle" "Ryan" ...
 $ salary    : num  623 515 611 729 843
 $ start_date: Date, format: "2012-01-01" ...

#문> emp.data객체에서  3행, 5행의 2열과 4열의 데이터만 추출해서 출력
> result<-emp.data[c(3,5),c(2,4)]
> print(result)      
  emp_name start_date
3 Michelle 2014-11-15
5     Gary 2015-03-27
```

#####  summary()

- 데이터 프레임 객체의 데이터를 대상으로 최소값, 최대값, 중위수,값 등을 확인 가능

```r
> summary(df2)
       x           y      z    
 Min.   :1   Min.   : 2   a:1  
 1st Qu.:2   1st Qu.: 4   b:1  
 Median :3   Median : 6   c:1  
 Mean   :3   Mean   : 6   d:1  
 3rd Qu.:4   3rd Qu.: 8   e:1  
 Max.   :5   Max.   :10        
> apply(df2[, c(1,2)],2,sum)
 x  y 
15 30 
> 
> df4<-data.frame(name=c('apple','banana','cherry'),
+                 price=c(300,200,100))          
> df5<-data.frame(name=c('apple','cherry','berry'),
+                 qty=c(10,20,30))          

```

##### 두 데이터 프레인 객체의 요소를 병합

- merge = 첫번째 열 기준으로 병합
- join = ?

```r
> print(df4)
    name price
1  apple   300
2 banana   200
3 cherry   100
> print(df5)
    name qty
1  apple  10
2 cherry  20
3  berry  30
#첫번쨰 열 데이터 기준으로 일치하는 데이터의 열 결합

> result<-merge(df4,df5)
> print(result)
    name price qty
1  apple   300  10
2 cherry   100  20
> 
> 
> str(result)
'data.frame':	2 obs. of  3 variables:
 $ name : Factor w/ 3 levels "apple","banana",..: 1 3
 $ price: num  300 100
 $ qty  : num  10 20
> 

#첫번 쨰 열 데이터 기준로 모든 데이터의 열 결합, Data가 없으면 NA
> result2<-merge(df4,df5,all=T)
> print(result2)
    name price qty
1  apple   300  10
2 banana   200  NA
3 cherry   100  20
4  berry    NA  30
> str(result2)
'data.frame':	4 obs. of  3 variables:
 $ name : Factor w/ 4 levels "apple","banana",..: 1 2 3 4
 $ price: num  300 200 100 NA
 $ qty  : num  10 NA 20 30
```

##### R에서 제공해주는 데이터 셋

```r
str(mtcars)
head(mtcars) #1~6행만
head(mtcars,20) 
tail(mtcars) #last에서 -5까지
data(mtcars)
View(mtcars)#테이블 탭이 열리며 테이블이 보인다.
summary(mtcars) #컬럼단위로 최소갑, 1/4분위값, 중앙값, 평균, 3/4분위
summary(emp.data)
```

## 문자열 처리와 관련된 패키지 stringr

- 텍스트 자료나 sns에서 가고 처리된 빅데이터를 처리하기 위해서 필요한 문자열을 적절하게 자르고, 교체하고 추출하는 작업을 수행

```r
install.packages("stringr")
library(stringr)
#str_length()
#str_c(),str_join()
#str_sub(),str_split()
#str_replace()
#str_extract()
#str_extract()_all() 정규표현식을 사용하여 문자열 추출
#str_locate()특정 문자열 패턴의 첫번쨰 위치 찾기
#str_locate_all()
#.... 등 다양함


```

##### 패턴을 포함한 요소에서 패턴 출현회수 리턴

```r

> fruits<-c('apple','banana','pineapple','berry','APPLE')
> print(str_count(fruits,"a"))
[1] 1 3 1 0 0
```

##### 문자열 결합 기본 R 함수 검색

```r
> rs1<-paste('hello','~R')
> print(rs1)
[1] "hello ~R"

> print(str_c(fruits,"name is",fruits))
[1] "applename isapple"         "banananame isbanana"      
[3] "pineapplename ispineapple" "berryname isberry"        
[5] "APPLEname isAPPLE"        
> print(str_c(fruits,collapse=" "))
[1] "apple banana pineapple berry APPLE"
> print(str_c(fruits,collapse = "-"))
[1] "apple-banana-pineapple-berry-APPLE"
> 
> print(str_detect(fruits,'A')) # dataset객체의 요소별로 'A'포함여부를
[1] FALSE FALSE FALSE FALSE  TRUE
> print(str_detect(fruits,'^a'))# 정규표현식의 형식문자^는 시작을 의미
[1]  TRUE FALSE FALSE FALSE FALSE
> print(str_detect(fruits,'a$'))# a로 끝나는것!
[1] FALSE  TRUE FALSE FALSE FALSE
> print(str_detect(fruits,'^[aA]'))# []의 ^은 not의 의미
[1]  TRUE FALSE FALSE FALSE  TRUE
> print(str_detect(fruits,'[^a]'))#여기서도 not
[1] TRUE TRUE TRUE TRUE TRUE
```

#####  부분추출

```R
> print(str_sub(fruits,start=1,end=3))
[1] "app" "ban" "pin" "ber" "APP"
> print(str_sub(fruits,start=6,end=9))
[1] ""     "a"    "pple" ""     ""    
> print(str_sub(fruits,start=-5))
[1] "apple" "anana" "apple" "berry" "APPLE"
```

##### 공백 제거

```r
> str_length(("    apple    banana    "))
[1] 23
> str_length(str_trim("    apple    banana    ")) #앞뒤 공백 제거 trim()
[1] 15
```

##### dataset객체의 요소 문자열을 길이를 벡터로 리턴

```r
> print(str_length(fruits))
[1] 5 6 9 5 5
> print(str_dup(fruits,3))
[1] "appleappleapple"             "bananabananabanana"         
[3] "pineapplepineapplepineapple" "berryberryberry"            
[5] "APPLEAPPLEAPPLE" 

> print(str_replace(fruits,'p','**'))
[1] "a**ple"     "banana"     "**ineapple" "berry"     
[5] "APPLE"     
> print(str_replace_all(fruits,'p','**')) #대소문자 신경 x
[1] "a****le"      "banana"       "**inea****le" "berry"       
[5] "APPLE"  

#----------------------------------------------------------------------
> fruits2<- str_c(fruits,collapse = "/")
> print(fruits2)
[1] "apple/banana/pineapple/berry/APPLE"
> str(fruits2)
 chr "apple/banana/pineapple/berry/APPLE"
> 
> result2<-str_split(fruits2,"/")
> print(result2)
[[1]]
[1] "apple"     "banana"    "pineapple" "berry"     "APPLE"    

> str(result2)
List of 1
 $ : chr [1:5] "apple" "banana" "pineapple" "berry" ...

> str_extract("홍길동35이순신45유관순25","[1-9]{2}")
[1] "35"
> str_extract_all("홍길동35이순신45유관순25","[1-9]{2}")
[[1]]
[1] "35" "45" "25"

> str_extract("honggil305koreaseoul1004you25jeju-hanlasan2005","[1-9]{2}")
[1] "25"
> str_extract("honggil305koreaseoul1004you25jeju-hanlasan2005","[1-9]{2}")
[1] "25"
#----------------------------------------------------------------------
#문str1객체에 저장된 문자열로부터 주민번호만 추출
> str1<-"korea123456-123456seoul"
> print(str1)
[1] "korea123456-123456seoul"
> str_extract(str1,"[1-9]{6}-[1-9]{6}")
[1] "123456-123456"

#문 str2객체에 저장된 문자열로부터 7글자 이상의 단어만 추출

> str2<-"홍길동1357,이순신,유관순1012"
> str_extract_all(str2,"\\w{7,}")
[[1]]
[1] "홍길동1357" "유관순1012"
```

##### 대문자 소문자

```r
> str_to_lower(str1)
[1] "korea123456-123456seoul"
> str_to_upper(str1)
[1] "KOREA123456-123456SEOUL"
```



## 데이터 입출력

##### scan() 

- 키보드로부터 데이터 입력 받기 위해 사용 입력할 데이터가 없으면 엔터키만 누르면 종료! 문자열로 입력받으려면 what=character()옵션 사용

##### 키보드로 숫자 입력

```r
> num<-scan()
1: 1
2: 2
3: 3
4: 4
5: 5
6: 6
7: 7
8: 8
9: 9
10: 10
11: 
Read 10 items
> sum(num)
[1] 55
```

##### edit() 

- 데이터 입력을 돕기 위해 표 형식의 데이터 편집기 제공

```r
> df=data.frame()

> df=edit(df)
#하면 팝업으로 데이터 편집기가 뜨며 아래의 표대로 입력 후 닫기를 누른다.
> print(df)
   학번   이름 국어 영어 수학
1     1 홍길동   80   80   80
2     2 이순신   95   90   95
3     3 강감찬   95   95  100
4     4 유관순   85   85   85
5     5 김유신   95   90   95
```

#####  라인 단위로 입력

```r
> input1<-scan(what="")
1: korea seoul chongreo-gu
4: 
Read 3 items
> print(input1)
[1] "korea"       "seoul"       "chongreo-gu"
> str(input1)
 chr [1:3] "korea" "seoul" "chongreo-gu"
> address<-readline() 
korea seoul chongreo-gu
> print(address)
[1] "korea seoul chongreo-gu"
> str(a)
List of 1
 $ : int [1:5] 1 2 3 4 5
> address<-readline("input your address=>")
input your address=>korea is my house
> print(address)
[1] "korea is my house"
> str(address)
 chr "korea is my house"
```



## 파일 입출력

##### 파일 유형

- text,csv,xml,html,json,db,excel,bigdata저장소(hd)

```r
getwd()
setwd("c:/workspaceR")
print(list.files())
> print(list.files())
[1] "sent.R"
```

c:workspaceR 디렉토리 아래 data디렉토리 생성 후 샘플 파일 다운로드 받아서 압출 풀어 파일 저장 후  

```r

> print(list.files(recursive=T))
 [1] "emp.csv"           "emp.txt"           "emp2.csv"         
 [4] "excel.csv"         "finviz.csv"        "sent.R"           
 [7] "stdf.csv"          "stock.csv"         "student.txt"      
[10] "student1.txt"      "student2.txt"      "student3.txt"     
[13] "student4.txt"      "studentexcel.xlsx" "studentx.xlsx"    
[16] "test.csv"         
> print(list.files(all.files=T))
 [1] "."                 ".."                "emp.csv"          
 [4] "emp.txt"           "emp2.csv"          "excel.csv"        
 [7] "finviz.csv"        "sent.R"            "stdf.csv"         
[10] "stock.csv"         "student.txt"       "student1.txt"     
[13] "student2.txt"      "student3.txt"      "student4.txt"     
[16] "studentexcel.xlsx" "studentx.xlsx"     "test.csv"  
```

##### csv 형식의 data가 저장된 파일로부터 ㅇata를 읽어서 R실행환경으로 로딩

```r
> data1<-read.csv("./emp.csv")
#또는 data1<-read.csv("c:/workspaceR/emp.csv")
> print(data1)
   no   name pay
1 101 홍길동 150
2 102 이순신 450
3 103 강감찬 500
4 104 유관순 350
5 105 김유신 400
> str(data1)
'data.frame':	5 obs. of  3 variables:
 $ no  : int  101 102 103 104 105
 $ name: Factor w/ 5 levels "강감찬","김유신",..: 5 4 1 3 2
 $ pay : int  150 450 500 350 400
```

##### 사원 데이터에서 최대 급여를 출력

```r
> max_sal<-max(data1$pay)
> print(max_sal)
[1] 500
```

##### 최대 급여를 받는 레코드(행)만 추출

```r
> person1<-subset(data1,pay==max(pay))
> print(person1)
   no   name pay
3 103 강감찬 500
> persion2<-subset(data1,pay>300)
> print(persion2)
   no   name pay
2 102 이순신 450
3 103 강감찬 500
4 104 유관순 350
5 105 김유신 400

#문) emp3.csv파일의 데이터를 data.frame객체에 저장한 후에
#IT부서에서 급여가 600이상인 사원 추출
 > p1<-subset(data.frame,salary>600)
> print(p1)
  id     name salary  startdate    dept
1  1     Rick 623.30 2012-01-01      IT
3  3 Michelle 611.00 2014-11-15      IT
4  4     Ryan 729.00 2014-11-05      HR
5  5     Gary 843.25 2015-03-27 Finance

##문) emp3.csv파일의 데이터를 data.frame객체에 저장한 후에
#입사날자가 2014년 7월 01일 이후인 사원추출
> p2<-subset(data.frame,as.Date(startdate)>as.Date("2014-07-01"))
> print(p2)      
  id     name salary  startdate    dept
3  3 Michelle 611.00 2014-11-15      IT
4  4     Ryan 729.00 2014-11-05      HR
5  5     Gary 843.25 2015-03-27 Finance
#또는! 
> data.frame$startdate<-as.Date(data.frame$startdate)
> str(data.frame)
'data.frame':	6 obs. of  5 variables:
 $ id       : int  1 2 3 4 5 6
 $ name     : Factor w/ 6 levels "Dan","Gary","Michelle",..: 5 1 3 6 2 4
 $ salary   : num  623 515 611 729 843 ...
 $ startdate: Date, format: "2012-01-01" ...
 $ dept     : Factor w/ 4 levels "Finance","HR",..: 3 4 3 2 1 3
> print(subset(data.frame,startdate>"2014-07-01"))
  id     name salary  startdate    dept
3  3 Michelle 611.00 2014-11-15      IT
4  4     Ryan 729.00 2014-11-05      HR
5  5     Gary 843.25 2015-03-27 Finance
```

##### it부서 사원만 추출해서 csv파일에 저장

- 먼저 파일 output폴더를 생성하자

```r
> itperson<-subset(data.frame,dept=="IT")
> print(itperson)
  id     name salary  startdate dept
1  1     Rick  623.3 2012-01-01   IT
3  3 Michelle  611.0 2014-11-15   IT
6  6     Nina  578.0       <NA>   IT
> write.csv(itperson,"./output/itperson.csv",row.names=FALSE)
> list.files("./output/")
[1] "itperson.csv"
> newdata<-read.csv("./output/itperson.csv")
> print(newdata)
  id     name salary  startdate dept
1  1     Rick  623.3 2012-01-01   IT
2  3 Michelle  611.0 2014-11-15   IT
3  6     Nina  578.0       <NA>   IT
```

#####  엑셀 파일로부터 데이터 읽기

- read.xlsz로 데이터를 일기 위해서는 xlsx패키지가 필요하며 설치해야 한다
- sheetIndex=1 은 선택한 엑셀 파일에서 첫 번째 시트 탭을 지정한다.

```r
install.packages("rJava")
install.packages("xlsx")
Sys.setenv(JAVA_HOME='C:\\Program Files\\JAVA\\jre1.8.0_151')
#위에것 다운로드!

> library(rJava)
> library(xlsx)
> Sys.setenv(JAVA_HOME='C:\\Program Files\\JAVA\\jre1.8.0_151')
> studentex<- read.xlsx(file.choose(),sheetIndex=1, encoding="UTF-8")
> studentex
  NA. 학번   이름 성적 평가
1   1  101 홍길동   80    B
2   2  102 이순신   95   A+
3   3  103 강감찬   78   C+
4   4  104 유관순   85   B+
5   5  105 김유신   65   D+
> itperson<-subset(data.frame,dept=="IT")
> print(itperson)
  id     name salary  startdate dept
1  1     Rick  623.3 2012-01-01   IT
3  3 Michelle  611.0 2014-11-15   IT
6  6     Nina  578.0       <NA>   IT
> write.xlsx(itperson,"./output/itperson.xlsx",sheetName="IT",row.names=FALSE)
#컬럼이름과 로우이름을 지정하지 않은 것 
> list.files("./output/")
[1] "itperson.csv"  "itperson.xlsx"
> newdata<-read.xlsx("./output/itperson.xlsx",sheetIndex=1,header=TRUE)
> print(newdata)
  id     name salary  startdate dept
1  1     Rick  623.3 2012-01-01   IT
2  3 Michelle  611.0 2014-11-15   IT
3  6     Nina  578.0       <NA>   IT
```

##### 텍스트 파일 읽기 readLines(),read.table()

```r
> file1 <- readLines("./fruits.txt")  
Warning message:
In readLines("./fruits.txt") :
  incomplete final line found on './fruits.txt'
> print(file1)
[1] "no  name  price   qty  " "1   apple   500     5  "
[3] "2   banana  200     2  " "3   peach   200     7  "
[5] "4   berry    50     9  "
> str(file1)
 chr [1:5] "no  name  price   qty  " ...


```

##### 텍스트 파일 내용 읽어서 data.frame객체로 생성

- 먼저 fruits.txt 파일 저장

```
no  name  price   qty  
1   apple   500     5  
2   banana  200     2  
3   peach   200     7  
4   berry    50     9 
```



```r
> fruits1 <- read.table("./fruits.txt" ) 
Warning message:
In read.table("./fruits.txt") :
  './fruits.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다
> print(fruits1)
  V1     V2    V3  V4
1 no   name price qty
2  1  apple   500   5
3  2 banana   200   2
4  3  peach   200   7
5  4  berry    50   9
> str(fruits1)
'data.frame':	5 obs. of  4 variables:
 $ V1: Factor w/ 5 levels "1","2","3","4",..: 5 1 2 3 4
 $ V2: Factor w/ 5 levels "apple","banana",..: 4 1 2 5 3
 $ V3: Factor w/ 4 levels "200","50","500",..: 4 3 1 1 2
 $ V4: Factor w/ 5 levels "2","5","7","9",..: 5 2 1 3 4
> 
> fruits1 <- read.table("./fruits.txt", header=T)
Warning message:
In read.table("./fruits.txt", header = T) :
  './fruits.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다
> print(fruits1)
  no   name price qty
1  1  apple   500   5
2  2 banana   200   2
3  3  peach   200   7
4  4  berry    50   9
> str(fruits1) 
'data.frame':	4 obs. of  4 variables:
 $ no   : int  1 2 3 4
 $ name : Factor w/ 4 levels "apple","banana",..: 1 2 4 3
 $ price: int  500 200 200 50
 $ qty  : int  5 2 7 9
> 
> fruits1 <- read.table("./fruits.txt", header=T, stringsAsFactor=FALSE)
Warning message:
In read.table("./fruits.txt", header = T, stringsAsFactor = FALSE) :
  './fruits.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다
> print(fruits1)
  no   name price qty
1  1  apple   500   5
2  2 banana   200   2
3  3  peach   200   7
4  4  berry    50   9
> str(fruits1)
'data.frame':	4 obs. of  4 variables:
 $ no   : int  1 2 3 4
 $ name : chr  "apple" "banana" "peach" "berry"
 $ price: int  500 200 200 50
 $ qty  : int  5 2 7 9
```



##### 저장 & 삭제

- fruits.txt는 미리 아패의 표를 참고해 만들어 놓는다.

```r
> fruits <- read.table("./fruits.txt" ) 
Warning message:
In read.table("./fruits.txt") :
  './fruits.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다
> print(fruits1)
Error in print(fruits1) : object 'fruits1' not found
> str(fruits)
'data.frame':	5 obs. of  4 variables:
 $ V1: Factor w/ 5 levels "1","2","3","4",..: 5 1 2 3 4
 $ V2: Factor w/ 5 levels "apple","banana",..: 4 1 2 5 3
 $ V3: Factor w/ 4 levels "200","50","500",..: 4 3 1 1 2
 $ V4: Factor w/ 5 levels "2","5","7","9",..: 5 2 1 3 4
> save(fruits,file="./output/fruits.RData")
> rm(list=ls())
```

##### XML구조의 파일을 Read/Write

- 먼저 emp.xml파일을 저장하고! xml 패키지를 설치해야한다.
- **xmlParse()** 로 xml파일 저장!

```r
install.packages("XML")
library(XML)
> data2<-xmlParse(file="./emp.xml")
> rootnode<-xmlRoot(data2)
> print(rootnode)
<RECORDS>
  <EMPLOYEE>
    <ID>1</ID>
    <NAME>Rick</NAME>
    <SALARY>623.3</SALARY>
    <STARTDATE>1/1/2012</STARTDATE>
    <DEPT>IT</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>2</ID>
    <NAME>Dan</NAME>
    <SALARY>515.2</SALARY>
    <STARTDATE>9/23/2013</STARTDATE>
    <DEPT>Operations</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>3</ID>
    <NAME>Michelle</NAME>
    <SALARY>611</SALARY>
    <STARTDATE>11/15/2014</STARTDATE>
    <DEPT>IT</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>4</ID>
    <NAME>Ryan</NAME>
    <SALARY>729</SALARY>
    <STARTDATE>5/11/2014</STARTDATE>
    <DEPT>HR</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>5</ID>
    <NAME>Gary</NAME>
    <SALARY>843.25</SALARY>
    <STARTDATE>3/27/2015</STARTDATE>
    <DEPT>Finance</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>6</ID>
    <NAME>Nina</NAME>
    <SALARY>578</SALARY>
    <STARTDATE>5/21/2013</STARTDATE>
    <DEPT>IT</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>7</ID>
    <NAME>Simon</NAME>
    <SALARY>632.8</SALARY>
    <STARTDATE>7/30/2013</STARTDATE>
    <DEPT>Operations</DEPT>
  </EMPLOYEE>
  <EMPLOYEE>
    <ID>8</ID>
    <NAME>Guru</NAME>
    <SALARY>722.5</SALARY>
    <STARTDATE>6/17/2014</STARTDATE>
    <DEPT>Finance</DEPT>
  </EMPLOYEE>
</RECORDS> 
> class(rootnode)
[1] "XMLInternalElementNode" "XMLInternalNode"       
[3] "XMLAbstractNode"       
> str(rootnode)
Classes 'XMLInternalElementNode', 'XMLInternalNode', 'XMLAbstractNode' <externalptr> 
> 
> rootsize<-xmlSize(rootnode)
> print(rootsize)
[1] 8
> print(rootnode[1])
$EMPLOYEE
<EMPLOYEE>
  <ID>1</ID>
  <NAME>Rick</NAME>
  <SALARY>623.3</SALARY>
  <STARTDATE>1/1/2012</STARTDATE>
  <DEPT>IT</DEPT>
</EMPLOYEE> 

attr(,"class")
[1] "XMLInternalNodeList" "XMLNodeList"        
> print(rootnode[[1]][[2]]);
<NAME>Rick</NAME> 
> print(rootnode[[1]][[3]]);
<SALARY>623.3</SALARY> 
> print(rootnode[[1]][[5]]);
<DEPT>IT</DEPT> 
> 
> xmldataframe<-xmlToDataFrame("./emp.xml")
> print(xmldataframe)
  ID     NAME SALARY  STARTDATE       DEPT
1  1     Rick  623.3   1/1/2012         IT
2  2      Dan  515.2  9/23/2013 Operations
3  3 Michelle    611 11/15/2014         IT
4  4     Ryan    729  5/11/2014         HR
5  5     Gary 843.25  3/27/2015    Finance
6  6     Nina    578  5/21/2013         IT
7  7    Simon  632.8  7/30/2013 Operations
8  8     Guru  722.5  6/17/2014    Finance
> str(xmldataframe)
'data.frame':	8 obs. of  5 variables:
 $ ID       : Factor w/ 8 levels "1","2","3","4",..: 1 2 3 4 5 6 7 8
 $ NAME     : Factor w/ 8 levels "Dan","Gary","Guru",..: 6 1 4 7 2 5 8 3
 $ SALARY   : Factor w/ 8 levels "515.2","578",..: 4 1 3 7 8 2 5 6
 $ STARTDATE: Factor w/ 8 levels "1/1/2012","11/15/2014",..: 1 8 2 4 3 5 7 6
 $ DEPT     : Factor w/ 4 levels "Finance","HR",..: 3 4 3 2 1 3 4 1
> class(xmldataframe)
[1] "data.frame"
```



##### JSON 데이터 Read/Write

```json
{ 
   "ID": ["1","2","3","4","5","6","7","8" ],
   "Name":["Rick","Dan","Michelle","Ryan","Gary","Nina","Simon","Guru" ],
   "Salary":["623.3","515.2","611","729","843.25","578","632.8","722.5" ],
   
   "StartDate":[ "1/1/2012","9/23/2013","11/15/2014","5/11/2014","3/27/2015","5/21/2013",
      "7/30/2013","6/17/2014"],
   "Dept":[ "IT","Operations","IT","HR","Finance","IT","Operations","Finance"]
}
```

- 를 emp.json으로 저장
- rjoin패키지를 저장한다.

```r
install.packages("rjson")
library()
> rm(list=ls())
> data1<-fromJSON(file="./emp.json")
> print(data1)
$ID
[1] "1" "2" "3" "4" "5" "6" "7" "8"

$Name
[1] "Rick"     "Dan"      "Michelle" "Ryan"     "Gary"    
[6] "Nina"     "Simon"    "Guru"    

$Salary
[1] "623.3"  "515.2"  "611"    "729"    "843.25" "578"    "632.8" 
[8] "722.5" 

$StartDate
[1] "1/1/2012"   "9/23/2013"  "11/15/2014" "5/11/2014" 
[5] "3/27/2015"  "5/21/2013"  "7/30/2013"  "6/17/2014" 

$Dept
[1] "IT"         "Operations" "IT"         "HR"        
[5] "Finance"    "IT"         "Operations" "Finance"   

> str(data1)
List of 5
 $ ID       : chr [1:8] "1" "2" "3" "4" ...
 $ Name     : chr [1:8] "Rick" "Dan" "Michelle" "Ryan" ...
 $ Salary   : chr [1:8] "623.3" "515.2" "611" "729" ...
 $ StartDate: chr [1:8] "1/1/2012" "9/23/2013" "11/15/2014" "5/11/2014" ...
 $ Dept     : chr [1:8] "IT" "Operations" "IT" "HR" ...
> emp.dataframe<-as.data.frame(data1)
> print(emp.dataframe)
  ID     Name Salary  StartDate       Dept
1  1     Rick  623.3   1/1/2012         IT
2  2      Dan  515.2  9/23/2013 Operations
3  3 Michelle    611 11/15/2014         IT
4  4     Ryan    729  5/11/2014         HR
5  5     Gary 843.25  3/27/2015    Finance
6  6     Nina    578  5/21/2013         IT
7  7    Simon  632.8  7/30/2013 Operations
8  8     Guru  722.5  6/17/2014    Finance
> str(emp.dataframe)
'data.frame':	8 obs. of  5 variables:
 $ ID       : Factor w/ 8 levels "1","2","3","4",..: 1 2 3 4 5 6 7 8
 $ Name     : Factor w/ 8 levels "Dan","Gary","Guru",..: 6 1 4 7 2 5 8 3
 $ Salary   : Factor w/ 8 levels "515.2","578",..: 4 1 3 7 8 2 5 6
 $ StartDate: Factor w/ 8 levels "1/1/2012","11/15/2014",..: 1 8 2 4 3 5 7 6
 $ Dept     : Factor w/ 4 levels "Finance","HR",..: 3 4 3 2 1 3 4 1

#txt파일 json으로 저장하기~

> fruits1<-read.table("./fruits.txt",header=T,stringsAsFactor=FALSE)
Warning message:
In read.table("./fruits.txt", header = T, stringsAsFactor = FALSE) :
  './fruits.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다
> print(fruits1)
  no   name price qty
1  1  apple   500   5
2  2 banana   200   2
3  3  peach   200   7
4  4  berry    50   9
> str(fruits1)
'data.frame':	4 obs. of  4 variables:
 $ no   : int  1 2 3 4
 $ name : chr  "apple" "banana" "peach" "berry"
 $ price: int  500 200 200 50
 $ qty  : int  5 2 7 9
> class(fruits1)
[1] "data.frame"
> result<-toJSON(fruits1)
> print(fruits1)
  no   name price qty
1  1  apple   500   5
2  2 banana   200   2
3  3  peach   200   7
4  4  berry    50   9
> str(fruits1)
'data.frame':	4 obs. of  4 variables:
 $ no   : int  1 2 3 4
 $ name : chr  "apple" "banana" "peach" "berry"
 $ price: int  500 200 200 50
 $ qty  : int  5 2 7 9
> write(result,"./output/fruits.json")
> list.files("./output/")
[1] "fruits.json"   "fruits.RData"  "itperson.csv" 
[4] "itperson.xlsx"
```

##### HTML

- httr패키지는 지정한 url의 HTMl의 소스를 가져오는 GET() 함수를 제공
- < table>태그의 내용을 읽어올 수 있는 readHTMLTable()함수 제공
- readHTMLTable()에 사용되는 속성 
  - get_url$content  : GET(url)함수에 의해서 가져온 HTML소스의 내용
  - rawToChar() : 바이너리(binary) 소스를 HTML 태그로 변환
  - stringsAsFactors = F : 문자열을 요인으로 처리하지 않고 순수한 문자열로 가져오기

```r
install.packages("httr")
library("httr")
> url<-"https://ssti.org/blog/useful-stats-capita-personal-income-state-2010-2015"
> get_url<-GET(url)
> html_cont<-readHTMLTable(rawToChar(get_url$content),stringsAsFactor=F)
> str(html_cont)
List of 1
 $ NULL:'data.frame':	52 obs. of  7 variables:
  ..$ State: Factor w/ 52 levels "Alabama","Alaska",..: 45 1 2 3 4 5 6 7 8 9 ...
  ..$ 2010 : Factor w/ 52 levels "$30,783","$31,991",..: 32 9 46 10 2 38 35 51 34 52 ...
  ..$ 2011 : Factor w/ 52 levels "$31,976","$33,544",..: 29 9 46 10 3 40 38 51 32 52 ...
  ..$ 2012 : Factor w/ 52 levels "$33,127","$34,846",..: 29 8 45 10 9 41 38 51 32 52 ...
  ..$ 2013 : Factor w/ 52 levels "$33,629","$35,163",..: 30 7 44 10 8 41 38 51 32 52 ...
  ..$ 2014 : Factor w/ 52 levels "$34,431","$36,132",..: 31 7 44 10 9 41 38 51 32 52 ...
  ..$ 2015 : Factor w/ 52 levels "$35,444","$37,047",..: 31 6 46 9 10 42 38 51 30 52 ...
> class(html_cont)
[1] "list"


> html_cont<-as.data.frame(html_cont)
> head(html_cont)
     NULL.State NULL.2010 NULL.2011 NULL.2012 NULL.2013 NULL.2014
1 United States   $40,277   $42,453   $44,266   $44,438   $46,049
2       Alabama   $34,073   $35,202   $36,036   $36,176   $37,512
3        Alaska   $47,773   $50,552   $52,269   $51,259   $54,012
4       Arizona   $34,185   $35,675   $36,788   $36,723   $37,895
5      Arkansas   $31,991   $33,961   $36,291   $36,529   $37,782
6    California   $42,411   $44,852   $47,614   $48,125   $49,985
  NULL.2015
1   $47,669
2   $38,965
3   $55,940
4   $39,060
5   $39,107
6   $52,651
> str(html_cont)
'data.frame':	52 obs. of  7 variables:
 $ NULL.State: Factor w/ 52 levels "Alabama","Alaska",..: 45 1 2 3 4 5 6 7 8 9 ...
 $ NULL.2010 : Factor w/ 52 levels "$30,783","$31,991",..: 32 9 46 10 2 38 35 51 34 52 ...
 $ NULL.2011 : Factor w/ 52 levels "$31,976","$33,544",..: 29 9 46 10 3 40 38 51 32 52 ...
 $ NULL.2012 : Factor w/ 52 levels "$33,127","$34,846",..: 29 8 45 10 9 41 38 51 32 52 ...
 $ NULL.2013 : Factor w/ 52 levels "$33,629","$35,163",..: 30 7 44 10 8 41 38 51 32 52 ...
 $ NULL.2014 : Factor w/ 52 levels "$34,431","$36,132",..: 31 7 44 10 9 41 38 51 32 52 ...
 $ NULL.2015 : Factor w/ 52 levels "$35,444","$37,047",..: 31 6 46 9 10 42 38 51 30 52 ...
> class(html_cont)
[1] "data.frame"

> names(html_cont)<-c("State","y2010","y2011","y2012","y2013","y2014","y2015")
> tail(html_cont)
           State   y2010   y2011   y2012   y2013   y2014   y2015
47       Vermont $40,066 $42,735 $44,287 $44,839 $46,428 $47,864
48      Virginia $45,412 $47,689 $49,320 $48,956 $50,345 $52,136
49    Washington $42,821 $44,800 $47,344 $47,468 $49,610 $51,146
50 West Virginia $32,104 $34,211 $35,374 $35,163 $36,132 $37,047
51     Wisconsin $38,815 $40,837 $42,463 $42,737 $44,186 $45,617
52       Wyoming $44,846 $49,140 $52,154 $51,791 $54,584 $55,303


```

##### sink() 

- 작업한 모든 내용 파일에 저장

```r
sink("./output/process1.txt")#시작! 파일 저장 위치 지정한다.!
url<-"https://ssti.org/blog/useful-stats-capita-personal-income-state-2010-2015"
get_url<-GET(url)
html_cont<-readHTMLTable(rawToChar(get_url$content),stringsAsFactor=F)
str(html_cont)
class(html_cont)
html_cont<-as.data.frame(html_cont)
head(html_cont)
str(html_cont)
class(html_cont)
sink()#close! 
#결과값이 console에 뜨지않고 파일에 저장된다. 

```

#####  저장시 행번호 따옴표 제거!(row.names, quote)

```r
library(xlsx) #없으면 설치후 실행
> studentx<-read.xlsx(file.choose(),sheetIndex = 1, encoding="UTF-8")
> print(studentx)
  학번   이름 성적 평가
1  101 홍길동   80    B
2  102 이순신   95   A+
3  103 강감찬   78   C+
4  104 유관순   85   B+
5  105 김유신   65   D+
> str(studentx)
'data.frame':	5 obs. of  4 variables:
 $ 학번: num  101 102 103 104 105
 $ 이름: Factor w/ 5 levels "강감찬","김유신",..: 5 4 1 3 2
 $ 성적: num  80 95 78 85 65
 $ 평가: Factor w/ 5 levels "A+","B","B+",..: 2 1 4 3 5
> class(studentx)
[1] "data.frame"
> write.table(studentx,'./output/std.txt') # 행번호, 따옴표 출력?
> write.table(studentx,"./output/st2.txt",row.names = FALSE,quote=FALSE)
```



std

```
"?й?" "?̸?" "????" "????"
"1" 101 "ȫ?浿" 80 "B"
"2" 102 "?̼???" 95 "A+"
"3" 103 "??????" 78 "C+"
"4" 104 "��????" 85 "B+"
"5" 105 "??��??" 65 "D+"

```

st2.txt

- 위의 파일과는 다르게 아래의 결과는 따옴표와 행번호가 사라진 것을 알 수 있다.

```
?й? ?̸? ???? ????
101 ȫ?浿 80 B
102 ?̼??? 95 A+
103 ?????? 78 C+
104 ��???? 85 B+
105 ??��?? 65 D+

```

## 조건문

##### if(조건식){참인경우 처리문} else{거짓인 경우 처리문}

```r
> x<-3
> y<-5
> if(x*y>=30){
+   cat("x*y의 결과는 30이상입니다.\n")
+ }else{
+   cat("x*y의 결과는 30미만입니다.\n")
+ }
x*y의 결과는 30미만입니다.

#사용자로부터 표준입력으로 점수를 입력받아서 학점을 출력
#if(조건){실행문} else if(조건){실행문장}...else{실행문장}
> score<-scan()
1: 60
2: 
Read 1 item
> if(score>=90){
+   cat("A")
+ }else if(score>=80){
+   cat("B")
+ }else if(score>=70){
+   cat("C")
+ }else if(score>=60){
+   cat("D")
+ }else {
+   cat("F")
+ }
D
```



##### ifelse(조건식, 참인 경우 처리문, 거짓인 경우 처리문)

```r
#사용자로부터 표준입력으로 점수를 입력 받아 짝수 인지, 홀수인지!
> score1<-scan()
1: 3
2: 
Read 1 item
> ifelse(score1%%2==0,"짝수","홀수")
[1] "홀수"
```



##### switch (비교문, 실행문1, 실행문2, 실행문3) : 비교 문장의 내용에 따라서 여러 개의 실행 문장 중 하나를 선택

```r
#switch(비교문, 실행문1, 실행문 2, 실행문 3....)
# 비교문의 변수의 값이 실행문에 있는 변수와 일치할때, 해당 변수에 할당된 값이 출력

> ename<-scan(what="")
1: park
2: 
Read 1 item
> switch(ename,hong=250,lee=300,park=350,kim=200)
[1] 350

```



##### which(조건)  : 벡터 객체를 대상으로 특정 데이터를 검색하는데 사용되는 함수

- which() 함수의 인수로 사용되는 조건식에 만족하는 경우 벡터 원소의 위치(인덱스)가 출력되며, 조건식이 거짓이면 0이 출력된다.

```r
> names<-c("kim","lee","choi","park")
> which(names=="choi")
[1] 3
> no<-c(1:5)
> name<-c("홍길동","이순신","강감찬","유관순","김유신")
> score<-c(85,90,78,74,80)
> exam<-data.frame(학번=no,이름=name,성적=score)
> ?which
> print(exam[which(exam$이름=="유관순"),])
  학번   이름 성적
4    4 유관순   74
```



##### for(변수 in 변수) {실행문} : 지정한 횟수만큼 실행문을 반복 수행

```r
> i<-c(1:10)
> for(n in i){
+   if(n%%2==0) print(n)
+ }
[1] 2
[1] 4
[1] 6
[1] 8
[1] 10


> for( n in i) {
+   if(n%%2==1) {
+     next
+   }else{
+     print(n) 
+   }
+ }
[1] 2
[1] 4
[1] 6
[1] 8
[1] 10
#데이터 프레임에서 컬럼명 추출, 출력
> name<-c(names(exam))
> for(n in name)
+   print(n)
[1] "학번"
[1] "이름"
[1] "성적"
```



##### while(조건) { 실행문 }

```r
#while문으로 짝수 출력
> l<-0
> while(l<10){
+   l<-l+1
+   if(l%%2==0) print(l)
+ }
[1] 2
[1] 4
[1] 6
[1] 8
[1] 10
```

## 함수: 코드의 집합

- `함수명 <- function(매개변수){실행문}`

##### 매개변수 없는 함수

```r
> f1<-function(){
+   cat("매개변수 없는 합수")
+ }
> f1()
매개변수 없는 합수
```

##### 매개변수가 있는 함수

```r
> f2<- function(x){
+   if(x%%2==0){
+     print(x)
+ }}
> f2(4)
[1] 4

> f3<-function(a,b){
+   add<-a+b
+   return(add)
+ }
> result<-f3(11,4)
> print(result)
[1] 15
```

##### repeat{반복 수행문장:반복문 탈출할 조건문 ;증감식}

```r
i<-0
> repeat{
+   
+   if(i==10){
+     break
+   } 
+   i<-i+1
+   if(i%%2==0){
+     print(i)
+   } 
+ }
[1] 2
[1] 4
[1] 6
[1] 8
[1] 10
```

##### 결과 반환 함수

- return

```r
#함수 정의하시오 (매개변수는 정수1개, 매개변수가 0이면 0을 반환
0이 아니면 매개변수의 2배의 값 반환)
> f4<-function(x){
+   if(x==0){
+     return(0)
+   }else{
+     return(2%*%x)
+   }
+ }
> print(f4(0))
[1] 0
> print(f4(3))
     [,1]
[1,]    6
> print(f4(-3))      
     [,1]
[1,]   -6


#함수를 정의하시오!(첫번째 매개변수는 벡터객체, 두번째 매개변수는 함수 타입-mean,sum,median을 문자열로 입력 받아 mean인경우 벡터의 평균 반환, sum은 벡터 요소의 합계 반환)
> f5<-function(x,y){
+   if(y=="sum"){
+     return(sum(x))
+   }else if(y=="mean"){
+     return(mean(x))
+   }else if(y=="median"){
+     return(median(x))
+   }
+ }
> nums<-(1:5)
> f5(nums,"sum")
[1] 15
> f5(nums,"mean")
[1] 3
> f5(nums,"median")
[1] 3
#또다른 방법!
> f5<-function(v,type){
+   switch(type,mean=mean(v),sum=sum(v),median=median(v))
+ }
> print(f5(nums,"mean"))
[1] 5.5
> print(f5(nums,"sum"))
[1] 55
> print(f5(nums,"median"))
[1] 5.5
```

##### 함수 내부에 함수 정의(내부 함수는 외부에서 호출 불가!)

```r
> outer<-function(x,y){
+   print(x)
+   inner<-function(y){
+     print(y*2)
+   }
+   inner(y)
+ }
> print(outer(3,7))
[1] 3
[1] 14
[1] 14
> print(inner(7))
Error in inner(7) : could not find function "inner"
> str(outer)
function (x, y)  
 - attr(*, "srcref")= 'srcref' int [1:8] 1 8 7 1 8 1 1 7
  ..- attr(*, "srcfile")=Classes 'srcfilecopy', 'srcfile' <environment: 0x000000001a417ae0> 

#내부함수는 외부에서 호출시 오류 뜨는 것을 확인한다!


> callee<-function(x){
+   print(x*2)
+ }
> caller<-function(v,call){
+   for(i in v){
+     call(i)
+   }
+ }
> print(caller(1:5,callee))
[1] 2
[1] 4
[1] 6
[1] 8
[1] 10
NULL
```

#####  전역변수, 글로벌 변수, 로컬 변수

```r
> g<-"global" # 전역 변수, 글로벌 변수
> f6<-function(){
+   loc<-"local" # 로컬 변수
+   print(loc)
+   print(g)
+ }
> f6()
[1] "local"
[1] "global"
> print(g)
[1] "global"
> print(loc)
Error in print(loc) : object 'loc' not found
# 즉 로컬 변수는 부르는 것 에러! 왜냐 로컬 변수이기 때문!
```

##### R에서 변수 검색 Scope 순서

- 함수 내부에서 검색=> 전역 메모리에서 검색 => 에러 발생

```r
> g1<-1000 # 전역 변수
> f7<-function(){
+   g1<-100  # 로컬 변수 (로컬 변수 새로 만드는 것)
+   print(g1)
+ }
> f7()
[1] 100  # 로컬 변수!
> print(g1)
[1] 1000 # 전역 변수가 결과로!


> f7<-function(){
+   g1<<-200 # <<- 하면 전역 변수 참조 ! 그렇기에 외부 호출 가능!
+   print(g1)
+ }
> f7()
[1] 200
> print(g1)
[1] 200





```

##### 클로저!

```r

> f8<-function(num1){
+   loc<-num1
+   return(function(num2){
+     return (loc+num2)# 클로저
+   })
+ }
> result.function<-f8(100)  #함수 리턴
> str(result.function)
function (num2)  # 원래는 가비지 컬렉터에 삭제되어야 하는데 return으로 인하여 삭제가 안된다 이것이 바로 클로저!
 - attr(*, "srcref")= 'srcref' int [1:8] 3 10 5 3 10 3 3 5
  ..- attr(*, "srcfile")=Classes 'srcfilecopy', 'srcfile' <environment: 0x0000000011721ec8> 
> result.function(200)
[1] 300


```

##### 위치기반, 이름 기반 파라미터 전달 방식

```r

> f9<-function(a,b,c){
+   result<-max(c(a,b,c))
+   print(result)
+ }
> 
> f9(5,3,11) #위치기반 파라미터 전달
[1] 11
> f9(c=5,a=3,b=11)
[1] 11 #이름기반으로 파라미터 전달

> f10<-function(a=3,b=6){
+   result<-a*b
+   print(result)
+ }
> f10()
[1] 18
> f10(9,5)
[1] 45
> f10(5) #a값이 바뀐다!
[1] 30
```

## 결측치가 포함된 데이터를 대상으로 평균 구하기

##### 결측치를 무조건 제거한 후 평균 구하기=>데이터 손실 발생

```r
> data<-c(10,20,5,4,40,7,NA,6,3,NA,2,NA)
> print(data)
 [1] 10 20  5  4 40  7 NA  6  3 NA  2 NA
> mean(data,na.rm=T)
[1] 10.77778

```

##### 결측치 0으로 대체후 평균 구하기

```r
> data1=ifelse(is.na(data),0,data)
> print(data1)
 [1] 10 20  5  4 40  7  0  6  3  0  2  0
> print(mean(data1))
[1] 8.083333
```

##### 결측치를 전체 변량의 평균으로 대체하여 구하기

```r
> data2=ifelse(is.na(data),round(mean(data,na.rm=T),2),data)
> print(data2)
 [1] 10.00 20.00  5.00  4.00 40.00  7.00 10.78  6.00  3.00 10.78
[11]  2.00 10.78
> print(mean(data2))
[1] 10.77833
```

## 몬테카를로 시뮬레이션

- 몬테 카를로 시뮬레이션은 현실적으로 불가능한 문제의 해답을 얻기 위해서 난수의 확률 분포를 이용하여  모의시험으로 근사적 해를 구하는 기법

* 동전 앞면과 뒷면의 난수 확률분포의 기대확률 모의시험 - 일정한 시행 횟수 이하이면 기대확률이 나타나지 않지만, 시행 횟수를 무수히 반복하면 동전 앞면과 뒷면의 기대확률은 0.5에 가까워진다.

```r
> coin<-function(n){
+   r<-runif(n,min=0,max=1)
+   result<-numeric()
+   for(i in 1:n){
+     if(r[i]<=0.5 )
+       result[i]<-0 #앞면이라 하든 뒤면이라 하든?
+     else
+       result[i]<-1# 뒷면
+   }
+   return(result)
+ }
> coin(10)
 [1] 1 0 1 0 1 0 1 0 1 0
> coin(10)
 [1] 1 1 1 1 0 0 0 1 0 0
> coin(10)
 [1] 0 1 1 1 1 0 0 1 1 0



# 몬테카를로 시뮬레이션
> monteCoin<-function(n){
+   cnt<-0
+   for(i in 1:n){
+     cnt<-cnt+coin(1)
+     
+   }
+   result<-cnt /n #동전 앞면과 뒷변의 누적 결과를 시행횟수(n)으로
+   return (result)
+ }
> monteCoin(10)
[1] 0.5
> monteCoin(30)
[1] 0.4
> monteCoin(100)
[1] 0.47
> monteCoin(1000)
[1] 0.521
> monteCoin(100000)
[1] 0.5009
```



## 기술 통계량 처리 관련 내장함수

- min(vec) 
- max(vec)
- range(vec) : 대상 벡터 범위값 반환(최소값~최대값)
- mean(vec) :평균
- median(vec) : 중앙값
- sum(vec)
- sort(x)
- order(x) : 벡터의 정렬된 값의 색인(index)을 보여주는 함수
- rank(x): 순위
- sd(x): 표준편차
- summary(x) : 기초 통계량(최소값, 등등 다양한것을 한방에)
- table(x): 빈도수
- sample(x, y) : x 범위에서 y만큼 sample 데이터를 생성하는 함수

```r
> t1<-rep(1:5,3)
> min(t1)
[1] 1
> max(t1)
[1] 5
> range(t1)
[1] 1 5
> mean(t1)
[1] 3
> median(t1)
[1] 3
> sum(t1)
[1] 45
> sort(t1, decreasing=T) # 내림차순 정렬
 [1] 5 5 5 4 4 4 3 3 3 2 2 2 1 1 1
> order(t1) # 벡터의 정렬된 값의 색인(index)를 보여주는 함수
#order는 첫 번째 인수를 오름차순 또는 내림차순으로 재정렬하여 추가 인수로 연결을 끊는 순열을 반환합니다. sort.list는 하나의 인수 만 사용하여 동일합니다. 가 번역 결과.....???? 1의 위치는 1, 6, 11에 있따는 뜻! 2의 위치는 2, 7, 12에 있다.
 [1]  1  6 11  2  7 12  3  8 13  4  9 14  5 10 15
> rank(t1) # 랭킹으로 동률의 경우 111 이므로 1,3 사이 2 등으로
 [1]  2  5  8 11 14  2  5  8 11 14  2  5  8 11 14
> t2<-rep(1:5,4)
> rank(t2) # 랭킹으로 1111 임으로 2,3등 사이의 값 2.5등으로 순위 매김
 [1]  2.5  6.5 10.5 14.5 18.5  2.5  6.5 10.5 14.5 18.5  2.5  6.5
[13] 10.5 14.5 18.5  2.5  6.5 10.5 14.5 18.5
> sd(t1)
[1] 1.46385
> summary(t1)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      1       2       3       3       4       5 
> table(t1) # 빈도수
t1
1 2 3 4 5 
3 3 3 3 3 
> sample(t1) # 조건 범위 없으면 길이만큼 생성
 [1] 4 5 4 2 4 5 2 5 1 1 3 3 1 3 2
> sample(t1,3) # 조건 있을때 조건까지!
[1] 2 5 2
> sample(t1,6)
[1] 5 4 3 4 1 1
```

## 정규분포 난수 생성

##### 정규분포(연속형)의 난수 형성 rnorm()

- rnorm(생성할 난수 개수, mean, sd)

```r
> n<-1000
> result<-rnorm(n,mean=0,sd=1)
> head(result,20)
 [1] -0.518659626  0.938813507  0.007800052  1.808197167
 [5] -2.649674144 -2.019918350 -0.835722937 -0.228234248
 [9]  0.608099010 -0.316254947  1.609989420 -0.963842402
[13]  0.341010981 -0.449625764  0.356989934  0.177982723
[17] -0.087677888  0.481810570 -0.248678607  0.951131529
> hist(result) # 정규분포 모양이 나와야 한다.
```

![1568009199249](R.assets/1568009199249.png)

```r
> rnorm(5,mean=0,sd=1)
[1]  1.7150650  0.4609162 -1.2650612 -0.6868529 -0.4456620
> rnorm(5,mean=0,sd=1)
[1]  1.2240818  0.3598138  0.4007715  0.1106827 -0.5558411
> set.seed(123)
> rnorm(5,mean=0,sd=1)
[1] -0.56047565 -0.23017749  1.55870831  0.07050839  0.12928774
> set.seed(123)
> rnorm(5,mean=0,sd=1)
[1] -0.56047565 -0.23017749  1.55870831  0.07050839  0.12928774

# 종자값(seed값이 같으면 난수 값도 같다!)
```



##### runif() 균등분포(연속형)의 난수 생성

- runif(생성할 난수 개수, min, max)
- seed값을 지정하면 동일한 난수 생성 가능

```r
> n<-1000
> result<-runif(n)
> head(result,20)
 [1] 0.04453188 0.34214735 0.92420083 0.33026058 0.01750387
 [6] 0.19461313 0.21369865 0.91756156 0.22675083 0.74739860
[11] 0.89994065 0.57883024 0.27558441 0.50661237 0.88952514
[16] 0.75827029 0.34839508 0.55427779 0.86370888 0.29365959
> hist(result)
```

![1568009431857](R.assets/1568009431857.png)

#####  rbinom() 이산변량(정수형)을 갖는 정규분포의 난수 생성

- seed값을 지정하면 동일한 난수 생성 가능
- rbinom()은 독립적인 반복 횟수와 변량의 크기, 확률을 적용

```r
> n<-20
> rbinom(n,1,prob=1/2) #0,1의 이산변량을 0.5확률로 20개 난수 생성
 [1] 0 1 1 1 1 0 0 1 0 1 0 1 0 1 1 1 0 1 1 1 #난수 20 개 생성 확인
> rbinom(n,2,prob=1/2) #0,1,2의 이산변량을 0.5확률로 20개 난수 생성
 [1] 1 2 0 2 2 2 0 1 1 1 0 0 1 1 1 1 1 1 2 1
> rbinom(n,10,prob=1/2)#1~10의 이산변량을 0.5확률로 20개 난수 생성
 [1] 4 7 3 5 2 4 3 5 7 2 6 5 5 4 6 2 4 4 7 5
> n<-1000
> result<-rbinom(n,5,prob=1/6)
> head(result,20)
 [1] 2 1 1 0 0 0 0 3 1 0 2 0 1 1 0 0 1 0 1 2
> hist(result)
```

![1568010170067](R.assets/1568010170067.png)

## 수학관련 내장 함수

- abs(x)
- sqrt(x)
- ceiling(x), floor(x), round()
- factorial(x)
- which.min(x) / which.max(x) : 벡터 내 최소값과 최대값의 인덱스를 구하는 함수
- pmin(x) /pmax(x) : 여러 벡터에서의 원소 단위 최소값과 최대값
- prod() : 벡터의 원소들의 곱을 구하는 함수
- cumsum() / cumprod() : 벡터의 원소들의 누적합과 누적곱을 구하는 함수
- cos(x), sin(x), tan(x)  : 삼각함수
- log(x) : 자연로그
- log10(x) : 10을 밑으로 하는 일반로그 함수
- exp(x) : 지수함수

```r
> x<-rep(1:5,3)
> abs(x)
 [1] 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
> sqrt(x)
 [1] 1.000000 1.414214 1.732051 2.000000 2.236068 1.000000
 [7] 1.414214 1.732051 2.000000 2.236068 1.000000 1.414214
[13] 1.732051 2.000000 2.236068
> ceiling(x)
 [1] 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
> floor(x)
 [1] 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
> round(x)
 [1] 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
> factorial(x)
 [1]   1   2   6  24 120   1   2   6  24 120   1   2   6  24 120
> which.min(x) 
[1] 1
> which.max(x) 
[1] 5
> pmin(x) /pmax(x) 
 [1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
> prod(x) 
[1] 1728000
> cumsum(x) 
 [1]  1  3  6 10 15 16 18 21 25 30 31 33 36 40 45
>  cumprod(x) 
 [1]       1       2       6      24     120     120     240
 [8]     720    2880   14400   14400   28800   86400  345600
[15] 1728000
> cos(x)
 [1]  0.5403023 -0.4161468 -0.9899925 -0.6536436  0.2836622
 [6]  0.5403023 -0.4161468 -0.9899925 -0.6536436  0.2836622
[11]  0.5403023 -0.4161468 -0.9899925 -0.6536436  0.2836622
> sin(x)
 [1]  0.8414710  0.9092974  0.1411200 -0.7568025 -0.9589243
 [6]  0.8414710  0.9092974  0.1411200 -0.7568025 -0.9589243
[11]  0.8414710  0.9092974  0.1411200 -0.7568025 -0.9589243
> tan(x)  
 [1]  1.5574077 -2.1850399 -0.1425465  1.1578213 -3.3805150
 [6]  1.5574077 -2.1850399 -0.1425465  1.1578213 -3.3805150
[11]  1.5574077 -2.1850399 -0.1425465  1.1578213 -3.3805150
> log(x) 
 [1] 0.0000000 0.6931472 1.0986123 1.3862944 1.6094379 0.0000000
 [7] 0.6931472 1.0986123 1.3862944 1.6094379 0.0000000 0.6931472
[13] 1.0986123 1.3862944 1.6094379
> log10(x) 
 [1] 0.0000000 0.3010300 0.4771213 0.6020600 0.6989700 0.0000000
 [7] 0.3010300 0.4771213 0.6020600 0.6989700 0.0000000 0.3010300
[13] 0.4771213 0.6020600 0.6989700
> exp(x) 
 [1]   2.718282   7.389056  20.085537  54.598150 148.413159
 [6]   2.718282   7.389056  20.085537  54.598150 148.413159
[11]   2.718282   7.389056  20.085537  54.598150 148.413159
```

## 행렬 연산 관련 내장 함수

- ncol(x) : x의 열(컬럼) 수를 구하는 함수
- nrow(x) : x의 행 수를 구하는 함수
- t(x) : x 대상의 전치행렬을 구하는 함수
- cbind(...) : 열을 추가할 때 이용되는 함수
- rbind(...) : 행을 추가할 때 이용되는 함수
- diag(x) : x의 대각행렬을 구하는 함수
- det(x) : x의 행렬식을 구하는 함수
- apply(x, m, fun) :  행 또는 열에 지정된 함수를 적용하는 함수
- solve(x) : x의 역행렬을 구하는 함수
- eigen(x) : 정방행렬을 대상으로 고유값을 분해하는 함수
- svd(x) : m x n 행렬을 대상으로 특이값을 분해하는 함수
- x %*% y : 두 행렬의 곱을 구하는 수식

## 데이터구조 분석 (그래프)

- 데이터 분석의 도입부 : 전체적인 데이터의 구조를 분석하거나 분석 방향을 제시

- 데이터 분석의 중반부 : 잘못된 처리 결과를 확인

- 데이터 분석의 후반부 : 분석결과를 도식화하여 의사결정에 반영하기 위해서 데이터를 시각화

- 이산변수로 구성된 데이터 셋을 이용하여 막대, 점, 원형 차트를 그릴 수 있다.

- 연속변수로 구성된 데이터프레임을 대상으로 히스토그램과 산점도를 그릴 수 있다.

- 데이터 분석의 도입부에서 전체적인 데이터의 구조를 살펴보기 위해서 시각화 도구를 사용한다.

  > 숫자형 컬럼 1개 시각화 도구 - hist, plot, barplot
  >
  > 범주형 컬럼 1개 시각화 도구 - pie, barplot (여자, 남자, 대중소 등)
  >
  > 숫자형 컬럼 2개 시각화 도구 - plot, abline, boxplot(x,y축을 나뉘는 것)
  >
  > 숫자형 컬럼 3개 시각화 도구 - scatterplot3d(3차원 산점도)
  >
  > n개의 컬럼 시각화 도구 - pairs(산점도 매트릭스)

- 이산변수(discrete  quantitative data)- 정수 단위로 나뉘어 측정할 수 있다.
  - barplot()-기본적으로 세로 막대 차트 제공
  - ylim(y축 범위), col(막대 색상) , main(제목)

## 그래프 그리기 barplot()

```r
> chart_data<-c(305,450,320,400,330,480,380,520)
> names(chart_data)<-c("2014 1분기",  "2015 1분기"
+                     , "2014 2분기","2015 2분기"
+                     , "2014 3분기","2015 3분기"
+                     , "2014 4분기","2015 4분기")
> str(chart_data)
 Named num [1:8] 305 450 320 400 330 480 380 520
 - attr(*, "names")= chr [1:8] "2014 1분기" "2015 1분기" "2014 2분기" "2015 2분기" ...
> print(chart_data)
2014 1분기 2015 1분기 2014 2분기 2015 2분기 2014 3분기 2015 3분기 
       305        450        320        400        330        480 
2014 4분기 2015 4분기 
       380        520 
> barplot(chart_data,ylim=c(0,600),col=rainbow(8),
+         main="2014년도 VS 2015년도 분기별 매출현황 비교",
+         ylab="매출액(단위:만원)",xlab="년도별 분기현환")
```

![1568011864902](R.assets/1568011864902.png)

##### 가로막대 차트( horiz=TRUE)



```r
barplot(chart_data, ylim=c(0, 10), horiz=TRUE,  col=rainbow(8), ## 혹은 ylim삭제
        main="2014년도 VS 2015년도 분기별 매출현황 비교",
        ylab="매출액(단위:만원)", xlab="년도별 분기현황")
```

![1568012938079](R.assets/1568012938079.png)

##### 막대의 굵기와 간격 설정 : space

- space(값이 클수록 막대의 굵기는 작아진다.)
- 축 이름 크기 설정 : cex.names

```r
barplot(chart_data, ylim=c(0, 600), horiz=TRUE, ## 혹은 ylim삭제
       main="2014년도 VS 2015년도 분기별 매출현황 비교",
        ylab="매출액(단위:만원)", xlab="년도별 분기현황"
        , space=2, cex.names=0.8, col=rep(c(2, 4), 4))
```

![1568013046832](R.assets/1568013046832.png)

##### 색상 index값 : 검은색(1), 빨간색(2), 초록색(3), 파란색(4), 하늘색(5), 자주색(6), 노란색(7)

```r
barplot(chart_data, ylim=c(0, 600), horiz=TRUE,  ## 혹은 ylim삭제
       main="2014년도 VS 2015년도 분기별 매출현황 비교",
        ylab="매출액(단위:만원)", xlab="년도별 분기현황"
        , space=5, cex.names=0.5, col=rep(c(1, 7), 4))

```

![1568013113856](R.assets/1568013113856.png)

##### VAdeaths 데이터셋

- VADeaths 데이터셋은 1940년 미국 버지니아주의 하위계층 사망비율을 기록한 데이터셋

```r
> data(VADeaths) 
> str(VADeaths) # 5행4열인지 확인
 num [1:5, 1:4] 11.7 18.1 26.9 41 66 8.7 11.7 20.3 30.9 54.3 ...
 - attr(*, "dimnames")=List of 2
  ..$ : chr [1:5] "50-54" "55-59" "60-64" "65-69" ...
  ..$ : chr [1:4] "Rural Male" "Rural Female" "Urban Male" "Urban Female"
> class(VADeaths) 
[1] "matrix"
> mode(VADeaths)
[1] "numeric"
> head(VADeaths, 10)
      Rural Male Rural Female Urban Male Urban Female
50-54       11.7          8.7       15.4          8.4
55-59       18.1         11.7       24.3         13.6
60-64       26.9         20.3       37.0         19.3
65-69       41.0         30.9       54.6         35.1
70-74       66.0         54.3       71.1         50.0
```

##### 범례 출력

- `legend(좌표 위치, 범위, cex=크기, fil=색 채우기)`

```r
par(mfrow=c(1,2))
barplot(VADeaths,beside=T,col=rainbow(5),
        main="미국 버지니아주의 사망비율")
legend(19,71, c("50-54","55-59","60-64","65-69","70-74"),
       cex=0.5,fil=rainbow(5))
```

![1568013851067](R.assets/1568013851067.png)

##### 누적막대 차트 

- `beside=F`

```r
barplot(VADeaths,beside=F,col=rainbow(5))
title(main="미국 버지니아주의 사망비율",font.main=4)
legend(3.8,180, c("50-54","55-59","60-64","65-69","70-74"),
       cex=0.5,fil=rainbow(5))

```

![1568014042171](R.assets/1568014042171.png)

##### 그래프 관련  다양한 요소 지정 

```r
#beside=T/F : X축 값이 측면으로 배열, F이면 하나의 막대에 누적
#font.main : 제목 글꼴 지정
#legend() : 범례 위치, 이름, 글자 크기, 색상 지정
#title() : 차트 제목, 차트 글꼴 지정
```

##### 점의 모양, 색상 설정, 선 색상등

```r
?plot # 점의 모양, 색상 설정 가능
"p" for points,
"l" for lines,
"b" for both,
"c" for the lines part alone of "b",
"o" for both ‘overplotted’,
"h" for ‘histogram’ like (or ‘high-density’) vertical lines,
"s" for stair steps,
"S" for other steps, see ‘Details’ below,
"n" for no plotting.
```

```r
#rables 점에 대한 설명문
#cex : 점의 확대
#pch: 점 모양 원(1), 삼각형(2),...
#color: 점 색상
# lcolor: 선 색상
```

![1568014698597](R.assets/1568014698597.png)

```r
par(mfrow=c(1,1))
dotchart(chart_data,color=c("blue","red"),lcolor="black",
         pch=1:2,labels=names(chart_data),xlab = "매출액",
         main="2014년도 VS 2015년도 분기별 매출현황 비교",
         cex=1.2)
```

![1568014643134](R.assets/1568014643134.png)

## pie 차트(분포도 확인시 good)

```r
pie(x, labels = names(x), edges = 200, radius = 0.8,
    clockwise = FALSE, init.angle = if(clockwise) 90 else 0,
    density = NULL, angle = 45, col = NULL, border = NULL,
    lty = NULL, main = NULL, ...)
```

```r
par(mfrow=c(1,1))
pie(chart_data,col=rainbow(8),
         pch=1:2,labels=names(chart_data),
         main="2014년도 VS 2015년도 분기별 매출현황 비교",
         cex=1.2)
```

![1568014959942](R.assets/1568014959942.png)

## 연속변수(boxplot)

- 연속변수(Continuous quantitative data)는 시간, 길이 등과 같이 연속성을 가진 변수
- boxplot은 요약 정보를 시각화하는데 효과적
- 데이터의 분포 정도와 이상치 발견을 목적으로 하는 경우 유용하게 사용
- boxplot(VADeaths, range=0) #컬럼의 최대값과 최속밧을 점선으로 연결

```r
boxplot(VADeaths,range=0)
```

![1568015132049](R.assets/1568015132049.png)

##### notch=T (허리선 비교)

- 중위수(허리선 비교)

```r
boxplot(VADeaths, range=0, notch=T )
```

![1568015310103](R.assets/1568015310103.png)

##### abline() : 기준선 추가(선 스타일, 선 색상)

```r
abline(h=37, lty=3, col="red")
```

![1568015361306](R.assets/1568015361306.png)

## 히스토그램

- 측정값의 범위(구간)를 그래프의 x축으로 놓고, 범위에 속하는 측정값의 출현 빈도수를 y축으로 나타낸 그래프 형태
- 도수의 값을 선으로 연결, 분포곡선을 얻는다.

```r
> data(iris)
> names(iris)
[1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width" 
[5] "Species"     
> str(iris)     #
'data.frame':	150 obs. of  5 variables:
 $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
 $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
 $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
 $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
 $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ...
> head(iris)
  Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa
```

##### 붓꽃 3종류의 관측 데이터 

- Sepal.length, Sepal.Width(꽃받침)
- Petal.length,Petal.Width(꽃잎)

```r
> summary(iris$Sepal.Length)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  4.300   5.100   5.800   5.843   6.400   7.900 
> summary(iris$Sepal.Width)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  2.000   2.800   3.000   3.057   3.300   4.400 
> hist(iris$Sepal.Length,xlab="iris$Sepal.Length",
+      col="magenta",main="꽃받침 길이histogram",xlim=c(4.3,7.9))
```

![1568016487177](R.assets/1568016487177.png)

##### 빈도수로 히스토그램 그리기

```r
par(mfrow=c(1,2))
hist(iris$Sepal.Width,xlab = "iris$Sepal.Width",
     col="green",main="꽃받침 넓이 histogram",xlim=c(2.0,4.5))
```

![1568016617699](R.assets/1568016617699.png)

##### 확률 밀도로 히스토그램 그리기

```r
hist(iris$Sepal.Width,xlab = "iris$Sepal.Width",
     col="mistyrose",freq=F,
     main="꽃받침 넓이 histogram", xlim=c(2.0,4.5))
```

![1568016760506](R.assets/1568016760506.png)

##### 밀도를 기준으로 분포 곡선 추가

```r
lines(density(iris$Sepal.Width), col="red") # col="red"를 추가하면 색이 바뀐다.
```

![1568016977201](R.assets/1568016977201.png)

##### 정규분포 곡선 추가

```r
x<-seq(20,4.5,0.1) #by 값이 잘못 됐다 뜨므로 0.1제거하면 오류는 생기지 않는다.
curve(dnorm(x,mean=mean(iris$Sepal.Width),sd=sd(iris$Sepal.Width)),
      col="blue",add=T)
```

![1568017011382](R.assets/1568017011382.png)

## 산점도(scatter plot)



