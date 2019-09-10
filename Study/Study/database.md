원래는 파일시스템으로 데이터를 관리했다.

프로그램 언어로 처리하기에 프로그램에 종속적이고 다양한 프로그램 관리시 중복 항목은 각각 다르게 저장되어 나중가면 불일치성이 커지게 된다. 또한 프로그램 개발 생산성이 나쁘다.

그렇기에 통합된 데이터 관리가 필요하게 되었다. 이런 필요에 의해서 등장한 것이 데이터베이스!

데이터베이스는 동시 공유와 실시간 접근성이 좋다. 내용에 따른 참조도 가능하다(검색기능)

## Database

- 2가지 유형이 있는데 Business 또는 User, Meta Data의  데이터로 저장된다.

## DBMS(Database와 다르다)

- database 관리하는 프로그램.(프로그램이기에 메모리가 있으며 database를 관리하기 위한 다양한 프로세스가 존재한다.) Memory+process , 데이터베이스의 무결점성을 보장한다.

- 계층구조가 가장 단순한 프로세스(계층형 DBMS) 

  - 여러 데이터에 의해서 참조가능.
  - 참조관계가 1:多
  - 참조하기위해서는 물리적 포인터가 필요했으며 이것은 관리가 어려웠다. 수정시 모든 물리적 포인터를 수정해야했다.

- 망형DBMS

  - 여러 데이터로부터 참조가능
  - 참조관게 多:多

- 상용DB인 RDBMS(관계형 DBMS)

  - 1970년 EF CODD 의 논문 이후 지금까지 사용 
  - 표준 언어 SQL
  - RDBMS에서는 table이라는 단어는 사용한다.(entity(관리대상)를 table로 사용)
  - 식별자 =primary key(not null unique)
  - 참조키=외래키(foreign key). 포함되어있지 않지만 외부에서 참조되어 추가

  - 고정된 구조를 가진다. 미리 표준화를 하기 때문에 초반부터 설계를 잘 해야한다.(정형 schema 구조)

  - 주요 목적-Transaction 처리다(분리되서 처리될 수 었는 작업 단위)

    - Tx = Unit Of work (작업단위로 원자성을 가져야 한다. 쪼개서 사용 못함)

      - 영속성을 주어야 한다(삭제하고 다시 켜도 이전작업을 갈 수 있어야 한다.) commit;
      - 작업 시 문제가 생겼을 때 다시 돌아가는 rollback;
      - **TCL**!!!!!이라 한다.

    - ex)이체 : A에서 만원 인출, B에게 주어야 할 때 

      - 변경 입장에서는 A에서 B에서 두번 update되어야 한다.
      - 그렇기 때문에 A가 수행되다 문제가 생기면 초기화 하는 작업이 필요하다 이것이 원자성!(...?)

    - ex)온라인 쇼핑 : 결제(insert) , 재고량 변경, 배송정보 추가, 고객구매history,  이런것 중 하나가 문제가 생길시 초기화 시키는 것이 필요하다.

      

- 객체지향 DBMS
  - 1980이후
  - 검색이 주요 목적이지만 추가도 되며 수정도 된다.
  - 사용자 정의 타입를 RDBMS에 추가하여 ORDBMS라 하여 사용하였다.
- 2000년대 쯤에는 web data를 추가
- no SQL =>가변 schema 구조다.
  
  - RDBMS의 표준언어인 SQL를 알아야 한다.
  
- 계층형-망형-관계형-객체관계형-클러스터 순서로 진화했다.

### 용어

Table=/entity(record 집합)

- Column(속성)+Row(Record)

- Row=/Record=/Tuple(속성값 모음)

- Column-=/Attribute(속성)

Primary Key -Not Null + Unique

Foreign Key- 참조관계(Parnent 테이블의 PK를 참조하는 child 테이블의 외래키)

null- 아직 값이 할당되지 않음을 의미, 0 아니며, " "와 다르며 산술 연산 결과는 null,비교연산(=,!=,>)결과는 null,논리연산 결과도 null 

- 이를 변환하기 위해 nul(컬럼, null일때 리털할 값)을 이용해 변환후 처리해야 한다.

###  DML

- DML - DQL(검색) Select~
  - 추가 Insert~
  -  수정 Update~
  - 삭제 Delete~

### DDL(데이터 구조)

- table
- View
- Index
- Sequence
- 생성 Creat~
- 변경 Alter~
- 삭제 Drop~
- truncate
- rename
- comment
- table 저장소 관리 truncate(테이블에만 있는 명령어)

### DCL

- DBMS보안 기능 
  - 인증(예로 로그인 같은)
  - 권한을 통해서 제어 Grant~(주는 것) revoke~(권한 삭제)

### TCL 

- 트랜젝션 데이터의 영구 저장, 취소 등과 관련된 명령어
- commit ~ 저장
- rollback ~취소
- savepoint ~ 

### 검색(SQL내부 돌아가는 구조), DB수행방식

- service process가

  1. syntax checking (문법 체크)
  2. library cache 검색 (동일한 SQL context정보 있으면 실행- 응답 진짜 빠름)
     - 두개를 soft parsing 이라 한다.
3. semantic checking(I/O BLOCK를 이용),Meta정보 이용
  4. optimizer(내부적으로 호출이 되어 객체 통계정보를 이용하여 경로선택(네이게이션의 경우)) 실행하여 service process로 리턴, Meta정보를 이용해 최적의 비용 실행계획
  5. library cashe에 저장
  6. 실행-Row Lock설정(배타적)-허나 이 값은 취소가 될 수 있다.
     - undo data(변경전 데이터)를 undo segnent에 저장
     - Redo date를 기록를 log buffer에 저장 -db인스턴스에 장애발생시 다시 실행위해 
     - memory buffer에 변경 (이 과정은 rollback때문에 있는과정)

### SQL

- 관계형 데이터베이스에서 데이터 조작과 데이터 정의를 하기 위해 사용하는 언어
- 표준 언어
- 선언적 언어
- 결과 중심 언어
- **sql문장의 키워드와 테이블명, 컬럼명등은 대소문자 구별 안한다. 그러나 컬럼값은 대소문자 구별한다.**

### 프로그램 언어

- 절차적(과정 기술)

## Select

- table 컬럼(열)기준 , projection
- table row(행)기준 ,selction
- 2개 이상의 table이 대상이 되며 공통 속성값을 기준으로 row를 결합하여 가져오는 검색방법, join

### Sqlplus 툴

- sql 실행, 결과 보여주는 환경 제공

- 명령어 - 세미콜론(;)사용 가능, 명령어 축약 사용 가능

- sql 문은 명령어 축약 불가, 반드시 한 문장은 세미콜로(;)으로 종료

- ```sql
  conn scott/oracle
  describe emp      -- 테이블 구조 조회
  desc dept 
  ```

![1559182595887](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1559182595887.png)

- NOT NULL인 NUMBER는 반드시 저장되어야 하며 SAL의 NUMBER<7,2>는 정수값은 5개 소수값은 2개란 뜻
- char(1) ~2000byte
- varchar2(1) ~4000byte 문자 저장가능
- number 타입 binary형식으로 정수, 실수 저장가능
- date 날짜를 7byte를 사용해서 수치값으로 저장 ((__세기, __년도 __월 __일 __시 __분 __초))
- select sysdate from dual ; -- 시스템 현재 시간을 리턴하는 함수(시, 분 ,초는 안나온다.)

![1559183020867](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1559183020867.png)

- ```sql
   alter session set nls_date_format ='YYYY/MM/DD HH24:MI:SS';
  alter session set nls_date_format='DD-MON-RR';
--   결과값은 01-jun-94
  ```
  
- 이것으로 변경 가능하지만 만약 세션을 종료한 후에 다시 시작하면 세션의 기본 날짜 출력 형식으로 변경 ,세션에 설정된 기본 날짜 출력 형식은  RR/MM/DD이다.
  
  - exit; ---db disconnection. 세션 종료!





### 컬럼타입과 사용 가능한  연산자

- 컬럼 연산자 값
- expression [as]alias(별칭)->Colum title Rename

- number타입 컬럼( number(p,s))은 산술연산(+,-,*,/) 
- char(size)/varchar2 타입 컬럼은 문자열 결합: ||  결합연산자

- date 타입컬럼 : date+n(정수), date-n, date-date, date±1/n
- timestamp , timestamp with timezone 등
- interval year to month, interval day to second
- select sal+100, sal-100, sal*2
  - 원래의 자료가 아닌 중간 block에 저장된 정보를 이용하기에 원본 내용에 지장 없다.
- 데이터가 추가될때 입력되지 않는 컬럼값은 null이다.
- 산술시 null 결과는 항상 null이며 모든 DBMS에서는 null아닌 값으로 변환해주는 내장 함수 제공
- nvl(column, null일때 리턴값)
- null은 비교연산, 논리연산 모두 null이 결과
- 문자, 날짜 데이터는 반드시 '   ' 를 사용해서 표현, 처리
- 날짜 데이터 세션에 설정된 포맷 형식하고 일치해야 한다.('RR/MM/DD')
- **select~ from**절이 필수절이다.
- 단순계산 결과, 함수 결과, 데이터 출력 등은 dual테이블을 사용한다.
  - desc dual
  - select*from dual

### 연산자

- 모든표의 값을 표현 하기 위해서는 `select*from emp;`
- select ename, sal, job, deptno from emp; 조회할 칼럼 순서는 맞추지 않아도 된다.

### distinct

`select distinct deptno from emp;`

- hashing 방식사용으로 중복값 제거
- 특징이 select바로 뒤에 써야 한다.(모든 칼럼 앞에)

### as

`select sal, comm,(sal+nvl(comm,0))*2 as salary
from emp;`

- --as를 하면 식이 아닌 이름으로 바뀐다.

#### ||

