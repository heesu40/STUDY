<%@ page contentType="text/html;charset=utf-8" %> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri = "http://java.sun.com/jsp/jstl/functions" prefix = "fn" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>원, 선, 사각형, 다각형 표시하기</title>
    
</head>
<body>
<div id="map" style="width:100%;height:500px;"></div>    

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=0f4f915f91717b8e6f20f6b1f4018f2a"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(35.162307, 128.985956), // 지도의 중심좌표
        level: 8 // 지도의 확대 레벨
    };  

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다



var linePath = [105]

linePath[0] = [
new kakao.maps.LatLng(35.129901, 128.971113),
new kakao.maps.LatLng(35.131311, 128.968603),
new kakao.maps.LatLng(35.13222, 128.964693)
];

linePath[1] = [             
new kakao.maps.LatLng(35.167559, 128.987179),
new kakao.maps.LatLng(35.168572, 128.986951),
new kakao.maps.LatLng(35.168738, 128.986548),
new kakao.maps.LatLng(35.168842, 128.986509),
new kakao.maps.LatLng(35.169122, 128.985803),
new kakao.maps.LatLng(35.168882, 128.984026),
new kakao.maps.LatLng(35.169182, 128.98237) 
];       

linePath[2] = [
new kakao.maps.LatLng(35.167309, 128.983693),
new kakao.maps.LatLng(35.16777, 128.983632),
new kakao.maps.LatLng(35.168296, 128.98342),
new kakao.maps.LatLng(35.168532, 128.983417),
new kakao.maps.LatLng(35.168965, 128.983504)
];       

linePath[3] = [           
new kakao.maps.LatLng(35.152574, 128.971679),
new kakao.maps.LatLng(35.14951, 128.989431),
new kakao.maps.LatLng(35.15164, 129.016219),
new kakao.maps.LatLng(35.151943, 129.017005),            
new kakao.maps.LatLng(35.150453, 129.003729),
new kakao.maps.LatLng(35.148729, 129.004451),
new kakao.maps.LatLng(35.148775, 129.004603),
new kakao.maps.LatLng(35.147815, 129.005261),
new kakao.maps.LatLng(35.147712, 129.005164),
new kakao.maps.LatLng(35.147544, 129.005202),
new kakao.maps.LatLng(35.147511, 129.005424),
new kakao.maps.LatLng(35.147403, 129.005527),
new kakao.maps.LatLng(35.14741, 129.006061) 
];       

linePath[4] = [      
new kakao.maps.LatLng(35.150973, 129.008754),
new kakao.maps.LatLng(35.146695, 129.009266) 
];       

linePath[5] = [             
new kakao.maps.LatLng(35.151095, 129.010062),
new kakao.maps.LatLng(35.146776, 129.010563) 
];       

linePath[6] = [             
new kakao.maps.LatLng(35.193313, 128.982026),
new kakao.maps.LatLng(35.19084, 128.986563),
new kakao.maps.LatLng(35.186573, 128.98963),
new kakao.maps.LatLng(35.186265, 128.99094),
new kakao.maps.LatLng(35.185805, 129.002057),
new kakao.maps.LatLng(35.169992, 129.026649),
new kakao.maps.LatLng(35.15906, 129.031834),
new kakao.maps.LatLng(35.153932, 129.032126),
new kakao.maps.LatLng(35.14602, 129.034283),
new kakao.maps.LatLng(35.143943, 129.035777),
new kakao.maps.LatLng(35.129654, 129.057736),
new kakao.maps.LatLng(35.130206, 129.065998)
];       

linePath[7] = [    
new kakao.maps.LatLng(35.197117, 128.988062),
new kakao.maps.LatLng(35.192857, 128.982856),
new kakao.maps.LatLng(35.188082, 128.978593),
new kakao.maps.LatLng(35.186135, 128.977382),
new kakao.maps.LatLng(35.184126, 128.976521),
new kakao.maps.LatLng(35.182153, 128.976073),
new kakao.maps.LatLng(35.180505, 128.975998),
new kakao.maps.LatLng(35.169587, 128.976882),
new kakao.maps.LatLng(35.168121, 128.976789),
new kakao.maps.LatLng(35.163309, 128.975865),
new kakao.maps.LatLng(35.152309, 128.972589),
new kakao.maps.LatLng(35.145061, 128.969601),
new kakao.maps.LatLng(35.144596, 128.96958),
new kakao.maps.LatLng(35.13111, 128.972043),
new kakao.maps.LatLng(35.12591, 128.968146),
new kakao.maps.LatLng(35.121733, 128.963686)
];       

