package lab.spring.parking.model;

public class DslotVO {
	private String city;
	private String province;
	private String address;
	private String detailAddr;
	private String lat1;
	private String lng1;
	private String lat2;
	private String lng2;
	private String lat3;
	private String lng3;
	public String getCity() {
		return city;
	}
	public String getProvince() {
		return province;
	}
	public String getAddress() {
		return address;
	}
	public String getDetailAddr() {
		return detailAddr;
	}
	public String getLat1() {
		return lat1;
	}
	public String getLng1() {
		return lng1;
	}
	public String getLat2() {
		return lat2;
	}
	public String getLng2() {
		return lng2;
	}
	public String getLat3() {
		return lat3;
	}
	public String getLng3() {
		return lng3;
	}
	
	@Override
	public String toString() {
		return "DslotVO [city=" + city + ", province=" + province + ", address=" + address + ", detailAddr="
				+ detailAddr + ", lat1=" + lat1 + ", lng1=" + lng1 + ", lat2=" + lat2 + ", lng2=" + lng2 + ", lat3="
				+ lat3 + ", lng3=" + lng3 + "]";
	}
	
	

}
