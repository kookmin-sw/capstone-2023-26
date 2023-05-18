import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import FlexBox from "./Common//FlexBox";
import FlexTextBox from "./Common/FlexTextBox";
import Button from '@mui/material/Button';
import Navbar from "./Navbar";

const Img = styled.img`
	width: 42.5%;
	height: 40vh;
`;

const ImgMap = styled.img`
	width: 20%;
	height: 30vh;
	border-radius: 1.4rem;
`;

const ImgAI = styled.img`
	margin: 3rem 0 0 0;
	width: 21%;
	height: 30vh;
	border-radius: 1.4rem;
`;



const BtnMap = styled(Button)`
	width: 7.6rem;
	height: 2.6rem;
	font-size: 0.8rem !important;
	font-weight: 600 !important;
	background-color: rgb(117 177 236 / 88%) !important;
`;


const Home = () =>{
	const navigate = useNavigate();
	  
	const onClickMap = (x, y) => {
		navigate("/area");
	};
	return (
	  <>
	        <Navbar/>
			<FlexBox column center margin="5rem 0 0 0" gap="5rem">
				<FlexBox center>
					<FlexBox column>
						<FlexTextBox fontSize="1.8rem">드론을 활용한 <br/> 인구 밀집도 및 위험 감지 <br/> </FlexTextBox>
						<FlexTextBox margin="1rem 0 0 0" fontSize="1.1rem" fontWeight="600" color="#353535">시민들의 안전하고 즐거운 야외활동에 DITTO가 함께합니다 :)</FlexTextBox>
					</FlexBox>
					<Img src="images/drone.jpg" alt=""/>
				</FlexBox>
				<FlexBox center width="100%" gap="7%">
					<ImgMap src="images/map.jpg"/>
					<FlexBox column>
					<FlexTextBox fontSize="1.5rem">인구 밀집도 지도</FlexTextBox>
					<FlexBox column center gap="1rem" margin="0.5rem 0 0 0">
						
						<FlexTextBox fontSize="0.85rem" fontWeight="600" color="#353535">인구 밀집도를 지도에 분류된 색상으로 표시합니다.  
							<br/>사용자는 이를 통해 혼잡한 곳은 피하며  
							<br/>사고를 예방하고 안전하게 야외활동을 즐길 수 있습니다.
						</FlexTextBox>
						<BtnMap variant="contained" onClick={()=> onClickMap(37.61066839994, 126.9973271351)}>지도 보기</BtnMap>
					</FlexBox>
					</FlexBox>
				</FlexBox>

				<FlexBox center width="100%" gap="5%">
					
					<FlexBox column>
					<FlexTextBox fontSize="1.5rem">인공지능을 활용한 <br/> 인구 밀집도 및 위험 감지</FlexTextBox>
					<FlexBox column center gap="1rem" margin="0.5rem 0 0 0">
						
						<FlexTextBox fontSize="0.85rem" fontWeight="600" color="#353535">드론을 통해 받아온 영상에서 사람 수를 알아내 인구 밀집도를 
							<br/> 계산합니다. 쓰러짐, 폭행 등 위험 상황을 감지하여 사고를 
							<br/> 예방하고 안전하게 야외활동을 즐길 수 있습니다.
						</FlexTextBox>
						<BtnMap variant="contained">관리자 화면</BtnMap>
					</FlexBox>
					</FlexBox>
					<ImgAI src="images/ai.png"/>
				</FlexBox>
			</FlexBox>
			

	  </>
	);
  }
  
  export default Home;
  