- 하나의 문자열로 결합할 수 있다.
- `select ename||' works as ' ||job
  from emp;` || 사이에 문자를 넣어 줄 수 있다.

#### 따옴표

`select '''A'''
from dual;
select q'['A']'
from dual;`

- 따옴표가 나오게 하고 싶을때 ,결과값은 둘다 ' A '가 된다.

#### 형변환

`select 10||10 from dual;
select '10'+'10' from dual;`

- 위의 값의 결과는  1010 아래의 값은 20 이 나온다. sql 이 연산자에 의해 값 알아서 형변환해서 계산한다. 위의 연산자는 문자 연산자이기에  문자로 아래는 산술연산자이기에 산술로.

### 날짜

- sysdate,sysdate+1/24,sysdate+5/1440

![1559209594604](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1559209594604.png)

- 위의 결과값이다. sysdate는 현재날짜, 1/24는 한시간  1/1440는 1분 1/86400 이 된다.
- 세션은 날짜만 받기에 시간까지 보려면 위의 형식대로 세션 format를 변경해주어야 한다.

```sql
--current_date() 세션의 timezone기반 현재시간을 date타입으로 리턴
--current_timestamp() 세션의 timezone기반 현재시간을 timestamp타입으로 리턴
select   sysdate, current_date, current_timestamp
from dual;

add_months(date, n)  -- 개월 수를 더한 날짜가 리턴

months_between(date, date) -- 사이 기간을 리턴

next_day(date, '요일명')
select next_day(sysdate, '목')
from emp;--다음에 오는 요일의 날짜를 리턴해준다.

last_day(date)
select last_day(to_date('14/02/14')), last_day(to_date('2000/02/14'))
       , last_day(to_date('2100/02/14'))
from dual;

last_day(date)
select last_day(to_date('14/02/14')), last_day(to_date('2000/02/14'))
       , last_day(to_date('2100/02/14'))
from dual;--각 달의 마지막 날짜를 리턴해 준다.

select sysdate, to_char(sysdate,'YYYY"년" MM"월"DD"일" DY')--허용되지않는 글자 추가위해서 ""사이에입력
from dual;-- 결과값은 19/05/30, 2019년 05월30일 목 (작성시의 날짜)
```



```sql
timestamp컬럼 타입 (YYYY/MM/DD HH24:MI:SS.SSSSSSSSS)
timestamp(3)  --6이 default (0)인 경우에는 6자리로나온다.
timestamp with time zone
```

- RR의 년도 표시의 경우 아래의 표의 규칙을 따른다.
- YY의 년도 표시의 경우 현재의 세기20YY의 년도로 본다.

|       | 0~49                                | 50~99             |
| ----- | ----------------------------------- | ----------------- |
| 0~49  | 같은 세대로 본다(1900년대 2000년대) | 전 세대로 본다    |
| 50~99 | 후 세대로 본다                      | 같은 세대로 본다. |



## 문자형식

```sql
select to_char(123456.789, '$9,999,999,9999')
from dual;
select to_number('$1,234,567.999','99,999,999.9999')
from dual;--달러의 유무가 문제가 된다
select to_number('$1,234,567.999','$99,999,999.9999')
from dual;--이정도 다른점은 알아서 처리 한다.
```



## substr,instr

- 문자를 잘라서 출력할 경우와 문자열의 개수를 세는 것으로
- substr(문자열,시작위치, 갯수)-문자열 추출
  - substr(문자열,시작위치)-시작위치 부터 끝까지 추출
- instr(문자열,시작위치,몇번째에서 리턴할 것인가) -- 결과값은 위치값으로

```sql
select substr('today is 2015년 4월 26일',1,5),
substr('today is 2015년 4월 26일',10,5),
substr('today is 2015년 4월 26일',15),
substr('today is 2015년 4월 26일',-3,2)--  -는 뒤에서 센다
from dual;
--결과값 today  , 2015  , 4월 26일 , 26
select instr('korea is wonderful','o'),
        instr('korea is wonderful','o',1,2),
        instr('korea is wonderful','o',9),
        instr('korea is wonderful','x')
from dual;
-- 결과값 1, 2, 11, 11, 0  참고로 값이 없는 경우 null이 아닌 0으로 나온다.
```



## lpad, rpad

`lpad : left padding,  
rpad : right padding`
문자열로 변환, 문자열 전체 길이내에 왼쪽 공백 또는 오른쪽 공백에 특정 문자를 padding

```sql
select 'HI,apple',
    lpad('HI,apple',10,'#') as lpad,
    rpad('HI,apple',10,'*') as rpad,
    lpad('HI,apple',10)as lapd1,
    rpad('HI,apple',10)as rpad1 from dual;
```



## trim, ltrim,rtrim,replace

- 문자를 제거하거나 변경할 때 사용

```sql
select length('  hello  '),  length(trim('  hello  '))
from dual;

select trim('H' from 'Hello wonderful'), trim('l' from 'Hello wonderful')
from dual;--양끝의 문자를 제거 결과 값은 ello wonderful  Hello wonderfu

select ltrim('Hello wonderful', 'He' ), rtrim( 'Hello wonderful' , 'ful')
from dual;--방향에 맞는 글자가 사라진다.

select replace('Jack AND Jue', 'J', 'BL')
from dual;--결과값은 BLack AND BLue
```

## translate

```sql
select translate('jack and jue','j','bl') from dual;
--결과값은 back and bue 앞뒤 같은 갯수만큼 바뀐다.
select translate('1111jack','+.0123456789',' ') from dual;
--결과값 jack
select translate('1111jack','0123456789'||'1111jack','0123456789')from dual;
--결과값 1111
```

## where절 연산자

- null은 연산자 못씀으로 is null과 is not null연산자 사용

  - null 은 '현재 무슨 값인지 확정되지 않은 상태' 혹은 '값 자체가 없는 상태' 이므로 연산자와 null을 결합할시 연산결과값이 모든것이 null이 될 수 있다. null은 무한대와 같은 의미이다.
  - null+100=null
  - null>100=null 

  ```sql
  select*from emp
  where comm=null;--결과는 아무것도 나오지않는다.
  
  selectselect*from emp
  where comm is null; --is null 연산자를 사용해서 null데이터를 출력한다.
  ```

  

- in 리스트 연산자 : in(값,값,값) 문장일 경우 '   ' 에 넣어준다. 

  - like '%,_': 문자 패턴 비교 연산자 `  like '%,_'
    - %는 문자 종류는 모든 문자, 개수는 0~m
    - _는 문자 종류는 모든 문자, 개수는 1을 의미한다.
    - _,%를 문자그대로 찾고 싶으면  escape  사용한다.
    
    ```sql
    select*from emp
    where like '_A%';
    select*from emp
    where not like '_A%'; 
    select*from emp
    where ename like 'A\_A%' escape '\'; // '\'를 이스케이프로 지정하므로 그 뒤에 오는  _ 를 문자로 인식한다.
    ```
    
    

- 논리연산자  not, and, or

- 범위연산자 between 하한값 and 상한값(순서 바뀌면 안된다.)

- order by절에는 컬럼 표현식, 별칭, 컬럼 포지션을 사용할 수 있다.

- =, >, <=, >=, !=, <> 

  ``` 
  order by 컬럼;
  order by 표현식;
  order by 별칭;
  order by 컬럼포지션(colunm position);
  ```

  

  

## 조건 검색

- 검색 방법
  - Projection
  - selection
  - join


employees, emp - 사원정보
departments, dept - 부서정보

ex) 사원이름, 부서번호, 부서이름

- oracle join syntax -- where절에 조인조건 선언

- sql1999 표준 syntax-- from 절에 조인조건 선언

- 조인 종류
  - equi join (inner join, 등가조인)
  - non-equi join(비등가조인)
  
  ```sql
  select*from emp a, salgrade b
