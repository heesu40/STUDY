require 'open-uri'
require 'nokogiri' #gen install nokogirl 



#해당링크 주소, 홍대 맛집 링크
doc = Nokogiri::HTML(open("https://eneun.tistory.com/3") ,nil, Encoding::UTF_8.to_s)

#tag가져오기
doc.css(".index_title h2").each do |x|
	print x
	print x.inner_text

end
