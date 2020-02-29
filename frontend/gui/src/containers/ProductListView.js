import React from "react";
import Products from "../components/Product";
import axios from "axios";
import CustomProductForm from "../components/ProductForm";

const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: "http://ant.design",
    title: `ant design part ${i}`,
    avatar: "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
    description:
      "Ant Design, a design language for background applications, is refined by Ant UED Team.",
    content:
      "We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently."
  });
}

class ProductList extends React.Component {
  state = {
    products: []
  };
  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/product").then(res => {
      this.setState({
        products: res.data
      });
      console.log(res.data);
    });
  }
  render() {
    return (
      <div>
        <Products data={this.state.products} />
        <br />
        <h2>Crear Producto</h2>
        <CustomProductForm requestType="post" productId={null} btnText="Add" />
      </div>
    );
  }
}

export default ProductList;
