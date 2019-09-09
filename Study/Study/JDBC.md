# JDBC

- JDBC란 자바를 이용하여 데이터베이스에 접근하여 각종 SQL문을 수행할 수 있도록 제공하는 API이다.
- 위치
  - `C:\app\student\product\11.2.0\dbhome_1\jdbc\lib` 오라클 홈 디렉토리 안에 ojdbc6 파일 복사
  - `C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext`에 붙여넣기 
    - ext는 확장자 영역이다. 

```java
package lab.java.core;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class DBTest {
	public static void main(String[] args){
		Connection con=null;//db 연결 상태 세션정보 저장
		String url ="jdbc:oracle:thin:@localhost:1521:orcl";
		try{
			Class.forName("oracle.jdbc.OracleDriver");
			System.out.println("driver loading 성공");
			con=DriverManager.getConnection(url,"scott","oracle");
			System.out.println("db connect 성공");
		}catch(ClassNotFoundException e){
			System.out.println("driver 없음");
		}catch(SQLException e){
			System.out.println(e.getMessage());
			//db 연결 실패
			
		}
	}
}--연결
```

```java
package lab.java.core;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class DBTest {
	public static void main(String[] args){
		Connection con=null;//db 연결 상태 세션정보 저장
		Statement stat=null;
		String url ="jdbc:oracle:thin:@localhost:1521:orcl";
		String sql="select *from dept";
		ResultSet rs=null;
		try{
			Class.forName("oracle.jdbc.OracleDriver");
			//System.out.println("driver loading 성공");
			con=DriverManager.getConnection(url,"scott","oracle");
			//System.out.println("db connect 성공");
			stat= con.createStatement();
			rs=stat.executeQuery(sql);
			while(rs.next()){
				//System.out.println(rs.getInt("deptno"));
				System.out.print(rs.getInt(1)); //도 가능
				//System.out.println(rs.getString("dname"));
				System.out.print(rs.getString(2));
				System.out.println(rs.getString(3));
				//System.out.println(rs.getString("loc"));
				
			}
			
			
		}catch(ClassNotFoundException e){
			System.out.println("driver 없음");
		}catch(SQLException e){
			System.out.println(e.getMessage());
			//db 연결 실패
			
		}finally{
			try{
			if(rs!=null) rs.close();
			if(stat!=null) stat.close();
			if(con!=null) con.close();
			}catch(Exception e){
				e.printStackTrace();
			}
		}//finally end
	}//main end

}//리턴

```

```java
//file 이름은 dbinfo properties
driver=oracle.jdbc.OracleDriver
url=jdbc:oracle:thin:@localhost:1521:orcl
user=scott
pwd=oracle

//DBTEST
package lab.java.core;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
public class DBTest {
	public static void main(String[] args){
		Connection con=null;//db 연결 상태 세션정보 저장
		PreparedStatement stat=null;//(?,?,?)를 사용했기 떄문에 그냥 statement가 아닌 PreparedStatement이다.
		String sql="insert into dept values(?,?,?)";
		
		try{
			Properties prop=new Properties();
			prop.load(new FileInputStream("C:/workspace/day13/src/dbinfo properties"));
			
			Class.forName(prop.getProperty("driver"));
			System.out.println("driver loading 성공");
			con=DriverManager.getConnection(prop.getProperty("url"),
					prop.getProperty("user"),
					prop.getProperty("pwd"));
			System.out.println("db connect 성공");
			stat= con.prepareStatement(sql);//미리 sql를 미리 보내야 한다.
			stat.setInt(1, 70);
			stat.setString(2, "BigData");
			stat.setString(3,"Seoul");//전송될 값을 셋팅 (?,?,?)에 해당되는 내용
			int rows=stat.executeUpdate();
			if(rows>0){
				System.out.println("insert 성공");
			}
			
			
			
		}catch(ClassNotFoundException e){
			System.out.println("driver 없음");
		}catch(SQLException e){
			System.out.println(e.getMessage());
			//db 연결 실패
			
		}catch(IOException e){
			System.out.println(e.getMessage());
			
		}finally{
			try{
			
			if(stat!=null) stat.close();
			if(con!=null) con.close();
			}catch(Exception e){
				e.printStackTrace();
			}
		}//finally end
	}//main end

}
//sql에 dept에 실제 값이 넣어졌는지 확인해보자!
```



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



