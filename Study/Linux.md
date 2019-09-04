#  리눅스

### 설치

1. 다운로드 후 실행!
2. 권장설치도 되고 커스텀도 가능! 커스텀으로 해보자!
3.  limitations 는 제한적인 것을 나타낸다. 한번 확인해 보자.
4.  I will install the operating system later(나중에 설치시 추가하도록 하자  iso추가이다.)
5.  Linux 선택! 버전은  CentOS 64-bit 
6. 이름과 위치를 지정해주자!
7.  processors  와  cores를 지정해주자 (명령어 공부할 정도는 1프로세스에 1코어 면 충분)
8. 메모리 양을 지정해주는데.......... 2GB정도 해주자
9. Use network address translation  선택!
10. LSI logic선택!
11. SCSI 선택!
12. Create a new virtual disk 선택
13. Maximum disk size는 한...30GB, single file은 하나로 저장 multiple file은 분산 저장
14. 완료후    VM를 눌러 setting   에서 IDE 에서 다운 받은 ISO 파일을 넣어준다. 그리고 실행!



## Day 1

[hadoop@localhost ~]$ pwd
[hadoop@localhost ~]$ cd /                  #절대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd /home/hadoop      #절대 경로 사용 경로 변경
[hadoop@localhost ~]$ pwd
[hadoop@localhost ~]$ cd /boot             #절대 경로 사용 경로 변경
[hadoop@localhost boot]$ pwd
[hadoop@localhost boot]$ cd /home/hadoop   #절대 경로 사용 경로 변경
[hadoop@localhost ~]$ cd ../../            #상대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd ./home/hadoop    #상대 경로 사용 경로 변경
[hadoop@localhost ~]$ pwd


[hadoop@localhost ~]$ cd ../../            #상대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd ~                 #~는사용자 홈디렉토리로 이동
[hadoop@localhost ~]$ pwd 
[hadoop@localhost ~]$ ls -l
[hadoop@localhost ~]$ ls -d
[hadoop@localhost ~]$ ls -R

[hadoop@localhost ~]$ cd temp
[hadoop@localhost temp]$ mv text1 data1
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ mv data1 ./temp2/
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ ls ../temp2/
#파일 이동, 이름변경 
[hadoop@localhost temp]$ mv text2 ./temp2/data2
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ ls ../temp2/

#쓰기권한 없는 디렉토리 이동 에러 발생
[hadoop@localhost ~]$ cd ~
[hadoop@localhost ~]$ mv ./temp2/data2    /etc  

#파일 여러 개를 디렉터리로 이동하기
[hadoop@localhost ~]$ mv ./temp2/data1 ./temp2/data2 .
[hadoop@localhost ~]$ ls ./temp2/
[hadoop@localhost ~]$ ls 

#디렉터리를 디렉터리로 이동하기(기존에 있던 디렉터리가 아닐 경우에는 디렉터리명이 변경)
[hadoop@localhost ~]$ mv ./temp  ./temp3
[hadoop@localhost ~]$ ls

[hadoop@localhost ~]$ ls ./temp3
[hadoop@localhost ~]$ ls ./temp2
[hadoop@localhost ~]$ mv  ./temp2/  ./temp3/
[hadoop@localhost ~]$ ls ./temp3
[hadoop@localhost ~]$ ls ./temp3/temp2    #디렉토리가 이동되었으므로


#파일 삭제
[hadoop@localhost ~]$ rm -i temp3/temp2/data2
[hadoop@localhost ~]$ ls ./temp3/temp2
#디렉토리 삭제
[hadoop@localhost ~]$ rm -r temp3/temp2 
[hadoop@localhost ~]$ ls ./temp3 

[hadoop@localhost ~]$ cp /etc/hosts   temp/data1
[hadoop@localhost ~]$ ls temp
[hadoop@localhost ~]$ ln temp/data1   temp/data1.ln
[hadoop@localhost ~]$ ls temp/
[hadoop@localhost ~]$ ls -i temp/   #data1파일과 data1.ln 의 inode비교





