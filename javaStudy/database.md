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

### 검색(SQL내부 돌아가는 구조)

- service process가

  1. syntax checking (문법 체크)
  2. library cache 검색 (동일한 SQL context정보 있으면 실행- 응답 진짜 빠름)
     - 두개를 soft parsing 이라 한다.

  3. semantic checking(I/O BLOCK를 이용)
  4. optimizer(내부적으로 호출이 되어 객체 통계정보를 이용하여 경로선택(네이게이션의 경우)) 실행하여 service process로 리턴

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

- ```cmd
   alter session set nls_date_format ='YYYY/MM/DD HH24:MI:SS';
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
- substr(문자열,시작위치, 갯수)
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

- in 리스트 연산자 : in(값,값,값) 문장일 경우 '   ' 에 넣어준다. 

  - like '%,_': 문자 패턴 비교 연산자 `  like '%,_'
    - %는 문자 종류는 모든 문자, 개수는 0~m
    - _는 문자 종류는 모든 문자, 개수는 1을 의미한다.

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
  - equi join (inner join
  - non-equi join
  - self-join (자기참조가 가능한 테이블에서만)
  - 조인 조건을 잘못 정의하거나 , 조인 조건을 누락하면 cartesian product (cross join)
    outer join (조인컬럼값이 null인 경우 결과집합에 포함시키기 위한 조인)

- empno 사번
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
- trunc()  버림
- mod() 나머지
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

sum(number 타입|expression)

avg(number타입|expression)

min(number,char,date 컬럼타입 | expression)

max(number,char,date,컬럼타입 |expression)

count([distinct]number, char, date 컬럼타입 |expression) :null이 아닌 값(행) 개수 리턴

stddev(number타입 |expression) :표준편차

variance(number타입|expression) :분산

conn scott/oracle

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

- group by 절은 column명만 선언 가능.

- group by 컬럼명, 컬럼명 ... 하면 순서대로 그룹화된다.

- group by 조건은 having절에 써야 한다.

  ```sql
  select deptno,count(deptno),sum(sal) --4 가 되면 그룹함수에 대한 조건을 where에 쓸 수 없음으로 그룹함수 조건은 having 절에 작성한다.
  from emp --1
  where ~	--2
  group by deptno  --3
  having count(deptno)<4;
  ```

  