linePath[8] = [
new kakao.maps.LatLng(35.149781, 128.971605),
new kakao.maps.LatLng(35.149019, 128.975967)
];       

linePath[9] = [              
new kakao.maps.LatLng(35.151035, 128.972115),
new kakao.maps.LatLng(35.150448, 128.97566),
new kakao.maps.LatLng(35.150753, 128.976132) 
];       

linePath[10] = [            
new kakao.maps.LatLng(35.168126, 128.976782),
new kakao.maps.LatLng(35.167237, 128.979666),
new kakao.maps.LatLng(35.167097, 128.982241)  
];       

linePath[11] = [           
new kakao.maps.LatLng(35.127799, 128.963328),
new kakao.maps.LatLng(35.126534, 128.968631) 
];       

linePath[12] = [             
new kakao.maps.LatLng(35.127545, 128.964423),
new kakao.maps.LatLng(35.131952, 128.96591)  
];       

linePath[13] = [            
new kakao.maps.LatLng(35.127131, 128.966182),
new kakao.maps.LatLng(35.131534, 128.967628) 
];       

linePath[14] = [             
new kakao.maps.LatLng(35.124127, 128.965204),
new kakao.maps.LatLng(35.127131, 128.966178) 
];       

linePath[15] = [             
new kakao.maps.LatLng(35.131108, 128.972048),
new kakao.maps.LatLng(35.133089, 128.973733),
new kakao.maps.LatLng(35.134766, 128.974514),
new kakao.maps.LatLng(35.137155, 128.976723),
new kakao.maps.LatLng(35.139522, 128.980357),
new kakao.maps.LatLng(35.140537, 128.982874),
new kakao.maps.LatLng(35.141276, 128.983621),
new kakao.maps.LatLng(35.142288, 128.983826),
new kakao.maps.LatLng(35.156576, 128.987337) 
];       

linePath[16] = [      
new kakao.maps.LatLng(35.183108, 128.976268),
new kakao.maps.LatLng(35.180751, 128.987967),
new kakao.maps.LatLng(35.18077, 128.988833),
new kakao.maps.LatLng(35.180996, 128.989229),
new kakao.maps.LatLng(35.181216, 128.989301),
new kakao.maps.LatLng(35.181602, 128.989046),
new kakao.maps.LatLng(35.181677, 128.988561) 
];       

linePath[17] = [        
new kakao.maps.LatLng(35.186257, 128.991559),
new kakao.maps.LatLng(35.18535, 128.991879),
new kakao.maps.LatLng(35.18474, 128.993297),
new kakao.maps.LatLng(35.184574, 128.99347),
new kakao.maps.LatLng(35.184331, 128.9943),
new kakao.maps.LatLng(35.184433, 128.995875),
new kakao.maps.LatLng(35.184709, 128.997357),
new kakao.maps.LatLng(35.184701, 128.99919)    
];       

linePath[18] = [    
new kakao.maps.LatLng(35.195368, 128.994054),
new kakao.maps.LatLng(35.193425, 128.992993),
new kakao.maps.LatLng(35.188349, 128.990979),
new kakao.maps.LatLng(35.18742, 128.990797),
new kakao.maps.LatLng(35.18572, 128.991071),
new kakao.maps.LatLng(35.184869, 128.99104),
new kakao.maps.LatLng(35.184132, 128.990485),
new kakao.maps.LatLng(35.182768, 128.988801),
new kakao.maps.LatLng(35.182148, 128.988562),
new kakao.maps.LatLng(35.17482, 128.988429),
new kakao.maps.LatLng(35.172116, 128.988067),
new kakao.maps.LatLng(35.170513, 128.988506),
new kakao.maps.LatLng(35.166675, 128.988822),
new kakao.maps.LatLng(35.16428, 128.990861),
new kakao.maps.LatLng(35.16089, 128.99108),
new kakao.maps.LatLng(35.159841, 128.991629),
new kakao.maps.LatLng(35.154788, 128.995899),
new kakao.maps.LatLng(35.153723, 128.998178),
new kakao.maps.LatLng(35.152873, 128.999516),
new kakao.maps.LatLng(35.152369, 129.006538),
new kakao.maps.LatLng(35.152806, 129.01287),
new kakao.maps.LatLng(35.153936, 129.016588)
];       

