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
		System.out.println(user);
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
		//System.out.println(service.addUser(user));
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
//			model.addAttribute("msg", "관리자만 접근가능한 페이지입니다.");
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
	public ModelAndView deleteNotice(String password, NoticeVO notice, HttpServletRequest request) {
		ModelAndView mav = new ModelAndView();
		HttpSession session= request.getSession();
		UserVO user= (UserVO)session.getAttribute("user");
		System.out.println(notice.getBid()+"번 공지사항 삭제 ## 비번 :"+password);
		if(user.getIsmanager().equals("Y")&&user.getUserpwd().equals(password)) {//[is manager] and [delete try password=manager password] can delete the notice.
			service.deleteNotice(notice.getBid());
			mav.setViewName("redirect:/notice.do");
		}else { //password is not correct or exist. and not manager!!
			System.out.println("비밀번호 입력 또는 일치하지 않음 // 관리자가 아님");
			mav.setViewName("redirect:/notice.do");
		}
		return mav;
	}

	/* board end */
	
	/* Comment */
	@RequestMapping(value = "/comment.do", method=RequestMethod.POST)
	public ModelAndView addComment(CommentVO comment, HttpServletResponse response) throws IOException{
		ModelAndView mav = new ModelAndView();
		if(service.addComment(comment)>0) {
			mav.setViewName("redirect:/parking.do");
		}
		return mav;
	}
	@RequestMapping(value = "/delete_comment.do", method=RequestMethod.POST)
	public ModelAndView deleteComment(CommentVO comment, HttpServletRequest request) {
		ModelAndView mav = new ModelAndView();
		//HttpSession session=request.getSession();
		mav.setViewName("redirect:/parking.do");
		return mav;
	}

	
	/* Parking */
	
	@RequestMapping(value = "/parking.do")
	public ModelAndView defaultMap(HttpSession session){
		ModelAndView mav = new ModelAndView();
		List<PrkplceVO> lots = null;
		lots =service.findAllList();
		mav.addObject("lots",lots);
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
		
		vo.setUseremail(point.get("usermail").toString());
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
		
		System.out.println(vo.toString());
		
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