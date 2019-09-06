package lab.spring.parking.model;

public class FileInfoVO {

	private int fid; 
	private int rbid; 
	private String filename; 
	private String fileType;
	private String savedfile;

	public int getFid() {
		return fid;
	}
	public void setFid(int fid) {
		this.fid = fid;
	}
	public int getRbid() {
		return rbid;
	}
	public void setRbid(int rbid) {
		this.rbid = rbid;
	}
	public String getFilename() {
		return filename;
	}
	public void setFilename(String filename) {
		this.filename = filename;
	}
	public String getFileType() {
		return fileType;
	}
	public void setFileType(String fileType) {
		this.fileType = fileType;
	}

	public String getSavedfile() {
		return savedfile;
	}
	public void setSavedfile(String savefile) {
		this.savedfile = savefile;
	}
	public String toString() {
		return "FileInfoVO [fid=" + fid + ", rbid=" + rbid + ", filename=" + filename + ", fileType=" + fileType + "]";
	}

}