linePath[19] = [
new kakao.maps.LatLng(35.155826, 129.013837),
new kakao.maps.LatLng(35.15328, 129.014503) 
];       

linePath[20] = [             
new kakao.maps.LatLng(35.152691, 129.01218),
new kakao.maps.LatLng(35.152619, 129.013515),
new kakao.maps.LatLng(35.153306, 129.016354) 
];       

linePath[21] = [            
new kakao.maps.LatLng(35.156535, 128.998495),
new kakao.maps.LatLng(35.155512, 128.99935),
new kakao.maps.LatLng(35.154986, 128.998431),
new kakao.maps.LatLng(35.153733, 128.998173) 
];       

linePath[22] = [           
new kakao.maps.LatLng(35.155403, 128.998443),
new kakao.maps.LatLng(35.155281, 128.998205),
new kakao.maps.LatLng(35.154392, 128.99784)  
];       

linePath[23] = [           
new kakao.maps.LatLng(35.156858, 128.998498),
new kakao.maps.LatLng(35.156525, 128.998487),
new kakao.maps.LatLng(35.15637, 128.998255),
new kakao.maps.LatLng(35.154487, 128.997481) 
];       

linePath[24] = [           
new kakao.maps.LatLng(35.156207, 128.999322),
new kakao.maps.LatLng(35.156845, 128.998729),
new kakao.maps.LatLng(35.156859, 128.998332),
new kakao.maps.LatLng(35.15658, 128.997922),
new kakao.maps.LatLng(35.15425, 128.99697)    
];       

linePath[25] = [       
new kakao.maps.LatLng(35.157884, 128.991609),
new kakao.maps.LatLng(35.157917, 128.992395),
new kakao.maps.LatLng(35.15665, 128.993486),
new kakao.maps.LatLng(35.156948, 128.994036) 
];       

linePath[26] = [           
new kakao.maps.LatLng(35.157999, 128.993174),
new kakao.maps.LatLng(35.157503, 128.992245),
new kakao.maps.LatLng(35.156328, 128.991959)   
];       

linePath[27] = [          
new kakao.maps.LatLng(35.158803, 128.990608),
new kakao.maps.LatLng(35.15847, 128.990729),
new kakao.maps.LatLng(35.158593, 128.991306),
new kakao.maps.LatLng(35.158322, 128.991716),
new kakao.maps.LatLng(35.158448, 128.992042),
new kakao.maps.LatLng(35.1589, 128.992388)      
];       

linePath[28] = [    
new kakao.maps.LatLng(35.164399, 128.989401),
new kakao.maps.LatLng(35.164047, 128.989618),
new kakao.maps.LatLng(35.163905, 128.98939),
new kakao.maps.LatLng(35.163059, 128.989636),
new kakao.maps.LatLng(35.162949, 128.989242),
new kakao.maps.LatLng(35.158821, 128.990616) 
];       

linePath[29] = [         
new kakao.maps.LatLng(35.163248, 128.989601),
new kakao.maps.LatLng(35.163311, 128.989058),
new kakao.maps.LatLng(35.163981, 128.98877),
new kakao.maps.LatLng(35.16478, 128.990075),
new kakao.maps.LatLng(35.164661, 128.990285),
new kakao.maps.LatLng(35.164709, 128.990666) 
];       

linePath[30] = [         
new kakao.maps.LatLng(35.162832, 128.988147),
new kakao.maps.LatLng(35.163573, 128.987879),
new kakao.maps.LatLng(35.163881, 128.988102),
new kakao.maps.LatLng(35.163894, 128.988297),
new kakao.maps.LatLng(35.164346, 128.989037),
new kakao.maps.LatLng(35.165019, 128.988951),
new kakao.maps.LatLng(35.165172, 128.989254),
new kakao.maps.LatLng(35.164977, 128.989863),
new kakao.maps.LatLng(35.164661, 128.990281)  
];       

