# 1hadoop

1. 신뢰성 있고, 확장성 있는 분산 컴퓨팅을 위한 오픈 소스 분산 병렬(파일 시스템) 프레임워크

   - 정보 전달 프레임워크에서 소스전달 프레임워크로 전환
- 기본적으로 파일로 저장
2. 대용량 데이터의 분산 처리 가능한 프레임워크
3. GFS, MapReduce 소프트웨어구현체

   - 아파치 Top-Level 프로젝트
   - 코어는 Java , C/C++, Python 등 지원
4. 대용량 데이터 처리를 위한 플랫폼

   - HDFS, MapReduce, Core, 여러 API
5. 클러스터
   - Master-Slave구조(계층적인 구조로 마스터가 있고, slave들이 있다)
   - Master담당 노드를 NameNode(HDFS의 namespace, Meta정보 저장)한다.
   - Slave 담당 노드를 DataNode(64M`꼭 64M인 것은 아니다`, 128M데이터 블럭이 분산되어 저장)한다.
   - 3개씩 Data블럭이 복제되어 저장 - 이 때문에 장애가 생겨도 문제가 없고 대응력이 높아진다

### 빅데이터의 6V?

1. 진실성
2. 다양성
3. 가치
4. 시각화
5. 크기
6. 속도



## 데이터가 있는 곳에 로직을 옮겨라!

### 왜 대용량에 apache Hadoop이 적합한가?

1. 오픈 소스
2. I/O집중적이면서 CPU도 많이 사용
3. 데이터베이스는 하드웨어 추가시 성능 향상이 linear하지 않다.
4. 애플리케이션/트랜잭션 로그 정보는 매우 크다



### Hadoop 저장소

1. File System - batch, 스트림(sequencial)
   - HDFS,GFS, Object
2. Record(document) 구조 저장 -NoSQL

# 설치 방법

- Oracle.com 에서 Java SE Development Kit 8u221 를 다운받는다. 리눅스 x64버전으로
- hadoop-2.7.7 다운 받고
- eclipse-jee-photon-R-linux-gtk-x86_64 도 다운 받는다.

```
[hadoop@master ~]$ su -
Password: 
Last login: Wed Jul 31 13:04:07 EDT 2019 on pts/0
[root@master ~]# cd /usr/local
[root@master local]# pwd
/usr/local
[root@master local]# tar -xvf /home/hadoop/Downloads/jdk-8u221-linux-x64.tar.gz 
[root@master local]# chown -R hadoop:hadoop /usr/local/jdk1.8.0_221/
[root@master local]# ls -al


[root@master local]# tar -xvf /home/hadoop/Downloads/eclipse-jee-photon-R-linux-gtk-x86_64.tar.gz 
[root@master local]# ls -al
[root@master local]# chown -R hadoop:hadoop /usr/local/eclipse/
[root@master local]# ls –al

[root@master local]# tar -xvf /home/hadoop/Downloads/hadoop-2.7.7.tar.gz 
[root@master local]# chown -R hadoop:hadoop /usr/local/hadoop-2.7.7/
[root@master local]# ls –al

```

를 입력 하여 압축을 푼다. 

hostname이 master여야 한다. 밑의 코드를 이용하여 바꿔주자.

```
#Hostname 변경

CentOS를 처음 시작하면 다음과 같이 Hostname이 localhost로 설정됩니다.
관리해야될 서버가 한대라면 모르지만 여러대를 관리한다면 서버별로 hostname을 지정해 주는것이 좋다.
[root@master local]# hostname
을 실행하면 현재 hostname을 확인할 수 있습니다. 

hostname변경 방법은 일회성 변경과 영구적 변경 방법이 있습니다.
hostname 호스트네임 을 실행하고 hostname을 실행하면 변경된 hostname을 확인할 수 있습니다.
하지만 서버를 재시작 하는 경우 hostname이 기존 localhost로 변경될 것입니다
영구적으로  hostname을 변경하기 위해서는 
[root@master ~]# hostnamectl set-hostname  slave1
실행하면 서버가 재시장 되어도 변경된  hostname을 유지합니다.

서버를 재시작 하지 않아도 아래의 명령을 실행하고 실행중인 터미널을 닫고 다시 열면 hostname이 변경된것을 확인할 수 있습니다.
/bin/hostname -F /etc/hostname

```

### .bashrc 환경설정

-  특정 실행파일을 쉽게 실행하기 위해  . bash_profile에 환경변수를 추가하는데, 예를 들어  /usr/app/eclipse가 설피 되었을시 eclipse를 실행시 #//usr/app/eclipse/bin/eclipse 같은 방법으로 실행해야 하는데 간단하게 #eclipse만 입력해도 실행하고 싶을시! 환경변수 등록을 해준다. 그것이 (.bash_profile)

```cmd
[root@master local]# su hadoop
[hadoop@master local]$ cd ~
[hadoop@master ~]$ vi .bash_profile
[hadoop@master ~]$ source .bash_profile ::bash_profile 적용되도록 할때
[hadoop@master ~]$ hadoop version ::설치버전 확인
```

**path 등록**

- PATH에 필요폴더를 추가 하면 굳이 해당폴더 이동필요 없이,

- tab으로 그위치의 파일에 접근할 수있다.

- PATH=$PATH:$HOME/bin:[원하는 폴더 위치] 

  



![1565751662680](D:\gitgithub\STUDY\javaStudy\사진\하둡)

![1565751675465](D:\gitgithub\STUDY\javaStudy\사진\하둡2)





제대로 되었는지 확인한번 해보자~

1. 그후 모든 것을 끈 후 저장된 장소로 가서 가상파일을 복사한다. 전체를! 하나를 master, 하나는 slave로 저장
2. vmware 로 master를 실행하자. 실행시 위치와 이름이 바뀌었기 때문에 copied로 하자. 후에 tad 에 오른쪽 버튼을 눌러 셋팅에서 이름을 master로 이름변경하고 hostname이 master임을 확인하자
3. vmware로 slave를 실행하고, 똑같이 copied하고,  똑같이 tab에 오른쪽 버튼을 눌러 이름을 slave1로 셋팅하고 hostname을 slave1로 바꾸자. 
4. 이름을 바꾸는 것은 그저 헷갈릴까봐!
5. 그 후 위의    hostname 바꾸는 방식으로 각각 master 와  slave로 바꿔주자.

master ipaddress 192.168.255.130

- NameNode + DataNode2

slave1 ipaddress 192.168.255.129

- Secondary+DataNode1

마스터키로 하자 `su -`

```
[root@slave1 ~]# vi /etc/hosts
192.168.255.130  master
192.168.255.129  secondary
192.168.255.129  slave1
192.168.255.130  slave2
//master 와 slave둘다 바꿔준다.
```

### ssh 설정

ssh설정시 하둡 계정이 아니 마스터 계정으로 해주어야 하기 때문에 exit를 눌러 로그아웃 후 해준다.

![1565760279745](D:\gitgithub\STUDY\javaStudy\사진\하둡3)

slave 노드에 베포할 공개키를 인증키로 복사한다!

![1565760524822](D:\gitgithub\STUDY\javaStudy\사진\하둡4)

slave에서 인증키 설정한다

```
Hadoop  home 디렉토리아래 ssh 디렉토리 생성 후 접근 권한 변경
[hadoop@slave1 ~]$ mkdir .ssh
[hadoop@slave1 ~]$ chmod 755 ~/.ssh

master 서버에서 공개 키 분배
[hadoop@master ~]$ scp ~/.ssh/authorized_keys hadoop@192.168.50.129:./.ssh/

slave 노드에 인증 키 복제 되었는지 확인
[hadoop@slave1 ~]$ ls .ssh/

master 노드에서 테스트
[hadoop@master ~]$ ssh hadoop@master date
[hadoop@master ~]$ ssh hadoop@secondary date
[hadoop@master ~]$ ssh hadoop@slave1 date
[hadoop@master ~]$ ssh hadoop@slave2 date


```

만약 실수록 인증키를 만들었다면 rm id_rsa 

