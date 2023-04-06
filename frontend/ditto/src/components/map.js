/*global kakao*/ 
import React, { useEffect } from 'react'
import FlexBox from "./Common/FlexBox";

const Map =(props)=> {
  useEffect(()=>{
    var container = document.getElementById('map');
    var options = {
      center: new kakao.maps.LatLng(props.x , props.y),
      level: 3
    };
    var map = new kakao.maps.Map(container, options);

    var circle = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.6109026256, 126.9961832276),  // 원의 중심좌표 입니다 
      radius: 26, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ff001691', // 채우기 색깔입니다
      fillOpacity: 0.8  // 채우기 불투명도 입니다   
    }); 
  
    circle.setMap(map);

    var circle2 = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.61130804, 126.9954130528),  // 원의 중심좌표 입니다 
      radius: 18, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ffac0091', // 채우기 색깔입니다
      fillOpacity: 0.8  // 채우기 불투명도 입니다   
    }); 
  
    circle2.setMap(map);

    var circle3 = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.6105084509, 126.99644090),  // 원의 중심좌표 입니다 
      radius: 17, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ffac0091', // 채우기 색깔입니다
      fillOpacity: 0.8  // 채우기 불투명도 입니다   
    }); 
  
    circle3.setMap(map);

    var circle4 = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.6106526312, 126.9972676758),  // 원의 중심좌표 입니다 
      radius: 14, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ff001691', // 채우기 색깔입니다
      fillOpacity: 0.8  // 채우기 불투명도 입니다   
    }); 
  
    circle4.setMap(map);

    var circle5 = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.6113193719, 126.9976753801),  // 원의 중심좌표 입니다 
      radius: 15, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ffac0091', // 채우기 색깔입니다
      fillOpacity: 0.6  // 채우기 불투명도 입니다   
    }); 
  
    circle5.setMap(map);

    var circle6 = new kakao.maps.Circle({
      center : new kakao.maps.LatLng(37.61193652435, 126.996633378),  // 원의 중심좌표 입니다 
      radius: 18, // 미터 단위의 원의 반지름입니다 
      strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      fillColor: '#ff001691', // 채우기 색깔입니다
      fillOpacity: 0.8  // 채우기 불투명도 입니다   
    }); 
  
    circle6.setMap(map);
  
  
  },)

    return (
        <FlexBox width="auto">
          <div id="map" style={{width:"100%", height:"100vh"}}></div>
        </FlexBox>
    )
}

export default Map;