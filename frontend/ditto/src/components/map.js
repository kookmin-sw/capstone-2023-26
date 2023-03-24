/*global kakao*/ 
import React, { useEffect } from 'react'

const Map =(props)=> {
  useEffect(()=>{
    var container = document.getElementById('map');
    var options = {
      center: new kakao.maps.LatLng(props.x , props.y),
      level: 2
    };
    var map = new kakao.maps.Map(container, options);

    var markerPosition  = new kakao.maps.LatLng(37.365264512305174, 127.10676860117488); 
    var marker = new kakao.maps.Marker({
      position: markerPosition
    });
    marker.setMap(map);
      
    var polygonPath = [
      new kakao.maps.LatLng(33.45133510810506, 126.57159381623066),
      new kakao.maps.LatLng(33.44955812811862, 126.5713551811832),
      new kakao.maps.LatLng(33.449986291544086, 126.57263296172184),
      new kakao.maps.LatLng(33.450682513554554, 126.57321034054742),
      new kakao.maps.LatLng(33.451346760004206, 126.57235740081413) 
    ];
    var polygon = new kakao.maps.Polygon({
      path:polygonPath, // 그려질 다각형의 좌표 배열입니다
      strokeWeight: 3, // 선의 두께입니다
      strokeColor: '#39DE2A', // 선의 색깔입니다
      strokeOpacity: 0.8, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
      strokeStyle: 'longdash', // 선의 스타일입니다
      fillColor: '#A2FF99', // 채우기 색깔입니다
      fillOpacity: 0.7 // 채우기 불투명도 입니다
    });
    polygon.setMap(map);
  
  },)

    return (
        <>
          <div id="map" style={{width:"100%", height:"100vh"}}></div>
        </>
    )
}

export default Map;