rm id_rsa.pub 혹은 rm -rf ./* 해주자

### 하둡 실행하는 쉘 스크립트 파일에서 필요한 환경변수 설정(여기서부터는 마스터계정에서만  하자~)



```
[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7/
[hadoop@master hadoop-2.7.7]$ cd etc/hadoop/
[hadoop@master hadoop]$ vi hadoop-env.sh

#자바 설치된 경로 확인 후 설정하세요
export JAVA_HOME=/usr/local/jdk1.8.0_221/


```

### slave를 설정한다

```
[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7/
[hadoop@master hadoop-2.7.7]$ cd etc/hadoop/
[hadoop@master hadoop]$ vi slaves

#slave 노드 host명 등록
slave1
slave2 
//localhost는 삭제하고 저장~


```

### core-site.xml

먼저 tmp 디렉토리를 만들어야 한다.

[hadoop@master hadoop]$ mkdir /usr/local/hadoop-2.7.7/tmp

그 후 

[hadoop@master hadoop]$ vi core-site.xml

```


<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://master:9000</value>
</property>
<property>
<name>hadoop.tmp.dir</name>
<value>/usr/local/hadoop-2.7.7/tmp</value>
</property>
</configuration>
```

로 저장

### hdfs-site.xml

vi hdfs-site.xml

```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.replication</name>
<value>1</value>
</property>
<property>
<name>dfs.permissions.enabled</name>
<value>false</value>
</property>
<property>
<name>dfs.secondary.http.address</name>
<value>secondary:50090</value>
</property>
</configuration>

```



### mapred-site.xml

저 파일이 없기때문에 복사해와서

[hadoop@master hadoop]$ cp  mapred-site.xml.template mapred-site.xml

[hadoop@master hadoop]$vi mapred-site.xml

```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
</configuration>
```

### yarn-site.xml

[hadoop@master hadoop]$vi yarn-site.xml

```
<?xml version="1.0"?>
<configuration>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
<value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
</configuration>
```

### 다른 노드 설정 파일 동기화

```
#마스터 노드에서
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/dfs
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/dfs/name
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/dfs/data
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/mapred
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/mapred/system
[hadoop@master ~]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/mapred/local
[hadoop@master ~]$ chmod 755 /usr/local/hadoop-2.7.7/tmp/dfs




[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7
[hadoop@master  hadoop-2.7.7]$ rsync -av . hadoop@slave1:/usr/local/hadoop-2.7.7

[hadoop@master  hadoop-2.7.7]$ rsync -av . hadoop@slave2:/usr/local/hadoop-2.7.7

[hadoop@master  hadoop-2.7.7]$ rsync -av . hadoop@secondary:/usr/local/hadoop-2.7.7


```

여기서 rsync 로 마스터계정에서 설정한 내용을 slave에  옮긴다! 그렇기에 마스터계정에서만 설정!



### 방화벽 설정

root 에서 ( su -)

yum install iptables-services-y 설치를 미리 하고

 위에것이 안된다면  [root@master ~]# yum -y install iptables-services  이리작성해주자.

아래를 dport 22 아래에 추가해 주어야 한다!

아래 있는 192.168.234.0/24 에서 0전 까지는 나의 ip를 작성해주도록 하자! 255였으므로 

192.168.255.0/24다

```
[root@master local]# vi /etc/sysconfig/iptables
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8088 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 50070 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 5432 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8032 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 12000 -j ACCEPT
-A INPUT -s 192.168.234.0/24 -d 192.168.234.0/24 -j ACCEPT
-A OUTPUT -s 192.168.234.0/24 -d 192.168.234.0/24 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT



```

[root@master local]# service iptables restart 작성해서 다시 시작해주자

slave1에도 같은 설정을 해주고 양쪽다 systemctl status iptables 로 active상태를 확인하자

### Namenode포맷을 해야한다!

```
#마스터 노드에서
[hadoop@master ~]$ hadoop  namenode  -format 

```

 su hadoop 하면 하둡으로 가지며

만약 위에께 안된다면 

[hadoop@master ~] $ source ~/.bash_profile 해주면 namenode포맷이 된다

### hadoop 시작

전체 한번에 시작시키는 명령어는

master의 namenode와 datanode2, slave의 secondary와 datanode1를 동시 시작!하기 위해서

```
#마스터 노드에서
[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7/sbin
[hadoop@master ~]$ ls
하면 다양한 명령어가 뜬다!
[hadoop@master sbin]$  ./start-all.sh
히스토리의 경우 따로 해주어야 실행이 된다. 허나 안해도 된다.(하지말자)
[hadoop@master sbin]$  ./mr-jobhistory-daemon.sh start historyserver
[hadoop@master sbin]$ jps

```

해서 확인해보자~ 

![1565772027387](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡5)

이리 나온 상태에서 (위에는 historyserver가 빠져있는데 안해도 된다

브라우저에서

http://master:50070/dfshealth.html 를 입력해보자

livenode 를 클릭해서 라이브노드가 2개임을 확인하자

### 종료하는 방법

```
[hadoop@master sbin]$ ./stop-all.sh
```



### 만약 확인시 라이브노드가 1개라면 다시 설정 해 볼 내용!

1. systemctl enable iptables 를 입력하여 actived상태인지 확인!(slave도!)

2. 그 후  systemctl  stop iptabels 한후 systemctl start optables 한다. 그 후 다시 하둡 실행!

   

3. 그래도 Live Node가 2개가 아닐 시 

먼저 master 와 slave둘다 

```java
[hadoop@master sbin]$ ./stop-all.sh
//먼저다 스탑!
[hadoop@slave .ssh]$ cd /usr/local/
[hadoop@slave hadoop-2.7.7]$ ls
[hadoop@slave hadoop-2.7.7]$ cd tmp
[hadoop@slave tmp]$ rm -rf *
[hadoop@slave tmp]$ cd ..
[hadoop@slave hadoop-2.7.7]$ ls
//tmp 아래의 정보만 삭제! master와 slave둘다!
//그후 마스터노드에서
[hadoop@master hadoop-2.7.7]$ hadoop namenode -format
[hadoop@master sbin]$ ./start-all.sh
 //시작한 후 slave 에서 tmp 파일 아래 자료가 생기는 것을 확인 후! 브라우저에서 live node가 2개임을 확인한다!

```



```
Live Node가 2개가 아닌경우 다시 설정해볼 내용
[hadoop@master hadoop-2.7.7]$ ls
#tmp 삭제
[hadoop@master hadoop-2.7.7]$ rm -rfR tmp
[hadoop@master hadoop-2.7.7]$ ls

#Slave1 노드에서도 삭제
[hadoop@slave1 hadoop-2.7.7]$ ls
bin  include  libexec      logs        README.txt  share
etc  lib      LICENSE.txt  NOTICE.txt  sbin        tmp
[hadoop@slave1 hadoop-2.7.7]$ rm -rfR tmp
[hadoop@slave1 hadoop-2.7.7]$ ls

#master 노드에서 tmp 디렉토리 다시 생성
[hadoop@master hadoop-2.7.7]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/dfs/name
[hadoop@master hadoop-2.7.7]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/dfs/data
[hadoop@master hadoop-2.7.7]$ ls -R /usr/local/hadoop-2.7.7/tmp

[hadoop@master hadoop-2.7.7]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/mapred/system
[hadoop@master hadoop-2.7.7]$ mkdir -p /usr/local/hadoop-2.7.7/tmp/mapred/local
[hadoop@master hadoop-2.7.7]$ ls -R /usr/local/hadoop-2.7.7/tmp

[hadoop@master hadoop-2.7.7]$rsync -av . hadoop@slave1:/usr/local/hadoop-2.7.7

[hadoop@master hadoop-2.7.7]$ cd etc/hadoop
[hadoop@master hadoop-2.7.7]$ rsync -av . hadoop@slave2:/usr/local/hadoop-2.7.7
[hadoop@master hadoop-2.7.7]$ rsync -av . hadoop@secondary:/usr/local/hadoop-2.7.7

[hadoop@master hadoop-2.7.7]$ rm -rf ./logs/yarn*
[hadoop@master hadoop-2.7.7]$ rm -rf ./logs/hadoop*

[hadoop@master ~]$ hadoop namenode -format

그 후 다시 생성하자
```



### 조심하자

#### 하둡 세이프모드 해제(비정상종료시 강제 세이프모드)

$ hadoop dfsadmin -safemode leave 

#### 시작시 서버 상태 확인해 보자

1. root 계정에서 `[root@master ~]# iptables -L`로 상태 확인
2. 자동으로 iptables에 접속 안되어있다면 firewalld를 끄자.(**주의점은 iptables가 안 연결 된 상태에서 firewalld 상태를  mark(끄게) 된다면 위험하다**)
3. `[root@master ~]# systemctl stop firewalld`
   `[root@master ~]# systemctl mask firewalld`
4. `[root@master ~]# systemctl status  firewalld` 로 꺼진 상태를 확인하자! 이제는 자동으로 iptables과 연결 될 것이다.





## 1. hadooop

### 1.1 하둡 분산 파일 시스템(HDFS)관리

**hadoop** **fs -옵션 …**

1. 파일 목록 보기 : ls, lsr
2. 파일 용량 확인 : du, dus
3. 파일 내용 보기 : cat, text
4. 디렉토리 생성 : mkdir
5. 파일 복사 : put, get, getmerge,  cp, copyFromLocal,  copyToLocal
6. 파일 이동 : mv, moveFromLocal
7. 카운트 값 조회 : count
8. 파일삭제, 디렉토리 삭제 : rm,  rmr
9. 파일의 마지막 내용 확인 : tail
10. 권한 변경 : chmod, chown,  chgrp
11. 0바이트파일 생성 : touchz
12. 통계 정보 조회 : stat
13. 복제 데이터 개수 변경 : setrep
14. 휴지통 비우기 : expunge
15. 파일 형식 확인 : test

```
[hadoop@master ~]$ hadoop fs mkdir /lab // 먼저 하둡에 파일 생성
[hadoop@master ~]$ vi test.txt
//내용 아무것이나 넣고 저장~(파일 생성한 것!)

[hadoop@master ~]$ hadoop fs -put ./test.txt /lab/
//하둡에 그 파일을 저장~

[hadoop@master ~]$ hadoop fs -ls /lab/
//저장된 파일 확인!

[hadoop@master ~]$ rm test.txt
[hadoop@master ~]$ ls
//로컬에서 삭제!

[hadoop@master ~]$ hadoop fs -get /lab/test.txt
[hadoop@master ~]$ ls
//하둡에서 파일 가져와서 다시 확인!


[hadoop@master ~]$ hadoop fs -rm /lab/test.txt
//하둡에서 그 파일을 삭제!

```



```
[hadoop@master ~]$ vi sample.txt 
//내용입력
[hadoop@master ~]$ vi sample2.txt
//내용입력

[hadoop@master ~]$ hadoop fs -put sampl* /lab/
//두개를 하둡에 올린다!
[hadoop@master ~]$ hadoop fs -ls /lab/
//잘 올라가있는지 확인!

[hadoop@master ~]$ hadoop fs -mkdir /data
[hadoop@master ~]$ hadoop fs -ls /
Found 2 items
drwxr-xr-x   - hadoop supergroup          0 2019-08-16 10:24 /data
drwxr-xr-x   - hadoop supergroup          0 2019-08-16 10:23 /lab

//data 디텍토리 생긴것을 확인!

[hadoop@master ~]$ hadoop fs -mv /lab/sample* /data/
//파일을 data디렉토리로 옮긴다!

[hadoop@master ~]$ hadoop fs -ls /lab
[hadoop@master ~]$ hadoop fs -ls /data
Found 2 items
-rw-r--r--   1 hadoop supergroup         27 2019-08-16 10:23 /data/sample.txt
-rw-r--r--   1 hadoop supergroup         22 2019-08-16 10:23 /data/sample2.txt
//옮겨진것을 확인하자

[hadoop@master ~]$ hadoop fs -getmerge /data/sample* ./sample3.txt
[hadoop@master ~]$ ls
Desktop    Downloads  Pictures  sample2.txt  sample.txt  test.txt
Documents  Music      Public    sample3.txt  Templates   Videos
[hadoop@master ~]$ cat sample3.txt
haha~ today is friday!!!!!
Tomorrow is saturday!

//두 파일이 합쳐져서 만들어진것을 확인할 수 있다!



```

### 1.2안전모드

하둡 실행 후 ^z 나 ^s와 같이 비정상 종료를 할 경우 hadoop은 safe모드로 진입한다. 이때는 파일 복사 삭제 등이 안된다.

### 1.3도구

###  1.4dfsadmin

hadoop dfsadmin -help 하면  다양한 관리 동작 명령어를 알 수 있다.

1. fsck : 파일 시스템 상태 체크
2. balancer : HDFS 재균형
3. deamonlog : 로그 레벨 동적 변경
4. dfsadmin : HDFS 상태 확인. HDFS 퇴거, DataNode 참가 등

### 1.5로깅

log4j는 

### 1.6클러스터에서 노드를 추가하기

1. nclude 파일에 새 노드의 네트워크 주소를 추가한다.
   - dfs.hosts와 mapreduce.jobtracker.hosts.filename속성을 통해 하나의 공유 파일을 참조한다.
2.  네임노드에 허가된 데이터 노드 집합을 반영한다.
   - `$ hadoop dfsadmin -refreshNodes`
3.  새로 허가된 태스크트래커 집합을 잡트래커에 반영한다.
   - `$ hadoop mradmin -refreshNodes`
4.  새 노드가 하둡 제어 스크립트에 의해 장차 클러스터에서 사용될 수 있게 slaves 파일을 갱신한다.
5.  새로운 데이터 노드와 대스크 트래커를 시작한다.
6.  새로운 데이터 노드와 태스크 트래커가 웹 UI에 나타나는지를 확인한다.

## 2. MapReduce Programming

1. MapReduce 프레임워크는 페타바이트 이상의 대용량 데이터를 신뢰할 수 없는 컴퓨터로 구성된 클러스터 환경에서 병렬 처리를 지원하기 위해서 개발되었습니다.

2. MapReduce프레임워크는 함수형 프로그래밍에서 일반적으로 사용되는 Map()과 Reduce() 함수 기반으로주로 구성

   - Map()은 (key, value) 쌍을 처리하여 또 다른 (key ,value) 쌍을 생성하는 함수입니다.
   - Reduce()는 맵(map)으로부터 생성된 (key, list(value)) 들을 병합(merge)하여 최종적으로 list(value) 들을 생성하는 함수입니다

   - 데이터 처리를 위한 프로그래밍 모델

   - 분산컴퓨팅에 적합한 함수형 프로그래밍

   - 배치형 데이터 처리 시스템

   - 자동화된 병렬처리 및 분산처리

   - Fault-tolerance(내고장성, 결함허용)

   - 프로그래머를 위한 추상클래스

   

### 2.1용어

1. 작업(Job)

- 데이터 집합을 이용하여 Mapper와 Reducer를 실행하는 "전체 프로그램“입니다.
- 20개의 파일로부터 "Word Count"를 실행하는 것은 1개의 작업(Job)입니다.

2. 태스크(Task)

- 1개의 데이터 조각을 처리하는 1개의 Mapper 또는 Reducer의 실행입니다.

- 20개의 파일은 20개의 Map 태스크에 의해 처리됩니다.

3. 태스크 시도(Task Attempt)

- 머신 위에서 1개의 태스크를 실행하는 특정 시도입니다.

- 최소한 20개의 Map 태스크 시도들이 수행됩니다. 서버 장애 시에는 더 많은 시도들이 수행됩니다.

4. Map

- 어떤 데이터의 집합을 받아들여 데이터를 생성하는 프로세스입니다.

- 주로 입력 파일을 한 줄씩 읽어서 filtering등의 처리를 수해

5. Reduce

- Map에 의해서 만들어진 데이터를 모아서 최종적으로 원하는 결과로 만들어 내는 프로세스입니다

- 데이터 집약 처리

6. 어떤 처리든 데이터는 키(key)와 밸류(value)의 쌍으로 이루어지고, 해당 쌍의 집합을 처리한다.

7. 입력 데이터도 출력 데이터도  key-value의 집합으로 구성된다.

8. Shuffle 

- Map 처리 후 데이터를 정렬해서, 같은 키를 가진 데이터를 같은 장소에 모은다.  

- 슬레이브 서버 간에 네트워크를 통한 전송이 발생한다



### 2.2이클립스 설치

```
su - 
//root 계정
cd /usr/local

tar -xvf /home/hadoop/Downloads/eclipse-jee-photon-R-linux-gtk-x86_64.tar.gz
ls -al (로 설치 확인)
chown -R hadoop:hadoop /usr/local/eclipse/
ls -al(로 그룹명 변화 확인)
```

![1566180247001](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡7)

```java

postgresql(추가해야하는 자르파일이다)
$HADOOP-HOME/share/hadoop/common/lib/common-cli-1.2.jar
$HADOOP-HOME/share/hadoop/common/hadoop-common-2.7.7.jar
$HADOOP-HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.7.7.jar
$HADOOP-HOME/share/hadoop/mapreduce/lib/log4j ~.jar






package lab.hadoop.fileio;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class SingleFileWriteRead {
  public static void main(String[] args) {
	// 입력 파라미터 확인
	if (args.length != 2) {
		System.err.println("Usage: SingleFileWriteRead <filename> <contents>");
			System.exit(2);
		}

	try {
		// 파일 시스템 제어 객체 생성
		Configuration conf = new Configuration();
		FileSystem hdfs = FileSystem.get(conf);

		// 경로 체크
		Path path = new Path(args[0]);
		if (hdfs.exists(path)) {
			hdfs.delete(path, true);
		}

		// 파일 저장
		FSDataOutputStream outStream = hdfs.create(path);
		outStream.writeUTF(args[1]);
		outStream.close();

		// 파일 출력
		FSDataInputStream inputStream = hdfs.open(path);
		String inputString = inputStream.readUTF();
		inputStream.close();

		System.out.println("## inputString:" +inputString);
                . System.out.println(path.getFileSystem(conf).getHomeDirectory()); //hdfs 홈 경로
 System.out.println(path.toUri()); //패스의 파일명
 System.out.println(path.getFileSystem(conf).getUri().getPath());

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

```

export 해서 jar파일을 이름을 fileio.jar 로 해서 home 에 저장하자

```
Hello hadoop HDFS[hadoop@master ~]$ hadoop jar ./fileio.jar test.txt "Hello hadoop HDFS"

[hadoop@master ~]$ hadoop fs -ls -R /

[hadoop@master ~]$ hadoop fs -cat test.txt 
//확인해보자!!! 잘 나오는가!?
```

### 2.3WordCount 프로그래밍 순서(reducer)

```java
package lab.hadoop.wordcount;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WordCountMapper  extends Mapper<LongWritable, Text, Text, IntWritable>{
	private final static IntWritable one=new IntWritable(1);
	private Text word=new Text();
	

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		
		StringTokenizer itr=new StringTokenizer(value.toString());
		while(itr.hasMoreTokens()) {
			word.set(itr.nextToken());
			context.write(word, one);
		}
	}

}

```



```java
package lab.hadoop.wordcount;

import java.io.IOException;


import org.apache.hadoop.io.IntWritable;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer  extends Reducer<Text, IntWritable, Text, IntWritable>{
	private final static IntWritable result=new IntWritable();
	
	

	
	protected void reduce(Text key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException {
		
		
		int sum=0;
		for(IntWritable val: values) {
			sum+= val.get();
		}
		result.set(sum);
		context.write(key,result);
	}	

}

```



```java
package lab.hadoop.wordcount;



import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class WordCount {

	public static void main(String[] args) throws Exception {
		Configuration conf= new Configuration();
		if(args.length !=2) {
			System.err.println("Usage: WordCount <input> <output>");
			System.exit(2);
		}
		Job job=new Job(conf, "WordCount");
		
		job.setJarByClass(WordCount.class);
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputValueClass(TextOutputFormat.class);
	
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		//file system control object making
		FileSystem hdfs =FileSystem.get(conf);
		
		//route check
		Path path= new Path(args[1]);
		if(hdfs.exists(path)) {
			hdfs.delete(path,true);
		}
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		job.waitForCompletion(true);
	}

}

```

![1565938606745](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡6)

이 과정을 실험해 보았따!

```
[hadoop@master ~]$ hadoop jar ./WordCount.jar /data/input.txt /output/

[hadoop@master ~]$ hadoop fs -ls -R /output
[hadoop@master ~]$ hadoop fs -cat /output/part-r-00000
로 확인해보자!!!!!
```

### 2.4항공기 정보 정리해보기(연습1)

1. http://stat-computing.org/dataexpo/2009/the-data.html 에서 2007년과 2008년의 .csv파일 다운

2. 압축 풀기

   - [hadoop@master Downloads]$ bunzip2 ./2007.csv.bz2
   - [hadoop@master Downloads]$ bunzip2 ./2008.csv.bz2

3. 하둡에 파일을 만들기

   - [hadoop@master ~]$ hadoop fs -mkdir /data/airline 
   - [hadoop@master ~]$ hadoop fs -put ./Downloads/2008.csv  /data/airline/
   - [hadoop@master ~]$ hadoop fs -ls /data/airline  (하둡에 넣은 파일 확인해보자)
   - [hadoop@master ~]$ hadoop fs -mkdir /output/airline
   - [hadoop@master ~]$ hadoop fs -ls /output

4. 이클립스에서 작업

   ```java
   package lab.hadoop.airline;
   
   import java.io.IOException;
   
   import org.apache.hadoop.io.IntWritable;
   import org.apache.hadoop.io.LongWritable;
   import org.apache.hadoop.io.Text;
   import org.apache.hadoop.mapreduce.Mapper;
   
   
   
   public class DepartureDelayCountMapper extends 
   	Mapper<LongWritable, Text, Text, IntWritable> {
   		
   	//map 출력값(value)
   		private final static IntWritable outputValue = new IntWritable(1);
   	//map 출력키(key)
   		private Text outputKey = new Text();
   	
   public void map(LongWritable key, Text value, Context context) throws IOException,InterruptedException {
   	if( key.get()>0) {
   		//콤마 구분자 분리
   		String[] colums = value.toString().split(",");
   		if(colums != null && colums.length >0) {
   			try{
   				//출력키 설정
   				outputKey.set(colums[0]+ "," +colums[1]);
   				if(!colums[15].equals("NA")) {
   					int depDelayTime =Integer.parseInt(colums[15]);
   					if(depDelayTime >0) {
                           //출력데이터 설정
   						context.write(outputKey,outputValue);
   					}
   						
   					}
   				}catch(Exception e) {
   					e.printStackTrace();
   				}
   		}
   	}
   }
   }
   ```

   ```java
   package lab.hadoop.airline;
   
   import java.io.IOException;
   
   import org.apache.hadoop.io.IntWritable;
   import org.apache.hadoop.io.Text;
   import org.apache.hadoop.mapreduce.Reducer;
   
   public class DelayCountReducer extends Reducer<Text,IntWritable, Text, IntWritable> {
   	private IntWritable result =new IntWritable();
   	//
   	public void reduce(Text key, Iterable<IntWritable>values, Context context)throws IOException, InterruptedException{
   		int sum=0;
   		for(IntWritable value: values)
   			sum+= value.get();
   		result.set(sum);
   		context.write(key, result);
   	}
   
   }
   
   ```

5. 출력할 드라이브 설정

   ```java
   package lab.hadoop.airline;
   
   
   
   import org.apache.hadoop.conf.Configuration;
   import org.apache.hadoop.fs.FileSystem;
   import org.apache.hadoop.fs.Path;
   import org.apache.hadoop.io.IntWritable;
   import org.apache.hadoop.io.Text;
   import org.apache.hadoop.mapreduce.Job;
   import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
   import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
   import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
   import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
   
   public class DepartureDelayCount {
   
   	public static void main(String[] args) throws Exception {
   		Configuration conf= new Configuration();
   		
   		if(args.length !=2) {
   			System.err.println("Usage: DepartureDelayCount <input> <output>");
   			System.exit(2);//셀 커맨드 잘못 사용시 종료!
   		}
   		FileSystem hdfs=FileSystem.get(conf);
   		//route check 
   				//경로 체크
   				Path path= new Path(args[1]);
   				if(hdfs.exists(path)) {
   					hdfs.delete(path,true);
   				}
   				
   		//job 이름 설정
   		Job job=new Job(conf, "DepartureDelayCount");
   		//입출력 데이터 경로 설정
   		FileInputFormat.addInputPath(job, new Path(args[0]));
   		FileOutputFormat.setOutputPath(job, new Path(args[1]));
   		//job 클래스 설정
   		job.setJarByClass(DepartureDelayCount.class);
           //mapper클래스 설정
   		job.setMapperClass(DepartureDelayCountMapper.class);
           //Reducer 클래스 설정
   		job.setReducerClass(DelayCountReducer.class);
   		
           //입출력 데이터 포맷 설정
   		job.setInputFormatClass(TextInputFormat.class);
   		job.setOutputValueClass(TextOutputFormat.class);
   	    //출력키 및 출력값 유형 설정
   		job.setOutputKeyClass(Text.class);
   		job.setOutputValueClass(IntWritable.class);
   		
   		job.waitForCompletion(true);
   	}
   
   }
   
   ```

6. 아카이브를 만들자

   - 먼저 이클립스에서 자르파일로 export하고 export 저장위치는 home아래 (main class설정! 자동으로 뜬다)
   - [hadoop@master ~]$ hadoop jar ./departure.jar /data/airline  /output/airline
   - [hadoop@master ~]$ hadoop fs -ls /output/airline(파일 완료 확인)
   - [hadoop@master ~]$ hadoop fs -cat /output/airline/part-r-00000(이것으로 누적 합계를 확인!)



### 2.5 연습2

```java
package lab.hadoop.delaycount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DelayCountMapper extends Mapper<LongWritable,Text , Text, IntWritable>{
    //<입력키 유형, 입력값 유형, 출력키 유형, 출력값 유형>을 의미


	private String workType;
	private Text outputKey =new Text();
	private final static IntWritable outputValue= new IntWritable(1);


	@Override
	protected void setup(Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {//setup은 Mapper class에서 작업시작히 한번 호출 되는 메서드

		workType=context.getConfiguration().get("workType");
	}
	
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{//입력 분할에서 각 키 / 값 쌍마다 한 번씩 호출된다.
		if (key.get()>0) {
			String[] colums=value.toString().split(",");
			if(colums !=null && colums.length>0) {
				try {
					if(workType.equals("departure")) {//실행시 옵션을 줄때 그것이 departure인가?
						if(!colums[15].equals("NA")){
							int depDelayTime=Integer.parseInt(colums[15]);
							if(depDelayTime>0) {
								outputKey.set(colums[0]+","+colums[1]);
                                //colums[0]=year colums[1]=month
                                //출력 데이터 생성
								context.write(outputKey, outputValue);
							}
						}
                        //도착 지연 데이터 출력
					}else if(workType.equals("arrival")) {//실행시 옵션을 줄때 그것이 arrival 인가?
						if(!colums[14].equals("NA")) {
							int arrDelayTime=Integer.parseInt(colums[14]);
							if(arrDelayTime>0) {
                                //출력키 설정
								outputKey.set(colums[0]+","+colums[1]);
                                //출력 데이터 생성
								context.write(outputKey, outputValue);
							}
						}
					}
				}catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
}

```



```java
package lab.hadoop.delaycount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class DelayCountReducer extends Reducer<Text,IntWritable, Text, IntWritable> {
	private IntWritable result =new IntWritable();
	
	public void reduce(Text key, Iterable<IntWritable>values, Context context)throws IOException, InterruptedException{
		int sum=0;
		for(IntWritable value: values)
			sum+= value.get();
		result.set(sum);
		context.write(key, result);
	}

}

```



```java
package lab.hadoop.delaycount;



import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class DelayCount extends Configured implements Tool{
	
	public int run(String[] args) throws Exception{
	
		String[] otherArgs=new GenericOptionsParser(getConf(),args).getRemainingArgs();
		//입추력 데이터 경로 확
		if(args.length !=2) {
			System.err.println("Usage: DelayCount <in> <out>");
			System.exit(2);
		}
		//job이름 설정 
		Job job=new Job(getConf(), "DelayCount");
		
		FileSystem hdfs=FileSystem.get(getConf());
		//route check 
				//경로 체크
				Path path= new Path(args[1]);
				if(hdfs.exists(path)) {
					hdfs.delete(path,true);
				}
		//입출력 데이터 경로 설
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		//job클래스 설
		job.setJarByClass(DelayCount.class);
		job.setMapperClass(DelayCountMapper.class);
		job.setReducerClass(DelayCountReducer.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputValueClass(TextOutputFormat.class);
	
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.waitForCompletion(true);
        //실행시키는 코드!
		return 0;
	}
	public static void main(String[] args)throws Exception{
		//Tool 인터페이스 실행
		int res=ToolRunner.run(new Configuration(),new DelayCount(),args);
		System.out.println("##RESULT:"+res);
	}
}

```

- 실행해 보자
- [hadoop@master ~]$ hadoop fs -mkdir /output/delaycount
- [hadoop@master ~]$ hadoop jar ./delaycount.jar -D workType=arrival /data/airline /output/delaycount
  - 여기서 -D workType 은 처음 Mapper class 시 주었던 것 arrival 로
- [hadoop@master ~]$ hadoop fs -mkdir /output/delaycount2
- [hadoop@master ~]$ hadoop jar ./delaycount.jar -D workType=departure /data/airline  /output/delaycount2
  - 이번에는 -D workType =departure로 해보자.

## 3. 정렬(sorting)

1. 맵리듀스의 핵심 기능
2. 하나의 리듀스 테스크만 실행되게 하면 쉽게 해결 가능 하지만, 여러 데이터 노드가 구성된 상황에서 하나의 리듀스 테스크만 실행하는 것은 분산 환경의 장점을 살리지 못하는 것!
3. 대량의 데이터를 정렬시 부하도 상당함
4. 하둡이 제공하는 정렬 방식
   - 보조 정렬, 부분정렬, 전체 정렬

### 3.1 보조 정렬

1. 키의 값들을 그룹핑하고, 그룹핑된 레코드에 순서를 부여
2. 구현 순서
   - 기존 키의 값들을 조합한 복합키(Composite Key)정의
   - 키의 값 중에서 그룹핑 키로 사용할 키 결정
   - 복합키의 레코드를 정렬하기 위한 비교기(comparator)정의
   - 그룹핑 키를 파티셔닝할 파티셔녀(partitioner)정의
   - 그룹 핑 키를 정렬하기 위한 비교기(Comparator)정의

```java
package lab.hadoop.sort;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableUtils;

public class DateKey implements WritableComparable<DateKey> {
	//년, 월을 키로 사용할 것(년은 문자여도 월의 경우 숫자로 해야 정렬된다..?)
	///직렬하기 위한
	private String year;
	private Integer month;
	public DateKey() {
		
	}
	public DateKey(String year, Integer month) {
		super();
		this.year = year;
		this.month = month;
	}
	@Override
	public void readFields(DataInput in) throws IOException {
		year=WritableUtils.readString(in);
		month=in.readInt();
		
	}
	@Override
	public void write(DataOutput out) throws IOException {
		WritableUtils.writeString(out, year);
		out.writeInt(month);
		
	}
	@Override
	public int compareTo(DateKey key) {
		int result = year.compareTo(key.year);
		if(0==result) {
			result=month.compareTo(key.month);
			
		}
		return result;
		
	}
	public String getYear() {
		return year;
	}
	public void setYear(String year) {
		this.year = year;
	}
	public Integer getMonth() {
		return month;
	}
	public void setMonth(Integer month) {
		this.month = month;
	}
/*	@Override
	public String toString() {
		return (new StringBuilder()).append(year).append(",").append(month).toString();
		
	}*/
	@Override
	public String toString() {
		return "DateKey [year=" + year + ", month=" + month + "]";
	}
	
	
	
	
}