## Day2

[hadoop@localhost ~]$ pwd
[hadoop@localhost ~]$ cd /                  #절대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd /home/hadoop      #절대 경로 사용 경로 변경
[hadoop@localhost ~]$ pwd
[hadoop@localhost ~]$ cd /boot             #절대 경로 사용 경로 변경
[hadoop@localhost boot]$ pwd
[hadoop@localhost boot]$ cd /home/hadoop   #절대 경로 사용 경로 변경
[hadoop@localhost ~]$ cd ../../            #상대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd ./home/hadoop    #상대 경로 사용 경로 변경
[hadoop@localhost ~]$ pwd


[hadoop@localhost ~]$ cd ../../            #상대 경로 사용 경로 변경
[hadoop@localhost /]$ pwd
[hadoop@localhost /]$ cd ~                 #~는사용자 홈디렉토리로 이동
[hadoop@localhost ~]$ pwd 
[hadoop@localhost ~]$ ls -l
[hadoop@localhost ~]$ ls -d
[hadoop@localhost ~]$ ls -R

[hadoop@localhost ~]$ cd temp
[hadoop@localhost temp]$ mv text1 data1
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ mv data1 ./temp2/
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ ls ../temp2/
#파일 이동, 이름변경 
[hadoop@localhost temp]$ mv text2 ./temp2/data2
[hadoop@localhost temp]$ ls
[hadoop@localhost temp]$ ls ../temp2/

#쓰기권한 없는 디렉토리 이동 에러 발생
[hadoop@localhost ~]$ cd ~
[hadoop@localhost ~]$ mv ./temp2/data2    /etc  

#파일 여러 개를 디렉터리로 이동하기
[hadoop@localhost ~]$ mv ./temp2/data1 ./temp2/data2 .
[hadoop@localhost ~]$ ls ./temp2/
[hadoop@localhost ~]$ ls 

#디렉터리를 디렉터리로 이동하기(기존에 있던 디렉터리가 아닐 경우에는 디렉터리명이 변경)
[hadoop@localhost ~]$ mv ./temp  ./temp3
[hadoop@localhost ~]$ ls

[hadoop@localhost ~]$ ls ./temp3
[hadoop@localhost ~]$ ls ./temp2
[hadoop@localhost ~]$ mv  ./temp2/  ./temp3/
[hadoop@localhost ~]$ ls ./temp3
[hadoop@localhost ~]$ ls ./temp3/temp2    #디렉토리가 이동되었으므로


#파일 삭제
[hadoop@localhost ~]$ rm -i temp3/temp2/data2
[hadoop@localhost ~]$ ls ./temp3/temp2
#디렉토리 삭제
[hadoop@localhost ~]$ rm -r temp3/temp2 
[hadoop@localhost ~]$ ls ./temp3 

[hadoop@localhost ~]$ cp /etc/hosts   temp/data1
[hadoop@localhost ~]$ ls temp
[hadoop@localhost ~]$ ln temp/data1   temp/data1.ln
[hadoop@localhost ~]$ ls temp/
[hadoop@localhost ~]$ ls -i temp/   #data1파일과 data1.ln 의 inode비교





### 복습

1. 배시 셀의 한 줄의 문자열 출력: **echo**
2. 배시 셀의 한 줄의 문자열을 %지시자와 w문자를 이용하여 출력형식을 지정:**printf**

***

1. 표준입력 파일 디스크립터 **stdin 0**
2. 표준출력 파일 디스크립터 **stdout 1**
3. 표준오류 파일 디스크립터 **stderr 2**

***

1. 출력 리다이렉션: **>** 기존파일의 내용을 삭제하고 새로 결과를 저장
   - ls -l (표준출력)
   - ls -l > ls.out (표준출력에서 파일출력으로 리다이렉션 할 수 있다.)
2. 출력 리다이렉션 : **>>** 기존 파일의 내용 뒤에 추가 저장
3. 입력 리다이렉션 : **<** 
   - ls -l   <    ls.in

***

