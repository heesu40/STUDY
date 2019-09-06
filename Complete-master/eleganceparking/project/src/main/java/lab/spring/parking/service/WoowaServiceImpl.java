package lab.spring.parking.service;



import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;
import lab.spring.parking.dao.WoowaDAO;
import lab.spring.parking.model.*;

@Service("woowaService")
public class WoowaServiceImpl implements WoowaService{

	@Autowired
	private WoowaDAO dao;

	/* USER */
	public UserVO login(String useremail, String userpwd) {
		return dao.login(useremail, userpwd);
	}
	public int addUser(UserVO user) {
		return dao.addUser(user);
	}

	/* Notice */
	public List<NoticeVO> getNoticeList() {
		return dao.getNoticeList();
	}
	public NoticeVO getNotice(int bid) {
		return dao.getNotice(bid);
	}

	public int addNotice(NoticeVO notice) {		
		return dao.addNotice(notice);
	}

	public int updateNotice(NoticeVO notice) {
		return dao.updateNotice(notice);
	}
	public int deleteNotice(int bid) { //delete notice
		return dao.deleteNotice(bid);
	}

	/* PARKING LOT */
	public List<PrkplceVO> findAllList() {
		return dao.findAllList();
	}

	public List<CommentVO> getCommentList() {
		return dao.getCommentList(); //댓글리스트 보여주기
	}

	public int addComment(CommentVO comment) {
		return dao.addComment(comment);	//댓글 추가
	}
	public int deleteComment(int cid) {
		return dao.deleteComment(cid);//댓글 삭제
	}

	public List<DslotVO> getDSList() {	
		return null;
	}
	
	public List<RPplceVO> getRPList() {
		return dao.getAllList();		
	}

	/* MY FAVORTIE, PLACE */
	public int AllMyPlace(MyParkVO vo) {
		
		return dao.AllMyPlace(vo);
	}
	public List<MyFavVO> getAllMyFav(){
		return dao.getAllMyFav();
	}

	public int addMyfav(MyFavVO usermail) {
		return dao.addMyfav(usermail);
	}

	public int delMyfav(MyFavVO favlat) {
		return dao.delMyfav(favlat);
	}	


	public List<MyParkVO> getAllMyPlace() {
		return dao.getAllMyPlace();
	}

	public  int delMypark(MyParkVO parklat) {
		return dao.delMypark(parklat);
	}


	
}
