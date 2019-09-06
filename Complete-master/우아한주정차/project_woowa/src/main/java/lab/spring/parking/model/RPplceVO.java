package lab.spring.parking.model;

public class RPplceVO {
	private String rpnum;
	private String latitude;
	private String longitude;
	private String rpplacenm;
	private String address;
	private String operday;
	public String getRpnum() {
		return rpnum;
	}
	public String getLatitude() {
		return latitude;
	}
	public String getLongitude() {
		return longitude;
	}
	public String getRpplacenm() {
		return rpplacenm;
	}
	public String getAddress() {
		return address;
	}
	public String getOperday() {
		return operday;
	}
	@Override
	public String toString() {
		return "RPplceVO [rpnum=" + rpnum + ", latitude=" + latitude + ", longitude=" + longitude + ", rpplacenm="
				+ rpplacenm + ", address=" + address + ", operday=" + operday + "]";
	}
	
	
	
	
	
	

}
