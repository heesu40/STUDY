# R

- 데이터 분석을 위한 통계및 시각화를 지원하는 자유 소프트웨어 환경

- R은 컴퓨터 언어이자 다양한 패키지 집합

- **객체지향 프로그래밍 언어**

- data의 시각화를 위한 다양한 그래픽 도구 제공

- 모든 객체는 메모리로 로딩되어 고속으로 처리

  

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



