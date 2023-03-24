import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
// import { useNavigate } from "react-router-dom";
// import { useEffect } from 'react';
import { useState } from 'react';
import Buttons from "./components/Buttons";
import Map from "./components/map";

const App = () =>{
  // const navigate = useNavigate();
  const [x, setX] = useState(37.61066839994)
  const [y, setY] = useState(126.9973271351)


  
  return (
    <>
     <Router>
     <Routes>
        <Route path="/" element={<Buttons changeX={setX} changeY={setY} />} />
        <Route path="/map" element={<Map x={x} y={y}/>} />
      </Routes>

      </Router>
    </>
  );
}

export default App;
