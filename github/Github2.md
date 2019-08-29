# Github

***



## 기술 면접 가이드 GIthub

- 예비 개발자들 또는 개발자들의 기술 면접 준비를 위한 자료를 정리해놓은 저장소
- https://github.com/JaeYeopHan/Interview_Question_for_Beginner

## 채용 관련가이드

- https://github.com/jojoldu/junior-recruit-scheduler

## 깃허브 정리

### 깃?

- (분산)버전관리 시스템 
- 코드의 history를 관리하는 도구, 개발된 과정과 역사를 볼 수 있고, 특정 시점으로 복구 가능
- **GIt,DVCS(Distributed Version Control System)**

### 깃 생성

```bash
$ git init
#주의 점은 git init 한 후에 

$git status 
# 우리가 쓰고 있는 환경은 CLI(command line interface), 명령을 하기 전까지 지금 상태를 알려주지 않는다.

$touch README.md 
# 빈파일 만들기

$ git add README.md

$git commit -m '백준 1001번 풀이'

$git log (--oneline [은 기록을 짧게 보여주는 것])
# commit 의 기록을 볼 수 있다.
```



```bash
$ git init

# 주의 점은 git init 한 후에 

$git status 

# 우리가 쓰고 있는 환경은 CLI(command line interface), 명령을 하기 전까지 지금 상태를 알려주지 않는다.

$touch README.md 

# 빈파일 만들기

$ git add README.md

$git commit -m '백준 1001번 풀이'

$git log (--oneline [은 기록을 짧게 보여주는 것])

# commit 의 기록을 볼 수 있다.

### 사용자 변경

$ git config --global user.name

$git config --global user.email

# 위 두가지로 검색하면 현재 커밋하는 사용자의 이름을 확인 가능

$git config --global user.name 'edutak'

$git config --global user.email 'edutak.ssafy@gamil.com'
# 위 두가지로 사용자 변경 가능
```



### 깃허브에 파일 올리기

```bash
 $git remote add origin https://github.com/~ #각자의주소 
 $git remote -v #지금 현재 리모트되고 있는 장소 를 보여준다.
 $git remote add algo https://github.com/~ #리모트 추가장소
 $git remote -v #하면 올리는 장소가 2개가 된다.
 $git remote rm algo #하면 삭제된다.
 $git remote -v #확인해보자.
 
```

### 깃 마크다운

```bash
​```java 하면 java 코드 블럭 생성
> 인용문 주석등 사용
[Git.scm][git-scm.com] 링크 연결 #실제로 가장 많이 쓰이는 마크문법 언어
```

- [Git 입문][https://backlog.com/git-tutorial/kr/]

1. git 저장소 초기화

   ```bash
   $git init
   $git 
   ```

2. add

   ```bash
   $git add .
   $git add REAEME.md
   $git add folder/
   ```

   - add 명령어를 통해 working directory에서 INDEX(staging area)로 특정 파일 이동
   - 커밋을 할 목록을 쌓는 것

3. commit

   ```bash
   $git commit -m'커밋메시지'
   ```

4. 커밋 히스토리 확인하기(log)

   ```bash
   $git log
   $git log -2
   $git log --oneline
   ```

5. 현재 git 상태 알아보기(status)**★★★★★★★★★★**

   ```bash
   $git status
   ```

6. 원격 저장소 활용

   - add, -v , rm

   ```bash
   # remote저장소 등록
   $git remote add origin{github URL}#깃이 아닌 다른 URL일수도있다.
   
   #remote저장소 확인
   $git remote -v
   
   #remote 저장소 삭제
   $git remote rm {저장소 이름}
   
   #저장하면서 커밋하기
   $git commit -am '올라가기'
   ```

   -  push , pull

   ```bash
   #원격 저장소로 (push)
   $giit push origin master
   
   #원격 저장소로부터 가져오기(pull)
   $git pull origin master
   ```

   - Local A, Local B, Github 으로 활동을 하는 경우 원격저장소 이력과 달라져서 충돌 발생 가능성 있음, 항상 작업 시작하기 전 pull을 받과, 작업을 완료한 이후에 push를 진행하면 충돌

     1. auto-merge

        -  동일한 파일을 수정하지 않은 경우 자동으로 merge commit이 발생

        ```
        1. local A에서 작업 후 push
        2. local B에서 작업시 pull을 받지 않음
        3. local B에서 작업 후 commit-> push
        4. 오류 발생(~~ git pull~~)
        5. local B에서 git pull
        6. 자동으로 vim commit 할 수 있도록 뜸.
        7. 저장하면, merge commit 발생
        8. local B에서 git push!
        ```

     2. merge comflict

        - 다른 이력(커밋)으로 동일한 파일이 수정되는 경우  merge comfilict가 발생.
        - 직접 충돌 파일을 해결 해야 한다.

        ```
        1. local A에서 작업 후 push
        2. local B에서 작업시 pull을 받지 않음
        3. local B에서 작업 후 commit-> push
        4. 오류 발생(~~ git pull~~)
        5. local B에서 git pull
        6. 충돌 발생(merge comflict)
        7. 직접 오류 수정 및 add, commit
        8. local B에서 git push
        ```

        - git status 명령어를 통해 어느 파일에서 충돌이 발생하였는지 확인 가능!

7. 되돌리기

   - staging area 에서 unstage

     ```bash
     $git status
     $git reset HEAD b.txt
     ```

   - commit 메시지 수정하기

     ```bash
     $git commit --amend
     ```

     - 커밋메시지를 수정하게 되면 해시값이 변경되어 이력이 변화
     - 따라서 언격 저장소에 push된 이력이라면 절대 변경하면 안된다.
     - 커밋을 하는 과정에서 파일을 빠뜨렸다면, 위의 명령어를 통해서 수정 가능

      ```bash
     $git add omit_file.txt
     $git commit -mend
      ```

8. wording directory 변경사항 버리기

   ```bash
   $git checkout --파일명
   ```

   - 변경사항이 모두 삭제 되고,  해당 파일의 이전 커밋 상태로 변화

## 깃헙 링크 정리

1. [백준알고리즘][/Text.md] - 상대 경로로 지정한 경우

#### 단계별 풀기

- 1001 - 출력하기[링크][풀이][.boj/1001]

2. 이미지 삽입시 환경설정의 이미지 삽입의 ./asserts 경로로 이미지 복사를 선택해 주자.