where a.sal between b.losal and b.hisal;-- 범위를 이용한 조인이다. 이떄는 between을 사용해 준다.
  ```
  
  
  
  - self-join (자기참조가 가능한 테이블에서만)
  
  ```sql
  select a.empno,a.ename,a.mgr
  , b.empno ,b.ename from emp a, emp b where a.mgr=b.empno;
  --테이블 두개를 만들어 뽑아내는 방법. 같은 테이블에 별칭만 다르게!!
  ```
  
  
  
  - 조인 조건을 잘못 정의하거나 , 조인 조건을 누락하면 cartesian product (cross join)
  
- outer join (조인컬럼값이 null인 경우 결과집합에 포함시키기 위한 조인)
  
  ```sql
  select a.empno,a.ename,a.mgr,b.empno,b.ename
  from emp a, emp b where a.mgr=b.empno(+) order by a.empno ;--왼쪽 외부조인(왼쪽의 null값도 모두 출력)
  
  select a.empno,a.ename,a.mgr,b.empno,b.ename
  from emp a, emp b where a.mgr(+)=b.empno order by a.empno ;--오른쪽 외부조인(오른쪽의 null값도 모두 출력)
  ```
  
  
  
- empno 사번s

- ename 이름

- job 직무

- hiredate 입사날짜

- comm 커미션

- deptno 부서번호

- sal급여

- mgr 관리자번호 

- 원래 정보는 heap메모리에 정렬없이 저장되어 있는데, 메모리에 불려져 buffercache에 의해 함수처리되어 pca..?에서 정렬된다.

```sql
select~ *|[distinct] column.....| expression [as] Alias --허용치 않은 문자열의 경우 "" 사용
from~
[where 필터 조건]
[group by 컬럼]
[having 조건]
[order by 정렬기준컬럼 정렬방식]--asc오름차순 default, desc내림차순
```

## 단점

- 조건처리 함수로 제공
  - 함수는 SQL를 더 강력하게 사용하도록 보조
- 반복처리=>table의 행 단위 반복처리,명시적 for**x** while**x** exception처리 **x** 변수사용 **x**



## 함수

- predefine=>DB벤더 NVL,sysdate,user.....
- custom(pL/SQL)
- 단일행 함수(하나의 행에 하나의 결과값)는 1개의 결과리턴해야한다.
- 복수행 함수(그룹 함수)도 1개의 결과를 리턴한다.(어떤 함수든 1개의 값을 리턴한다)
- 분석함수(window)함수 
- 함수는 종류가 다양
  - Character
  - Number
  - Date
  - null처리, 기타
  - Conversion함수
    - to_date() 등등
  - round 반올림 
- date function
- 변환함수는 to_date, to_char, to_number 등등 과 같이 to로 시작하는 경우가 많다.
  - hiredate='14/02/14' 의 경우  오라클은 자동으로 hiredate를 문자열로 변환하여 값과 비교를 하게 된다.\

## 함수 종류

- initcap(),lower(),upper()
- length()-문자 길이 lengthb()- 문자 길이 byte
- `select concat(concat(ename, ' is '), job)
  from emp;` concat는 문자열을 결합하는 것으로 가로 안의 내용부터 처리한다.
- round(값,반올림 위치) 반올림

```sql
select round(12.345, 2), round(12.345, 0), round(12.345, -1)
from dual;-- 결과는 12.35   12   10
```



- trunc()  버림

```sql
select trunc(12.345,2),trunc(12.345),trunc(12.345,-1)
from dual;-- 결과는 12.34  12   10 
```



- mod() 나머지

```sql
select mod(99,4), mod(11,5) from dual;--결과는 3   1
```



- ceil()가장 가까운 큰 정수
- floor()가장 가까운 작은 정수
- power()  제곱

#### null처리 조건 처리

- nvl(컬럼, 바꿀 표현)  컬럼과 바꿀 표현이 동일한 타입이어야 한다.
- nvl2(컬럼, 표현1, 표현2) 표현1,2가 동일한 타입이어야 한다.
  - 컬럼 이 null아니면 표현1 null이면 표현2
- coalesce(컬럼,표현1,표현2....) 함수의 파라미터 값에서 null이 아닌값을 리턴하고 함수는 종료한다.
- nullif(표현1,표현2) 표현1,2이 동일한 타입이어야 한다. 표현 1=표현2이면 null리턴하고 다르면 표현1을 리턴한다.

#### 조건처리 함수

- decode 함수  decode(column, 표현1, 리턴값1, 표현2, 리턴값2.....)

- 조건은 작은 수부터 해야한다. 

```sql
select sal, deptno,sal,
decode(deptno , 10, sal*1.05
                ,20, sal*1.1
                ,30,sal*1.03 , sal+100) "increase"-- 증가 값을
from emp; --singlow함수다.

 select sal, deptno,sal,
 decode(trunc(sal/1000) ,0,0
                        ,1,sal*0.05
                        ,2,sal*0.1
                        ,3,sal*0.15
                        ,sal*0.2) "세금" from emp;--조건식을 쓸 수 없다.표현식에 주의하자
```

조건처리 표현식, 표준 sql3 :case[표현식] when [값|조건표현식] then 값 [else 값] end

```sql
select sal, deptno,sal,
case deptno when 10 then sal*1.05
            when 20 then sal*1.1
            when 30 then sal*1.03 else sal+100 end "increase"
from emp;-- end는 마지막에 반드시 써주어야 하며 가로가 필요 없다!

select sal,ename,deptno,
case  when sal>=4000 then sal*0.2
        when sal>=3000 then sal*0.15
        when sal>=2000 then sal*0.1
        when sal>=1000 then sal*0.05 else sal*0 end "세금" from emp;-- case와 when사이에 컬럼명을 넣지 않아야 조건식을 넣을 수 있다.
```



### 그룹 함수

그룹핑된 행 집합, 테이블의 전체 행 집합의 컬럼이 함수의 인수로 전달되고 결과는 반드시 1개 리턴

`sum(number 타입|expression)`

`avg(number타입|expression)`

`min(number,char,date 컬럼타입 | expression)`

`max(number,char,date,컬럼타입 |expression)`

`count([all or distinct]number, char, date 컬럼타입 |expression)` :null이 아닌 값(행) 개수 리턴

- `count(*)` 테이블의 전체 행수를 리턴, 내부적으로는 not null 또는 PK 제약조건이 선언된 컬럼을 기준으로

`stddev(number타입 |expression) `:표준편차

`variance(number타입|expression)` :분산

`conn scott/oracle`

- 이중 날짜, 숫자, 문자 데이터유형에 사용 가능 함수는 min, max,count

- 모든 그룹함수는 null을 함수 연산에 포함하지 않는다.

```sql
select sum(sal),avg(sal),max(sal),min(sal) from emp;
select count(*), count(empno) from emp;-- count는 특이하게 * 사용 가능, 또는 key사용
select max(hiredate) as "신입", min(hiredate)as "왕고" from emp;
select max(ename), min(ename) from emp;
select count(distinct deptno) from emp;
select count(comm) from emp;-- null은 count하지 않습니다.
select avg(comm), sum(comm)/count(*) from emp;--avg는 null을 제외한 명수로 평균을 구한다.

select deptno,avg(sal) from emp;--오류!!!!!!!!!!그룹함수는 여러행이 결과로 나오는 열과 같이 실행 못한다.
select deptno,avg(sal)
from emp group by deptno; --이건 가능하다 deptno를 그룹으로 평균이 각각 구해진다.
select avg(sal) from emp group by deptno;--group by절은 select문에 선언 안되도 된다.
```

## group by

- group by 절은 column명만 선언 가능.

- group by 컬럼명, 컬럼명 ... 하면 순서대로 그룹화된다.

- group by 조건은 having절에 써야 한다.

- 그룹함수를 적용한 컬럼과 그룹함수를 적용하지 않은 컬럼이 select절에 선언될 경우 group by절에 그룹함수를 적용하지 않은 컬럼을 반드시 선언해 줘야 한다. 그렇지않으면 오류 행 갯수가 맞지 않기 때문에

  ```sql
  select deptno,count(deptno),sum(sal) --4 --5가 되면 그룹함수에 대한 조건을 where에 쓸 수 없음으로 그룹함수 조건은 having 절에 작성한다.
  from emp --1
  where ~	--2
  group by deptno  --3
  having count(deptno)<4;--4
  order by 컬럼 정렬방식--6
  ```

  


## 검색방법

## projection,join, selection,join

- join 하나 이상이ㅡ 테이블에서 동일한 속성의 컬럼값이 일치할때 테이블의

1. inner join = equi join (행수가 같은 경우)
2. non-equi join(행수가 다른 경우)
3. self join(자기참조가 가능한 테이블에서만)
4. outer join 일치하는 조인컬럼값이 없건, 조인컬럼값이 null인  row 결과로 생성하려면
5. cartesian product -조인 조건을 생략하거나, 조인 족너을 논리적으로 잘 못 정한 경우  두 테이블의 모든 row가 한번씩 join되는 경우

#### 오라클에서 지원하는 sql1999 조인 구문

- 초기 오라클에서는 where 조인조건 을 이용했다.

1. `from tab1 a natural join tab2 b `(동일한 이름의 컬럼이 있는경우 , 허나 같은 행이지만 이름이 다른 컬럼은 안되며 타입이 다른 경우에는 안된다.

2. `from tab1 a join tab1 a using (조인컬럼명)`  다양한 컬럼이 있는 경우 딱 하나랑만 조인한다.

3. `from tab1 a join tab2 a on a.col=b.col2` 

4. `from tab1 a join tab1 a on a.col=b.col2`

   `from tab1 a join tab1 a on a.col=b.col2`  select조인하는 경우..........?

5. 부서번호가 null 인 사원데이터를 조인 결과에 포함하려면

   ```sql
   select e.ename, e.deptno, d.dname
   from emp e cross join  dept d
   where e.deptno =d.deptno(+);
   
   select e.ename, e.deptno, d.dname
   from emp e left outer join dept d  on e.deptno = d.depto;
   ```

6. ```sql
   --소속 사원이 없는 부서정보를 조인 결과에 포함하려면
   select e.ename, e.deptno, d.dname
   from emp e, dept d
   where e.deptno(+) = d.deptno;
   
   select e.ename, e.deptno, d.dname
   from emp e right outer join dept d on e.deptno = d.deptno;
   
   ```

7. ```sql
   --부서번호가 null인 사원데이터와 소속 사원이 없는 부서정보를 조인 결과에 포함하려면
   select e.ename, e.deptno, d.dname
   from emp e, dept d
   where e.deptno(+) = d.deptno(+); --error
   
   select e.ename, e.deptno, d.dname
   from emp e full outer join dept d on e.deptno = d.deptno;
   ```

   | emp    | dept   |
   | ------ | ------ |
   | deptno | deptno |
   | 30     | 10     |
   | 20     | 20     |
   | 10     | 30     |
   | null   | 40     |

   - left outer join의 경우 null 값을 가져오며
   - fight outer join의 경우 40값을 가져오며
   - full outer join의 경우 null값 40 값을 모두 가져온다.
   - inner join의 경우 null과 40은 올 수 없다.

8. n개의 테이블을 조인 하려면 최소 조인조건은 n-1개 선언해야 합니다.

### 서브쿼리(subquery)

```sql
select 조회할 열--메인쿼리
from 조회할 테이블
where 조건식(select 조회할 열
			from 조회할 테이블
			where 조건식)--서브쿼리(서브쿼리는 select에도 from 에도 having 절 order by절에 올 수 있다.)
```

- 조건 값을 알수 없어서 query를 2번 수행해야 하는 경우 subquery를 활용할 수  있다.
  
  `subquery = inner query= nested query
