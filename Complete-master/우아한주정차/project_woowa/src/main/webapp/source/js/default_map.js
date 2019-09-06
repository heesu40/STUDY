function createDefaultMap(){

	var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: map.getCenter(),
        	//new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: map.getLevel() // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 지도에 확대 축소 컨트롤을 생성한다
var zoomControl = new kakao.maps.ZoomControl();

// 지도의 우측에 확대 축소 컨트롤을 추가한다
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

}