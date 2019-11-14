***

복습 가볍게~

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python (master)
$ cd Framword\(Django\)/

student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ ls
django_ex  django_intro  venv

student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ mkdir django_orm

student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ ls
django_ex  django_intro  django_orm  venv

student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ source venv/Scripts/activate
#가상환경 진입!
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ pip list
Package         Version  
--------------- ---------
certifi         2019.9.11
chardet         3.0.4
Django          2.2.7    
Faker           2.0.3
idna            2.8
pip             19.3.1
python-dateutil 2.8.1
pytz            2019.3
requests        2.22.0
setuptools      41.6.0
six             1.13.0
sqlparse        0.3.0
text-unidecode  1.3
urllib3         1.25.7
wheel           0.33.6
(venv) 
#장고 설치 확인!
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django) (master)
$ cd django_orm/
(venv) 
#작업 폴더로 이동!
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ ls
(venv) 
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ django-admin startproject config .
(venv) 
#장고 프로젝트 시작 설정 파일 설정! 

```

```python
#settings.py 파일 설정!


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



## 앱 생성

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py startapp boards
(venv) 
```

```python
#settings.py 에 만든 앱 추가

# Application definition

INSTALLED_APPS = [
    'boards',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



#### 앱  urls 설정

```python 
#config(프로젝트 설정 파일의 urls.py)

from django.contrib import admin
from django.urls import path , include
#include를 추가하여 urls 연결 !

urlpatterns = [
    path('board/', include('boards.urls')),
    path('admin/', admin.site.urls),
    
]

```

- 이제 boards app폴더에 urls.py 파일 생성!

```python
#boards의 ulrs.py

from django.urls import path
from . import views
#현재 파일의 views를 읽겠다.
urlpatterns = [
    path('' , views.index),
]
#기본 페이지 index로 설정하자.
```

```python 
#board 의 views

from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'boards/index.html')
```

#### 앱  tempates 설정

- boards 폴더 아래 templates 만들고 그안에 boards파일을 만들어 index.html 을 넣어 준다! 
- 전체적으로 사용할 templates또한 만들어 주자~
- html에 templates상속을 위해서 셋팅이 필요!

```python
#설정파일 config 의 settings.py


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , "config" , "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- BASE_DIR만들 준비 완료!
- config폴더에 templates 폴더 생성!(공통적으로 사용할 html이 들어간다.)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                      <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Dropdown
                      </a>
                      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                      </div>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                    </li>
                  </ul>
                  <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                  </form>
                </div>
              </nav>
    
    {% block content %}
    {% endblock %}


        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

```python
#boards>index.html
{% extends 'base.html' %}

{% block content %}
<h1>hi~ index page</h1>
{% endblock %}
```

![image-20191114094844924](image-20191114094844924.png)

***

# ORM(Object Relational Mapping)

- MTV패턴에서 model 부분이다.
- MTV(MVC)(모델/템플릿(뷰)/뷰(컨트롤러))

## 데이터베이스 기본 구조

#### Query란?

- 쿼리를 날린다! 라고도 한다.
- 데이터를 질의, 조회하는 명령어
- 데이터베이스의 요청(쿼리)을 해서 받는 것이 쿼리 세트이다.

#### Database란?

- 이러한 데이터의 모임이 데이터베이스!
- 체계화된 데이터의 모임이라고 한다.

#### SKIMA? 스키마란?

- DB자료의 구조
- 어떻게 그 DB를 표현할지!
- 어떻게  관계를 표현할지!

#### Table?

- 필드 : 컬럼
- 레코드 :  데이터

## ORM?

- 파이썬은 객체지향이며, 데이터 베이스를 이용하기 위해 장고에서 사용하는 것
- flask에서는 Pytest? 쓴다.

#### 장점

- sql을 몰라도 DB접근 가능하며 쉽게 사용 가능
- 클래스의 인스턴스를 생성하는 방법으로 ORM을 다루는데, sql이 길면 해석하는데 시간이 걸리는데, ORM의 경우 코드의 가독성이 좋다. 
- 객체지향으로 접근 가능해서 생상성이 좋아진다.
- mapping정보가 확실해서 ERD 보는것의 의존도가 낮아진다.(?)
- ORM은 독립적으로 작성되어 있고, 해당객체들을 재활용 할 수 있다. 그렇기에 모델에서 가공된 데이터를 컨트롤러(views.py)에 의해 뷰(templates)와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리
- 객체 재생산성이 좋기떄문에 MVC패턴을 좀더 견고하게 만들어 준다.
- 별도 mysql설치해도 , 원래는 query 문이 조금씩 다른데, ORM이 기본적으로 설치되어 있어 이 부분에서 완화된다. 



#### 단점

- 모든것을 ORM으로 구현하기 힘들다
- 설계시 신중해야한다.
- 큰 프로젝트의 경우 난이도가 올라간다. 잘못 구현되면 속도 저하가 생길 수 있다.

#### 실습

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py shell
# 파이썬 쉘을 실행해 준다.
```

```cmd
>>> class Person : 
...     name = "사람의 고유한 이름"
...     age = "출생 이후로 부터 삶을 마감할 때까지의 기간"
...     def greeting(self):
...             print(f'{self.name}이 인사합니다.')
...     def eating(self):
...             print(f'{self.name}이 밥을 먹고 있습니다.')
...     def aging(self):
...             print(f'{self.name}은 현재 {self.age}살이지만  점점 나이를 더 먹겠죠.' 
... )
#enter두번 치면 나와진다.

>>> justin = Person() 
>>> print(justin.name)
사람의 고유한 이름
>>> print(justin.age)
출생 이후로 부터 삶을 마감할 때까지의 기간
>>> justin.age=19
>>> print(justin.age)
19
>>> print(Person.name)
사람의 고유한 이름

>>> print(Person.age)
출생 이후로 부터 삶을 마감할 때까지의 기간
>>> justin.greeting()
사람의 고유한 이름이 인사합니다.
>>> justin.name = justin
>>> justin.name = "수능보는 justin"
>>> justin.greeting
<bound method Person.greeting of <Person object at 0x000001E41C463B48>>
>>> justin.greeting()
수능보는 justin이 인사합니다.
>>> justin.aging()
수능보는 justin은 현재 19살이지만  점점 나이를 더 먹겠죠.
>>> exit() # 종료! 
```



## Model?

- 모델은 단일 데이터에 대한 정보를 가지고 있다.
- 필수적인 필드(컬럼)과 데이터(레코드)에 대한 정보를 포함
- 각각의 모델은 단일 데이터베이스 테이블과 매핑
- 사용자가 저장하는 데이터들의 필수적인 필드(컬럼) 동작을 포함

#### 실습

```python
#boards의 models.py
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10) #CharField는최대 글자를 설정해 주어야 한다.
    content = models.TextField() #Text Field는 maxlength주어도 DB에서 글자수 제한이 주어지지 않는다.
    created_at = models.DateTimeField(auto_now_add=True) #글이 생성되면 날짜가 자동으로 저장되기 위해서 auto_now_add
    #장고는 아이디를 자동으로 만들어주기 때문에 컬럼명만 신경 쓰면 된다! 
```

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py makemigrations
Migrations for 'boards':
  boards\migrations\0001_initial.py
    - Create model Board
(venv) 
#작성한 모델을 기본으로 만든다!
#새로고침해서 보면 migrations폴더가 생성되어있다 1
```

```python
#자동으로 만들어진 파일로 id 가 주어진 것을 확인 가능!
#생성된 파일이름은 0001_initial.py
# Generated by Django 2.2.7 on 2019-11-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

```

- 추가도가능하다~

```python
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10) #CharField는최대 글자를 설정해 주어야 한다.
    content = models.TextField() #Text Field는 maxlength주어도 DB에서 글자수 제한이 주어지지 않는다.
    created_at = models.DateTimeField(auto_now_add=True) #글이 생성되면 날짜가 자동으로 저장되기 위해서 auto_now_add
    updated_at = models.DateTImeField(auto_now=True) #수정될때마다 시간 자동으로 저장하기 위해서
    
    
    
    #장고는 아이디를 자동으로 만들어주기 때문에 컬럼명만 신경 쓰면 된다! VO생성 안해도 된다