1. 셀 변수와 환경변수 차이점
   - 셀 변수: 현재 셀에서만 사용 가능, 서브 셀로는 전달되지 않음
   - 환경변수 : 현재 셀에서 사용 가능, 서브 셀로도 전달 가능
   - **set** : 셀 변수, 환경 변수 모두 출력
   - 환경변수만 출력 : **env**
2. 환경변수 종류
   - HISTSIZE, HOME, LANG, PATH, PWD, SHELL.....
3. 셀 변수 정의(설정)
   - 변수명=문자열 
   - 정의된 셀변수를 환경변수로 설정 : **export** 변수명=문자열, **export **변수명
   - 환경 변수를 다시 셀변수로 전환: **export -n** 
4. 기존 명령을 대신하여 다른 이름을 붙여서 사용하려면 : **alias** 이름 ='명령'
   - alias 설정 해제 : **unalias**

***

1. 사용자가 이전에 입력한 명령을 다시 부럴와서 사용하려면: **history**
2. 바로 직전에 사용했었던 명령을 재 실행하려면  **!!**
3. 히스토리에서 해당 번호의 명령을 재실행하려면 **!번호**
4. 히스토리에서 문자열로 시작하는 명령중에서 마지막에 실행된 명령을 재실행하려면 **!문자열**

***

1. 배시셀에서 시스템 환경 설정 파일
   - `/etc/profile` - 모든 셀에 공통으로 적용 되는 환경 설정, bash.bashrc파일을 실행
   - `/etc/bash.bashrc` - 기본 프롬프트 설정, 시스템에 공통으로 적용되는 환경 설정
   - `/etc/profile.d/*.sh` - 언어나 명령별로 필요한 환경을 설정
2. 배시셀에서 사용자의 환경 설정 파일
   - `~/.profile ` 사용자가 정의하는 환경 설정, .bashrc 파일을 실행
   - `~/.bashrc` 히스토리 크기 설정, alias설정 , 함수 설정
   - `~/.bash_aliases` 사용자가 정의한 alias를 별도 파일로 저장
   - `~/.bash_logout` 로그아웃할때 필요한 함수들을 설정

***

1. `ls -l` 옵션으로 출력 내용
   - `-`또는 `d`는 파일의 종류
2. `rwxrwxrwx`  소유자의 파일접근 권한, 소유자가 속해있는 그룹의 파일접근 권한, 다른 사용자들의 파일 접근 권한
   - 하드링크 개수  
   - 소유자 ID
   - 소유자의 그룹 이름
   -  파일 크기
   - 파일이 마지막 수정된 날짜와 시간
   - 파일명

***

1. 파일 접근 권한 변경 :**chmod**
2. 하위 디렉토리까지 파일 접근 권한 변경 : **chmod -R**
3. 접근시 두 가지 방법이 있다
   - 기호 모드: `+,-,r(읽기),w(쓰기),x(실행)`
   - 숫자 모드: `chmod 777`, `chmod 644`,......
4. 기본 접근 권한 확인 : **umask**
5. 기본 접근 권한 변경: **umask**
   - 기본 접근 권한 변경 umask는 파일이나 디렉토리 생성 시 부여하지 않을 권한을 지정함
   - 특수 접근 권한 : **SetUID, SetGID, stick bit**
   - **SetUID** : 맨 앞자리가 ***4***로 설정, 해당 파일이 실행되는 동안에 파일 실행자 권한이 아닌 소유자 권한으로 실행, 소유자의 실행 권한에 `s`로 표시
   - **SetGID** : 맨 앞자리가 ***2***로 설정 해당 파일이 실행되는 동안에는 파일을 실행한 사용자 권한이 아니라 파일 소유자의 그룹 권한으로 실행
   - **stick bit ** :  맨 앞자리가 ***1***로 설정 , 디렉토리에 설정, 누구나 파일을 생성 가능, 파일을 생성한 소유자가 아니면 삭제 불가능(ex : /tmp, 누구든지 생성 가능하지만 생성한 소유자가 아니면 삭제 불가능)

***