main query = outer query`
  
- subquery 는 mainquery의  select절, from절, where절, having절, order by절 에  subquery가 정의될 수 있다.

- where절과 having절의 subquery는 연산자 오른쪽에 () 안에 정의한다.

#### 서브쿼리 종류

1. 단일 행을 리턴하는 subquery : single row subquery

2. 복수행을 리턴하는 subquery : multiple row subquery

3. 단일 행, 단일 컬럼값을 리턴 subquery : scalar subquery

   - select절에 사용되는 subquery

4. 두개 이상의 컬럼값을 리턴하는 subquery : multiple column subquery

5. 상관관계 서브쿼리 :`where exists(co-related subquery)` :서브쿼리에 결과 값이 하나 이상 존재하면 조건식이 모두 true,아니면 false가 되는 연산자(false값을 얻고 싶은 경우 not exists를 사용한다.) 

   - subquery가 main query의 컬럼을 참조해서, main query의 행수만큼 subquery 반복적으로 수행하는 Query

     ```sql
     select~~
     from table1 a
     where column 연산자 (select ~
                      	from table2
                      	where a.colunm =column2)
     --존재 유무를 확인하는 연산자는 exists, not exists,
     ```

     

6. subquery가 올 수 있는 위치

   - select
   - from - inline wiew
   - where- 연산자 오른쪽(subquery)
   - having-연산자 오른쪽(subquery)
   - order by

- where절과 having절에 single row subquery 를 사용할 경우 반드시 single row operator(>, >=, <=, <, =, <>)와 함께 사용한다.

- where절과 having절에 multiple row subquery를 사용할 경우 반드시 multiple row operator(In, any>,any<, all>,all<)와 함께 사용합니다.

  - any(some)

    ```sql
    (1000,1500,2000)
    1000> or
1500> or
    2000> or
--위의 경우로 표현하고 싶을시
    >any(1000,1500,2000)--으로 표현 하나만 만족 해도 된다
    ```
    
  - all
  
    ```sql
    (1000,1500,2000)
    1000< and
    1500< and
    2000<= and
    >all(1000,1500,2000) --모두 만족 시키고 싶을 경우
    ```
    
  - exists
  
  ```sql
  select*from emp
  where exists (select deptno
               from dept
               where deptno=20);--조건식이 하나이상 존재하면 모두 ture가 되어 emp의 모든 행이 출력된다. 존재하지 않으면 아무것도 뜨지않는다.
  ```
  
  
  
  7. subquerydpsms 모든 select 절, 함수등 제약없이 사용 가능하지만, order by 절은 from절의 inline view에서만 허용된다.



#### rownum

- 결과행에 순차적인 번호를 입력해주는 내장컬럼
- order by전에 발생하므로, order by 후에 하고 싶으면 subquery이용한다.



문>ADAMS 보다 급여를 많이 받는 사원

```sql
select ename, sal
from emp
where sal > (ADAMS의 급여)

select ename, sal
from emp
where sal > (select sal 
             from emp
             where ename = 'ADAMS')
```



문> 사원번호 7839번과 동일한 직무를 담당하는 사원정보 검색

```sql
select ename,sal,job from emp where job=(select job from emp where empno=7839);
```



문> emp 테이블에서 최소 월급을 받는 사원 정보 검색

```sql
select ename from emp where sal=(select min(sal) from emp);
```



문> emp 테이블에서 전체 사원 평균 월급보다 급여가 적게 받는 사원 검색

```sql
select ename from emp where sal<(select avg(sal) from emp);
```



문>EMP 테이블에서 사원번호가 7521인 사원과 업무가 같고 
급여가 7934인 사원보다 많은 사원의 사원번호, 이름, 담당업무, 입사일자, 급여를 조회하라.

```sql
select ename, deptno,job,hiredate,sal from emp where job=(select job from emp where empno=7521);
```



문> EMP 테이블에서 사원의 급여가 20번 부서의 최소 급여보다  많은 부서번호와 부서의 최소급여를 조회하라

```sql
select deptno,min(sal) 
from emp  group by deptno 
having min(sal)>(select min(sal) from emp where deptno=20); 
```



문> 10번부서 사원의 월급과 동일한 월급을 받는 다른 부서의 사원을 검색하시오

```sql
select*from emp
where sal in(select sal from emp where deptno=10) and deptno <>10;--10번 부서가 아닌 것까지 포함해주어야 한다. multiple row subquery 의 값을  =, or 로 비교하려면 in 사용
```



문>부서별로 가장 급여를 많이 받는 사원의  사원번호 , 이름, 급여, 부서번호를 
조회하라

```sql
select empno,ename,sal,deptno
from emp
where (deptno,sal)in(select deptno,max(sal) from emp group by deptno);
--multiple column subquery,pair-wise 비교 (deptno,sal)하게 되면 두개를 동시에 비교하게 된다.
```



문>업무가 SALESMAN인 최소 한명 이상의 사원보다 급여를 많이 받는 사원의 이름,  급여, 업무를 조회하라

```sql
select ename,sal,job 
from emp 
where sal >any(select sal from emp where job <>'SALESMAN');

```



문>업무가 SALESMAN인 모든 사원이 받는 급여보다 급여를 많이 받는 사원의 이름,  급여, 업무를 조회하라

```sql
select ename,sal,job 
from emp 
where sal >all(select sal from emp where job <>'SALESMAN');
```



문> 직무별 평균 급여중에서 직무별 평균급여가 가장 작은 직무를 조회하시오 
(직무, 평균월급)

```sql
select job,avg(sal) 
from emp
group by job
having avg(sal)=(select min(avg(sal))from emp group by job ) ;
```



문> 부서번호 80번 사원들중에서 월급이 높은 3사람을 조회하시오

```sql
select rownum, empno, sal 
from emp
order by sal desc; --이렇게 되면 rownum에 의해 번호가 붙은 후 sal 가 되므로
select rownum,empno,sal
from(select rownum,empno,sal 
from emp
order by sal desc) where rownum<4;--from 절에 사용해줘야한다.
--최종 정답은
select employee_id,department_id,last_name,salary
from (select rownum,employee_id,department_id,last_name,salary
from employees where department_id=80 order by salary desc) where rownum<4;
--메인쿼리에 rownum 넣어주면 1,2,3번호가 추가된다. 안넣어도 오류는 없다.
```

문>subquery를 사용해서 관리자인 사원들만 검색

```sql
select empno
from emp
where empno in (select mgr from emp);--또는 이기에 null이 있어도 상관없다. in 은 or = 의 의미기에
select empno
from emp a
where exists (select '1' from emp where a.empno=mgr);--'1'은 이 곳의 위치에 어느것이 들어가도 의미없기에 아무것을 작성 한것
```

문>subquery를 사용해서 관리자가 아닌 사원들만 검색

```sql
select empno 
from emp 
where empno  not in(select mgr from emp);--서브쿼리의 모든 값을 비교해야 하는 연산에서는 null이 포함되어 있는지 여부를 먼저 체크해서 null처리하거나 제외시켜야 한다. null 값때문에 오류는 없지만 아무값도 안나온다.not in 은 and !=의 의미이기 때문이다.
select empno 
from emp
where empno  not in(select mgr from emp where mgr is not null);--is not으로 null값 제외! 중요
select empno
from emp a
where not exists (select '1' from emp where a.empno=mgr);
```



문> 각 부서별로 평균급여보다 급여를 많이 받는 사원 검색 (이름, 부서, 급여) - correlated subquery, join(상호연관 서브쿼리)

```sql
select a.ename, a.deptno, a.sal
from emp a , (select deptno, avg(sal) avgsal
             from emp
             group by deptno) b
where a.deptno = b.deptno
and a.sal > b.avgsal;--join 이용
```

```sql
select e1.ename,e1.deptno,e1.sal 
from emp e1 
where sal>(select avg(sal) from emp e2 where e1.deptno=e2.deptno group by deptno ) 
order by deptno;--서브쿼리가 계속 돌아가는 구문 이 구문의 경우 서브쿼리가 먼저 돌아가지 않는 것은 서브쿼리 안에 메인쿼리 관련 인자가 있기 떄문 
```

문>사원들 중에서 2번이상 부서 또는 직무를 변경한 이력이 있는 사원의 사번, 이름(last_name) 출력.

```sql
select a.employee_id,a.last_name
from employees a, (select employee_id,count(employee_id) cnt
                    from job_history
                    group by employee_id)b
where a.employee_id=b.employee_id
and b.cnt>=2;


select a.employee_id,a.last_name
from employees a
where 2<=(select count(employee_id) 
            from job_history
            where a.employee_id=employee_id);
```





### with절

- select문을 통해 일부 테이터를 먼저 추출후 별칭을 주어 사용하는 것

  ```sql
  with
  [별칭1]as (select문 1),
  [별칭2]as (select문 2),
  ....
  [별칭n]as (select문  n)--마지막은 ,를 찍지 않는다.
  select
  from 별칭1, 별칭2, 별칭3....
  ```
```
  
  

부서별 총 급여가 전체 부서의 평균급여보다 큰 부서번호와 총급여를 출력

​```sql
with 
dept_sum as (select department_id, sum(salary) sum_sal
             from employees
             group by department_id),
emp_avg as (select avg(sum_sal) total_avg
             from dept_sum)
select a.department_id, a.sum_sal
from dept_sum a, emp_avg b
where a.sum_sal > b.total_avg;--with를 사용한 것
```

#### 집합연산자

- union -합집합 이며 중복값을 제거하며 중복행을 제거 위해 첫번째 select 로 sorting한다.

- union all-append방식

- intersect - 중복된 행만 가져온다.첫번째 select로 sorting해서 비교

- minus-첫번째 select결과만 가져오기에 sorting해서 비교

- 위치 는  order by절을 제외하고 모두 올 수 있다.

  ```sql
  select~
  from~
  [where~]
  [group by~]
  [having]
  union | union all | intersect | minus
  select~
  from~
  [where~]
  [group by~]
  [having]
  [order by~];--맨 마지막에만 가능
  ```

