package lab.spring.parking.dao;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import lab.spring.parking.model.*;


@Repository
public class WoowaDAO {
	
	@Autowired
	SqlSession sqlSession;

	/* user */
	
	//login
	public UserVO login(String useremail, String userpwd) {
		Object obj = null;
		HashMap<String, String> map = new HashMap<String, String>();
		map.put("useremail", useremail);
		map.put("userpwd", userpwd);
		obj = sqlSession.selectOne("lab.mybatis.mapper.UserMapper.login", map);
		return (UserVO) obj;
	}
	
	//join to memeber
	public int addUser(UserVO user) {
		if (user.getEmail_dns().length() > 1) {
			user.setUseremail(user.getEmail() + "@" + user.getEmail_dns());
		} else {
			user.setUseremail(user.getEmail() + "@" + user.getDns_Add());
		}
		System.out.println(user);
		return sqlSession.insert("lab.mybatis.mapper.UserMapper.addUser", user);
	}
	
	//resignation
	public int removeUser(final String uemail) {
		return sqlSession.delete("lab.mybatis.mapper.UserMapper.removeUser", uemail);
	}


	/* NOTICE */
	
	public int addNotice(NoticeVO notice) { //공지 저장
		System.out.println(notice);
		return sqlSession.insert("lab.mybatis.mapper.NoticeMapper.addNotice", notice);		
	}
	public List<NoticeVO> getNoticeList(){		
		return sqlSession.selectList("lab.mybatis.mapper.NoticeMapper.getNoticeList");
	}
	public NoticeVO getNotice(int bid) {
		return sqlSession.selectOne("lab.mybatis.mapper.NoticeMapper.getNotice", bid);
	}
	public int deleteNotice(int bid) {
		return sqlSession.delete("lab.mybatis.mapper.NoticeMapper.deleteNotice", bid);
	}
	public int updateNotice(NoticeVO notice) {
		return sqlSession.update("lab.mybatis.mapper.NoticeMapper.updateNotice", notice);
	}
	
	
	/* 주차장 정보 */
	
	//public , private parking lot
	public List<PrkplceVO> findAllList() {
		return sqlSession.selectList("lab.mybatis.mapper.ParkingLot.getAllList");
	}
	
	//stop parking 
	public List<RPplceVO> getAllList(){
		return sqlSession.selectList("lab.mybatis.mapper.ParkingLot.RPAllList");
	}
	
	/* Comment */
	
	//get comment
	public List<CommentVO> getCommentList(){
		return sqlSession.selectList("lab.mybatis.mapper.CommentMapper.getCommentList");
	}
	
	//write, add comment
	public int addComment(CommentVO comment){ 
		return sqlSession.insert("lab.mybatis.mapper.CommentMapper.addComment", comment);
	}
	
	//delete comment
	public int deleteComment(int cid){
		return sqlSession.delete("lab.mybatis.mapper.CommentMapper.deleteComment", cid);
	}
	
	/*MY FAVORITE, PLACE */
	
	//Mycarplace
	public int AllMyPlace(MyParkVO vo){
		
		return sqlSession.insert("lab.mybatis.mapper.ParkingLot.addMyplace",vo);
	}
	
	//MyFavPlace 모두
	public List<MyFavVO> getAllMyFav() {
		return sqlSession.selectList("lab.mybatis.mapper.ParkingLot.getAllMyplace");
	}
	//내 즐겨찾기 장소 추가
	public int addMyfav(MyFavVO usermail) {
		return sqlSession.insert("lab.mybatis.mapper.ParkingLot.addMyfav",usermail);
				
	}
	//나의 즐겨찾기 삭제하기
	public int delMyfav(MyFavVO favlat) {
		return sqlSession.delete("lab.mybatis.mapper.ParkingLot.delMyfav",favlat);
	}
	//나의 장소 불러오기
	public List<MyParkVO> getAllMyPlace() {
		return sqlSession.selectList("lab.mybatis.mapper.ParkingLot.getMyPlace");
	}
	//내 주차위치 삭제
		public int delMypark(MyParkVO parklat) {
			return sqlSession.delete("lab.mybatis.mapper.ParkingLot.delMypark",parklat );
		}

	

}
