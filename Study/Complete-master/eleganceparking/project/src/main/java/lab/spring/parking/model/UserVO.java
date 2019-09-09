package lab.spring.parking.model;

public class UserVO {
	private String useremail;
	
	private String email;
	private String email_dns;
	private String dns_Add;
	
	private String userpwd;
	private String username;
	private String ismanager;
	
	public String getUseremail() {
		return useremail;
	}
	public void setUseremail(String useremail) {
		this.useremail = useremail;
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
	public String getEmail_dns() {
		return email_dns;
	}
	public void setEmail_dns(String email_dns) {
		this.email_dns = email_dns;
	}
	public String getDns_Add() {
		return dns_Add;
	}
	public void setDns_Add(String dns_Add) {
		this.dns_Add = dns_Add;
	}
	public String getIsmanager() {
		return ismanager;
	}
	public void setIsmanager(String ismanager) {
		this.ismanager = ismanager;
	}
	
	
	
	
}
