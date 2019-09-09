package lab.spring.parking.service;

import java.util.List;

import lab.spring.parking.model.*;


public interface WoowaService {
	
	//user 
	public UserVO login(String uemail, String upwd);
	public int addUser(UserVO user);
	
	//notice
	public List<NoticeVO> getNoticeList();
	public NoticeVO getNotice(int bid);
	public int addNotice(NoticeVO notice);
	public int updateNotice(NoticeVO notice); //update notice
	public int deleteNotice(int bid); //delete notice
	
	//comment
	public List<CommentVO> getCommentList(); //주차장에 대한 댓글 받아오기 (markerid=주차장 seq)
	public int addComment(CommentVO comment); //주차장에 대한 댓글 쓰기
	public int deleteComment(int cid);// 댓글 삭제
	
	//parklot
	public List<PrkplceVO> findAllList(); //주차장 정보 받아오기
	public List<DslotVO> getDSList(); //주정차금지구역 가져오기
	public List<RPplceVO> getRPList();//주정차 지역 정보 받아오기
	
	//myFav, myPlace
	public int AllMyPlace(MyParkVO vo);
	public List<MyFavVO> getAllMyFav();	
	public int addMyfav(MyFavVO vo);	
	public int delMyfav(MyFavVO favlat);	
	public List<MyParkVO> getAllMyPlace();		
	public int delMypark(MyParkVO parklat);

}
