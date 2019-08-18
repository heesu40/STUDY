# hadoop

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



### Oracle

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

# .bashrc 환경설정

-  특정 실행파일을 쉽게 실행하기 위해  . bash_profile에 환경변수를 추가하는데, 예를 들어  /usr/app/eclipse가 설피 되었을시 eclipse를 실행시 #//usr/app/eclipse/bin/eclipse 같은 방법으로 실행해야 하는데 간단하게 #eclipse만 입력해도 실행하고 싶을시! 환경변수 등록을 해준다. 그것이 (.bash_profile)

```cmd
[root@master local]# su hadoop
[hadoop@master local]$ cd ~
[hadoop@master ~]$ vi .bash_profile
[hadoop@master ~]$ source .bash_profile ::bash_profile 적용되도록 할때
[hadoop@master ~]$ hadoop version ::설치버전 확인
```





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

## ssh 설정

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

vi core-site.xml 에 가서



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

[hadoop@master ~] $ source ~/.bash_profile 해주면 위에것이 된다

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

1. systemctl enable iptables 를 입력하여 activedt상태인지 확인!(slave도!)

Live Node가 2개가 아닐 시 

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







## hadooop

### 하둡 분산 파일 시스템(HDFS)관리

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

### 안전모드

하둡 실행 후 ^z 나 ^s와 같이 비정상 종료를 할 경우 hadoop은 safe모드로 진입한다. 이때는 파일 복사 삭제 등이 안된다.

### 도구

###  dfsadmin

hadoop dfsadmin -help 하면  다양한 관리 동작 명령어를 알 수 있다.

1. fsck : 파일 시스템 상태 체크
2. balancer : HDFS 재균형
3. deamonlog : 로그 레벨 동적 변경
4. dfsadmin : HDFS 상태 확인. HDFS 퇴거, DataNode 참가 등

### 로깅

log4j는 

### 클러스터에서 노드를 추가하기

1. nclude 파일에 새 노드의 네트워크 주소를 추가한다.
   - dfs.hosts와 mapreduce.jobtracker.hosts.filename속성을 통해 하나의 공유 파일을 참조한다.
2.  네임노드에 허가된 데이터 노드 집합을 반영한다.
   - `$ hadoop dfsadmin -refreshNodes`
3.  새로 허가된 태스크트래커 집합을 잡트래커에 반영한다.
   - `$ hadoop mradmin -refreshNodes`
4.  새 노드가 하둡 제어 스크립트에 의해 장차 클러스터에서 사용될 수 있게 slaves 파일을 갱신한다.
5.  새로운 데이터 노드와 대스크 트래커를 시작한다.
6.  새로운 데이터 노드와 태스크 트래커가 웹 UI에 나타나는지를 확인한다.

## MapReduce Programming

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

   

### 용어

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



### 이클립스 설치

```
su - 
//root 계정
cd /usr/local

tar -xvf /home/hadoop/Downloads/eclipse-jee-photon-R-linux-gtk-x86_64.tar.gz
ls -al (로 설치 확인)
chown -R hadoop:hadoop /usr/local/eclipse/
ls -al(로 그룹명 변화 확인)
```



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



####  WordCount 프로그래밍 순서

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

