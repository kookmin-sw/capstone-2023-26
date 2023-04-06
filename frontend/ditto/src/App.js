import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import { useState } from 'react';
import Home from "./components/Home";
import Area from "./components/Area";
import Place from "./components/Place";
import Map from "./components/Map";

const App = () =>{
  const [x, setX] = useState(37.61066839994)
  const [y, setY] = useState(126.9973271351)
  const [id, setId] = useState(0)

  return (
    <>
     <Router>
     <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/area" element={<Area id={id} changeId={setId}/>} />
        <Route path="/place" element={<Place x={x} y={y} changeX={setX} changeY={setY} id={id}/>} />
        <Route path="/map" element={<Map x={x} y={y}/>} />
      </Routes>

      </Router>
    </>
  );
}

export default App;