1. 데몬 프로세스 : JVM의 garbage collector를 생각하면 된다, 특정 서비스를 제공하기 위해서 존재하는 프로세스, 리눅스 커널에 의해서 실행
2. 고아 프로세스 : 자식 프로세스가 아직 실행 중인데 부모 프로세스가 먼저 종료된 프로세스
3. 일반 프로세스
4. 좀비 프로세스: 자식 프로세스가 종료했는데도 (`ps`로 종료) 프로세스 테이블 목록에 남아 있는 경우(`defunct` 프로세스로 출력), 좀비 프로세스가 많아지면 일반 프로세스가 실행 안될 수 있다.

***

1. 현재 실행 중인 프로세스의 목록을 보는 명령 : **ps**
2. 현재 실행 중인 프로세스의 상세 정보 출력: **-f** (u도  a도 있었다, UID, PID, PPID, C, STIME, TTY, TIME, CMD)
3. 터미널에서 실행한 프로세스의 정보 출력: **-a**
4. **STAT 필드** : 
5. 현재 실행 중인 프로세스의 메모리 사용량 출력 **- u**  (%CPU, %MEM, VSZ, RSS, .....)
6. 실행중인 특정 프로세스 정보 검색 : **pgrep**
7. 프로세스 강제 종료 : **kill[-시그널] pid**
   - pkill 프로세스이름으로 강제 종료

***

1. 현재 실행중인 모든 작업을 보려면 : **jobs**
2. 백그라운드, 포그라운드 작업 
   - `ctrl + z`
   - `bg %작업번호`
   - `fg %작업번호`
3. 특정 시간에 작업을 수행하도록 예약 : **at [옵션] 시간 **
   - `at 12pm + 2days`
   - `at 12am tomorrow`
4. 정해진 시간에 작업을 반복적으로 수행하도록 예약 : `crontab`
   - `분 시 일 월 요일 작업내용`
5. 

## Day 3

### 파일시스템과 디스크 관리

#### 파일시스템

- 파일과 디렉터리의 집합을 구조적으로 관리하는 체계
- 어떤 구조를 구성하여 파일이나 디렉터리를 관리하느냐에 따라 다양한 형식의 파일 시스템이 존재

**리눅스** **고유의 디스크 기반 파일** **시스템**

1. ext(ext1)

- Extended File System’의 약자로  1992년 4월 리눅스 0.96c에 포함되어 발표
- 파일 시스템의 최대 크기는 2GB, 파일 이름의 길이는 255바이트까지 지원
- inode 수정과 데이터의 수정 시간 지원이 안 되고, 파일 시스템이 복잡해지고 파편화되는 문제
- 현재 리눅스에서는 ext 파일 시스템을 사용하지 않음

2. ext2

- ext 파일 시스템이 가지고 있던 문제를 해결하고, 1993년 1월 발표
- ext2는 ext3 파일 시스템이 도입되기 전까지 사실상 리눅스의 표준 파일 시스템으로 사용
- 이론적으로 32TB까지 가능

3. ext3

- ext3는 ext2를 기반으로 개발되어 호환이 가능하며 2001년 11월 공개
- ext3의 가장 큰 장점은 저널링(journaling) 기능을 도입 복구기능 강화
-  파일 시스템의 최대 크기는 블록의 크기에 따라 2~32TB까지 지원

4. ext4

- ext4 파일 시스템은 1EB(엑사바이트, 1EB=1,024×1,024TB) 이상의 볼륨과 16TB 이상의 파일을 지원
- ext2 및 ext3와 호환성을 유지하며 2008년 12월 발표

5. XFS

- eXtended File System의 약자
- 1993년 실리콘그래픽스가 개발한 고성능 저널링 파일 시스템. 2000년 5월 GNU GPL로 공개
- 2001년 리눅스에 이식되었고 현재 대부분의 리눅스 배포판에서 지원
- XFS는 64bit 파일 시스템으로 최대 16EB까지 지원



##### 리눅스 파일 시스템

1. 기본적인 계층 구조

