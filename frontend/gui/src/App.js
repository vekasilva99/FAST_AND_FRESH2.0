import React, { Component } from "react";
import "bootswatch/dist/minty/bootstrap.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "antd/dist/antd.css";
import BaseRouter from "./routes";
import { BrowserRouter as Router } from "react-router-dom";
import CustomLayout from "./containers/Layout";
import ProductList from "./containers/ProductListView";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
    );
  }
}

export default App;
