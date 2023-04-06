/* eslint-disable react/jsx-props-no-spreading */
import { useState } from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import FaceIcon from '@mui/icons-material/Face';
import styled from "styled-components";
import FlexBox from "./FlexBox";
// import { NotiList } from "components/Navbar/Noti";

const Logo = styled.div`
  margin: 0.5rem 2rem 0 0;
  font-size: 1.4rem;
  font-weight: 800;
  color: #1976d2;
`;


const TabsLib = styled(Tabs)`
  .css-heg063-MuiTabs-flexContainer {
    color: "#ffffff";
  }
  .css-1h9z7r5-MuiButtonBase-root-MuiTab-root.Mui-selected {

    font-size: 0.9rem;
  }
  .css-1aquho2-MuiTabs-indicator {
  }
  [type="reset"],
  [type="submit"],
  button,
  html [type="button"] {
    color: "#a3a3a3";
    font-size: 0.9rem;
    font-weight: 500;
  }
`;

const TabPanel = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 2, padding: 0, marginTop: 1.5 }}>
          <div>{children}</div>
        </Box>
      )}
    </div>
  );
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}



const Navbar = ({ notis, isFetched }) => {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <FlexBox>
    <Logo>DITTO</Logo>
    <Box sx={{ width: "100%" }}>
      <Box sx={{ borderBottom: 1, borderColor: "divider", padding:"0 42%" }}>
        <TabsLib
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
        >
          <Tab label="장소" {...a11yProps(0)} />
          <Tab label="관리자" {...a11yProps(1)} />
        </TabsLib>
      </Box>
      {/* <TabPanel value={value} index={0}>
        {isFetched && <NotiList newNoti notis={notis} />}
      </TabPanel>
      <TabPanel value={value} index={1}>
        {isFetched && <NotiList notis={notis} />}
      </TabPanel> */}
    </Box>
    </FlexBox>
  );
};
export default Navbar;