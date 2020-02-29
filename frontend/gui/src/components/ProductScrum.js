import React from "react";
import Products from "../components/Product";
import axios from "axios";
import { Divider } from "antd";

class ProductScrum extends React.Component {
  reder() {
    return (
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
    );
  }
}

export default ProductScrum;