- 각 select 문에서 컬럼갯수와 컬럼타입 일치해야한다.

  ```sql
  select empno,ename,sal,deptno
  from emp
  where deptno=30
  union
  select empno,ename,sal
  from emp
  where deptno=10;--ORA-01789: 질의 블록은 부정확한 수의 결과 열을 가지고 있습니다.
  
  select empno,ename,sal,deptno
  from emp
  where deptno=10
  union
  select empno,deptno,ename,sal
  from emp
  where deptno=20;--ORA-01790: 대응하는 식과 같은 데이터 유형이어야 합니다. 
  ```

  

- 결과는 첫번째 컬럼값을 기준으로 정렬된다. order by절은 맨 마지막에 작성해야한다.



- grouping sets

  - 특정 그룹으로만 출력하고 싶을때

  ```sql
  select deptno,job,mgr,avg(sal)
  from emp
  group by gruoping sets ((deptno,mgr),(mgr),(job),());
  ```

  

- group by rollup

  - 그룹화데이터의 합계를 출력할 때 유용하게 사용
  - select 절의 n+1개의 조합이 출력

```sql
group by rollup(A,B)
->group by (A,B)
->group by(A)
->group by()

group by rollup(A,B,C)
->group by (A,B,C)
->group by(A,B)
->group by(A)
->group by()

select deptno,job,count(*)
from emp
group by deptno, rollup(job);

select deptno,job,count(*)
from emp
group by deptno, rollup(job);--필요한 조합의 출력만 보기 위해서는 열 중 일부만 지정 할 수 있다. 

```

- group by cube

  - select절의 2^n개의 조합이 출력
  
  ```sql
  group by cube(A,B)
  ->group by (A,B)
  ->group by(A)
  ->group by(B)
  ->group by()
  
  group by Cube(A,B,C)
  ->group by (A,B,C)
  ->group by(A,B)
  ->group by(A,C)
  ->group by(B,C)
  ->group by(A)
  ->group by(A)
  ->group by(C)
->group by()
  ```
  
  

문> 20명 사원의 현재와 과거의 모든 부서, 직무 이력을 출력 (동일한 직무와 부서 근무 이력은 중복 데이터로 출력합니다.)

```sql
select employee_id, job_id, department_id
from employees
union all
select employee_id,  job_id, department_id
from job_history;

```



문> 20명 사원의 현재와 과거의 모든 부서, 직무 이력을 출력 (동일한 직무와 부서 근무 이력은 한번만 결과 데이터로 출력합니다.)

```sql
select employee_id, job_id, department_id
from employees
union  
select employee_id,  job_id, department_id
from job_history;  
```



문> 20명 사원중 의 현재 직무와 부서를 과거에 동일한 부서와 직무를 담당한 사원 조회
(사원번호, 직무, 부서번호)

```sql
select employee_id, job_id, department_id
from employees
intersect 
select employee_id,  job_id, department_id
from job_history;
```



문> 입사한 이후에 한번도 직무나 부서를 변경한 적이 없는 사원번호 출력

```sql
select employee_id 
from employees
minus
select employee_id 
from job_history;

```

문> 전체 사원들의 급여 평균과
    부서별 사원들의 급여 평균과 
    부서와 직무별 사원들의 급여 평균을 단일 결과 집합으로 출력

```sql
select to_number(null),to_char(null),avg(sal)
from emp
union all
select deptno, to_char(null),avg(sal)
from emp
group by deptno
union all
select deptno,job,avg(sal)
from emp
group by deptno,job;
--비효율적


select  deptno,job,avg(sal)
from emp
group by rollup(deptno, job);
```

문> 전체 사원들의 급여 평균과
    부서별 사원들의 급여 평균과 
    직무별 사원들의 급여 평균과
    부서와 직무별 사원들의 급여 평균을 단일 결과 집합으로 출력

```sql
select to_number(null), to_char(null), avg(sal)
from emp
union all
select deptno, to_char(null), avg(sal)
from emp
group by deptno
union all
select to_number(null), job, avg(sal)
from emp
group by deptno, job
union all
select deptno, job, avg(sal)
from emp
group by deptno, job;
--비효율적

select deptno, job, avg(sal)
from emp
group by cube (deptno, job);

```



## 테이블 추가

### 추가

- 테이블을 추가하려면 대상 테이블에 insert권한 또는 테이블의 소유자여야 한다.

  ```sql
  insert into 테이블명 [(컬럼명,컬럼명....)]
  values (컬럼리스트의 순서대로 값...);
  --새로 추가되는 행의 일부 컬럼값만 정의할 경우, 필수 컬럼은 반드시
  insert into 테이블명 --생략시
  values (테이블에 정의된 컬럼 순서대로 모든 값이 선언);
  
  insert into dept(dname,loc)
  values ('IT','Seoul');
  ```

  

#### insert문에서 서브쿼리 사용시

- values절은 사용하지 않는다.



### 수정

```sql
update 테이블명
set 컬럼명=new 컬럼값 [,컬럼명=new컬럼값,...]
--테이블의 모든 데이터를 

update 테이블명
set 컬럼명=new 컬럼값 [,컬럼명=new컬럼값,...]
where 조건;
```

- 메모리에만 저장상태
- rollback; 하면 테이블 생성 후 모든 insert는 삭제 된다
- 오류가 뜨는 경우
  - 컬럼 사이즈 초과, 전체 자리수보다 클때
  - 무결성 오류, PK중복값 일때
  - 참조무결성 제약조건 오류, FK오류이다.
- 함수사용 가능

```sql
insert into emp (empno,ename,deptno,hiredate)
values (9000,'Kim',50,sysdate);-- 함수사용 가능
insert into emp (empno,ename,deptno,hiredate)
values (9001,'Lee',50,'19년3월2일');---리터럴이 형식 문자열과 일치 하지 않아 오류가 뜨므로
insert into emp (empno,ename,deptno,hiredate)
values (9001,'Lee',50,'19/3/2');--해도 에러면 to_date()함수 사용 to_date('19/03/02') 한다.
```

#### 구조복제

```sql
create table emp10
as select*from emp
where 1=2; --false조건을 준다. 검색된 내용이 없을 것이다. 이렇게 하면 테이블 구조만 복제한다.CTAS

desc emp10
select*from emp10;--구조만 있는 것을 확인할 수 있다.
```





문> SMITH사원의 급여를 KING사원과 급여와 동일하도록 변경

```sql
update emp
set sal=(select sal from emp where ename='KING')
where ename='SMITH';
```

문>king사원과 동일한 부서에 근무하는 KING을 제외한 다른 사원의 급여를 20%인상

```sql

```



### 삭제

```sql
delete from 테이블명;--전체 행 삭제
delete 테이블명;--오라클에서는from절 생략 가능
delete from 테이블명 where 조건;
--조건 만족 하는 행만 삭제
delete from 테이블명 where 컬럼 연산자(subquery);
```

문> ADAMS 사원과 동일한 직무를 담당하는 사원 삭제(ADAMS는 제외)

```sql
 delete 
 from emp
 where job=(select job from emp where ename='ADAMS') 
 and ename<>'ADAMS
```



### merge문

- 운용계 DB 목적 : Tx

  - 데이터 변경이 계속 발생(ex 인터넷 쇼핑-가입 탈퇴 등등)
  - 분석기능-DSS예측 필요
  - Data amining 하게 된다.

- 데이터 이관 작업은 ETL 한다.이런 ETL에 사용되는 것이 merge문

  ```sql
  merge into 대상테이블 t(엘리아스 지정해야한다.)
  using 소스테이블 s(alias)
  on t.PK컬럼 =s.PK컬럼--같으면 row존재한다
  when matched then
  update set t.컬럼=s.컬럼....(테이블명은 미리 썼기 때문에 생략)
  [delete where 조건]
  when not matched then --일치하는 것이 없기에 추가해야한다.
  insert (t.컬럼리스트)
  values (s.컬럼리스트);
  ```

  

문>emp테이블로부터 30번 부서 사원정보를 emp30테이블로 복제하고

30번 부서 사원은 직무와 급여를 update하고

급여가 2500이상이면 삭제하라

20,10번부서  사원은 사원번호와 이름과 부서번호만 입력하라.

```

```



## Trasaction

ACID -원자성, 일관성,격리성, 영속성

DB-Transaction은 변경(DML,DDL,DCL)이 포함되면 

select는 transaction으로 포함되지 않고 

- 수행중인 DML트랜잭션의 세션이 비정상적종료하면 oracle server는 rollback한다.
- 정상종료(exit;)oracle server는 commit

### 읽기 일관성

select하는 user들이 변경중인 user작업이 종료될때까지 

변경 작업하려는 user들은 select하는 user들이 검색을 종료할때까지 기다리않고

변경 작업중인 user들은 변경중인 값을 조회 결과로 볼 수 있고,

변경 작업중이 아닌 user들은 DB에 저장된(commit된)데이터 값을 조회 결과

오라클 서버는 읽기 일관성을 위해서 lock,undo segment등을 지원합니다.







### 단위

1개 이상의 DML들로 구성- 명시적 commit, rollback

1개의 DDL-auto commit;

1개의 DCL-auto commit;

### savepoint

```sql
 create table test(num number(2));
 insert into test values(1);
insert into test values(2); 
 savepoint a;
 insert into test values(3);
 insert into test values(4);
 savepoint b;
 insert into test values(5);
 insert into test values(6);
select*from test; 
 rollback to savepoint b;
select*from test;  --지정한 곳 까지 취소가 된다.
 rollback to savepoint a;
select*from test;  
rollback;
```

palyback...? 기능이 있어 savepoint하지 않아도 볼수 있다! --오라클 전용 지원

## 데이터 정의어