```



```java
package lab.hadoop.sort;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;

public class DateKeyComparator extends WritableComparator{
	protected DateKeyComparator() {
		super(DateKey.class,true);
	}
	@SuppressWarnings("rawtypes")
	@Override
	public int compare(WritableComparable w1, WritableComparable w2) {
		//복합키 클래스 캐스팅
		
		DateKey k1=(DateKey) w1;
		DateKey k2=(DateKey) w2;
		
		//연도 비교
		int cmp=k1.getYear().compareTo(k2.getYear());
		if(cmp !=0) {
			return cmp;
			
		}
		///월 비교
		return k1.getMonth() == k2.getMonth() ? 0:(k1.getMonth()<k2.getMonth() ? -1:1);
	}
	
}

```

그룹핑 키의 파티셔널~

``` java
package lab.hadoop.sort;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Partitioner;

public class GroupKeyPartitioner extends Partitioner<DateKey, IntWritable>{

	@Override
	public int getPartition(DateKey key, IntWritable val, int numPartitions) {
		
		int hash=key.getYear().hashCode();
		int partition=hash % numPartitions;
		return partition;
	}
}
```

그룹핑 키의 비교기(comparator)

```java
package lab.hadoop.sort;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;

public class GroupKeyComparator extends WritableComparator{
protected GroupKeyComparator() {
	super(DateKey.class,true);
}
@SuppressWarnings("rawtypes")
@Override
public int compare(WritableComparable w1, WritableComparable w2) {
	
DateKey k1=(DateKey)w1;
DateKey k2 =(DateKey)w2;
//연도값 비교
return k1.getYear().compareTo(k2.getYear());
}
}

