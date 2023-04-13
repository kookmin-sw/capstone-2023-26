/*global kakao*/ 
import React, { useEffect } from 'react'
import FlexBox from "./Common/FlexBox";
import dummyMaps from './dummyMaps';

const Map =(props)=> {
  useEffect(()=>{
    var container = document.getElementById('map');
    var options = {
      center: new kakao.maps.LatLng(dummyMaps[props.areaId][props.plcId].location[0] , dummyMaps[props.areaId][props.plcId].location[1]),
      level: 3
    };
    var map = new kakao.maps.Map(container, options);

    var tmp = dummyMaps[props.areaId][props.plcId].crowd;

    for (let i = 0; i < tmp.length; i += 1) {
      var circle = new kakao.maps.Circle({
        center : new kakao.maps.LatLng(tmp[i][0], tmp[i][1]),  // 원의 중심좌표 입니다 
        radius: 16, // 미터 단위의 원의 반지름입니다 
        strokeOpacity: 0, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
        fillColor: '#ff001691', // 채우기 색깔입니다
        fillOpacity: 0.8  // 채우기 불투명도 입니다   
      }); 
      circle.setMap(map);
    }

  },)

    return (
        <FlexBox width="auto">
          <div id="map" style={{width:"100%", height:"100vh"}}></div>
        </FlexBox>
    )
}

export default Map;