### 객체 생성

#### table

- Row+cloumn
- 물리적 data 저장
- heap,IOT,partition, cluster(종류)

#### table생성하기 위해서

- create table 시스템 권한이 있어야 한다.
- tablespace(data container)저장소에 quota가 할당되어 있어야 한다.
- table 또는 컬럼 이름 규칙
  - 영문자 또는 _,$,# 시작
  - 두번째 문자부터 숫자 허용
  - 키워드안되며 중복도 안된다
  - schema- 서로 연관된 table,index등의 객체를 그룹핑하는 논리적 개념, 객체 명을 재사용할 수 있는 namespace역활을 한다. 오라클은 user명을 schema명으로 사용한다. schema내에서 중복 이름 사용 불가
  - 길이 제한 30자
  - DB이름 길이 제한 8자
- 컬럼타입을 알아야 한다.
  - char 고정길이 문자열 ~2000byte
  - varchar2 가변길이 문자열 ~4000byte
  - number(p,s)
  - date --__세기 _ 년 _ 월 _ 일 _ 시 _  분 _ 초
  - timestamp --date타입 확장,1/10^9의 정밀한 초값 저장
  - timestamp with timezone
  - interval year to month
  - interval day to second
  - rowid
  - CLOB (character large object)~4G
  - raw-binary형식의 값 저장 예(지문,,,)~2000byte
  - BLOB(binary large object)~4G
  - BFILE- read only 가능한 file을 DB외부에 운영체제의 폴더에 저장,TX처리

```sql
create table 테이블명(
컬럼명 컬럼타입(size),
컬럼명 컬럼타입(size) [default 값],
컬럼명 컬럼타입(size) [제약조건],--컬럼 레벨에서의 제약조건
    ......
[제약조건]--테이블레벨에서 제약 조건
);

CTAS이용해서 테이블 구조만 복제,테이블 구조+데이터 복제 가능
create table 테이블이름
as
	(subquery);
as select empno,ename,deptno,sal*12
from emp
where deptno=20;--error

create table emp20
as select empno, ename, deptno, sal*12 salary
   from emp
   where deptno = 20;
desc emp20
select * from emp20;


drop table emp20 purge;--undo생성없이 물리적 삭제(복구불가),구조 삭제 복구하려면 backup이 있어야 한다.

create table emp20 (empid, name, deptid, salary)
as select empno, ename, deptno, sal*12  
   from emp
   where deptno = 20;
desc emp20
select * from emp20;
	
	

```

#### 제약조건

- constraint-table의 DML 수행시 규칙
- Primar key
- not null
- Unique Key
- Foreign key
- check

```sql
create table userinfo
(userid varchar2(10) not null,
username varchar2(15) constraint userinfo_nn not null,
age number(30)
);

desc userinfo
insert into userinfo
values('tester1','테스터1',20);

insert into userinfo (username,age)
values('테스터1',20);--에러 발생 컬럼수가 맞지 않기 때문
select*from userinfo;

select constraint_name,constraint_type
from user_constraints
where table_name='USERINFO';

alter table userinfo disable constraint userinfo_nn;--이걸 하고 나서는
insert into userinfo(userid,age)
values('test2',30);--삽입가능하다.
```

```sql
drop table userinfo;
select*from userinfo;
desc userinfo --검색 안됨 삭제되어서

select constraint_name,constraint_type
from user_constraints
where table_name='USERINFO';--함께 삭제

select*from recyclebin;
flashback table userinfo to before drop;

select constraint_name,constraint_type
from user_constraints
where table_name='USERINFO';-- 테이블과 함꼐 복원 rename해서 쓰면 된다! 
```

#### unique제약 조건

```sql
drop table userinfo purge;--하기 전 삭제!!! 깨끗하게
create table userinfo
(userid varchar2(10) constraint userinfo_uk unique,
username varchar2(15),
age number(30)
);

desc userinfo
insert into userinfo
values('tester1','테스터1',20);

insert into userinfo (username,age)
values('테스터1',25);--userid는 null?

insert into userinfo (username,age)
values('테스터1',30);--userid는 null?

insert into userinfo
values('tester1','테스터5',35);

select*from userinfo;

select constraint_name, constraint_type
from user_constraints
where table_name='USERINFO';--oracle sever는 unique제약조건이 선언된 칼럼에 자동으로 unique index

select index_name,uniqueness
from user_indexes
where table_name='USERINFO';

alter table userinfo disable constraint userinfo_uk;

select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';--제약조건 비활성화하면 인덱스 자동 삭제

alter table userinfo enable constraint userinfo_uk;

select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';--다시생성
```

#### prinary key제약조건

```sql
drop table userinfo purge;--하기 전 삭제!!! 깨끗하게
create table userinfo
(userid varchar2(10) constraint userinfo_pk primary key,
username varchar2(15),
age number(30)
);

desc userinfo
insert into userinfo
values('tester1','테스터1',20);

insert into userinfo (username,age)
values('테스터1',25);--null이 있기 때문이다

insert into userinfo (username,age)
values('tester1','테스터5',35);-- 값수가 너무 많다?



select*from userinfo;

select constraint_name, constraint_type
from user_constraints
where table_name='USERINFO';

select index_name, uniqueness
from user_indexes
where table_name='USERINFO';

```

#### check 제약조건

````sql
drop table userinfo purge;--하기 전 삭제!!! 깨끗하게

create table userinfo(
userid  varchar2(10),
username  varchar2(15),
gender   char(1) constraint userinfo_ck  check (gender in ('F', 'M')),
age  number(2) check (age > 0 and age < 100)
);


select constraint_name, constraint_type,search_condition
from user_constraints
where table_name='USERINFO';

insert into userinfo values('a001','an','f',20);-- error
insert into userinfo values('a001','an','w',20);--error
insert into userinfo values('a001','an',null,20);--
insert into userinfo values('a002','choi','M',0);--error
insert into userinfo values('a002','choi','M',100);--error
insert into userinfo values('a002','choi','M',25);--
````



#### view

- table의 data를 보여주는 윈도우 역활
- 물리적 data없다.(cf, MView-성능때문에 이 경우에는 있다)
- 논리적 table
- select문으로 정의
- 복잡한 query문을 간결하게 사용하기 위해서 사용
- 보안을 위해 사용

```sql
select*from VW_EMP20;
```

##### view 종류

- simple view
  - 하나의 대상 테이블로부터 view 생성, not null 제약조건이  선언된 컬럼은 모두 포함,컬럼표현식**'X**,그룹함수**X**, rowid**X**,row
  - DML이 가능한 view(간접적 table access DML 수행)
- complex view
  - 하나 이상의 테이블에 대한 select문으로 정의, 컬럼표현식
  - DML이 불가능한 View
- create view 권한이 있어야 한다.
- create or replace view~~~~=>alter view 역할

```sql
create [or replace][force : noforce] 
	view ㅂ이름
```

- 우선 권한이 있어야 한다 

1. 권한 부여 새로운 데이터베이스 접속 선택
2. 접속이름 local_sys
3. 사용자이름 sys
4. 비밀번호 oracle
5. sid orcl 
6. 접속 유형 기본, 롤 sysdba
7. 접속 후 `grant create view to scott,hr;` 작성!! 그럼 권한 부여 된다.
8. 다시 scott로 돌아가 작업을 계속하자.

```sql
--------------------------------------------------------------------강제 설정
create or replace view dept
as select *from dept10;--dept10이란 테이블이 없기 때문에

create or replace force view dept_vu
as select *from dept10;
--경고: 컴파일 오류와 함께 뷰가 생성되었습니다.강제로 테이블 생성
------------------------------------------------------------------------------
select object_name,object_type,status 
from user_objects
where object_name='DEPT_VU';--dept_vu는 생성되었으나 유효하지 않음.

select*from emp20_vu;--뷰의 데이터 조회

insert into emp20vu values(9005,'Song',20,'SALESMAN',2000);--insert 가능한가 
--SQL 오류: ORA-00942: 테이블 또는 뷰가 존재하지 않습니다

create view emp20_vu
as select empno,ename,deptno,job,sal
from emp
where deptno=20;--ORA-00955: 기존의 객체가 이름을 사용하고 있습니다.
create or replace view emp20_vu
as select empno,ename,deptno,job,sal
from emp
where deptno=20; --대체하거나 삭제하거나 해야한다.
---------------------------------------------------------------------------------

insert into emp20_vu values(9005,'Song',20,'SALESMAN',2000);--삽입
update emp20_vu set sal=1900 where empno=9005;--변경
delete from emp20_vu where empno=9005;--삭제


----------------------------view 삭제는 table에 영향을 주는가?
drop view emp20_vu;--view 삭제
select*from emp20_vu;--삭제 확인
 select empno,ename,deptno,job,sal
from emp
where deptno=20;--하지만 table은 건재함.
```

- view 객체 삭제는 테이블에 영향을 주지 않고, 메타 정보만 data dictionary로

```sql
create or replace view emp20_vu
as select empno,ename,deptno,job,sal
from emp
where deptno=20
with check option;--chect제약조건을 설정(deptno=20인경우에만 insert delete등이 가능)

select constraint_name,constraint_type
from user_constraints
where table_name='EMP20_VU';

insert into emp20_vu values(9005,'Song',30,'SALESMAN',2000);--error
-------------------------------------------------------------------
create or replace view emp20_vu
as select empno,ename,deptno,job,sal
from emp
where deptno=20
with read only;--제약조건 설정, select만 가능

select constraint_name,constraint_type
from user_constraints
where table_name='EMP20_VU';

insert into emp20_vu values(9005,'Song',30,'SALESMAN',2000);--error
```

#### 시퀀스