2. 마운트

   - 파일 시스템을 디렉터리 계층 구조의 특정 디렉터리와 연결하는 것

3. 마운트 포인트

   - 디렉터리 계층 구조에서 파일 시스템이 연결되는 디렉터리를 마운트 포인트

4. 파일 시스템 마운트 설정 파일

   - 리눅스에서 시스템이 부팅될 때 자동으로 파일 시스템이 마운트되게 하려면 /etc/fstab 파일에 설정

   - `/etc/fstab` 파일의 기능: 파일 시스템의 마운트 설정 정보 저장
   - 구조는 장치명 - 마운트 포인트- 파일 시스템의 종류- 옵션 - 덤프 관련 설정 - 파일 점검 옵션



### 복습



1. 리눅스 고유의 디스크 기반 파일 시스템 종류
   - ext, ext2, ext3,ext4, XFS
2. 파일 시스템을 디렉토리 계층 구조의 특정 디렉토리와 연결하는 것을 ***마운트(mount)***
   - `/etc/fstab 파일에 설정`

***

### 프로세스관리 명령

1. 디스크 파티션 생성, 삭제, 보기 등 파티션 관리 명령 ***fdisk***
2. 리눅스 시스템이 부팅될 때 스크립트를 순차적으로 실행시켜서 다른 프로세스를 동작시키는 프로세스 ***init프로세스***
3. init은 시스템의 단계를 일곱개로 정의, 각 단계별로 셀 스크립트를 실행 ***런레벨(0~6)***
   - 0 시스템 종료 `/ebc/rc0.d`
   - 1, s 응급 복구  모드(싱글 사용자 모드) `/etc/rc1.d`
   - 2,3,4 다중 사용자 모드
   - 5 그래피컬 다중 사용자 모드(우리가 사용하는 것)
   - 6 재시작
4. 리눅스 종료 - ***poweroff, shutdown, halt, init 0, init 6, reboot***

***

### 아카이브

1. 파일을 묶어서 하나로 만드는 것 ***파일 아카이브***
2. 하나의 아카이브 파일로 생성, 추출, 업데이트 하는 명령 ***tar***
3. 새 아카이브 생성 ***tar cvf***
4. 아카이브 파일 내용 확인  ***tar tvf***
5. 아카이브 풀기 ***tar xvf***
6. gzip으로 압춘된 경우 ***tar xvfz***
7. 아카이브 업데이트 ***tar uvf***
8. 아카이브 파일 추가 ***tar rvf***
9. 아파이브 생성, 동시에 압축 ***tar cvzf(gzip) , tar cvjf(bzip2)***
10. 압축만 하기/풀기 ***gzip/gunzip(.gz), bzip2/bunzip2(.bz)***
11. 압출 파일의 내용 보기 ***zcat/bzcat***

***

### 사용자 관리

1. 사용자 계정 정보가  저장된 기본 파일 ***/etc/passwd***
2. 사용자 계정의 암호화된 비밀번호 저장된 기본 파일 ***/etc/shadow***
3. 사용자가 속해있는 그룹 정보가 저장된 기본 파일 ***/etc/group***
4. 사용자가 속해있는 계정의 암호화된 비밀저장 기본 파일 ***/etc/gshadow***
5. 사용자 계정 생성 ***useradd,adduser***
6. 사용자 계정 수정 ***usermod***
7. 사용자 계정 삭제 ***userdel***
8. 사용자 계정의 패스워 에이징 설정 관리 명령어 ***chage***
9. 사용자 그룹 생성 ***groupadd, addgroup***
10. 사용자 그룹 수정 ***groupmod***
11. 사용자 그룹  삭제***groupdel***
12. 사용자 로그인 정보 확인 ***who***
13. 사용자 이름, 로그인한 시간, 로그아웃한 시간, 로그인한 터미널 번호, ip 주소 확인 ***last***
14. 사용자 소속된 그룹 확인 ***groups***
15. 파일이나 디렉토리의 소유자,그룹 변경 ***chown -R 소유자:그룹, chown 소유자, chgrp 그룹***

