import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import FlexBox from "./Common/FlexBox";
import Navbar from "./Navbar";
import List from '@mui/material/List';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import RoomIcon from '@mui/icons-material/Room';
import dummyPlaces from "./dummyPlaces";

const Icon = styled(RoomIcon)`
	color: #74EABC  !important;
`;

const Place = (props) =>{
	const navigate = useNavigate();
	const onClickBtn = (id) => {
		props.changePlcId(id);
		navigate("/map");
	};

	const Btns = (places) => {
		const newArr = [];
		for (let i = 0; i < places.length; i += 1) {
		  newArr.push(
			<ListItem onClick={()=> onClickBtn(i)}>
			<ListItemText primary={places[i][0]} secondary={places[i][1]} />
			<ListItemAvatar>
			  <Avatar sx={{background:"#f4f4f4"}}>
				<Icon />
			  </Avatar>
			</ListItemAvatar>
		  </ListItem>
		  );
		}
		return newArr;
	};

  return (
    <FlexBox center column>
		<Navbar/>
		<List sx={{ width: '100%', maxWidth: 250, bgcolor: 'background.paper', marginTop:2 }}>
			{Btns(dummyPlaces[props.areaId]["place"])}
		</List>	
    </FlexBox>
  );
}

export default Place;