```sql
create sequence 시퀀스 이름
[increment by n]--생성한 시퀀스 이름 지정, 뒤에는 지정하지 않는 경우 1부터 시작하여 1만큼 계속 증가하는 시퀀스가 생성
[start with n]-- 시퀀스에서 생성할 번호의 증가값(기본값은 1)
[maxvalue n : nomaxvalue]-- 시퀀스에서 생성할 번호의 시작값(기본값은 1)
[minvalue n : nominvalue]--시퀀스에서 생성할 번호의 최솟값 지정,최솟값은 시작값(START WITH)이하, 최댓값(MAXVALUE)미만 값으로 지정.nominvalue로 지정시 오름차순 이면 1,내림차순이면 10^-26으로 설정
[cycle:nocycle]--시퀀스에서 생성한 번호가 최댓값에 도달했을 경우 CYCLE이면 시작값(START WITH)에 서 다시 시작,NOCYCLE이면 번호 생성이 중단되고,추가 번호 생성을 요청하면 오류 발생
[cache n:nocache]--시퀀스가 생성할 번호를 메모리에 미리 할당해 놓은 수를 지정, nochche는 미리 생성하지 않도록 설정. 옵션을 모두 생략하면 기본값은 20


```

```sql
create sequence emp_seq;
select*from user_sequences;--시퀀스 객체를 생성하면 자동으로 시퀀스의 내장 컬럼 curr_val,next_val을 생성합니다.

select emp_seq.currval
from dual;--시퀀스를 생성하면 최초값을 생성한 다음에 currval을 확인 가능하다.

select emp_seq.nextval
from dual;

select emp_seq.currval
from dual;
------------------------------------------------
insert into emp(empno,ename)
values (emp_seq.nextval,'Kang');
select empno,ename from emp;

update dept
set deptno=emp_seq.nextval
where deptno=50;

select deptno,dname from dept;
```

```sql
alter sequence 시쿼스명
increment by~
maxvalue~
minvalue~
cycle~
cache~;
```

```sql
drop sequence 시퀀스명; --메타 정보만 data dictionary로부터 삭제된다.
```

#### SYNONYM

- 동의어는 테이블,뷰,시퀀스 등 객체 이름 대신 사용할 수 있는 다른 이름을 부여하는 객체
- 우선 권한이 있어야 한다 
  1. 권한 부여 새로운 데이터베이스 접속 선택
  2. 접속이름 local_sys
  3. 사용자이름 sys
  4. 비밀번호 oracle
  5. sid orcl 
  6. 접속 유형 기본, 롤 sysdba
  7. 접속 후 `grant create synonym to scott;` 작성!! 그럼 권한 부여 된다.
  8. 다시 scott로 돌아가 작업을 계속하자.

```sql
create [public] synonym 동의어 이름
for [사용자.][객체 이름];

create synonym d
for dept;--생성
select*from d;--확인
select*from user_synonyms;--생성된 synonyms를 확인해보자.
drop synonym d;--삭제
```



## 순위 관련 함수

- rank() over(partition by 컬럼 order by 컬럼 rows|range  unbounded preceeding|unbounded following| )
- dense_rank()
- row_number()

## window 함수

sum(),min(),max(),avg(),count()

### 행순서 관련 함수

first_value()

last_value()

lag(컬럼,n,null 대체값)

lead(컬럼,n,null대체값)

## DML

사원테이터 추가

```sql
insert into 테이블명(컬럼명 리스트 ) values(컬럼명 리스트의 순서와 타입에)
insert into 테이블명 values(테이블에 선언된 컬럼순서대로의 모든 값);
insert into 테이블명 (클럼명 리스트) subquery :--컬럼명 리스트는 subquery의 컬럼 순서
```

- values절에 null,default,단일행함수 등 사용 가능
- insert 오류-컬럼타입 불일치, 컬럼크기 불일치, 제약조건 오류

### 컬럼값 변경

```sql
update 테이블명 set 컬럼명=변경할 값[,컬럼명=변경할 값,...];
--컬럼값이 동일한 타입으로 변경된다.
update 테이블명 set 컬럼명=변경할 값[,컬럼명=변경할 값,...] where 조건;
update 테이블명 set 컬럼명(subquery)[,컬럼명=변경할 값,...] where(subquery) ;
```

- update 오류-컬럼타입 불일치, 컬럼크기 불일치, 제약조건 오류
- 변경할 값에 null,default,단일행함수 등 사용 가능

### 테이블의 행 삭제

```sql
delete from 테이블명; --모든 행 삭제
delete 테이블명 --oralce에서 from 생략
delete from 테이블명 where 조건 ; --조건을 만족하는 행만 삭제
delete from 테이블명 where (subquery);
```

- 참조부결성제약조건 오류 
  - 참조하는 자식 레코드가 존재하면 부모 레코드는 삭제 불가(FK오류)

### ETL 작업에 사용되는 병합문

- 하나의 DML로 insert, update,delete수행 

```sql
merge into 대상테이블 t
using 소스테이블 s
on(s.pk컬럼=t.pk컬럼)
when matched then
	update set t.컬럼=s.컬럼,....
	delete where조건 
when not matched then
	insert(t.컬럼,t.컬럼,....)
	values(s.컬럼,s.컬럼,....);
```



## TCL (Transaction Control Language)

### Transaction-Unit or Work,all or nothing 

- ACID(A.원자성,C.I,격리성,고립성,D.영속성)
- DB에서 Transaction단위-하나 이상의 DML,하나의 DDL(auto commit,하나의 DCL)
- 하나 이상의 DML로 구성된 트랜잭션은 명시적으로 commit;,rollback;해야한다.
- 트랜잭션 수행중에 DB연결된 세션 정상 종료(exit;)할 경우 oracle server 는 트랜잭션을 commit한다.
- 트랜잭션 수행중에 DB연결된 세션 비정상 종료(exit;)할 경우 oracle server 는 트랜잭션을 rollback한다.
- 긴 트랜잭션의 경우 rollback을 일부 할 수 있다. 
  - savepoint 식별자;
    - rollback to savepoint 식별자;

### 읽기 일관성

-  변경 중인 user는 자신이  변경중인 값이 조회되고, 변경중이지 않는 user들은 DB에 이전에 commit되서 저장된 값을 조회.
  - Lock과(변경중인 유저가 사용) undo date(변경중이지 않은 유저데이터)를 이용해서 읽기 일관성을 보장 
  - undo date는 트랜잭션을 rollback을 하면 변경전값을 undo segement로부터 restore(복원)한다.

## 데이터베이스의 객체 

1. table(데이터저장객체)
   - 구조,물리적 data저장 , row+col로 구성
   - heap, partition,IOT,clustered....종류
2. view-table에 대해서 select로 정의된 table의 window역할
   - 보안,간결한 select문 사용을 위해서
   - base가 되는 table이나 view가 있어야 한다.
   - 예외적으로 성능향상이 목적인 MeterializedView 
3. index-테이블의 컬럼에 생성
   - where 절에 검색조건으로 사용되는 컬럼 ,join컬럼, order by절의 컬럼 내부적으로 oracle server가 select수행시 사용
   - balancetree 구조로 저장되어 비교적 빠르게 검색 가능
4. Sequence -숫자값이 저장되어야 하는 컬럼(주문번호, 게시판의 글번호등)의 값을 자동으로 발행해주는 객체 
   -  최소값,최대값,증감값 설정하
5. Synonym(동의어)  schema명.객체@dblink명 과 같은 객체이름을 간결하게 사용하기 위한 동의어
   - select, insert, update,delete등 다양하게 사용 

## 테이블 생성

```sql
create table 테이블명(
컬럼명 컬럼타입(크기) 제약조건|default 기본값,
...
)
[tablespace 저장소명
sotrage...];
```

- 테이블 생성을 위해 필요한 권한
  - create table권한
  -  tablespace에 대한 quota
- 테이블명,컬럼명 이름규칙
  - 대소문자 구별 안함(Data dictionory에는 대문자로 저장)
  - 첫문자로 영문자,_,$,# 허용
  - 두번째부터는 숫자 허용 _,$,#외에는 사용 못함
  - 키워드 허용 안됨
  - 동일 schema내에서 중복 안됨
  - 길이제한 30자(데이터 베이스이름 길이 제한 8)

### schema

- 서로 연관된 객체들을 그룹핑,  오라클에서는 user명을 schema명으로 사용함. user소유의 객체들을 그룹핑해서 다른 user소유의 객체들을 구별하기
- `schema명.객체명`

### 컬럼타입

- char
- varchar2
- number
- date
- timestamp
- timestamp with timezone
- interval year to month
- interval day to second
- Bfile
- BLOB(LONG RAW)
- CLOB(LONG)
- RAW
- rowid-타입명이자 컬럼명, 행주소(논리적인 행주소)
  - objectId+ fileid+blockid+행순서번호

```sql
create table 테이블명(컬럼명 리스트)
as select~
from~
[where~]
.....;
--주의점! select절의 컬럼 리스트와 create table절에 선언된 컬럼명 리스트의 순서 개수 일치 
```

### 테이블 구조 복제

```sql
create table 테이블명  
as select ~ 
   from ~
   where 1=2;   --false조건
```

### 제약조건(constrint)

- DML수행시 컬럼값의 허용 또는 제한규칙

- primary key

- not null

- unique

- check

- foreign key

- 컬럼에 index가 자동 생성되는 제약조건-primary key,unique key

- 제약 조건 메타 정보 조회 -user_constraints,all_constraints,dba_constraints

- 테이블의 메타 정보 조회- user_tables(tab),all_tables,dba_tables

- 컬럼 메타 정보 조회- user_tab_cloumns