```

enum(상수)

```java
package lab.hadoop.sort;

public enum DelayCounters {
not_available_arrival,
scheduled_arrival,
early_arrival,
not_available_departure,
scheduled_departure,
early_departure;
}

```



reducer

```java
package lab.hadoop.sort;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;

public class DelayCountReducerWithDateKey extends Reducer<DateKey,IntWritable,DateKey,IntWritable>{
	//병렬로 여러개의 아웃풋 을 생성하는 것!
	private MultipleOutputs<DateKey,IntWritable>mos;
	//reduce출력키
	private DateKey outputKey=new DateKey();
	//reduce 출력
	private IntWritable result=new IntWritable();
	
	@Override
	protected void setup(Context context)
			throws IOException, InterruptedException {
	mos=new MultipleOutputs<DateKey,IntWritable>(context);
	}
	public void reduce(DateKey key,Iterable<IntWritable> values,Context context)throws IOException,InterruptedException{
		//콤마 구분자 분리
		String[] colums =key.getYear().split(",");
		
		int sum =0;
		Integer bMonth=key.getMonth();
		
		if(colums[0].equals("D")) {
			for(IntWritable value:values) {
				if (bMonth !=key.getMonth()) {
					result.set(sum);
					outputKey.setYear(key.getYear().substring(2));
					outputKey.setMonth(bMonth);
					mos.write("departure", outputKey, result);
					sum=0;
				}
				sum+=value.get();
				bMonth=key.getMonth();
			}
			if(key.getMonth()==bMonth) {
				outputKey.setYear(key.getYear().substring(2));
				outputKey.setMonth(key.getMonth());
				result.set(sum);
				mos.write("departure", outputKey, result);
			}
		}else {
			for(IntWritable value:values) {
				if(bMonth !=key.getMonth()) {
					result.set(sum);
					outputKey.setYear(key.getYear().substring(2));
					outputKey.setMonth(bMonth);
					mos.write("arrival", outputKey, result);
					sum=0;
				}
				sum+=value.get();
				bMonth=key.getMonth();
			}
			if(key.getMonth()==bMonth) {
				outputKey.setYear(key.getYear().substring(2));
				outputKey.setMonth(key.getMonth());
				result.set(sum);
				mos.write("arrival", outputKey, result);
			}
				}
			}
	@Override
	protected void cleanup(Context context)
			throws IOException, InterruptedException {
		mos.close();
	}
	
		
	}


```



mapper

```java
package lab.hadoop.sort;