```

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py makemigrations
Migrations for 'boards':
  boards\migrations\0002_board_updated_at.py
    - Add field updated_at to board
(venv) 
#migrations만든다!
```

```python
#0002_board_updated_at.py
#새로 파일 생성!!!

# Generated by Django 2.2.7 on 2019-11-14 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

```

- query 확인을 위해

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py sqlmigrate boards 0001
#앱 이름과 번호를 작성해 준다.
BEGIN;
--
-- Create model Board
--
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, 
"created_at" datetime NOT NULL);
COMMIT;
(venv) 

#자동으로 not null옵션이 들어간 것을 확인 가능!

```

- 아직 DB가 생성되지않은 명세서뿐이다.
- DB적용 유무 확인 가능!

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
boards
 [ ] 0001_initial
 [ ] 0002_board_updated_at
 #두가지가 준비된것을 확인 가능! 빈칸은 아직 DB가 적용되지 않았음을 확인 할 수 있다.
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
(venv) 
```

## DB 적용

`python manage.py migrate`

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying boards.0001_initial... OK
  Applying boards.0002_board_updated_at... OK
  Applying sessions.0001_initial... OK
(venv) 

# 적용 상태 확인!
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
boards
 [X] 0001_initial
 [X] 0002_board_updated_at
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
(venv) 
```

- boards의 db.sqlite3를 읽기 위해서는

![image-20191114111643189](ORM(%EC%9E%A5%EA%B3%A03).assets/image-20191114111643189.png)

- 64비트와 sqpite-tools를 다운받자
- 압축을 풀고 사용하기 쉽도록 각각의 파일을 압축 풀고 C드라이브 아래 sqlite폴더 만든 후

![image-20191114111954229](ORM(%EC%9E%A5%EA%B3%A03).assets/image-20191114111954229.png)

- 이런식으로 넣어준다~
- vscode로 돌아와서 

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ vim ~/.bashrc
(venv) 
#내용은 alias sqlite="c:/sqlite/sqlite3.exe"
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ source ~/.bashrc
(venv) 

```



