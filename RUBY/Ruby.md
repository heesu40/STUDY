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
  # s는 server의 약자이다.
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
#컨트롤러 삭제는
# rails d controller <컨트롤러명> <액션명>
# d는 destroy의 약자! g 는 generate 의 약자!
# 액션 생성을 동시에 하는 경우 
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



## CRUD

[참고페이지](https://railsboyz.tistory.com/14)

### index 

- 기본 페이지를 설정하려고 할때

- ```ruby
  Rails.application.routes.draw do
    # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
    get '/' => 'home#index'
    root 'home#index'
  end
  # root 설정을 해주면 된다! 그렇다면 기본 페이지가 root에서 설정한 페이지로 나오게 된다.
  ```

#### RESTful

- REST? ' Representational State Transfer'의 약자

- HTTP의 메소드가  REST이다.

- | URL             | 액션    | 메소드 | 역할                      |
  | --------------- | ------- | ------ | ------------------------- |
  | /posts          | index   | GET    | 목록 페이지               |
  | /posts/:id      | show    | GET    | 개별 콘텐츠 페이지        |
  | /posts/new      | new     | GET    | 새로운 콘텐츠 입력 페이지 |
  | /posts          | create  | POST   | 입력 받은 콘텐츠 등록     |
  | /posts/:id/edit | edit    | GET    | 기존의 콘텐츠 수정 페이지 |
  | /posts/:id      | update  | PATCH  | 수정한 콘텐츠 내용 등록   |
  | /posts/:id      | destroy | DELETE | 선택한 콘텐츠 제거        |

  

#### 라우팅 설정

-  ```ruby
  #project > config > routes.rb
  
  Rails.application.routes.draw do
    # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
    get '/' => 'home#index'
  
    resources :posts
      #resources메소드를 사용! 
    root 'home#index'
  end
  
  ```

- cmd 창에 `rails routes`를 입력하면 모든 라우터를 확인할 수 있다.

- 

## 루비 코드 실행시간 측정

```ruby
start = Time.now
#코드
finish = Time.now
puts(finish - start)
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
  
  ## 다양한 메서드
  
  ``` ruby
  phrase = "Giraffe Academy"
  ```
  
  
  
  - phrase.upcase() - 대문자
  - phrase.downcase() - 소문자
  - phrase.strip() - 양끝 스페이스 처리
  - phrase.length() - 길이(스페이스 포함)
  - phrase.include? "Academy"   - true of false return
  -  phrase[0] -  G 가 리턴된다.
  - phrase[0,3] - Gir 끝의 숫자는 포함하지 않게 나온다.
  - phrase.index("G") - 0 시작 위치를 알려준다.
  - 구글에서 ruby Sring method를 참고하자.
  
  ## Math & number
  
  - ```ruby
    puts 2**3 #2^3과 같다
    puts 10 % 3 #나머지값 리턴
    num = 20
    puts "num" + num # 에러
    puts ("num" + num.to_s) #to_s 문자로 변환
    puts num.abs() #절대값
    puts num.round() #반올림 (정수값만)
    puts num.ceil() #올림
    puts num.floor() #내림
    puts Math.sqrt(36) # 6 루트값
    puts Math.log(1) # 0.0 
    puts 1.0 + 7 # 8.0 
    puts 10 / 7 # 1
    puts 10 / 7.0 # 1.4285714285714286
    
    
    ```
  
  ## Getting User input
  
  - ```ruby
    puts "Enter your Name: "
    name  = gets 
    puts ("Hello " + name )
    #결과
    Hellohee
    
    puts "Enter your Name: "
    name  = gets
    puts ("Hello " + name  + ", you are cool")
    #결과
    Hello hee
    , you are cool # enter가 삽입된다. 자동으로
    
    puts "Enter your Name: "
    name  = gets.chomp()
    puts ("Hello " + name  + ", you are cool")
    #결과
    Hello hee, you are cool
    
    
    ```

## Building a Calculator

- ```ruby
  puts "Enter a number: "
  num1 =  gets.chomp()
  puts "Enter another number"
  num2 = gets.chomp()
  puts (num1 + num2)
  #결과
  Enter a number:
  50
  Enter another number
  30
  5030
  ```

- ```ruby
  puts "Enter a number: "
  num1 =  gets.chomp()
  puts "Enter another number"
  num2 = gets.chomp()
  puts (num1.to_i + num2.to_i)
  #결과
  Enter a number:
  50
  Enter another number
  30
  80
  #결과
  Enter a number:
  5
  Enter another number
  2.5
  7 #ingeter로 바꾸었기때문에 5 + 2 가 된다.
  ```

- ```ruby
  puts "Enter a number: "
  num1 =  gets.chomp()
  puts "Enter another number"
  num2 = gets.chomp()
  puts (num1.to_f + num2.to_f)
  #결과
  Enter a number:
  5
  Enter another number
  2.5
  7.5
  ```

## Building a Mad Libs Game

- ```ruby
  puts "Enter a color: "
  color = gets.chomp()
  
  puts("Roses are {color}")
  puts("{plural_noun} are blue")
  puts("I love {celebrity}")
  ```

- 



## 열거자(Enumerable)

- [참고페이지](https://blog.nacyot.com/articles/2014-04-19-ruby-enumerable/)

## 배열

[참고사이트](https://jinbroing.tistory.com/41)





## 크롤링

[참고2, 셀레니움 기본 설명](https://gist.github.com/shoesCodeFor/083bfd82889e37cf896e69a2bbb112b3) , [참고3 셀레니움 API](https://www.rubydoc.info/gems/selenium-webdriver/0.0.28/Selenium/WebDriver/Find#find_elements-instance_method)

- 크롤링에는 selenium과 konogiri 가 있다.

- 크롤링을 하기 전에 확인해 볼것은 frame 또는 javascript로 작성됐는지 확인하는 것이다.

- 참고 사이트는 [여기를 클릭해서 참고!](https://www.askcompany.kr/vod/crawling/57/) 유튜브로 강의를 들을 수있다.

- iframe은 html안에 또 다른 html이 오는 경우이기 때문에 **switch_to_frame()** 함수를 사용해 iframe 안에있는 elenemt를 확인할 수 있게 해줘야 합니다. 그리고 iframe에서 원래있던 전체 웹 페이지로 나오려면 **switch_to_default_content()** 함수로 빠저나와야 합니다.

- ```ruby
  
  ```

- 셀리니움 오류 처리는 [사이트](https://elementalselenium.com/tips/44-exception-handling)를 참고하세요!


## 전처리 형태소분석

- 정규표현식으로 특수문자 제거(python) [참고](https://niceman.tistory.com/156)

## word count

- word count를 python 으로! [참고사이트](https://code.tutsplus.com/ko/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965)

## TF-IDF

- [참고사이트](https://donghwa-kim.github.io/TFIDF.html)

- TF-IDF 해부 사이트로 벡터화에 중점적[참고사이트주소](https://chan-lab.tistory.com/24)

- TF-IDF 의 가중치까지 계산해주지만 lower()의 벽에 막혔다. [사이트주소](https://iyzico.engineering/how-to-calculate-tf-idf-term-frequency-inverse-document-frequency-from-the-beatles-biography-in-c4c3cd968296)

- 두개의 문장을 비교하는 것이지만 같은 결과 lower()의 벽에 막혔다. [사이트주소](https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76)

- 전체적인 글을 한번에 TF-IDF처리하는 것으로 형태소 분석을 따로 하지 않았다.[사이트주소는](https://kugancity.tistory.com/entry/sklearn-TFIDF-vectorizer-%EC%82%AC%EC%9A%A9-%EC%98%88%EC%8B%9C) 다 포인트는 모든 글을 넣어주는 것!

- 가장 도움이 되었던 TF-IDF 참고 사이트 [주소](https://m.blog.naver.com/PostView.nhn?blogId=vangarang&logNo=221072014624&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

  - ```python
    #allitemre 은 전체적인 총 글이다. 
    #for문 부분만 돌려도 돌아간다. 하지만 반드시 cv = TfidVecotorizer() r가 있어야 한다.
    cv = TfidfVectorizer()
    X = cv.fit_transform(allitemre)
    # for i in allitemre:
    #     X = cv.fit_transform(i)
    #     print(X.shape)
    #     print(X)
    features = cv.get_feature_names()
    for feature in features:
        print(feature) # 사용된 글을 보여주는 것으로 띄어쓰기로 분할 된 글을 볼 수 있따.
    ```

  - 

## 파일 입출력

[참고](http://pleac.sourceforge.net/pleac_ruby/fileaccess.html) 

[참고2](https://medium.com/@ryannovas/ruby-file-and-directory-cheatsheet-16bd36315d46)

- 파일 디렉토리 다루기  python [참고용](https://wikidocs.net/3717)
- 파일 읽기 쓰기 python [참고용](https://wikidocs.net/26)



- 참고를 통한 새로 파일 만들면서 글내용 작성

- ```ruby
  file = File.open("./new.txt" , File::RDWR|File::CREAT , 0600)
  file.puts "잘되나?"
  file.close
  ```


## 분석기

- 참고 사이트는 [여기](https://ko.programqa.com/question/7704719/) 단어 카운트를 하고 있다.
- TF-IDF 참고 사이트는 [여기](https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/)다.

# 참고할 만한 코드!

- 크롤링에 이용

- ```ruby
  browser = Selenium::WebDriver.for :firefox
  browser.navigate.to 'C:\Scripts\Misc\Programming\Selenium-Webdriver\test.htm'
  
  # Refresh the page until there is at least 1 dog
  items = browser.find_elements(:class=> 'item')
  dog_items = items.find_all{ |item| item.find_element(:class => 'description').text == 'Dog' }   
  while dog_items.length == 0
    sleep(30)
    browser.navigate.refresh
    items = browser.find_elements(:class=> 'item')
    dog_items = items.find_all{ |item| item.find_element(:class => 'description').text == 'Dog' }     
  end
  
  # Select the dog with the greatest price
  most_expensive = dog_items.sort_by{ |dog| dog.find_element(:class => 'price').text.delete('$').to_f }.last
  
  # Click the selected dog
  most_expensive.find_element(:css => '.detailslink a').click
  ```

- nokogiri

- ```ruby
  require 'open-uri'
  require 'nokogiri'
  
  doc = Nokogiri::HTML(open('/scripts/test.html'))
  items = doc.css(".item").reject{|item| item.css(".description").text == "Dog"}
  items_hash = items.map do |item|
        {description: item.css(".description").text,
         price: item.css(".price").text.gsub("$",'').to_f,
         link: item.css(".detailsLink a").attributes["href"].value
        }
      end
  ```