import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DelayCountMapperWithDateKey extends Mapper<LongWritable,Text,DateKey,IntWritable> {

	//map출력값
	private final static IntWritable outputValue=new IntWritable(1);
	//
	private DateKey outputKey =new DateKey();
	
	public void map(LongWritable key,Text value,Context context)throws IOException,InterruptedException{
		if (key.get()>0) {
			//콤마 구분자 분리
			String[] colums=value.toString().split(",");
			if(colums !=null&&colums.length>0) {
				try {
					//출발지연 제이터 출력
					if(!colums[15].equals("NA")) {
						int depDelayTime=Integer.parseInt(colums[15]);
						if(depDelayTime>0) {
							//출력키 설정 
							outputKey.setYear(("D,"+colums[0]));
							outputKey.setMonth(new Integer(colums[1]));
							//출력데이터 생성
							context.write(outputKey, outputValue);
						}else if(depDelayTime==0) {
							context.getCounter(DelayCounters.scheduled_departure).increment(1);
						}else if(depDelayTime<0) {
							context.getCounter(DelayCounters.early_departure).increment(1);
						}
					}else {
						context.getCounter(DelayCounters.not_available_departure).increment(1);
					}
					//도착 지연 데이터 출력
					if(!colums[14].equals("NA")) {
						int arrDelayTime=Integer.parseInt(colums[14]);
						if(arrDelayTime>0) {
							//출력키 설정 
							outputKey.setYear(("A,"+colums[0]));
							outputKey.setMonth(new Integer(colums[1]));
							//출력데이터 생성
							context.write(outputKey, outputValue);
						}else if(arrDelayTime==0) {
							context.getCounter(DelayCounters.scheduled_arrival).increment(1);
						}else if(arrDelayTime<0) {
							context.getCounter(DelayCounters.early_arrival).increment(1);
						}
					}else {
						context.getCounter(DelayCounters.not_available_arrival).increment(1);
					}
					
				}catch(Exception e) {
					e.printStackTrace();
				}
				
			}
		}
	}
}

```

driver

```java
package lab.hadoop.sort;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import lab.hadoop.delaycount.DelayCount;

public class DelayCountwithDateKey extends Configured implements Tool{
	public int run(String[] args) throws Exception{
		
		String[] otherArgs=new GenericOptionsParser(getConf(),args).getRemainingArgs();
		//입추력 데이터 경로 확
		if(args.length !=2) {
			System.err.println("Usage: DelayCountwithDateKey <in> <out>");
			System.exit(2);
		}
		//job이름 설정 
		Job job=new Job(getConf(), "DelayCountWithDateKey");
		
		FileSystem hdfs=FileSystem.get(getConf());
		//route check 
				//경로 체크
				Path path= new Path(args[1]);
				if(hdfs.exists(path)) {
					hdfs.delete(path,true);
				}
		//입출력 데이터 경로 설
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		//job클래스 설
		job.setJarByClass(DelayCountwithDateKey.class);
		job.setPartitionerClass(GroupKeyPartitioner.class);
		job.setGroupingComparatorClass(GroupKeyComparator.class);
		job.setSortComparatorClass(DateKeyComparator.class);
		
		//Mapper클래스 설정
		job.setMapperClass(DelayCountMapperWithDateKey.class);
		//Reducer클래스 설
		job.setReducerClass(DelayCountReducerWithDateKey.class);
		
		job.setMapOutputKeyClass(DateKey.class);
		job.setMapOutputValueClass(IntWritable.class);
		
		//입출력 데이터 포맷 설정
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
	
	
		//출력키 및 출력값 유형 설정 
		job.setOutputKeyClass(DateKey.class);
		job.setOutputValueClass(IntWritable.class);
		//MultipleOupputs 설정
		MultipleOutputs.addNamedOutput(job, "departure", TextOutputFormat.class, DateKey.class, IntWritable.class);
		MultipleOutputs.addNamedOutput(job, "arrival",TextOutputFormat.class,DateKey.class , IntWritable.class);
		
		
		job.waitForCompletion(true);
		return 0;
	}
	public static void main(String[] args)throws Exception{
		//Tool 인터페이스 실행
		int res=ToolRunner.run(new Configuration(),new DelayCountwithDateKey(),args);
		System.out.println("##RESULT:"+res);
	}

}

```

### 복습

#### 1. 분산 컴퓨팅

- 어플리케이션이 한 host에서만 수행이 되는 것이 아닌 client의 요청에 의해 다양한(두개 이상의) host에 요청 처리가 되는 것을 분산 컴퓨팅이라 한다.
- 조건
  1. 장애 허용(노드 중 하나가 비정상적 작동해도 메인 시스템에 부정적 영향 없다)
  2. 복구능력(분산 클러스터 노드에서 수행중인 작업이 실패해도 손실 발생 없다.)
  3. 선형적 확장성(컴퓨팅 능력, 스토리지 공간 확장등,성능도 선형적으로 증가)

#### 2. 하둡 아키텍처

- HDFS, Yarn , MapReduce, API

#### 3. 하둡 클러스터

- 하둡 분산파일 시스템(HDFS)과 클러스서 리소스 매니저(Yarn)를 기반으로 하는 하둡 소프트웨어를 사용하는 컴퓨터들의 집합 (ex 야후의 경우 이런 클러스터가 1만개 이상)

- hadoop2.0부터 마스터 노드 2개 이상 구성가능하며 이로인해 고가용성 지원가능(Active, Standby) 하며 주 키퍼도 함께 구성을 해야한다

- **마스터노드 + 워커노트(slave 노드)**로 구성

  - 마스터노트(Active,Standby) 

    > 하둡 클러스터의 작업을 중재
    >
    > 하둡 클라이언트는 파일을 저장, 읽고, 처리하려면 master노드에 접속해야한다.
    >
    > namenode 구성해서 파일 시스템의 메타정보를 읽고 쓰는 작업 처리(namenode는 프로세스라 생각하면 된다.)
    >
    > JobTracker는 mapreduce 작업을 중재하는 프로세스, Datanode에 task 할당

  - 워커노트 (slave node)

    > 마스터 노드의 지시를 받아 명령을 수행(실제 데이터를 저장, 데이터를 처리 프로세싱하는 노드), 워커 노드에서 실행되며 애플리케이션을 분산처리 태스크를 담당하는 에이전트로 실제 작업을 담당하는 것이 **executor**

- HDFS 는 HDFS의 스토리지를 관리&구성

  - Namenode

    > HDFS 파일 시스템 디렉토리 트리와 파일의 위치등 HDFS스토리지 관련 메타 정보(블럭 데이터와 데이터 노드에 매핑)를 관리
    >
    > 파일 , 디렉토리, 생성, 열기, 쓰기 오퍼레이션 수행
    >
    > 어떤 데이터 노드에 복제되고, 복제 후 삭제 할지 결정
    >
    > 데이터 노드에서 보내온 하트비와 블럭 리포트를 처리(블럭 위치 유지, 데이터 노드의 상태 관리)

  - SecondaryNameNode

    > 한 시간 간격 으로 Http 프로토콜을 이용해서 메모리에 있는 FS이미지를 가져오고 기록된 edit log를 결합하여 새로운 FS이미지를 만들어서 교체하는 작업을 한다. 즉 *업데이트 관리* (fsimage파일과 editlog파일을 merge한다 라고 표현)

  - DataNode

    > 마스터 노드에 접속 유지, 3초 간격으로 heartbit , block report를 주기적으로 전송, 마스터 노드의 요청을 처리(block 저장=청크,block 삭제),로컬 파일 시스템에 블럭을 저장, 데이터에 대한 읽기, 쓰기 수행, 데이터 블럭 생성 및 삭제 수행, 클러스터에 데이터 블럭 복제

  - Yarn(하둡운영시스템)

    > **리소스 매니저 (resouce manager)**는 마스터 노드에서 실행, 클러스터의 리소르를 나눠주는 역할, TaskTracker들의 Task를 스케줄링
    >
    > **노드 매니저(node manager) **는 워커 노드에서 실행, Task들을 실행시키고 관리, Task실행을 위해서  resource manager와 밀접하게 통신, Task 상태 관리, 노드 상태 관리, map reduce job이 hadoop에 제출되어 수행 시작하고 수행 끝나면 종료되는 데몬이다.
    >
    > **어플리케이션 매니저(application manager)** 클러스터에서의 메인프로세스로 어플리케이션별로 하나씩 실행, 클러스터에서 실행되는 어플리케이션의 실행조율, 리소스 매니저와 밀접하게 통신하며 리소스 관리 

- 하둡 클러스터에서 장애 허용과 복구 능력을 위해 sharding(분산), replication(복제)수행

- 배치 처리, 파일 기반 처리(map의 처리 결과도 map처리된 datanode에 저장, reducer의 출력결과도 hdfs에 저장,disk기반, stream기반, sequential하게 처리)

### 복습 끝

***

먼저 준비하자.

1. `[hadoop@master sbin]$ ./start-all.sh ` 하둡 실행
2. `[hadoop@master sbin]$ ./mr-jobhistory-daemon.sh  start historyserver` 히스토리 실행
3. `[hadoop@master sbin]$ jps `확인!

### 3.2 사이드 조인

1. 맵 사이드 조인

-  setup 메서드에서 조인될 데이터를 준비합니다.
-  Hashtable을 전역변수로 선언하고 Hashtable에 데이터를 저장함
-  읽어들일 데이터가 분산캐시에 등록되어 있어야 함
- ​    파일의 유형에 따라 등록하는 파일이 다름
-  map 메서드에서 write할 때 Hashtable의 값을 키로 저장합니다.
-  실행하기 전에 분산캐시로 사용할 파일을 HDFS 에 업로드 해야 함
- 조인될 데이터를 setup 메서드에서 Hashtable에 저장
- 조인될 데이터가 많을 경우 Hashtable에 저장되는 데이터의 증가로 성능 저하 우려리듀스 사이드 조인

2. 리듀스 사이드 조인

-  두 개의 데이터를 키/값으로 출력합니다.
-  조인될 키를 구분하기 위해 키 뒤에 임의의 문자 추가해서 출력
-  ex)
-  WN_A(항공운항통계 데이터의 항공사 코드)
-  WN_B(항공사 코드 데이터의 항공사 코드)
-  리듀스에서 출력 시 추가된 문자열에 따라 다른 키의 값을 키로 저장
-  _A가 붙어있으면 키를 WN_B의 값으로 저장
- 조인될 데이터의 키와 조인할 데이터의 키에 두 키를 구분할 수 있는 문자열을 추가하여 맵의 출력으로 보냄
- 리듀서에서 키에 따라 다른 키의 값으로 대체

### 3.3 연습(맵 사이드 조인)

1. http://stat-computing.org/dataexpo/2009/supplemental-data.html 로 들어가 carriers.csv 파일을 다운로드

2.  파일생성

   - [hadoop@master ~]$ hadoop fs -mkdir /data/metadata
   - [hadoop@master ~]$ hadoop fs -ls /data
   - [hadoop@master ~]$ hadoop fs -put ./Downloads/carriers.csv  /data/metadata
   - [hadoop@master ~]$ hadoop fs -ls /data/metadata

3. 이클립스에서 mapper 만들면 된다! reducer필요없다

   ```java
   import java.io.BufferedReader;
   import java.io.FileReader;
   import java.io.IOException;
   import java.util.Hashtable;
   
   import org.apache.hadoop.filecache.DistributedCache;
   import org.apache.hadoop.fs.Path;
   import org.apache.hadoop.io.LongWritable;
   import org.apache.hadoop.io.Text;
   import org.apache.hadoop.mapreduce.Mapper;
   
   public class MapperWithMapsideJoin extends
   		Mapper<LongWritable, Text, Text, Text> {
   
   	private Hashtable<String, String> joinMap 
   	                     = new Hashtable<String, String>();
   
   	// map 출력키
   	private Text outputKey = new Text();
   
   	@Override
   	public void setup(Context context) throws IOException, 
   	                                       InterruptedException {
   		try {
   			// 분산캐시 조회
   			Path[] cacheFiles = DistributedCache.getLocalCacheFiles(context
   					.getConfiguration());
   			// 조인 데이터 생성
   			if (cacheFiles != null && cacheFiles.length > 0) {
   				String line;
   				String[] tokens;
   				BufferedReader br = new BufferedReader(new FileReader(
   						cacheFiles[0].toString()));
   				try {
   					while ((line = br.readLine()) != null) {
   						tokens = line.toString().replaceAll("\"", "")
   								.split(",");
   						joinMap.put(tokens[0], tokens[1]);
   					}
   				} finally {
   					br.close();
   				}
   			} else {
   				System.out.println("### cache files is null!");
   			}
   		} catch (IOException e) {
   			e.printStackTrace();
   		}
   	}
   
   	public void map(LongWritable key, Text value, Context context)
   			throws IOException, InterruptedException {
   
   		if (key.get() > 0) {
   			// 콤마 구분자 분리
   			String[] colums = value.toString().split(",");
   			if (colums != null && colums.length > 0) {
   				try {
   					outputKey.set(joinMap.get(colums[8]));
   					context.write(outputKey, value);
   				} catch (Exception e) {
   					e.printStackTrace();
   				}
   			}
   		}
   	}
   
   ```

drive 클래스



```java
package lab.hadoop.join;



import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class MapsideJoin extends Configured implements Tool {

	public int run(String[] args) throws Exception {
		String[] otherArgs = new GenericOptionsParser(getConf(), args)
				.getRemainingArgs();
		// 입력출 데이터 경로 확인
		if (otherArgs.length != 3) {
			System.err.println("Usage: MapsideJoin <metadata> <in> <out>");
			System.exit(2);
		}
		
		Configuration conf = new Configuration();

		// 파일 시스템 제어 객체 생성
		FileSystem hdfs = FileSystem.get(conf);
		// 경로 체크
		Path path = new Path(args[2]);
		if (hdfs.exists(path)) {
			hdfs.delete(path, true);
		}
		
		// Job 이름 설정
		Job job = new Job(getConf(), "MapsideJoin");

		// 분산 캐시 설정
		DistributedCache.addCacheFile(new Path(otherArgs[0]).toUri(),
				job.getConfiguration());

		// 입출력 데이터 경로 설정
		FileInputFormat.addInputPath(job, new Path(otherArgs[1]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[2]));

		// Job 클래스 설정
		job.setJarByClass(MapsideJoin.class);
		// Mapper 설정
		job.setMapperClass(MapperWithMapsideJoin.class);
		// Reducer 설정
		job.setNumReduceTasks(0);

		// 입출력 데이터 포맷 설정
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		// 출력키 및 출력값 유형 설정
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		job.waitForCompletion(true);
		return 0;
	}

	public static void main(String[] args) throws Exception {
		// Tool 인터페이스 실행
		int res = ToolRunner.run(new Configuration(), new MapsideJoin(), args);
		System.out.println("## RESULT:" + res);
	}
}

}

