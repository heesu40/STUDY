package lab.spring.parking.model;

import java.sql.Date;

public class CommentVO {
	private int cid;
	private String markerid;
	private String writer;
	private Date idate;
	private String contents;
	private String password;

	public int getCid() {
		return cid;
	}
	public void setCid(int cmid) {
		this.cid = cmid;
	}

	public String getMarkerid() {
		return markerid;
	}
	public void setMarkerid(String markerid) {
		this.markerid = markerid;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public Date getIdate() {
		return idate;
	}
	public void setIdate(Date idate) {
		this.idate = idate;
	}
	public String getContents() {
		return contents;
	}
	public void setContents(String contents) {
		this.contents = contents;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	@Override
	public String toString() {
		return "CommentVO [cid=" + cid + ", markerid=" + markerid + ", writer=" + writer + ", idate=" + idate
				+ ", contents=" + contents + ", password=" + password + "]";
	}

	
}
