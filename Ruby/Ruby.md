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



## ~~ruby and rails~~

## 윈도우에서 개발환경 설정

- ~~레일스 인스톨러 이용하여 설치!~~

- ~~[설치위치](http://railsinstaller.org/en)는 이곳을 참고한다.~~ ==> 하지만 이걸로 했을때 오류가 났기 때문에! 취소!

- 번들러 최신화

- ```bash
  gen install rails #루비를 통해 rails를 설치할 수 있다.
  gem install bundler
  #번들러 최신업데이트! 번들러를 통해 젬의 의존성을 관리한다.
  gem install sqlite3
  #이것이 없으면 프로젝트 생성시 오류가 생긴다~
  
  ```
  
- node.js를 설치해주자~ 프로젝트 생성시 필요한지 미리 설치를 요구한다.

- [설치장소](https://nodejs.org/ko/)는 여기다.

- yarn또한 설치해 주어야 한다. [설치장소](https://yarnpkg.com/lang/en/docs/install/#windows-stable)는 여기다. 

- ```cmd
  choco install yarn
  ```

- 

## 프로젝트 생성!

- ```bash
  rails new <프로젝트 이름>
  ```

- ![image-20200106220622797](Ruby.assets/image-20200106220622797.png)

- r1으로 프로젝트 이름을 만들었고 자동 생성됨을 확인 할 수 있다.

## 서버 실행

- ```bash
  cd <프로젝트이름> #프로젝트 파일안에서 서버실행 해주어야 한다.
  rails s
  ```
  
- 로 실행한다. 실행은 r1 (만든 프로젝트이름) 파일안에 cd로 이동한 후 실행하도록 한다.

- `127.0.0.1:3000`으로 실행되며(다를수도..?)

- ![image-20200107135330839](Ruby.assets/image-20200107135330839.png)

- 브라우저 확인 가능하다~



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
user@DESKTOP-OT4VEF9 MINGW64 /d/gitgithub/STUDY/Ruby (master)
$ cd r1

user@DESKTOP-OT4VEF9 MINGW64 /d/gitgithub/STUDY/Ruby/r1 (master)
$ ls
app              config     Gemfile       log           postcss.config.js  README.md  tmp
babel.config.js  config.ru  Gemfile.lock  node_modules  public             storage    vendor
bin              db         lib           package.json  Rakefile           test       yarn.lock

user@DESKTOP-OT4VEF9 MINGW64 /d/gitgithub/STUDY/Ruby/r1 (master)
$ rails generate controller home
      create  app/controllers/home_controller.rb
      invoke  erb
      create    app/views/home
      invoke  test_unit
      create    test/controllers/home_controller_test.rb
      invoke  helper
      create    app/helpers/home_helper.rb
      invoke    test_unit
      invoke  assets
      invoke    scss
      create      app/assets/stylesheets/home.scss
```

- 먼저 컨트롤러 생성 위해서 bash창에 입력!
- ![image-20200107135628913](Ruby.assets/image-20200107135628913.png)
- 이렇게 컨트롤러 밑에 home_controller.rb파일이 생성된다.

- home_controller.rb파일로 들어가면

- ```ruby
  class HomeController < ApplicationController
  end
  #이렇게 존재~
  ```

- ```ruby
  class HomeController < ApplicationController
  	def index
  	end
  end
  
  ```

- index라는 액션을 만든다.

- View파일 생성 위해서

- ![image-20200107135905726](Ruby.assets/image-20200107135905726.png)

- app>vies>home파일에 index.erb 를 생성하자~

- 이곳에서 html 코드를 입력할 수 있다.

#### 2.3 routes.rb로 url과  action 연결

- ![image-20200107140119471](Ruby.assets/image-20200107140119471.png)

-  app > config > routes.rb 폴더안에는

- ```ruby
  Rails.application.routes.draw do
    # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  end
  #이렇게~ 존재한다.
  ```

- ```ruby
  Rails.application.routes.draw do
    # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
    get '/' => 'home#index'
  end
  
  ```

#### 2.4 controller 와 View연결

- ```ruby
  #home_controller.rb
  class HomeController < ApplicationController
  	def index
  		@hello = "world"
  	end
  end
  
  ```

- ```erb
  <!-- index.erb-->
  <h1>Hello index</h1>
  <%= @hello %>
  
  ```

- 브라우저에서 127.0.0.1:3000/   */*를 index 의 url로 정했기에 꼭 추가해준다.

- ![image-20200107140522731](Ruby.assets/image-20200107140522731.png)

- 이렇게 결과가 나오게 된다.









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





## 크롤링

- ```ruby
  
  ```

- 

