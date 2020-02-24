import React from "react";
import { Layout } from "antd";
import CustomNavbar from "./Navbar";
const { Header, Footer, Content } = Layout;

const CustomLayout = props => {
  return (
    <Layout>
      <CustomNavbar></CustomNavbar>
      <Header style={{ padding: "0 50px", background: "#F0F2F5" }}></Header>
      <Content style={{ padding: "0 50px" }}>
        <div style={{ background: "#fff", padding: 24, minHeight: 280 }}>
          {props.children}
        </div>
      </Content>
      <Footer>Footer</Footer>
    </Layout>
  );
};

export default CustomLayout;
