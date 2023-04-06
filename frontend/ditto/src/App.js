import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import { useState } from 'react';
import Home from "./components/Home";
import Area from "./components/Area";
import Place from "./components/Place";
import Map from "./components/Map";

const App = () =>{
  const [areaId, setAreaId] = useState(0)
  const [plcId, setPlcId] = useState(0)

  return (
    <>
     <Router>
     <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/area" element={<Area areaId={areaId} changeAreaId={setAreaId}/>} />
        <Route path="/place" element={<Place areaId={areaId} changePlcId={setPlcId}/>} />
        <Route path="/map" element={<Map areaId={areaId} plcId={plcId}/>} />
      </Routes>

      </Router>
    </>
  );
}

export default App;
