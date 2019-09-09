function getPosition(){
		if (navigator.geolocation) {		    
		    navigator.geolocation.getCurrentPosition(function(position) {		        
		        var lat = position.coords.latitude, // 위도
		            lon = position.coords.longitude; // 경도
		        
		        var locPosition = new kakao.maps.LatLng(lat, lon), 
		            message = '<div style="padding:5px;">여기에 계신가요?!</div>'; 
		        
		      displayMarker(locPosition, message);
		            
		      });		    
		} else { 
		    
		    var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),    
		        message = 'geolocation을 사용할수 없어요..'		        
		    displayMarker(locPosition, message);
		}
}

function displayMarker(locPosition, message) {		   
    var marker = new kakao.maps.Marker({  
        map: map, 
        position: locPosition
    }); 
    	var iwContent = message, 
        iwRemoveable = true;
 
    var infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable : iwRemoveable
    });
    	    
    infowindow.open(map, marker);		        
    map.setCenter(locPosition);      
} 