```cmd

student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ sqlite db.sqlite3
#해당 파일 보기 위해 실행!
```

```sqlite
SQLite version 3.30.1 2019-10-10 20:19:45
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  boards_board
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions
/*테이블 확인*/

/*구조 확인!*/
sqlite> .schema boards_board
CREATE TABLE IF NOT EXISTS "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
/*다른 것도 구조 확인 해보자~*/
sqlite> .schema auth_group
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
```



- DB에 넣은 내용 확인

```cmd
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py shell
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board
>>> Board.objects.all()
<QuerySet []>
#내용이 없어 빈칸으로 나온다.

```

## DB 데이터 넣기

```cmd
>>> board = Board() #인스턴스 생성
>>> board.title = "first"
>>> board.content = "jango !!!!!"
>>> board
<Board: Board object (None)>
>>> board.save()
>>> board
<Board: Board object (1)>
#하나가 생성됐음을 확인!

>>> board = Board(title = "second" , content = "django")  
#내용을 한번에 저장 가능!
>>> board.save()
>>> board
<Board: Board object (2)>

#내용을 한줄로 처리!
#objects는 인스턴스 즉, UI다.
>>> Board.objects.create(title = "third", content = "django")
<Board: Board object (3)>
```

## DB 내용 확인

- 반환은 리스트로

```cmd
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>]>
```

- 편하게 내용을 확인하기 위해서

```python
#boards의 modesl.py
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10) #CharField는최대 글자를 설정해 주어야 한다.
    content = models.TextField() #Text Field는 maxlength주어도 DB에서 글자수 제한이 주어지지 않는다.
    created_at = models.DateTimeField(auto_now_add=True) #글이 생성되면 날짜가 자동으로 저장되기 위해서 auto_now_add
    updated_at = models.DateTimeField(auto_now=True) #수정될때마다 시간 자동으로 저장하기 위해서
    #장고는 아이디를 자동으로 만들어주기 때문에 컬럼명만 신경 쓰면 된다! VO생성 안해도 된다

    def __str__(self):
        return f'{self.id} : {self.title}'
```

- 마지막에 함수를 추가해주는데 이것의 경우 migrations와 migrate 는 할 필요 없다.

```cmd
>>> ^Z  
#ctrl + "z"+ enter
now exiting InteractiveConsole...
(venv) 
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ ls
boards  config  db.sqlite3  manage.py
(venv) 
student@M1504 MINGW64 ~/Documents/GitHub/STUDY/Python/Framword(Django)/django_orm (master)
$ python manage.py  shell
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board
>>> Board.objects.all()
<QuerySet [<Board: 1 : first>, <Board: 2 : second>, <Board: 3 : third>]>
#이쁘게 잘 나오는 것을 확인!
```









## ORM 변경 순서

1. models.py 작성
2. makemigrations : migration 파일(명세서) 생성
3. migrate : 실제 적용되는 부분

## 데이터 객체를 만드는 3가지 방법(DB에)

1. board = Board()

   board.title = "값"

   board.save()

2. board = Board(title = "값" , content = "값")

   board.save()

3. board = Board.objects.create(title="값" , content = "값")

   - 세번째 방법은 세이브 없어도 적용!



 





