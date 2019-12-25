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

