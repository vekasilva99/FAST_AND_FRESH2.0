import React, { Component } from "react";
import "bootswatch/dist/minty/bootstrap.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "antd/dist/antd.css";
import BaseRouter from "./routes";
import { BrowserRouter as Router } from "react-router-dom";
import CustomLayout from "./containers/Layout";
import ProductList from "./containers/ProductListView";
import ProductScrum from "./components/ProductScrum";
import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="container">
          <div id="task-container">
            <div id="form-wrapper">
              <form id="form">
                <div className="flex-wrapper">
                  <div style={{ flex: 6 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="title"
                      placeholder="Add task"
                    ></input>
                  </div>
                  <div style={{ flex: 1 }}>
                    <input
                      className="btn btn-warning"
                      id="sumbit"
                      type="submit"
                      name="Add"
                    ></input>
                  </div>
                </div>
              </form>
            </div>
            <div id="list-wrapper"></div>
          </div>
        </div>

        {/* <Router>
          <CustomLayout>
            <BaseRouter />
          </CustomLayout>
        </Router> */}
      </div>
    );
  }
}

export default App;