- 인덱스 메타 정보 조회-user_indexes,user_ind_columns

  - PK와 UK에 index자동 생성 목적-정합성 체크, 중복값 체크를 빠르게 수행
  - 적합 조건
    - where 조건에 사용되는 컬럼
    - join컬럼
    - order by컬럼
    - 컬럼중에서 distinct value(선택도)값이 많아야 한다. 예를 들어 deptno은 10,20,30이므로 3이다. 
    - where절의= 연산조건의 결과 행이 5%이내

  ```sql
  desc dict--혹은
  desc dictionary--이렇게 작성
  select table_name
  from dict
  where table_name like 'USER%COLUMNS%';
  
  desc user_tab_columns--컬럼 메타 정보 조회
  select*from user_ind_columns;--생성된 인덱스 살펴보기
  ```

  

#### primary key

- unique+not null
- 테이블에 하나만 정의 가능

#### not null

- null 허용 안함, 컬럼레벨에서만 제약조건 선언 가능. 여러개 가능

#### unique

- 중복값 허용 않음, oracle은 null 여러개 허용(unique취급)

#### check

- 특정값의 허용 범위

#### foreign kdy

- foreign key제약조건이 참조하는 부모 컬럼에는 primary key 또는 unique key제약조건이 설정되어 야 한다.



- 제약조건 예

```sql
create table emp2(
	empno number(4)
	ename varchar2(15) constraint 이름--컬럼 레벨
	hiredate date,
    job varchar2(15),
    sal number(8,2),
constraint emp2_pk primary key(empno,ename)--테이블  레벨 하나만 정의 가능
    );
  
```

```sql
create table category(
cid number(5),
cname varchar2(20)
);
insert into category values(10000,'BOOK');
insert into category values(20000,'Music');
insert into category values(30000,'Game');
insert into category values(40000,'Movie');
 select*from category;
 
 create table product(
 prodid number(5),
 pname varchar2(50),
 price number(6),
 cid  number(5) constraint product_fk references category(cid)
 );--error ORA-02270: 이 열목록에 대해 일치하는 고유 또는 기본 키가 없습니다.
 
 alter table category add constraint category_pk primary key(cid);--추가후! 다시생성하면 만들어진다!
 
 
select constraint_name, constraint_type
from user_constraints
where table_name = 'PRODUCT';

insert into product values (1, 'java', 5000, 10000);
insert into product values (2, 'oracle', 5000, 50000);  --error
insert into product values (3, 'BTS', 15000, 20000);
update product 
set cid = 2222 where prodid = 3;   ---error

delete from category where cid = 40000;    
delete from category where cid = 10000;  ---error
update category set cid = 15000 where cid = 10000;  ---?



create table product (
prodid   number(5),
pname    varchar2(50),
price    number(6),
cid      number(5) ,
constraint product_fk foreign key (cid) references category(cid)  -- on delete cascade 또는 on delete set null
);
```

### alter

```sql
alter table 테이블명  modify(컬럼 컬럼타입(크기));
```

- 컬럼 타입 변경할 때  컬럼값이 존재하더라도 char5->varchar2(10) 변경은 가능
- 컬럼 타입 변경할 때 호환되지 않는 컬럼타입으로 변경할때는 컬럼값을 null로 변경한후에 컬럼타입을 변경할 수 있다.
- 컬럼 크기를 변경할 때 크기 증가는 항상 가능하지만, 컬럼값이 존재할때 컬럼 크기를 줄이려면 저장된 컬럼값의 최대 길이보다 작게 줄일 수 없다.

```sql
alter table 테이블명 add constraint~;
alter table 테이블명 drop constraint~;
alter table 테이블명 add(컬럼 컬럼타입(크기),컬럼 컬럼타입(크기,....)
alter table 테이블명 drop(컬럼 컬럼타입(크기),컬럼 컬럼타입(크기,....)
alter table 테이블명 drop column 컬럼명;
alter table 테이블명 rename column old명 to new 명;
alter table 테이블명 enable constraint~;                   
alter table 테이블명 disable constraint~;                      
```



```sql
truncate table 테이블명 [reuse storage];--구조만 남겨두고, data는 완전 삭제(recyclebine에도 undo data도 생성하지 않음), 정리를 위해 사용했던 것으로 실제 사용은 못(?) 한다. 권한이 없다.
```



#### 삭제

```sql
drop table 테이블명; --테이블이름 rename되어 recyclebin에 저장됨 저장 공간 부족시 oracle server가 삭제
drop table 테이블명 purge;--recyclebin을 bypass하고 물리적으로 완전 삭제
purge recyclebine;
```

- 삭제되는 정보는 table에 대한 메타 정보, data, 제약조건,index도 함께 삭제된다. 

## index

- PK와 UK에 index자동 생성 목적-정합성 체크, 중복값 체크를 빠르게 수행

- 적합 조건

  - where 조건에 사용되는 컬럼
  - join컬럼
  - order by컬럼
  - 컬럼중에서 distinct value(선택도)값이 많아야 한다. 예를 들어 deptno은 10,20,30이므로 3이다. 
  - where절의= 연산조건의 결과 행이 5%이내 
    - 인덱스 생성 컬럼으로 조회 결과 행수가 10%를 초과하면 손익분기점으로 table full scan이 유리하다.
  - 거의 update가 발생하지 않는 컬럼 - 자주 update되는 컬럼은 인덱스 생성하면 성능 저하
  - 4~6개 블럭이상에  데이터가 저장된 테이블 (보통 4개 블럭)

  

  OLTP-

  - B*tree 인덱스
  - 소량 bata,빠른 검색

  OLAP ,DW,DSS

  - 분석처리를 하는데

  ​			

  

1. 단일컬럼인덱스

```sql
create index 인텍스 이름
on 테이블 이름(열이름);

create index ename on emp(ename desc);--생성
select*from user_ind_columns;--확인
drop index ename;--삭제
```



2. 복합컬럼 인덱스

3. unique 인덱스

4. non-unique인덱스

5. funcation-based 인덱스(컬럼값이 내림차순으로 생성)

6. bitmap 인덱스

- 데이터 종류가 적고 같은 데이터가 많이 존재할때 주로 사용



## 사용자 관리

### 사용자란?

- 데이터베이스에 접속하여 데이터를 관리하는 계정
- 데이터를 사용 및 관리하기 위해 오라클 데이터베이스에 접속하는 개체

### 스키마란?

- 오라클 데이터베이스에 접속한 사용자와 연결된 객체

```sql
select owner,table_name from all_tables where table_name='DUAL';--sys가 주인이다. public으로 daul테이블에 대한 select권함을 주었다.
desc dual--dummy컬럼 존재
select*from dual;--dummy컬럼값은 X
```

- dual의 목적...from 절이 필수이므로 단순 계산결과, 함수 결과를 확인할때 

```sql
create user 사용자 이름(필수)
identified by 패스워드 (필수)
default tablespace 테이블 스페이스 이름(선택)
temporary tablespacte 테이블 스페이스(그룹)이름 (선택)
quota 테이블 스페이스 크기 on 테이블 스페이스 이름(선택)
profile 프로파일 이름(선택)
password expire(선택)
account [lock/unlock](선택);
```



### 권한

- 권한 확인 방법

```sql
select*from session_privs;
select*from 'user%privs';--user_tab_privs,user_sys_privs
```



- sys에서 작성!

```sql
create user kim
identified by 1234
password expire;
 conn kim/1234
 --alter user kim identified by 새 비밀번호:
 --password 명령어로 비밀번호 변경
 conn kim/oracle--권한(DB connetion권한)없다고 오류
 
 grant create session to kim;--데이터베이스 접속 권한
 grant create table to kim;--테이블 생성 권한을 줘야
 
 conn kim/oracle
 create table test(name varchar2(10));--테이블 생성 가능
 
 select user from dual;--권한자 확인
 
 ---------------------------#dual -----소유자? 
select owner, table_name
from all_tables
where table_name='DUAL';   --sys임을 확인

--public으로 dual 테이블에 대한 select권한을 줌

desc dual  -- ?  dummy컬럼 존재
select * from dual;   ---? dummy컬럼값은 x

--dual의 목적....from절이 필수이므로 단순 계산결과, 함수 결과를 확인할때
```

#### 시스템 권한

- DB에서 특정 sql을 수행할 수 있는 권한, DBA가 주어야 한다.

#### 객체 권한

- 예)table에는 insert,update,select,alter,delete등을 수행 
  - view에는 select,drop,insert,update,delete
  - sequence는 select,alter,drop
- 객체의 소유자 , DBA

```sql
conn kim/oracle
select*from scott.emp;

conn scott/oracle
grant select on emp to kim;

conn kim/oracle
select*from scott.emp;
grant select on scott.emp to hr;--error

comm kim/oracle
select*from scott.emp;
grant select on scott.emp to hr;--권한없음(..아마?)

conn hr/oracle
select*from scott.emp;

conn scott/oracle
revoke select on emp from hr;--error, 객체 권한은 직접 권한을 준 user가 회수 가능하다.
revoke select on emp from kim;--권한 회수

conn kim/oracle
select*from scott.emp;--권한회수로 검색 불가
conn hr/oracle
select*from scott.emp;--객체 권한은 cascade로 회수됨.
```

#### 권한 관리(Role)

- 권한관리를 쉽게 하려면 직무별, 업무별로 필요한 권한을 그룹핑-**Role**
- role을 생성할 수 있는 권한은 DBA만 가지고 있다.
- 장점- 동적 권한 관리 가능

```sql
create role 롤이름;
grant 시스템권한,객체 권한 to 롤이름;
grant 롤이름 to 사용자 | 롤이름| public;
revoke 롤이름 from 사용자|롤이름|public;--권한 취소
--user_role_privs
drop role 롤이름--권한 삭제
```

##### 사전 정의된 롤

- connect 롤
  - create session권한이 있다.
- resource 롤
  - 테이블,시퀀스를 비롯한 여러 객체를 생성할 수 있는 기본 시스템 권한을 묶어 놓은 롤
- DBA 롤
  - 데이터베이스 관리 시스템 권한을 대부분 소유