linePath[31] = [     
new kakao.maps.LatLng(35.166435, 128.987802),
new kakao.maps.LatLng(35.165566, 128.988239),
new kakao.maps.LatLng(35.166037, 128.989301)  
];       

linePath[32] = [           
new kakao.maps.LatLng(35.168131, 128.98864),
new kakao.maps.LatLng(35.168124, 128.990059)
];       

linePath[33] = [              
new kakao.maps.LatLng(35.169515, 128.988521),
new kakao.maps.LatLng(35.169066, 128.990622),
new kakao.maps.LatLng(35.168772, 128.990818),
new kakao.maps.LatLng(35.167771, 128.990589),
new kakao.maps.LatLng(35.167392, 128.990787),
new kakao.maps.LatLng(35.166857, 128.993354)  
];       

linePath[34] = [        
new kakao.maps.LatLng(35.169757, 128.988488),
new kakao.maps.LatLng(35.169798, 128.98746),
new kakao.maps.LatLng(35.168463, 128.987317),
new kakao.maps.LatLng(35.167527, 128.987503) 
];       

linePath[35] = [           
new kakao.maps.LatLng(35.176384, 128.988492),
new kakao.maps.LatLng(35.176305, 128.989876) 
];       

linePath[36] = [             
new kakao.maps.LatLng(35.181372, 128.991115),
new kakao.maps.LatLng(35.178879, 128.990508),
new kakao.maps.LatLng(35.178633, 128.988555) 
];       

linePath[37] = [            
new kakao.maps.LatLng(35.189269, 128.992485),
new kakao.maps.LatLng(35.188665, 128.992264),
new kakao.maps.LatLng(35.187829, 128.992578),
new kakao.maps.LatLng(35.186878, 128.992472),
new kakao.maps.LatLng(35.186582, 128.991932),
new kakao.maps.LatLng(35.186855, 128.990802) 
];       

linePath[38] = [         
new kakao.maps.LatLng(35.192344, 128.99345),
new kakao.maps.LatLng(35.192207, 128.993738),
new kakao.maps.LatLng(35.189462, 128.993142),
new kakao.maps.LatLng(35.189257, 128.992485),
new kakao.maps.LatLng(35.189518, 128.991412) 
];       

linePath[39] = [          
new kakao.maps.LatLng(35.194921, 128.99435),
new kakao.maps.LatLng(35.193763, 128.993663),
new kakao.maps.LatLng(35.190822, 128.992412)
];       

linePath[40] = [            
new kakao.maps.LatLng(35.19479, 128.99467),
new kakao.maps.LatLng(35.193637, 128.994011),
new kakao.maps.LatLng(35.190732, 128.992743) 
];       

linePath[41] = [            
new kakao.maps.LatLng(35.193435, 128.993008),
new kakao.maps.LatLng(35.193897, 128.991587),
new kakao.maps.LatLng(35.193689, 128.991218),
new kakao.maps.LatLng(35.193745, 128.990804),
new kakao.maps.LatLng(35.191433, 128.990309) 
];       

linePath[42] = [          
new kakao.maps.LatLng(35.193562, 128.992535),
new kakao.maps.LatLng(35.19163, 128.991717)   
];       

linePath[43] = [           
new kakao.maps.LatLng(35.19369, 128.992222),
new kakao.maps.LatLng(35.191171, 128.991177) 
];       

linePath[44] = [             
new kakao.maps.LatLng(35.193833, 128.991783),
new kakao.maps.LatLng(35.19181, 128.991061)   
];       

linePath[45] = [           
new kakao.maps.LatLng(35.19369, 128.991225),
new kakao.maps.LatLng(35.1919, 128.990751)  
];       

linePath[46] = [            
new kakao.maps.LatLng(35.191434, 128.99031),
new kakao.maps.LatLng(35.188949, 128.989778),
new kakao.maps.LatLng(35.187802, 128.989883),
new kakao.maps.LatLng(35.187276, 128.990428),
new kakao.maps.LatLng(35.187234, 128.990808)   
];       

linePath[47] = [        
new kakao.maps.LatLng(35.190536, 128.991311),
new kakao.maps.LatLng(35.187426, 128.990261) 
];       

