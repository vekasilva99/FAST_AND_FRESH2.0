import React from "react";
import { Route } from "react-router-dom";
import ProductList from "./containers/ProductListView";

const BaseRouter = () => (
  <div>
    <Route exact path="/" component={ProductList} />
  </div>
);

export default BaseRouter;
