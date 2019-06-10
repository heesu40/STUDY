# JDBC

- JDBC란 자바를 이용하여 데이터베이스에 접근하여 각종 SQL문을 수행할 수 있도록 제공하는 API이다.
- 위치
  - `C:\app\student\product\11.2.0\dbhome_1\jdbc\lib` 오라클 홈 디렉토리 안에 ojdbc6 파일 복사
  - `C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext`에 붙여넣기 
    - ext는 확장자 영역이다. 

## 종류

1. JDBC-ODBC 드라이버

2. 데이터 베이스 api드라이버

   - 타입 2에 해당 
   - JDBC API호출을 특정 데이터 베이스의 클라이언트 호출 API로 바꿔주는 드라이버
   - OCI드라이버가 여기 속함

3. 네트워크 프로토콜 드라이버

   - 타입 3

   - 특정 데이터 베이스의 프로토콜과 전혀 상관없는 독자적인 방식의 프로토콜로 바꾸어 서버로 전송
   - 3tier가 여기에 해당

4. 데이터 베이스 프로토콜 드라이버

   - 타입 4, 많이 사용한다.
   - oracle thin driver

## Tier,layer

### tier

- 물리적으로 떨어져있으면 tier라 한다.
- 2tier ,3tier중 3tier는 2tier에 비해 유지보수에 비용을 절약 할 수 있지만 속도는 다소 느리다.

### layer

- 계층을 나눠 놓은 것