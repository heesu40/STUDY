[공부참고 사이트](http://rubylearning.com/satishtalim/numbers_in_ruby.html)

#  Ruby 설치

- Ruby  다운로드 [위치](https://rubyinstaller.org/downloads/)는 이곳이다.클릭!

- 실행후 설치

- 완료하면 

- ![루비 설치 중에 뜨는 화면2](Ruby.assets/RubyInstallation2.jpg)

- 파일이 뜨며 1 , 2 , 3 을 순서대로 설치해준다.

- ![image-20191227225723944](Ruby.assets/image-20191227225723944.png)

- cmd창에서 `gem -v`를 사용해 버전을 확인하여 설치를 확인한다.

- ` gem install jekyll`를 설치...하라는데 이게뭐딩? 

  > [Jekyll](https://jekyllrb.com/)은 여러(특히 마크다운) 형태의 텍스트와 테마를 소스로 하여 정적 HTML 웹사이트를 제너레이트하는 툴이다. Ruby 스크립트로 만들어져 있으나, 블로그를 만드는 데에는 루비를 전혀 몰라도 된다. 출처 네이버
  >
  > 한마디로 심플하고 블로그 지향적인 정적 사이트 생성기이다. Liquid 기능이 추가된 HTMl 템플릿을 사용해 사이트의 모양을 만들고 Jekyll 은 자동으로 내용물과 템플릿들을 함께 함쳐 어떤 서비스에서도 작동하는 완전한 정적 웹 사이트를 생성한다. github  pages의 내부 엔진이기 때문에 github서버에 무료로 호스팅 할 수 있다.



## Hello ruby

- 먼저 기본 실행을 확인해보자.

- ```ruby
  #ru_1.rb
  puts 'hello world'
  ```

- console창에서 `ruby rb_1.rb`를 작성하면 파일 실행이 되면서 확인할 수 있다.



## ruby and rails

#### 윈도우에서 개발환경 설정

- 레일스 인스톨러 이용하여 설치!

- [설치위치](http://railsinstaller.org/en)는 이곳을 참고한다.

- 번들러 최신화

- ```bash
  gem install bundler
  #번들러 최신업데이트!
  ```

## 프로젝트 생성!

- ```bash
  rails new <프로젝트 이름>
  ```

- ![image-20200106220622797](Ruby.assets/image-20200106220622797.png)

- r1으로 프로젝트 이름을 만들었고 자동 생성됨을 확인 할 수 있다.

## 서버 실행

- ```bash
  rails s
  #가 실행이 안되서 
  bundle install
  
  ```

- 로 실행한다. 실행은 r1 (만든 프로젝트이름) 파일안에 cd로 이동한 후 실행하도록 한다.

- 버전이 다르지 않은지 확인하도록 한다



## 기본 구조

### 1. 브라우저와 서버

- 브라우저 : 클라이언트
- 서버 : Rails서버는 MVC패턴으로 이루어져 있기 떄문에 Model, View , Controller가 서로 상호작용하여 정보를 가공

#### 1.1 서버와 클라이언트간 데이터교환

- 클라이언트가 서버에 연결 요청
- 서버는 클라이언트에 확인 메시지, 클라이언트는 확인메시지를 받았다는 확인 메시지를 서버에
- TCP연결 완료

#### 1.2. 브라우저(클라이어언트)

- HTML, CSS파일을 읽어, 사용자가 사용하기 편하도록 화면상에 띄워준다.
- JS파일을 읽어 화면을 동적 구성

#### 1.3. 서버가 하는 일

- Model : 어플리케이션 데이터와 정보 
- View : 데이터 표현 , 동적  정적 표현.
- Controller  :  Model과  View를 이어주며, 데이터 가공을 수행



### 2. 새로운 페이지 만들기

#### 2.1 페이지 생성 조건

1. controller action 존재
2. action과 연결된 view파일 존재
3. routes.rb에 url과  action이 연결

#### 2.2 Controller와 action 생성

```bash
rails generate controller home
```

- 먼저 컨트롤러 생성 위해서 bash창에 입력!
- 그 다음 Controller에서 액션 추가

```ruby
#ruby

```







## print put차이!

- ```ruby
  puts "Hello"
  puts " Hee!"
  print "Hello"
  print " Hee!"
  
  #############결과~
  Hello
   Hee!
  Hello Hee!
  
  ```