linePath[48] = [             
new kakao.maps.LatLng(35.191185, 128.99118),
new kakao.maps.LatLng(35.188765, 128.990332)
];       

linePath[49] = [              
new kakao.maps.LatLng(35.190723, 128.990581),
new kakao.maps.LatLng(35.188814, 128.990156),
new kakao.maps.LatLng(35.188064, 128.990248),
new kakao.maps.LatLng(35.188007, 128.99044)   
];       

linePath[50] = [         
new kakao.maps.LatLng(35.17442, 128.976637),
new kakao.maps.LatLng(35.174011, 128.983817),
new kakao.maps.LatLng(35.172856, 128.988125)  
];       

linePath[51] = [           
new kakao.maps.LatLng(35.182483, 128.979407),
new kakao.maps.LatLng(35.174372, 128.977408) 
];       

linePath[52] = [             
new kakao.maps.LatLng(35.181636, 128.983636),
new kakao.maps.LatLng(35.17412, 128.981776)   
];       

linePath[53] = [           
new kakao.maps.LatLng(35.17412, 128.981776),
new kakao.maps.LatLng(35.168611, 128.980378)
];       

linePath[54] = [              
new kakao.maps.LatLng(35.171787, 128.981203),
new kakao.maps.LatLng(35.172105, 128.979114)  
];       

linePath[55] = [            
new kakao.maps.LatLng(35.197088, 128.988083),
new kakao.maps.LatLng(35.193729, 128.987546),
new kakao.maps.LatLng(35.192987, 128.98609),
new kakao.maps.LatLng(35.190503, 128.983572),
new kakao.maps.LatLng(35.16948, 128.978497),
new kakao.maps.LatLng(35.167927, 128.977497)
];       

linePath[56] = [          
new kakao.maps.LatLng(35.195645, 128.99057),
new kakao.maps.LatLng(35.191703, 128.98963),
new kakao.maps.LatLng(35.186377, 128.987091),
new kakao.maps.LatLng(35.173952, 128.984067),
new kakao.maps.LatLng(35.167967, 128.982053),
new kakao.maps.LatLng(35.167445, 128.982115),
new kakao.maps.LatLng(35.162173, 128.984698),
new kakao.maps.LatLng(35.155642, 128.991024),
new kakao.maps.LatLng(35.152027, 128.996253),
new kakao.maps.LatLng(35.150376, 129.000043) 
];       

linePath[57] = [     
new kakao.maps.LatLng(35.156335, 128.991935),
new kakao.maps.LatLng(35.1561, 128.991959),
new kakao.maps.LatLng(35.1533, 128.995236),
new kakao.maps.LatLng(35.152638, 128.995429)  
];       

linePath[58] = [          
new kakao.maps.LatLng(35.158819, 128.989919),
new kakao.maps.LatLng(35.158061, 128.990263),
new kakao.maps.LatLng(35.157305, 128.990289),
new kakao.maps.LatLng(35.156425, 128.990775),
new kakao.maps.LatLng(35.155923, 128.99074)  
];       

linePath[59] = [         
new kakao.maps.LatLng(35.157421, 128.989285),
new kakao.maps.LatLng(35.156273, 128.988954) 
];       

linePath[60] = [             
new kakao.maps.LatLng(35.158409, 128.988322),
new kakao.maps.LatLng(35.156488, 128.987846) 
];       

linePath[61] = [             
new kakao.maps.LatLng(35.159123, 128.987643),
new kakao.maps.LatLng(35.158814, 128.989927) 
];       

linePath[62] = [             
new kakao.maps.LatLng(35.159122, 128.987620),
new kakao.maps.LatLng(35.158560, 128.987240),
new kakao.maps.LatLng(35.156714, 128.986910) 
];

linePath[63] = [                         
new kakao.maps.LatLng(35.159133, 128.987621),
new kakao.maps.LatLng(35.159559, 128.988300),
new kakao.maps.LatLng(35.159336, 128.989719),
new kakao.maps.LatLng(35.158810, 128.990062),
new kakao.maps.LatLng(35.158804, 128.990619)  
];

linePath[64] = [                      
new kakao.maps.LatLng(35.155694, 128.985409),
new kakao.maps.LatLng(35.160178, 128.986622)  
];

