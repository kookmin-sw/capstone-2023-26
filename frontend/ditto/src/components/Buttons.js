import styled from "styled-components";
import FlexBox from "./FlexBox";
import Button from '@mui/material/Button';

const Buttonn =  styled(Button)`
	width: 16rem;
	height: 3.2rem;
	font-size: 1rem !important;
	font-weight: 600 !important;
`;

const Buttons = () =>{
	return (
	  <>
		 <FlexBox column center gap="1rem" padding="3rem 0">
			<Buttonn variant="outlined">국민대학교</Buttonn>
			<Buttonn variant="outlined">한강시민공원</Buttonn>
			<Buttonn variant="outlined">롯데월드</Buttonn>
			<Buttonn variant="outlined">신촌 물총 축제</Buttonn>
			<Buttonn variant="outlined">이태원 축제</Buttonn>
			<Buttonn variant="outlined">서울시</Buttonn>
		 </FlexBox>
	  </>
	);
  }
  
  export default Buttons;
  