```

데이터를 3개를 받도록 한다< metadata>< in>< out> 이렇게 세개!

- `[hadoop@master ~]$ hadoop fs -mkdir /output/mapjoin`

- `[hadoop@master ~]$ hadoop jar ./mapjoin.jar  /data/metadata/carriers.csv /data/airline  /output/mapjoin ` 

  > < metadata> < in> < out> 이 순서로 jar해주자~

  

### 3.4 연습(리듀스 사이드 조인)

```java
package lab.hadoop.join;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CarrierCodeMapper extends Mapper<LongWritable,Text,Text,Text>{
//태크 선언
	public final static String DATA_TAG="A";
	
	private Text outputKey= new Text();
	private Text outputValue=new Text();
	
	public void map(LongWritable key, Text value,Context context)throws IOException,InterruptedException{
		if(key.get()>0) {
			String[] colums =value.toString().replaceAll("\"", "").split(",");
			if(colums != null&&colums.length>0) {
				outputKey.set(colums[0]+"_"+DATA_TAG);
				outputValue.set(colums[1]);
				context.write(outputKey, outputValue);
			}
		}
	}
}

```



```java
package lab.hadoop.join;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperWithReducesideJoin extends Mapper<LongWritable,Text,Text,Text>{
//태크 선언
	public final static String DATA_TAG="B";
	
	//map출력
	private Text outputKey= new Text();
	
	
	public void map(LongWritable key, Text value,Context context)throws IOException,InterruptedException{
		if(key.get()>0) {
			String[] colums =value.toString().split(",");
			if(colums != null&&colums.length>0) {
				try {
				outputKey.set(colums[8]+"_"+DATA_TAG);
				context.write(outputKey, value);
			}catch(Exception e) {
				e.printStackTrace();
			}
			}
		}
	}
}

```

reducer

```java
package lab.hadoop.join;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

public class ReducerWithReducesideJoin extends Reducer<Text,Text,Text,Text>{

	//reducer출력키
	private Text outputKey= new Text();
	private Text outputValue=new Text();
	
	public void reduce(Text key, Iterable<Text>values,Context context)throws IOException,InterruptedException{
		//태크조회
		String tagValue=key.toString().split("_")[1];
		for(Text value :values) {
			///출력키 설정
		
		if(tagValue.equals(CarrierCodeMapper.DATA_TAG)) {
			outputKey.set(value);
			//출력값 설정 및 출력 데이터 생성
		}else if(tagValue.equals(MapperWithReducesideJoin.DATA_TAG)) {
			outputValue.set(value);
			context.write(outputKey, outputValue);
		}
		
			}
		}
	}


```

driver class

```java
package lab.hadoop.join;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class ReducesideJoin extends Configured implements Tool{


		public int run(String[] args) throws Exception {
			String[] otherArgs = new GenericOptionsParser(getConf(), args)
					.getRemainingArgs();
			// 입력출 데이터 경로 확인
			if (otherArgs.length != 3) {
				System.err.println("Usage: ReducesideJoin <metadata> <in> <out>");
				System.exit(2);
			}
			
			Configuration conf = new Configuration();

			// 파일 시스템 제어 객체 생성
			FileSystem hdfs = FileSystem.get(conf);
			// 경로 체크
			Path path = new Path(args[2]);
			if (hdfs.exists(path)) {
				hdfs.delete(path, true);
			}
			
			// Job 이름 설정
			Job job = new Job(getConf(), "ReducesideJoin");
			
			//출력 데이터 경로 설정
			FileOutputFormat.setOutputPath(job, new Path(otherArgs[2]));
			
			// 분산 캐시 설정
			DistributedCache.addCacheFile(new Path(otherArgs[0]).toUri(),
					job.getConfiguration());

			

			// Job 클래스 설정
			job.setJarByClass(ReducesideJoin.class);
			
			// Reducer 설정
			job.setReducerClass(ReducerWithReducesideJoin.class);

			// 입출력 데이터 포맷 설정
			job.setInputFormatClass(TextInputFormat.class);
			job.setOutputFormatClass(TextOutputFormat.class);

			// 출력키 및 출력값 유형 설정
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(Text.class);
			
			//MultipleInputs 설정
			MultipleInputs.addInputPath(job, new Path(otherArgs[0]), TextInputFormat.class,CarrierCodeMapper.class);
			MultipleInputs.addInputPath(job, new Path(otherArgs[1]), TextInputFormat.class,MapperWithReducesideJoin.class);

			job.waitForCompletion(true);
			return 0;
		}

		public static void main(String[] args) throws Exception {
			// Tool 인터페이스 실행
			int res = ToolRunner.run(new Configuration(), new ReducesideJoin(), args);
			System.out.println("## RESULT:" + res);
		}
	

	}