linePath[65] = [                         
new kakao.maps.LatLng(35.160178, 128.986622),
new kakao.maps.LatLng(35.161180, 128.988219)    
];

linePath[66] = [                       
new kakao.maps.LatLng(35.160346, 128.984136),
new kakao.maps.LatLng(35.160256, 128.986540)  
];

linePath[67] = [                         
new kakao.maps.LatLng(35.160709, 128.986124),
new kakao.maps.LatLng(35.161359, 128.987195),
new kakao.maps.LatLng(35.161195, 128.988240) 
];

linePath[68] = [                         
new kakao.maps.LatLng(35.157393, 128.984854),
new kakao.maps.LatLng(35.158871, 128.985340),
new kakao.maps.LatLng(35.161501, 128.985317)   
];

linePath[69] = [                       
new kakao.maps.LatLng(35.163167, 128.984206),
new kakao.maps.LatLng(35.164434, 128.987757)  
];

linePath[70] = [                         
new kakao.maps.LatLng(35.164201, 128.979382),
new kakao.maps.LatLng(35.163745, 128.983082),
new kakao.maps.LatLng(35.163997, 128.983787)   
];

linePath[71] = [                       
new kakao.maps.LatLng(35.163997, 128.983787),
new kakao.maps.LatLng(35.165260, 128.987363) 
];

linePath[72] = [                          
new kakao.maps.LatLng(35.165283, 128.977313),
new kakao.maps.LatLng(35.164839, 128.981157),
new kakao.maps.LatLng(35.165023, 128.983276) 
];

linePath[73] = [                         
new kakao.maps.LatLng(35.170847, 128.982851),
new kakao.maps.LatLng(35.170783, 128.983055),
new kakao.maps.LatLng(35.169901, 128.983665),
new kakao.maps.LatLng(35.168967, 128.983503) 
];

linePath[74] = [                        
new kakao.maps.LatLng(35.172747, 128.979251),
new kakao.maps.LatLng(35.172302, 128.983395) 
];

linePath[75] = [                          
new kakao.maps.LatLng(35.172305, 128.983392),
new kakao.maps.LatLng(35.172140, 128.986134),
new kakao.maps.LatLng(35.170810, 128.986655),
new kakao.maps.LatLng(35.170344, 128.986853),
new kakao.maps.LatLng(35.169704, 128.987066),
new kakao.maps.LatLng(35.168683, 128.986661)  
];

linePath[76] = [                     
new kakao.maps.LatLng(35.162073, 128.984437),
new kakao.maps.LatLng(35.141231, 128.979579) 
];

linePath[77] = [                          
new kakao.maps.LatLng(35.142797, 128.979927),
new kakao.maps.LatLng(35.144183, 128.975474) 
];

linePath[78] = [                          
new kakao.maps.LatLng(35.142796, 128.979936),
new kakao.maps.LatLng(35.142420, 128.982034) 
];

linePath[79] = [                          
new kakao.maps.LatLng(35.156321, 128.973802),
new kakao.maps.LatLng(35.153455, 128.990448)  
];

linePath[80] = [                         
new kakao.maps.LatLng(35.155466, 128.978725),
new kakao.maps.LatLng(35.158500, 128.979602) 
];

linePath[81] = [                          
new kakao.maps.LatLng(35.155459, 128.978737),
new kakao.maps.LatLng(35.154186, 128.978119),
new kakao.maps.LatLng(35.152875, 128.977788)    
];

linePath[82] = [                      
new kakao.maps.LatLng(35.152788, 129.001519),
new kakao.maps.LatLng(35.152788, 129.001519),
new kakao.maps.LatLng(35.153758, 129.004927),
new kakao.maps.LatLng(35.152479, 129.005671)  
];

linePath[83] = [                       
new kakao.maps.LatLng(35.153186, 129.005371),
new kakao.maps.LatLng(35.153553, 129.005951),
new kakao.maps.LatLng(35.154299, 129.005372),
new kakao.maps.LatLng(35.155250, 129.005020),
new kakao.maps.LatLng(35.155485, 129.005019),
new kakao.maps.LatLng(35.155953, 129.005328),
new kakao.maps.LatLng(35.156136, 129.005810) 
];

