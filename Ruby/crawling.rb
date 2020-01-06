require 'open-uri'
require 'nokogiri' #gen install nokogirl 



#해당링크 주소, 홍대 맛집 링크
doc = Nokogiri::HTML(open("https://store.naver.com/restaurants/list?entry=pll&filterId=s11556055&query=%ED%99%8D%EB%8C%80%20%EB%A7%9B%EC%A7%91&sessionid=75lDEwwJ%2FqeosKs1ezQTBfmd"))

#tag가져오기
doc.css(".info_area  .tit .tit_inner .name .alphabet span").each do |x|
	print x

end
