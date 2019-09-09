package lab.spring.parking.model;

public class MyFavVO {
private String usermail;
private String favlat;
private String favlng;

public String getUsermail() {
	return usermail;
}
public void setUsermail(String usermail) {
	this.usermail = usermail;
}
public String getFavlat() {
	return favlat;
}
public void setFavlat(String favlat) {
	this.favlat = favlat;
}
public String getFavlng() {
	return favlng;
}
public void setFavlng(String favlng) {
	this.favlng = favlng;
}
@Override
public String toString() {
	return "MyfavVO [usermail=" + usermail + ", favlat=" + favlat + ", favlng=" + favlng + "]";
}

}
