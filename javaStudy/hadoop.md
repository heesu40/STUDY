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
[root@master local]# su hadoop
[hadoop@master local]$ cd ~
[hadoop@master ~]$ vi .bash_profile

![1565751662680](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡)

![1565751675465](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡2)

제대로 되었는지 확인한번 해보자~

1. 그후 모든 것을 끈 후 저장된 장소로 가서 가상파일을 복사한다. 전체를! 하나를 master, 하나는 slave로 저장
2. vmware 로 master를 실행하자. 실행시 위치와 이름이 바뀌었기 때문에 copied로 하자. 후에 tad 에 오른쪽 버튼을 눌러 셋팅에서 이름을 master로 이름변경하고 hostname이 master임을 확인하자
3. vmware로 slace를 실행하고, 똑같이 copied하고,  똑같이 tab에 오른쪽 버튼을 눌러 이름을 slave1로 셋팅하고 hostname을 slave1로 바꾸자. 

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

![1565760279745](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡3)

slave 노드에 베포할 공개키를 인증키로 복사한다!

![1565760524822](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡4)

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

### 하둡 실행하는 쉘 스크립트 파일에서 필요한 환경변수 설정

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
//localhost는 삭제하고 저장~ 저장은 


```

### core-site.xml

vi core-site.xml 에 가서

```

[hadoop@master hadoop]$ vi core-site.xml
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

[hadoop@master ~]$ rsync -av . hadoop@slave1:/usr/local/hadoop-2.7.7

[hadoop@master ~]$ cd /usr/local/hadoop-2.7.7/etc/hadoop

[hadoop@master ~]$ rsync -av . hadoop@slave1:/usr/local/hadoop-2.7.7/etc/hadoop


```





### 방화벽 설정

root 에서 ( su -)

yum install iptables-services-y 설치를 미리 하고

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
히스토리의 경우 따로 해주어야 실행이 된다
[hadoop@master sbin]$  ./mr-jobhistory-daemon.sh start historyserver
[hadoop@master sbin]$ jps

```

해서 확인해보자~ 

![1565772027387](C:\Users\student\Documents\STUDY\javaStudy\사진\하둡5)

이리 나온 상태에서 (위에는 historyserver가 빠졌다 있어야 한다)

브라우저에서

http://master:50070/dfshealth.html 를 입력해보자

livenode 를 클릭해서 라이브노드가 2개임을 확인하자

### 종료하는 방법

```
[hadoop@master sbin]$ ./stop-all.sh
```