```

- `[hadoop@master ~]$ hadoop fs -mkdir /output/reducejoin`
- `[hadoop@master ~]$ hadoop fs -ls /output/reducejoin`
- `[hadoop@master ~]$ hadoop jar ./reducejoin.jar  /data/metadata/carriers.csv  /data/airline  /output/reducejoin`
- `[hadoop@master ~]$ hadoop fs -ls /output/reducejoin`
- `[hadoop@master ~]$ hadoop fs -cat /output/reducejoin/part-r-00000`

## 4. HIVE

1. OLTP- transaction 처리 목적 
   - DML-> DW(data warehouse)로 이관(ETL) 작업, 분석 쿼리
   - select를 통해 데이터 요약정리
2. OLAP

### 4.1 Hive를 통해 MapReduce를 실행

1. "SQL"기반의 하둡 에코 시스템을 HIVE라 한다.
2. 다소 복합한 "MR 프로그래밍"이 보다 친근하고, 직관적인 "SQL"지원
3. 다이나믹한 검색 조건 지정(다시 jar압축 할 필요 없다)
4. 매번 "Name Node"배포 없이 원격에서"MR job"실행 지원

#### 4.1.1 Hive 내장모드

1. 설정 변경을 하지 않는 기본 구성
2. DBMS로 Derby를 이용
3. 혼자서 테스트 용도로 사용하기에 적합한 구성

#### 4.1.2 Hive 로컬 모드

1. Hive 클라이언트와 메타스토어로부터 DBMS를 독립시킨 것
2. DBMS는 JDBC를 통해 접속
3. 로컬 모드에서는 다수의 접속을 동시에 허용하지만 Hive클라이언트가 모드 같은 노드에 존재

#### 4.1.3 Hive 원격 모드

1. DBMS뿐만 아니라 메타스토어도 독립시킨 구성
2. 메타스토어도 독립됐기에 직렬화 통신(?)필요
3. Hive클라이언트가 Thrift API를 경유해서 원격으로 메타스토어에 접속가능 

#### 4.1.4 HiveQL 

1. SQL유사 언어로써 MapReduce실행하는 것이다
2. 페이스북 멤버 중심으로 개발 진행 중
3. HiveQL이 취급하는 데이터는 논리적 행과 열과 이루어진 테이블로 HDFS상에 파일로 존재
4. HiveQL로 기술한 쿼리는 MapReduce 같은 일련의 처리로 변환되어 테이블로 조작
5. 컴파일 없이 바로 실행 가능하므로, Ad-hoc처리에 적합
6. Hive는 테이블 정의 등의 정보를 Metastore로 관리하며, 테이블 Meta정보를 저장하기 위해 RDBMS가 필요

#### 4.1.5 Hive의  RDBMS와 다른 차이점

1. 온라인 처리에 부적합
2. 인텍스 및 트랜잭션 기능이 없다
3. 콜백 처리가 없다
4. MapReduce의 Keep.failed.task.files파라미터는 MapReduce잡이 실패하면 MapReduce프레임워크 중간 파일은 종료시에 삭제되도록 초기 설정
5. Hive에는 Update나 Delete문이 없다.

#### 4.1.6 Hive 데이터

1. Hive데이터는 HDFS상의 파일로 존재, Hive테이블은 HDFS디렉토리로 존재
2. Hive 데이터베이스나 스키마도 HDFS상의 디렉토리로 존재 (/user/hive/warehouse/테이블명 디렉터리로 존재)
3. Hive에서 컬럼이나 속성 등 테이블 실체가 아닌, 속성 정보에 해당하는 테이블 정의는 Metastore라 불리며, RDBMS에 저장
4. Hive의 테이블 정의에서는 파티션이라 불리는 물리적 관리 단위 지정
5. 파티션은 HDFS 상의 디렉토리를 분할 하는 것과 같다
6. 파티션을 설정함으로 처리 범위 제어 가능, 처리 고속화 가능
7. 파티션 내의 모든 데이터가 필요 없어지면, 파티션 단위로 삭제 할수 있어 관리 수월, 백업, 분할, 등등 가능
8. HiveQL의 흐름은 Hive쿼리문 앞에 EXPLAIN을 붙여 실행하면 확인 가능(실행계획 확인 가능)
9. HiveQL은 Stage라는 단위로 MapReduce나 부속 처리로 변환하여, Stage간 의존 관계가 생성

https://cwiki.apache.org/confluence/display/Hive/LanguageManual

- HiveQL이 기술되어 있다.

### 4.2 설치

##### 4.2.1 다운로드

http://www.apache.org/dyn/closer.cgi/hive/에서 apache-hive-1.2.2-bin.tar.gz를 찾거나

http://apache.tt.co.kr/hive/hive-1.2.2/ 에서 apache-hive-1.2.2-bin.tar.gz 다운로드

```cmd
[hadoop@master ~]$ cd Downloads/
[hadoop@master Downloads]$ wget http://apache.tt.co.kr/hive/hive-1.2.2/apache-hive-1.2.2-bin.tar.gz
#이리 해도 다운 가능! 
```

##### 4.2.2 압축 풀기

```cmd
#root계정에서
[root@master local]# tar -xzvf /home/hadoop/Downloads/apache-hive-1.2.2-bin.tar.gz 
#압축풀고! 소유자를 바꾸어 주자
[root@master local]# chown -R hadoop:hadoop apache-hive-1.2.2-bin/
[root@master local]# ls -l
#확인 하고 심볼릭 링크 만들어서 이름 짧게!(바로가기)
[root@master local]# ln -s apache-hive-1.2.2-bin hive
[root@master local]# ls -l
#소유자 바꾸기
[root@master local]# chown -R hadoop:hadoop hive
[root@master local]# ls -l
drwxr-xr-x.  8 hadoop hadoop 159 Aug 20 16:51 apache-hive-1.2.2-bin
drwxr-xr-x.  2 root   root     6 Apr 11  2018 bin
drwxrwxr-x.  8 hadoop hadoop 191 Aug 20 15:55 eclipse
drwxr-xr-x.  2 root   root     6 Apr 11  2018 etc
drwxr-xr-x.  2 root   root     6 Apr 11  2018 games
drwxr-xr-x. 11 hadoop hadoop 172 Aug 16 17:14 hadoop-2.7.7
lrwxrwxrwx.  1 hadoop hadoop  21 Aug 20 16:53 hive -> apache-hive-1.2.2-bin
drwxr-xr-x.  2 root   root     6 Apr 11  2018 include
drwxr-xr-x.  7 hadoop hadoop 245 Jul  4 20:37 jdk1.8.0_221
drwxr-xr-x.  2 root   root     6 Apr 11  2018 lib
drwxr-xr-x.  2 root   root     6 Apr 11  2018 lib64
drwxr-xr-x.  2 root   root     6 Apr 11  2018 libexec
drwxr-xr-x.  2 root   root     6 Apr 11  2018 sbin
drwxr-xr-x.  5 root   root    49 Aug 13 13:12 share
drwxr-xr-x.  2 root   root     6 Apr 11  2018 src
#이리 나오게 되며 ls apache-hive-1.2.2-vin 이나 ls hive 나 값이 같음을 확인할 수 있다!(바로가기임으로)



```

##### 4.2.3 환경변수 설정

```cmd
#마스터에서 hadoop 환경설정 파일 변경
[root@master local]# su - hadoop
[hadoop@master ~]$ vi .bash_profile

export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HIVE_HOME/bin:
[hadoop@master ~]$ source .bash_profile
#소스 실행
```

##### 4.2.4 hive 메타스토어 mysql 구성(로컬 모드)

http://repo.mysql.com/ 에sql-community-release-el6-5.noarch.rpm

과 https://downloads.mysql.com/archives/c-j/ 에서 mysql-connector-java-5.1.36.tar.gz 다운로드

```cmd
[hadoop@master Downloads]$ unzip mysql.zip
#압출 풀기

#마스터 노드에 hive 메타스토어 mysql 구성 (로컬모드)
[root@master ~]# rpm -ivh /home/hadoop/Downloads/mysql-community-release-el6-5.noarch.rpm
#위치가 다르다면 다르게 해서 하자~ 
[root@master ~]#  ls -la /etc/yum.repos.d/
[root@master ~]# yum install mysql-server

[root@master ~]# ls /usr/bin/mysql
#있는지 확인 (실행파일이다)
[root@master ~]# ls /usr/sbin/mysqld
#있는지 확인(서버 실행 파일)
[root@master ~]#  service mysqld start
#터미널에서 mysql를 실행

[root@master ~]# mysql --version
#클라이언트로 버전을 확인!
[root@master ~]# netstat -anp | grep mysql
#포트 번호를 mysql에서 사용하는지 확인하는 것
```

##### 4.2.5 mysql 실행

```cmd
[root@master ~]# mysql
#mysql실행
#루트 사용자의 암호를 설정한다.
 
mysql> grant all privileges on *.* to hive@localhost identified by 'hive' with grant option;  
mysql> show databases;
mysql> use mysql;
mysql> show tables;
mysql> select user from user;
mysql> flush privileges; #보통은 insert,delete,update를 통해 사용자를 추가, 삭제, 권한 변경 등을 수행할 때 이를 반영하기 위해 사용 , grant테이블을  reload함으로 변경사항 즉시 반영

```

##### 4.2.6 Hive-env.sh 설정파일 생성 및 변경

```cmd
#하둡 계정으로
# hive-env.sh  설정파일 생성 및 변경
[hadoop@master ~]$ cd /usr/local/hive/conf/
[hadoop@master ~]$ cp hive-env.sh.template  hive-env.sh
[hadoop@master ~]$ vi hive-env.sh
HADOOP_HOME=/usr/local/hadoop-2.7.7
#주석처리되어 있기 때문에 #를 지우고 위의 경로를 작성해준다.
[hadoop@master ~]$  chmod 755 hive-env.sh 
#권한을 바꿔준다!



```

##### 4.2.7 설정파일 변경

```xml
# /usr/local/hive/conf/hive-site.xml을 수정
[hadoop@master ~]$ vi /usr/local/hive/conf/hive-site.xml
<!--파일이 없기 때문에 새로 만들어 주자. -->
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
<property>
  <name>hive.metastore.local</name>
  <value>true</value>
</property>
<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:mysql://localhost:3306/metastore_db?createDatabaseIfNotExist=true</value>
  <description>JDBC connect string for a JDBC metastore</description>
</property>
<property>
  <name>javax.jdo.option.ConnectionDriverName</name>
  <value>com.mysql.jdbc.Driver</value>
  <description>Driver class name for a JDBC metastore</description>
</property>
<property>
  <name>javax.jdo.option.ConnectionUserName</name>
  <value>hive</value>
  <description>username to use against metastore database</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionPassword</name>
  <value>hive</value>
  <description>password to use against metastore database</description>
</property> 
  </configuration>
퍄
```

##### 4.2.8 metastore로 사용할 database 생성 및 metastore에 스키마 생성

```cmd
[hadoop@master ~]$ su -
[root@master ~] mysql -u root -p
Enter password:
mysql> show databases;
mysql> CREATE DATABASE metastore_db;

mysql> USE metastore_db;
mysql> show tables;
mysql> SOURCE /usr/local/hive/scripts/metastore/upgrade/mysql/hive-schema-1.1.0.mysql.sql;
mysql> show tables;
```

##### 4.2.9hive에서 mysql 커넥터를 위해(jdbc 드라이버)

```cmd
[hadoop@master ~]$ tar -xvf ./Downloads/mysql-connector-java-5.1.36.tar.gz
[hadoop@master ~]$ ls
[hadoop@master ~]$ cd  /home/hadoop/mysql-connector-java-5.1.36/
[hadoop@master ~]$ cp  mysql-connector-java-5.1.36-bin.jar /usr/local/hive/lib/
```



##### 4.2.10 하둡 실행과 hive연동 확인

```cmd
#하둡 시작
[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7/sbin
[hadoop@master ~]$ ./start-all.sh

#hive 실행
[hadoop@master ~]$ hive
hive> show databases;
hive> create database test_db;#데이터베이스생성
hive> use test_db;
hive> create table test(name varchar(10)); # 테이블 생성
hive> describe test; #테이블 확인
#실제로 하둡에 디렉토리가 생성되었나 확인해보자
[hadoop@master ~]$ hadoop fs -ls -R /user/
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 09:27 /user/hive
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 09:27 /user/hive/warehous      e
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 09:52 /user/hive/warehous      e/test_db.db
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 09:52 /user/hive/warehous      e/test_db.db/test
#생성되었음을 확인한다 생성됨을 확인하고 mysql에서 테이블 확인!
mysql> use metastore_db;
mysql> select OWNER,TBL_NAME,TBL_TYPE from TBLS;
+--------+----------+---------------+
| OWNER  | TBL_NAME | TBL_TYPE      |
+--------+----------+---------------+
| hadoop | test     | MANAGED_TABLE |
+--------+----------+---------------+
1 row in set (0.00 sec)

mysql>  select OWNER_NAME, OWNER_TYPE, NAME from DBS;
+------------+------------+---------+
| OWNER_NAME | OWNER_TYPE | NAME    |
+------------+------------+---------+
| public     | ROLE       | default |
| hadoop     | USER       | test_db |
+------------+------------+---------+
2 rows in set (0.00 sec)

#hive에서 테이블을 삭제하고
[hadoop@master ~]$ hadoop fs -ls -R /user/hive/warehouse/
hive> drop database test_db cascade;
hive> use default;
hive> show tables;
#하둡에 파일을 확인하면 없어진 것을 확인할 수 있다! 연동 확인@
[hadoop@master ~]$ hadoop fs -ls -R /user/
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 09:27 /user/hive
drwxr-xr-x   - hadoop supergroup          0 2019-08-21 10:03 /user/hive/warehouse


```



### 4.3 hiveQL

1. 운영체제 명령어를 ! 와 함께 사용 가능

```cmd
hive> !ls /home/hadoop/; #OS  명령어 사용 가능
hive> !hadoop fs -ls /data; ##하둡 명령어 사용 가능
```

2. Hive 테이블에 데이터를 등록할 때는 입력 데이터가 파일 시스템 상에 있으면 LOAD,  Hive 테이블이면 INSERT를 이용
3. Hive 테이블 데이터를 파일 시스템 상의 파일로 출력할 때도 INSERT문을 이용

```sql
LOAD  DATA  [LOCAL]  INPATH   ‘<파일 경로>’  [OVERWRITE]   INTO  TABLE   <테이블명>  [PARTITION  (partcol1 = val1, partcol2=col2,…)]

INSERT  OVERWRITE  TABLE  <테이블명>  [PARTITION  (partcol1 = val1, partcol2=col2,…)]     [IF  NOT  EXISTS]]  <SELECT구>  FROM  <FROM 구> ;