linePath[84] = [                     
new kakao.maps.LatLng(35.156713, 129.005485),
new kakao.maps.LatLng(35.156296, 129.005047),
new kakao.maps.LatLng(35.156058, 129.004959),
new kakao.maps.LatLng(35.155525, 129.004632),
new kakao.maps.LatLng(35.154843, 129.004622),
new kakao.maps.LatLng(35.154404, 129.004316),
new kakao.maps.LatLng(35.153774, 129.004296) 
];

linePath[85] = [                     
new kakao.maps.LatLng(35.157032, 129.005395),
new kakao.maps.LatLng(35.156429, 129.004756),
new kakao.maps.LatLng(35.155612, 129.004262),
new kakao.maps.LatLng(35.154885, 129.004240),
new kakao.maps.LatLng(35.154564, 129.003995),
new kakao.maps.LatLng(35.154187, 129.003925)  
];

linePath[86] = [                     
new kakao.maps.LatLng(35.153757, 129.003459),
new kakao.maps.LatLng(35.154610, 129.003601),
new kakao.maps.LatLng(35.154991, 129.003871),
new kakao.maps.LatLng(35.156044, 129.003849) 
];

linePath[87] = [                        
new kakao.maps.LatLng(35.156043, 129.003842),
new kakao.maps.LatLng(35.156029, 129.002023),
new kakao.maps.LatLng(35.155843, 129.001865),
new kakao.maps.LatLng(35.155591, 129.001836),
new kakao.maps.LatLng(35.155343, 129.002248),
new kakao.maps.LatLng(35.154401, 129.002284),
new kakao.maps.LatLng(35.153742, 129.002110)  
];

linePath[88] = [                    
new kakao.maps.LatLng(35.169579, 128.976867),
new kakao.maps.LatLng(35.169457, 128.978631),
new kakao.maps.LatLng(35.167598, 128.982415),
new kakao.maps.LatLng(35.167308, 128.983446),
new kakao.maps.LatLng(35.167731, 128.986318),
new kakao.maps.LatLng(35.167514, 128.987489),
new kakao.maps.LatLng(35.166981, 128.987903),
new kakao.maps.LatLng(35.166666, 128.988815)
];

linePath[89] = [                     
new kakao.maps.LatLng(35.131079, 128.972028),
new kakao.maps.LatLng(35.129354, 128.975200),
new kakao.maps.LatLng(35.129113, 128.977354),
new kakao.maps.LatLng(35.128758, 128.978160),
new kakao.maps.LatLng(35.128087, 128.978525),
new kakao.maps.LatLng(35.127700, 128.978440),
new kakao.maps.LatLng(35.126608, 128.977833),
new kakao.maps.LatLng(35.123936, 128.974723),
new kakao.maps.LatLng(35.122972, 128.973151),
new kakao.maps.LatLng(35.123058, 128.972680),
new kakao.maps.LatLng(35.123894, 128.971420),
new kakao.maps.LatLng(35.124907, 128.969009),
new kakao.maps.LatLng(35.124255, 128.966964),
new kakao.maps.LatLng(35.124422, 128.966362) 
];

linePath[90] = [              
new kakao.maps.LatLng(35.129067, 128.970392),
new kakao.maps.LatLng(35.128645, 128.971550),
new kakao.maps.LatLng(35.128495, 128.973136),
new kakao.maps.LatLng(35.127714, 128.978428) 
];

linePath[91] = [                        
new kakao.maps.LatLng(35.128201, 128.969777),
new kakao.maps.LatLng(35.126546, 128.970715),
new kakao.maps.LatLng(35.125424, 128.972125),
new kakao.maps.LatLng(35.124771, 128.972600),
new kakao.maps.LatLng(35.124520, 128.973294),
new kakao.maps.LatLng(35.123648, 128.974208)  
];

linePath[92] = [                     
new kakao.maps.LatLng(35.157433, 128.989284),
new kakao.maps.LatLng(35.158082, 128.990317),
new kakao.maps.LatLng(35.156363, 128.991879),
new kakao.maps.LatLng(35.152953, 128.996377),
new kakao.maps.LatLng(35.152373, 128.997867),
new kakao.maps.LatLng(35.151251, 129.002510),
new kakao.maps.LatLng(35.151187, 129.004030),
new kakao.maps.LatLng(35.151959, 129.014004),
new kakao.maps.LatLng(35.152562, 129.016379)
];

