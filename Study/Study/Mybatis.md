# Mybatis

<http://www.mybatis.org/mybatis-3/ko/index.html>

이 사이트에 들어가서 알아보자



##### lab.spring.orm.dao

1.UserManageDAO.java

```java
package lab.spring.orm.dao;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;


import lab.spring.orm.model.UserVO;


public class UserManageDAO {
	
	SqlSessionFactory sqlSessionFactory;
	
	
	public void setSqlSessionFactory(SqlSessionFactory sqlSessionFactory) {
		this.sqlSessionFactory = sqlSessionFactory;
	}
	
	public UserVO login(String uid,String upwd) {
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		Object vo=null;
		HashMap<String,String> hm=new HashMap<String,String>();
		hm.put("uid", uid);
		hm.put("upwd",upwd);
		vo= sqlSession.selectOne("lab.mybatis.user.UserMapper.login",hm);
		return (UserVO)vo;
		
	}
	public int addUser(UserVO user) {
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		return sqlSession.insert("lab.mybatis.user.UserMapper.addUser",user);
	}
	public List<UserVO> findUserList(){
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		return sqlSession.selectList("lab.mybatis.user.UserMapper.getUserList");
	}
	public int updateUser(UserVO user) {
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		return sqlSession.update("lab.mybatis.user.UserMapper.modifyUser",user);
	}
	public int removeuser(final String uid) {
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		return sqlSession.delete("lab.mybatis.user.UserMapper.removeUser",uid);
	}
	public UserVO findUser(String uid) {
		SqlSession sqlSession =sqlSessionFactory.openSession(true);
		return sqlSession.selectOne("lab.mybatis.user.UserMapper.getUser",uid);
	}
}

```



##### lab.spring.orm.model

UserVO.java

```java
package lab.spring.orm.model;

public class UserVO {
	 private String userid;
	 private String userpwd;
	 private String username;
	 private String email;
	 private String phone;
	 private String address;
	 private String job;
	public String getUserid() {
		return userid;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		 return "userid:" + getUserid() + "\n" +
        "userpwd:" + getUserpwd() + "\n" +
        "username:" + getUsername() + "\n" +
        "phone:" + getPhone() + "\n" +
        "email:" + getEmail() + "\n" +
        "address:" + getAddress() + "\n" +
        "job:"+ getJob() + "\n";
				
	}

	public void setUserid(String userid) {
		this.userid = userid;
	}
	public String getUserpwd() {
		return userpwd;
	}
	public void setUserpwd(String userpwd) {
		this.userpwd = userpwd;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getJob() {
		return job;
	}
	public void setJob(String job) {
		this.job = job;
	}
	 
}

```



##### lab.spring.orm.test

SqlmappingTest.java

```java
package lab.spring.orm.test;

import java.io.IOException;
import java.io.InputStream;
import java.util.Iterator;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;


import lab.spring.orm.dao.UserManageDAO;
import lab.spring.orm.model.UserVO;

public class SqlmappingTest {

	public static void main(String[] args) throws IOException{
		String resource ="mybatis-config.xml";//MyBatis 설정파일
		InputStream inputStream =Resources.getResourceAsStream(resource);
		SqlSessionFactory sqlSessionFactory
		=new SqlSessionFactoryBuilder().build(inputStream);
		UserManageDAO userDao=new UserManageDAO();
		userDao.setSqlSessionFactory(sqlSessionFactory);

		System.out.println("###############전체 목록###################");
		List<UserVO> lists=userDao.findUserList();
		Iterator<UserVO> iter=lists.iterator();
		while(iter.hasNext()) {
			UserVO u=iter.next();
			System.out.println(u);
			
			
			
		}
		
		UserVO vo=new UserVO();
		vo.setUserid("s3");
		vo.setUsername("서울3");
		vo.setUserpwd("1234");
		vo.setEmail("seoul3@korea.or.kr");
		vo.setPhone("02-129");
		vo.setAddress("서울");
		vo.setJob("IT개발");
		System.out.println("insert rows = > "+userDao.addUser(vo));
		System.out.println("#################s3아이디 한행 검색 ###############");
		System.out.println(userDao.findUser("s3"));
		
		vo.setUserid("s3");
		vo.setEmail("s3@gmail.or.kr");
		vo.setPhone("02-129-1234");
		vo.setAddress("부산");
		vo.setJob("데이터 분석");
		System.out.println("update :s3 = > "+userDao.updateUser(vo));
		System.out.println("#################s3 아이디 한행 검색 ###############");
		System.out.println("delete :s3 = > "+userDao.removeuser("s3"));
		System.out.println("#################s3 아이디 한행 검색 ###############");
		lists=userDao.findUserList();
		iter=lists.iterator();
		
		while(iter.hasNext()) {
			UserVO u=iter.next();
			System.out.println(u);
			
			
			
		}
		

	}
		
	

}

```



##### xml

UserMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="lab.mybatis.user.UserMapper">
   <select id="login" resultType="lab.spring.orm.model.UserVO" parameterType="hashmap">
      select * from userinfo where userid=#{uid} and userpwd=#{upwd}
   </select>
   <select id="getUserList" resultType="lab.spring.orm.model.UserVO">
      select * from userinfo 
   </select>
   <select id="getUser" resultType="lab.spring.orm.model.UserVO" parameterType="string">
      select * from userinfo where userid = #{uid}
   </select>
   <insert id="addUser" parameterType="lab.spring.orm.model.UserVO">
      insert into userinfo (userid, username, userpwd, email, phone, job, address)
      values ( #{userid},#{username},#{userpwd},#{email},#{phone},#{job} ,#{address})
   </insert>
   <update id="modifyUser" parameterType="lab.spring.orm.model.UserVO">
      update userinfo set email=#{email},phone= #{phone},address=#{address},job=#{job} where
      userid = #{userid}
   </update>
   <delete id="removeUser" parameterType="string">
      delete userinfo where userid=#{uid}
   </delete>
</mapper>
```







# 문제풀어보기

```java
drop table products purge;

create table products (
prodnum    varchar2(20)  primary key ,  -- 제품번호
pname      varchar2(30),   --상품 이름
category   varchar2(30), --상품 분류
description  varchar2(1000),--상품 특성, 설명
filename    varchar2(100),        ----이미지 파일 경로
manufacturer  varchar2(50), --제조사
unitPrice    number(7),     --개당 가격
condition varchar2(20),
unitsInStock   number(5)    --제고
);


insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1234', 'iPhone 6s',800000, '4.7-inch, 1334X750 Renina HD display 8-megapixel iSight Camera',
'Smart Phone','Apple', 1000, 'New', 'P1234.png');

insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1235','LG PC 그램',
1500000,
'13.3-inch, IPS LED display, 5rd Generation Intel Core processors',
'Notebook',
'LG',
1000,
'Refurbished',
'P1235.png');

insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1236',
'Galaxy Tab S',
900000,
'212.8*125.6*6.6mm,  Super AMOLED display, Octa-Core processor',
'Tablet',
'Samsung',
1000,
'Old',
'P1236.png');
commit;


select * from products;

select * from products where prodnum =? ;

select * from products where unitPrice between ? and ?;


update products set unitPrice = ?, UnitsInStock=?  where prodnum = ? ;

delete from products  where prodnum = ? ;
 
 
===========================================================
1. maven 프로젝트 생성 (pom.xml)
2. mapper 파일 설정  (ProductMapper.xml)
3. spring 설정 파일 설정  (application.xml)
4. 엔티티 클래스 생성
5. DAO 클래스 생성
6. 서비스 클래스 생성
7. test 클래스 생성 실행 결과 보기 
 
 public class SpringMybatisTest {

	public static void main(String[] args) {
		String[] configs = new String[]{"application.xml"};
		ApplicationContext context = 
				   new ClassPathXmlApplicationContext(configs);
		UserService service = 
				context.getBean("productService", ProductService.class);
		System.out.println("#######전체 상품 목록 ###########");
		List<Product> lists = service.findProductList();
		Iterator<Product> iter = lists.iterator();
		while (iter.hasNext()) {
			Product u = iter.next();
			System.out.println(u);
		}
		
		Product p = new Product();
        p.setProductId("B1000");
    	p.setPname("Spring과 MyBatis");
    	p.setCategory("Book");
    	p.setDescription("프로젝트로 배우는 프레임워크");
    	p.setFilename("spring.jpeg");
    	p.setManufacturer("멀티캠퍼스");
    	p.setUnitPrice(10000);
    	p.setUnitsInStock(300); 
		 
		System.out.println("insert rows = >" + service.addProduct(p));		
		System.out.println("#######s3 아이디 한행 검색 ###########"); 
		System.out.println(service.findProduct("s3"));		
		
		p.setUnitPrice(15000);
    			p.setUnitsInStock(200);  
    			p.setFilename('spring-mybatis.jpeg');
		System.out.println("update :s3 =>"+service.updateProduct(p));
		System.out.println(service.findProduct"s3"));
		System.out.println("delete :s3 =>"+service.removeProduct("s3"));
		System.out.println("#######전체 상품목록 ###########");
		 lists = service.findProductList();
		 iter = lists.iterator();
		while (iter.hasNext()) {
			Product u = iter.next();
			System.out.println(u);
		}
	}
 
 
 
 
 
```





# 복습해보자

1. MyBatis, SQL Mapping),Framwork 를 설정하기 위해서 

- config.xml
  - DB연결
  - Logging 설정
  - mapper.xml리스트
  - mode설정(운영,개발)
- mapper.xml
  - namespace선언
  - <  select id= resuletype= parameterType= >
  - < insert id= parameterType>
  - < update id>
  - < delete id>

2. 정의하기

- Connect 해당 -SqlSessionFactory(전역 Scope)(생성하기위해서는 SqlSessionFactoryBuilde (메서드 scope)로 부터 생성한다. SqlSessionFactory.openSession을 이용하여 SqlSession생성)
- Statement 해당 -SqlSession(메서드 scope) 이며 이를 이용하여 query(),update(),

3. Spring Frame

- Templet 패던(스프링에서 제공)
  - 저수준 작업으로 
    1. DB connection
    2. 예외처리
    3. Restore
- DataSource(는 tepmlete에 주입된다.)
  1. DriveManager
  2. Connection lib  ex)DBLP
  3. 

```xml
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
  <property name="dataSource" ref="dataSource" />
  <property name="mapperLocations" value="classpath*:lab/mybatis/mappers/*.xml" />
</bean>

<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
  <constructor-arg index="0" ref="sqlSessionFactory" />
</bean>
```

를 설정 후 (application.xml)

```java
@Repository
public class UserDAO {
	@Autowired
	SqlSession sqlSession;//설정 application.xml에서 한 설정Session이 들어올것이다.
	
```

로 설정했다.