```

4. HiveQL은  JOIN,  서브쿼리, UNION ALL을 지원한다.
5. GROUP BY는  Reduce에서 처리하지만, Map에서 처리하도록 명시적으로 지정할 수 있다.  Map 태스크의  메모리 사용량이 늘어날 가능성이 있지만, Map에서 집계할 수 있으므로 Reduce로 보내는 전송량을 줄 일 수 있다.
6. Map에서 GROUP BY를 실행하려면  hive.map.agg 속성을 true로 한다
7. ORDER BY로 출력 결과 전체를 정렬할  때는 reducer 수가 하나로 제한한다.
8. SORT BY를 지정하면  Reducer를 다수 동작시킬 수 있으며, 처리 결과를 Reducer내에 정렬한다.

#### 4.3.1 sort by (p228)

sort by 는 hadoop의 shuffle정렬 기능 이용, shuffle 은 reduce처리 단위로 실행되기 때문에 select문과 같이 모든 데이터를 정렬한 결과를 얻을 수 있따.

```sql
SELECT  col1  FROM  table1  SORT BY col1  ASC;

```

틀정 행을 어떤 Reducer로 보낼지 제어하고 싶을 때 cluster by



#### 4.3.2 연습(외부데이터 이용하여 정렬)

database 생성

```cmd
# external table은 구조는 db에 안에 내용은 외부 에서 불러오는 것!
hive> create database airline_db;
CREATE EXTERNAL TABLE airline (
Year string,
Month string,
DayofMonth string,
DayOfWeek string,
DepTime string,
CRSDepTime string,
ArrTime string,
CRSArrTime string,
UniqueCarrier string,
FlightNum string,
TailNum string,
ActualElapsedTime string,
CRSElapsedTime string,
AirTime string,
ArrDelay string,
DepDelay string,
Origin string,
Dest string,
Distance string,
TaxiIn string,
TaxiOut string,
Cancelled string,
CancellationCode string,
Diverted string,
CarrierDelay string,
WeatherDelay string,
NASDelay string,
SecurityDelay string,
LateAircraftDelay  string
)
ROW FORMAT DELIMITED
 FIELDS TERMINATED BY ',' 
 LINES TERMINATED BY '\n'
LOCATION '/data/airline/';
hive> show tables; ##확인
# 월별 도착지연횟수를 출력하는 select문
hive> SELECT Year,Month, count(DepDelay)
      FROM airline
      GROUP BY Year,Month
      SORT BY Year,Month;   #reducer 별 처리 데이터 정렬, 전체 결과 정렬되지 않음


hive> SELECT Year,Month, count(DepDelay)
      FROM airline
      GROUP BY Year,Month
      ORDER BY Year,Month;   #reducer개수 1개로 제한, 전체 정렬
```

#### 4.3.3 연습2(외부데이터 overwrite)

```sql
[hadoop@master ~]$ vi /home/hadoop/dept.txt 
10,'ACCOUNTING','NEW YORK'
20,'RESEARCH','DALLAS'
30,'SALES','CHICAGO'
40,'OPERATIONS','BOSTON'
--위의 내용을 dept.txt에 써준다.

hive> CREATE TABLE IF NOT EXISTS dept (
deptno INT, dname STRING, loc STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
-- 테이블 생성
hive> describe dept
--확인

hive> load data local inpath '/home/hadoop/dept.txt' 
      overwrite into table dept;
--내용 테이블에 넣고
hive> select  * from dept;
--넣어졋는지 확인해보자! 
--외부에 있는 데이터를 db에 구조를 만들고 넣어주는 것
hive> !hadoop fs -ls -R /user/hive/warehouse/;
hive> !hadoop fs -cat /user/hive/warehouse/airline_db.db/dept/dept.txt;
--확인 완료~

```

#### 4.3.4 연습3(3. airline테이블과 carriers테이블의 조인 결과를 airlineinfo 테이블에 로딩)

```cmd
hive> INSERT  OVERWRITE  TABLE  airlineinfo 
 select  a.UniqueCarrier ,
   b.CarrierFullName ,
   a.FlightNum,
   a.TailNum ,
   a.Dest ,
   a.Distance ,
   a.Cancelled 
 from  airline a , carriers b  
where a.UniqueCarrier = substr(b.UniqueCarrier2, 2);
#허나 이것은 3글자는 지워지므로 다른 명령어로 해보자
```

### 4.3 Hadoop R 연동

1. R의 다양한 패키지는 CRAN(http://cran.r-project.org/web/views/)을 통해 한곳에서 살펴 볼 수 있다.

2. R은 공개 소프트웨어로 http://www.r-project.org/에서 다운 가능!

3. 또는 하둡에서 설치 가능

   ```cmd
   [root@master ~]# yum install epel-release
   [root@master ~]# yum install npm
   [root@master ~]# yum install R
   
   #R설치 디렉토리
   [root@master ~]# ls -l /usr/lib64/
   #R확인 가능 소유자가 R임으로 바꿔준다.
   [root@master ~]# chown -R hadoop:hadoop /usr/lib64/R
   [root@master ~]# chown -R hadoop:hadoop /usr/share/doc/R-3.6.0/html/
   
   [root@master ~]# ls -l /usr/lib64/
   
   
   #hadoop의 .bash_profile에 추가
   [hadoop@master ~]$ vi .bash_profile
   
   export HADOOP_CMD=/usr/local/hadoop-2.7.7/bin/hadoop
   export HADOOP_STREAMING=/usr/local/hadoop-2.7.7/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar
   #bash)_profile 소스 실행해야 한다.
   [hadoop@master ~]$ source ./.bash_profile
   [hadoop@master ~]$ R #해주면 들어가진다
   
   #R에서 패키지 설치해야한다.
   >install.packages(c("rJava", "Rcpp", "RJSONIO", "bitops", "digest", "functional", "stringr", "plyr", "reshape2", "caTools"))
   # 만약 중간 에러가 생기면 해결 후 
   >update.packages() 
   
   
   ```

   

https://github.com/RevolutionAnalytics/RHadoop/wiki/Downloads

에서 for windows뺴고 다 받아주자 그 후 R 에서 설치!

```R
> install.packages("/home/hadoop/Downloads/rhdfs_1.0.8.tar.gz", repos=NULL, type="source")

>install.packages("/home/hadoop/Downloads/rmr2_3.3.1.tar.gz", repos=NULL, type="source")
>install.packages("/home/hadoop/Downloads/plyrmr_0.6.0.tar.gz", repos=NULL, type="source")
>install.packages("/home/hadoop/Downloads/rhbase_1.2.1.tar.gz", repos=NULL, type="source")

>install.packages("/home/hadoop/Downloads/ravro_1.0.4.tar.gz", repos=NULL, type="source")

>install.packages(c("bit64", "rjson"))

```



#### 4.3.1 Hadoop R 연습

```cmd
[hadoop@master ~]$ vi test.R

#작성해보자
print("R running~ from source");
a <- seq(1,100,by=2)
print(class(a))
print(a)

[hadoop@master ~]$ cat test.R
#확인
#R에서 실행해보자
>source ("/home/hadoop/test.R")

#다른 실행방법!
>getwd()
#하면 현재 경로가 뜬다 (/home/hadoop/) 이므로
>source("test.R")
#라 쳐도 결과가 나온다!
```

#### 4.3.2 연습

```R
>setwd("디렉토리명")
> sum(1,NA,2)
[1] NA
> sum (1, 2, NA, na.rm=T)
[1] 3 #na.rm=T는 na를 삭제한다는 의믜 그러므로 3이 나온다.
> sum (1, NULL, 2)
[1] 3


```

#### 4.3.3 연습(1부터 1000까지의 숫자를 생성/각 숫자 모두를 제곱하는 연산 수행)

home/hadoop 위치에서 test2.R로 작성

```R
library(rhdfs) # Rhadoop package for hdfs
hdfs.init()    # Start to connect HDFS, 반드시 rmr2를 로드하기 전
library(rmr2)  # RHadoop package for MapReduce

hadoop fs -mkdir /tmp/ex1

 dfs.rmr("/tmp/ex1")
 small.ints <- to.dfs(1:1000, "/tmp/ex1")

 result <- mapreduce(input = small.ints, 
	map = function(k,v) cbind(v,v^2)
)
 out <- from.dfs(result)
print( out)

```

`>`source ("test2.R")로 실행해보자

#### 4.3.4 연습

/home/hadoop 위치에 

[hadoop@master ~]$ vi mapreduce_test.R 

```R
brary(rhdfs) # Rhadoop package for hdfs
hdfs.init()    # Start to connect HDFS, 반드시 rmr2를 로드하기 전
library(rmr2)  # RHadoop package for MapReduce 
random <- to.dfs(rnorm(100))
map <- function(k,v) {
        key <- ifelse(v < 0, "less", "greater")
        keyval(key, 1)
}
reduce <- function(k,v) {
        keyval(k, length(v))
}
Freq <- mapreduce (
        input= random, output="/tmp/ex3",
        map = map, reduce = reduce
)
out <- from.dfs(Freq)
print(out)

```

작성 후 

`>`resource("mapreduce_test.R")

#### 4.3.5 연습

hadoop fs -put /usr/local/hadoop-2.7.7/README.txt /tmp/ex3

```R
library(rhdfs) # Rhadoop package for hdfs
hdfs.init()    # Start to connect HDFS, 반드시 rmr2를 로드하기 전
library(rmr2)  # RHadoop package for MapReduce
 
inputfile <- "/tmp/README.txt"
if(!hdfs.exists(inputfile)) stop("File is not found")
outputfile <- "/tmp/ex4"
if(hdfs.exists(outputfile)) hdfs.rm(outputfile)
 
map <- function(key, val){
	words.vec <- unlist(strsplit(val, split = " "))
	#lapply(words.vec, function(word) 
    keyval(words.vec, 1)
}
 
reduce <- function(word, counts ) {
	keyval(word, sum(counts))
}
result <- mapreduce(input = inputfile,
	output = outputfile, 
	input.format = "text", 
	map = map, 
	reduce = reduce, 
	combine = T
)
 
## wordcount output
freq.dfs <- from.dfs(result)
freq <- freq.dfs$val
word <- freq.dfs$key
oidx <- order(freq, decreasing=T)[1:10]
 
# Words frequency plot
barplot(freq[oidx], names.arg=word[oidx] )

```

## Swap 공간 늘리기

```cmd
[root@master ~]# mkdir swap
[root@master ~]# dd if=/dev/zero of=swap/swapfile bs=1024 count=4194304
[root@master ~]# ls
#swap파일 확인
[root@master ~]# cd swap
#mkswap 명령어를 이용하여 swapfile이 스왑공간을 쓰도록 만든다. (스왑 영역 생성)
[root@master ~]#  mkswap swapfile

 
#스왑파일을 즉시 활성화 할 수 있다.
[root@master ~]# swapon swapfile
[root@master ~]# swapon -s  
[root@master ~]# free
```



#### 4.3.6 연습





