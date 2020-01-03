#  programmer

## day7  없어진 기록 찾기( 차집합 이용)

```sql
select distinct a.animal_id,a.name 
from  animal_ins a left join  animal_outs b
on a.animal_id=b.animal_id and a.datetime!=b.datetime
where b.animal_id is null
```

- 차집합

```sql
--mysql
select a.id,a.name 
from Atable a left join Btable b 
on a.id=b.id 
where b.id is null
```

## day7  animal_outs  보다  animal_ins 의 입양일이 빠른  sql

``` sql
SELECT  a.animal_id ,a.name
from animal_ins a, animal_outs b
where a.animal_id=b.animal_id 
and a.datetime>b.datetime
order by a.datetime 
```

## 



# SQL 고득점



#### 중복제거 null값 제거위해서는?

- ```sql
  select count(distinct name) from animal_ins /* 집합함수는 알아서 null제거하고 게산 */
  ```

#### 0~23시간 사이의 입양 구하기

- 없는 시간대의 범위도 구해야하기때문에 

- sql 내 변수 설정을 한다.

- ```sql
  set @변수 := -1 /*초기 변수설정*/
  @변수 := @변수 + 1 /*변수 변화시 사용 /*
  ```

- ```sql
  set @hour := -1;
  SELECT ( @hour := @hour + 1) as 'HOUR' ,
  (select count(*) from animal_outs where hour(datetime) = @hour ) as 'COUNT'
  from animal_outs
  where @HOUR < 23
  ```

- 





##  완주하지 못한 선수 구하기

#### python

```python
#문제! 
#아래 그림처럼 완주하지 못한 선수를 구해보자.
```

![image-20191230214715982](programmers.assets/image-20191230214715982.png)

```python
def solution(participant, completion):
    answer = ''
    completion.append('z')
    for p, c  in zip(sorted(participant) , sorted(completion)):
        if p != c:
            answer = p
            return answer 
            

```

```python
def solution(participant, completion):
    answer = ''
  	answer = collections.Counter(participant) - collections.Counter(completion)
	return list(answer.keys())[0]

###########참고로
print("대답리스트" , list(answer))
print("대답 키" , list(answer.keys()))
print(list(answer.keys())[0])


```

![image-20191230215056126](programmers.assets/image-20191230215056126.png)

- 이렇게 나오게 된다. 
- colloections는....
  - 컨테이너에 동일한 값의 자료가 몇개 인지 파악하는데 사 용하는 객체이다.
  - 결과값은  dictionary형태로
  - 추가사항은 [사이트](https://excelsior-cjh.tistory.com/94)를 참고하자.



## 전화번호 목록

![image-20191231183013026](programmers.assets/image-20191231183013026.png)

```python
#문제
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
```

```python
def solution(phone_book):
    answer = True
    pb = sorted(phone_book)
    for i , y  in zip(pb , pb[1:]):
         if y.startswith(i):
            answer = False
            
            
    return answer
```

- 정렬한 후 `strB.startswith(strA , beg = 0  , end(string))로 0~end로 strB에서 strA문자열 찾기이다.
- strA가 맨앞에 있으면  True를 아니라면 False를 반환





# 스택/큐

## 1. 탑

- ```
  문제 설명
  수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다. 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한, 한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.
  
  예를 들어 높이가 6, 9, 5, 7, 4인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다. 그러면, 탑은 다음과 같이 신호를 주고받습니다. 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑이 수신하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다. 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신할 수 없습니다.
  
  제한 사항
  - heights는 길이 2 이상 100 이하인 정수 배열입니다.
  - 모든 탑의 높이는 1 이상 100 이하입니다.
  - 신호를 수신하는 탑이 없으면 0으로 표시합니다.
  ```

- ![image-20200102225054999](programmers.assets/image-20200102225054999.png)

- ```python
  def solution(heights):
      answer = [0] * len(heights)
      while heights:
          tt = heights.pop()
          for idx in range(len(heights)-1 , -1 , -1):
              if heights[idx] > tt:
                  answer[len(heights)] = idx + 1
                  break
      return answer
  ```

- ```python
  for idx in range(len(heights)-1 ,-1 , -1): #range(start , stop , step)
      print(idx) # 6 5 4 3 2 1 0
  for idx in range(len(heights)-1 , 0 , 0):
      print(idx) # 6 5 4 3 2 1   요렇게 나온다. stop전에서 끝난다!
      
  answer = [0] * len(heights) # [0,0,0,0,0,0,0]
  
  ```

- 

#  힙(Heap)

## 1. 더 맵게

- ```python
  
  ```

- 