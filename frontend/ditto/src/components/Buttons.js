import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import FlexBox from "./FlexBox";
import Button from '@mui/material/Button';

const Buttonn =  styled(Button)`
	width: 16rem;
	height: 3.2rem;
	font-size: 1rem !important;
	font-weight: 600 !important;
`;


const Buttons = (props) =>{
	const navigate = useNavigate();
	  
	const onClickBtn = (x, y) => {
		props.changeX(x);
		props.changeY(y);
		navigate("/map");
	};
	return (
	  <>
		 <FlexBox column center gap="1rem" padding="5rem 0">
			<Buttonn variant="outlined" onClick={()=> onClickBtn(37.61066839994, 126.9973271351)}>국민대학교</Buttonn>
			<Buttonn variant="outlined" onClick={()=> onClickBtn(37.52611006837, 126.934905562)}>한강시민공원</Buttonn>
			<Buttonn variant="outlined" onClick={()=> onClickBtn(37.5088133991, 127.1000508263)}>롯데월드</Buttonn>
			<Buttonn variant="outlined" onClick={()=> onClickBtn(37.5551684267, 126.9369626773)}>신촌 물총 축제</Buttonn>
			<Buttonn variant="outlined" onClick={()=> onClickBtn(37.5344801681, 126.994614456)}>이태원 축제</Buttonn>
			<Buttonn variant="outlined">서울시</Buttonn>
		 </FlexBox>
	  </>
	);
  }
  
  export default Buttons;
  