linePath[93] = [                    
new kakao.maps.LatLng(35.142064, 128.988367),
new kakao.maps.LatLng(35.143892, 128.991917),
new kakao.maps.LatLng(35.144456, 128.995666),
new kakao.maps.LatLng(35.144441, 128.997526),
new kakao.maps.LatLng(35.145885, 129.000773),
new kakao.maps.LatLng(35.146875, 129.011136),
new kakao.maps.LatLng(35.148697, 129.011600),
new kakao.maps.LatLng(35.151157, 129.011305) 
];

linePath[94] = [                    
new kakao.maps.LatLng(35.150299, 129.011429),
new kakao.maps.LatLng(35.150609, 129.015138),
new kakao.maps.LatLng(35.150801, 129.016249) 
];

linePath[95] = [                         
new kakao.maps.LatLng(35.149275, 129.004038),
new kakao.maps.LatLng(35.149740, 129.005373),
new kakao.maps.LatLng(35.150295, 129.011422)  
];

linePath[96] = [                        
new kakao.maps.LatLng(35.145953, 129.001132),
new kakao.maps.LatLng(35.145494, 129.001297),
new kakao.maps.LatLng(35.145434, 129.002786),
new kakao.maps.LatLng(35.145314, 129.002798),
new kakao.maps.LatLng(35.145286, 129.003127),
new kakao.maps.LatLng(35.145172, 129.003161),
new kakao.maps.LatLng(35.145160, 129.003420),
new kakao.maps.LatLng(35.144823, 129.003466),
new kakao.maps.LatLng(35.144824, 129.003781),
new kakao.maps.LatLng(35.144427, 129.004056) 
];

linePath[97] = [                  
new kakao.maps.LatLng(35.145778, 129.000235),
new kakao.maps.LatLng(35.144683, 129.000204),
new kakao.maps.LatLng(35.144598, 129.000511) 
];

linePath[98] = [                         
new kakao.maps.LatLng(35.148688, 129.011577),
new kakao.maps.LatLng(35.148877, 129.014186) 
];

linePath[99] = [                          
new kakao.maps.LatLng(35.148346, 129.007662),
new kakao.maps.LatLng(35.148681, 129.011576) 
];

linePath[100] = [                          
new kakao.maps.LatLng(35.147672, 129.006332),
new kakao.maps.LatLng(35.148034, 129.011435) 
];

linePath[101] = [                          
new kakao.maps.LatLng(35.155669, 128.991020),
new kakao.maps.LatLng(35.143223, 128.987806),
new kakao.maps.LatLng(35.140489, 128.989472),
new kakao.maps.LatLng(35.138954, 128.992448),
new kakao.maps.LatLng(35.129109, 129.004066) 
];

linePath[102] = [                       
new kakao.maps.LatLng(35.136866, 128.994875),
new kakao.maps.LatLng(35.135904, 128.995663),
new kakao.maps.LatLng(35.131449, 128.996244) 
];

linePath[103] = [                         
new kakao.maps.LatLng(35.137712, 128.993996),
new kakao.maps.LatLng(35.137251, 128.993460),
new kakao.maps.LatLng(35.137014, 128.992575),
new kakao.maps.LatLng(35.136127, 128.992917),
new kakao.maps.LatLng(35.135036, 128.992853),
new kakao.maps.LatLng(35.134220, 128.993067) 
];

linePath[104] = [                      
new kakao.maps.LatLng(35.140736, 128.983169),
new kakao.maps.LatLng(35.142067, 128.988352)              
];




// 지도에 표시할 선을 생성합니다
for(i =0; i<linePath.length; i++){
var polyline = new kakao.maps.Polyline({
    path: linePath[i], // 선을 구성하는 좌표배열 입니다
    strokeWeight: 4, // 선의 두께 입니다
    strokeColor: '#f00', // 선의 색깔입니다
    strokeOpacity: 0.7, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
    strokeStyle: 'solid' // 선의 스타일입니다
});

// 지도에 선을 표시합니다 
polyline.setMap(map);  
}

</script>
</body>
</html>