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

```

