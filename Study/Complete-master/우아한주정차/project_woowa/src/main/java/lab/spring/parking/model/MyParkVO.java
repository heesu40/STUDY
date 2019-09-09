package lab.spring.parking.model;

public class MyParkVO {
	
private String usermail;
private String parklat;
private String parklng;


public String getUsermail() {
	return usermail;
}
public void setUsermail(String usermail) {
	this.usermail = usermail;
}
public String getParklat() {
	return parklat;
}
public void setParklat(String parklat) {
	this.parklat = parklat;
}
public String getParklng() {
	return parklng;
}
public void setParklng(String parklng) {
	this.parklng = parklng;
}
@Override
public String toString() {
	return "MyParkVO [usermail=" + usermail + ", parklat=" + parklat + ", parklng=" + parklng + "]";
}


}
