package lab.spring.parking.controller;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.parking.model.*;
import lab.spring.parking.service.WoowaService;


@RestController
public class WoowaController {
	
	@Autowired
	WoowaService service;
	HttpSession session;
	
	/* user start*/
	//main page
	@RequestMapping("/main.do")
	public ModelAndView main() {
		ModelAndView mav=new ModelAndView();
		mav.setViewName("home_view");
		return mav;
	}
	
	@RequestMapping(value="/login.do", method=RequestMethod.POST)
	public ModelAndView loginTry(String useremail, String userpwd, HttpServletRequest request) {
		ModelAndView mav= new ModelAndView();
		UserVO user =null;
		HttpSession session=request.getSession();		
		user=service.login(useremail, userpwd);
		session.setAttribute("user", user);
		//System.out.println(user);
		if(user==null) {
			mav.setViewName("home_view(login_fail)");
		}else {
			mav.setViewName("home_view");
		}
		return mav;
	}
	@RequestMapping(value="/logout.do", method=RequestMethod.GET)
	public ModelAndView logoutSuccess( HttpServletRequest request) throws Exception {
		ModelAndView mav= new ModelAndView();
		HttpSession session=request.getSession();
		session.invalidate();
		mav.setViewName("home_view");
		return mav;
	}
	//join page//
	@RequestMapping(value="/join.do", method=RequestMethod.GET)
	public ModelAndView getjoin() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("member");
		return mav;
	}
	@RequestMapping(value="/join.do", method=RequestMethod.POST)
	public ModelAndView joinSuccess(UserVO user) {
		ModelAndView mav = new ModelAndView();
		System.out.println(user.getUseremail());
		if(service.addUser(user)>0) {
			mav.setViewName("home_view");
		}
		return mav;
	}
	/* user end */
	
	@RequestMapping(value="/notice.do", method=RequestMethod.GET)
	public ModelAndView listNotice() {
		ModelAndView mav = new ModelAndView();
		List<NoticeVO> list =null;
		list=service.getNoticeList();
		mav.addObject("list", list);
		mav.setViewName("notice_list");
		return mav;
	}
	
	@RequestMapping(value="/notice_view.do", method=RequestMethod.GET)
	public ModelAndView viewNotice(int bid) {
		ModelAndView mav = new ModelAndView();
		NoticeVO notice=null;
		notice=service.getNotice(bid);
		mav.addObject("notice", notice);
		mav.setViewName("notice_view");
		return mav;
	}
	@RequestMapping(value="/notice_write.do", method=RequestMethod.GET)
	public ModelAndView writeNotice( Model model, HttpServletRequest request, HttpServletResponse response) throws IOException {
		ModelAndView mav = new ModelAndView();
		HttpSession session=request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");	
		
		if(user==null) {
			System.out.println("로그인이 필요합니다.");
			
			mav.setViewName("redirect:/notice.do");
			
		}else if(user.getIsmanager().equals("N")){
			System.out.println("x관계자 외 출입x");		
			System.out.println("elseif"+user.getIsmanager());
			response.setContentType("text/html; charset=UTF-8");
            PrintWriter out = response.getWriter();
            out.println("<script>");
            out.println("alert('로그인 정보를 확인해주세요.');");
            out.println("location.href='./notice.do'");
            out.println("</script>");            
            out.flush();
            out.close();			
		}else {
			System.out.println("else:"+user.getIsmanager());
			 mav.setViewName("notice_write");
			
		}
		return mav;
	}
	@RequestMapping(value="/notice_write.do", method=RequestMethod.POST)
	public ModelAndView postNotice(Model model, NoticeVO notice, HttpServletRequest request) throws FileNotFoundException {
		ModelAndView mav = new ModelAndView();
		HttpSession session=request.getSession();
		session.setAttribute("notice", notice);
		System.out.println(notice);
		if(service.addNotice(notice)>0) {
			mav.setViewName("redirect:/notice.do");
		}
		
		return mav;
	}
	
	

	@RequestMapping(value="/try_modify_notice.do", method=RequestMethod.GET)
	public ModelAndView tryModifyNotice(HttpServletRequest request) {
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		//NoticeVO notice=(NoticeVO)session.getAttribute("notice");
		if(user!=null) {
				mav.setViewName("redirect:/try_modify_notice.do");
		}else {
				mav.setViewName("redirect:/notice.do");
		}
		return mav;
	}
	
	@RequestMapping(value = "/try_modify_notice.do", method=RequestMethod.POST)
	public ModelAndView tryModifyNotice(String password, HttpServletRequest request){
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		//NoticeVO notice=(NoticeVO)session.getAttribute("notice");
		if(user.getIsmanager().equals("Y")&&user.getUserpwd().equals(password)) {//[is manager] and [delete try password=manager password] can moidfy the notice.
			mav.setViewName("notice_modify");
		}else { //password is not correct or exist. and not manager!!
			System.out.println("비밀번호 입력 또는 일치하지 않음 // 관리자가 아님");
			mav.setViewName("redirect:/notice.do");
		}
		return mav;
	}
	
	@RequestMapping(value = "/modify_notice.do", method=RequestMethod.POST)
	public ModelAndView modifyNotice(NoticeVO notice, HttpServletRequest request){
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		if(user.getIsmanager().equals("Y")) {
			service.updateNotice(notice);
			mav.setViewName("redirect:/notice.do");
		}else { //password is not correct or exist. and not manager!!
			System.out.println("비밀번호 입력 또는 일치하지 않음 // 관리자가 아님");
			mav.setViewName("redirect:/notice.do");
		}
		return mav;
	}

	@RequestMapping(value="/notice_delete.do", method=RequestMethod.GET)
	public ModelAndView trydeleteNotice(NoticeVO notice, HttpServletRequest request) {
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		System.out.println(notice.getBid()+"번 공지사항 삭제 시도");
		if(user!=null) {
				mav.setViewName("redirect:/notice_delete.do");
		}else {
				mav.setViewName("redirect:/notice.do");
		}
		return mav;
	}
	
	@RequestMapping(value="/notice_delete.do",method = RequestMethod.POST)
	public ModelAndView deleteNotice(String password, NoticeVO notice, HttpServletRequest request, HttpServletResponse response) throws IOException {
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		System.out.println(notice.getBid()+"번 공지사항 삭제 ## 비번 :"+password);
		if(user.getIsmanager().equals("Y")&&user.getUserpwd().equals(password)) {//[is manager] and [delete try password=manager password] can delete the notice.
			service.deleteNotice(notice.getBid());
			response.setContentType("text/html; charset=UTF-8");
			PrintWriter out = response.getWriter();
            out.println("<script>");
            out.println("alert('해당 공지사항이 삭제되었습니다.');");
            out.println("location.href='./notice.do'");
            out.println("</script>");            
            out.flush();
            out.close();
		}else if(user.getIsmanager().equals("Y")) { //password is not correct or exist. and not manager!!
			response.setContentType("text/html; charset=UTF-8");
			PrintWriter out = response.getWriter();
            out.println("<script>");
            out.println("alert('관리자 비밀번호 오류')");
            out.println("location.href='./notice.do'");
            out.println("</script>");            
            out.flush();
            out.close();
		}else {
			response.setContentType("text/html; charset=UTF-8");
			PrintWriter out = response.getWriter();
            out.println("<script>");
            out.println("alert('삭제권한이 없습니다.')");
            out.println("location.href='./notice.do'");
            out.println("</script>");            
            out.flush();
            out.close();
		}
		return mav;
	}

	/* board end */
	
	/* Comment */
	@RequestMapping(value = "/comment.do", method=RequestMethod.POST)
	public ModelAndView addComment(CommentVO comment, HttpServletRequest request, HttpServletResponse response) throws IOException{
		ModelAndView mav = new ModelAndView();
		HttpSession session=request.getSession();
		session.setAttribute("comment", comment);
		if(session.getAttribute("user")==null) {
			response.setContentType("text/html; charset=UTF-8");
			PrintWriter out = response.getWriter();
            out.println("<script>");
            out.println("alert('로그인이 필요합니다.')");
            out.println("location.href='./parking.do'");
            out.println("</script>");            
            out.flush();
            out.close();			
		}else{
			if(comment.getPassword()=="") {//비밀번호 입력하지 않음
				response.setContentType("text/html; charset=UTF-8");
				PrintWriter out = response.getWriter();
	            out.println("<script>");
	            out.println("alert('비밀번호를 입력 필수.')");
	            out.println("location.href='./parking.do'");
	            out.println("</script>");            
	            out.flush();
	            out.close();
			}else {//댓글 등록 완료
				service.addComment(comment);
				mav.setViewName("redirect:/parking.do");
			}
		}
		return mav;
	}
	
	@RequestMapping(value = "/delete_comment.do", method=RequestMethod.POST)
	public ModelAndView deleteComment(CommentVO comment, HttpServletRequest request){
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user=(UserVO)session.getAttribute("user");
		if(user==null) { //didn't login
			mav.setViewName("redirect:/parking.do");
		}else if(user.getIsmanager().equals("Y")){//매니저는 모든 글 삭제 가능
			if(service.deleteComment(comment)>0) {			
				mav.setViewName("redirect:/parking.do");
			}
		}else if(!comment.getWriter().equals(user.getUsername())) {//이용자와 댓글 작성자와 다르면 삭제하지 못함
			System.out.println("삭제 권한이 없음");
			mav.setViewName("redirect:/parking.do");
		}else{//이용자와 댓글 작성자가 같은 경우 삭제 이행, delete 실행되면 parking뷰 페이지 reload
			if(service.deleteComment(comment)>0) {			
				mav.setViewName("redirect:/parking.do");
			}
		}
		return mav;
	}


	
	/* Parking */
	
	@RequestMapping(value = "/parking.do")
	public ModelAndView defaultMap(HttpSession session){
		ModelAndView mav = new ModelAndView();
		List<PrkplceVO> lots = null;
		List<MyFavVO> list=null;		  
		List<MyParkVO> vo=null;
		List<CommentVO> comments= null;

		lots =service.findAllList();
		list=service.getAllMyFav();
		vo=service.getAllMyPlace();
		comments= service.getCommentList();
	      
		
		mav.addObject("lots",lots);
		mav.addObject("MyFav", list);
		mav.addObject("Mypark", vo);	
		mav.addObject("comments", comments);
		
		mav.setViewName("parking_view");
		return mav;


	}
	
	@RequestMapping(value = "/stop.do") 
	public ModelAndView stopMap(HttpSession session){
		ModelAndView mav = new ModelAndView();
		List<RPplceVO> RPlots = null;
		RPlots =service.getRPList();
		mav.addObject("RPlots",RPlots);
		mav.setViewName("stop_view");
		return mav;
	}	
	
	//set myPark Location
	@PostMapping(value = "/MyParkLo.do")
	@ResponseBody
	public String MyParkmap(@RequestBody Map<String,Object> point)  {
		MyParkVO vo = new MyParkVO();
		
		vo.setUsermail(point.get("usermail").toString());
		vo.setParklng(point.get("parklng").toString()); 
		vo.setParklat(point.get("parklat").toString()); 
		
		//System.out.println(vo.toString());
		
		if(service.AllMyPlace(vo)>0) {
			return "{ \"status\" : 1 }";		
			
		}else {
			return "{\"status\" : 4}";
		}
	
	}
	
	//set MyFav Location
	@PostMapping(value = "/MyFavLo.do")
	@ResponseBody
	public String MyFavmap(@RequestBody Map<String,Object> fav)  {
		MyFavVO vo = new MyFavVO();
		
		vo.setUsermail(fav.get("usermail").toString());
		vo.setFavlng(fav.get("favlng").toString()); 
		vo.setFavlat(fav.get("favlat").toString()); 
		
		//System.out.println(vo.toString());
		
		if(service.addMyfav(vo)>0) {
			return "{ \"status\" : 1 }";		
			
		}else {
			return "{\"status\" : 4}";
		}
	
	}

	
//	  @RequestMapping(value = "/MyFavLo.do")
//	  
//	   public ModelAndView MyFavmap() { 
//		  ModelAndView mav=new ModelAndView();
//		  List<MyFavVO> list=null;
//		  
//		  List<MyParkVO> vo=null;
//		  
//		 
//		  list=service.getAllMyFav();
//		  vo=service.getAllMyPlace();
//		  mav.addObject("MyFav", list);
//		  mav.addObject("Mypark", vo);
//		 // mav.setViewName("parking_view");
//		  mav.setViewName("Test");
//	  
//	  
//	  return mav ; 
//	  }
	
	
	
	
	//test
	@RequestMapping(value = "/test.do")
	@ResponseBody
	public String defaultMap(@RequestBody Map<String,Object> point) {
		
		return "{ \"status\" : 1 }";
	}


}