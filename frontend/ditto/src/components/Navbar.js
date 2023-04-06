import * as React from 'react';
import styled from "styled-components";

const Logo = styled.img`
  width: 8.5rem;
`


const Navbar =()=> {

  return (
    <>
      <Logo src="images/logo.png"/>
      {/* <Logo src="images/logo2.png"/> */}
    </>
  );
}

export default Navbar;