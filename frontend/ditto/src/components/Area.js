import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import FlexBox from "./Common/FlexBox";
import FlexTextBox from "./Common/FlexTextBox";
import Navbar from "./Navbar";
import ListItem from '@mui/material/ListItem';
import AddLocationAltIcon from '@mui/icons-material/AddLocationAlt';
import Button from '@mui/material/Button';

const Icon = styled(AddLocationAltIcon)`
  color: #74EABC  !important;
  margin: 0 0.3rem 0 0;
`;

const Btn = styled(Button)`
 width: 12rem;
 height: 3rem;
 border: 1.8px solid rgb(0 0 0 / 15%) !important;
 color: #333333 !important;
 margin-bottom: 0.4rem !important;

`;

const areaList = ["서울특별시", "인천광역시", "대구광역시", "대전광역시", "광주광역시", "부산광역시", "울산광역시", "제주특별자치도" ];

const Area = (props) =>{
	const navigate = useNavigate();
	const onClickBtn = (x) => {
		props.changeAreaId(x);
		navigate("/place");
	};

  const Btns = () => {
		const newArr = [];
		for (let i = 0; i < 8; i += 1) {
		  newArr.push(
        <ListItem disablePadding onClick={()=> onClickBtn(i)}>
        <Btn variant="outlined">
          <Icon/>
          <FlexTextBox fontWeight={400} fontSize="0.9rem">{areaList[i]}
          </FlexTextBox>
        </Btn>
        </ListItem>
		  );
		}
		return newArr;
	};

  return (
    <FlexBox column center gap="2rem" >
	    <Navbar/>
      <FlexBox center column>
			  {Btns()}
      </FlexBox>
     
    </FlexBox>
  );
}

export default Area;
