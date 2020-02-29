import React from "react";
import { Form, Input, Button, Radio, Select } from "antd";
import axios from "axios";
const FormItem = Form.Item;
const { Option } = Select;

class CustomProductForm extends React.Component {
  state = {
    providers: []
  };
  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/provider/").then(res => {
      this.setState({
        providers: res.data
      });
      console.log(res.data);
    });
  }

  handleFormSubmit = event => {
    event.preventDefault();
    const product_name = event.target.elements.product_name.value;
    const provider = event.target.elements.provider.value;
    const is_special = event.target.elements.is_special.value;
    const is_active = event.target.elements.is_active.value;

    console.log(product_name, is_active, is_special, provider);

    // switch (requestType) {
    //   case "post":
    //     return axios
    //       .post("http://127.0.0.1:8000/api/product", {
    //         product_name: product_name,
    //         provider: provider,
    //         is_special: is_special,
    //         is_active: is_active
    //       })
    //       .then(res => console.log(res))
    //       .catch(error => console.err(error));

    //   case "put":
    //     return axios
    //       .put("http://127.0.0.1:8000/api/product/${productId}", {
    //         product_name: product_name,
    //         provider: null,
    //         is_special: is_special,
    //         is_active: is_active
    //       })
    //       .then(res => console.log(res))
    //       .catch(error => console.err(error));
    // }
  };

  render() {
    return (
      <div>
        <Form onSubmit={event => this.handleFormSubmit(event)}>
          <FormItem label="Product Name">
            <Input name="product_name" placeholder="Name of the Product" />
          </FormItem>

          <Form.Item name="provider" ref="providerSelected" label="Provider">
            <Select name="provider" placeholder="Please select a Provider">
              {this.state.providers.map(provider => (
                <Option key={provider.id} value={provider.id}>
                  {provider.provider_name}
                </Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item name="is_special" label="Is it Special?">
            <Radio.Group name="is_special">
              <Radio.Button value="True">Yes</Radio.Button>
              <Radio.Button value="False">No</Radio.Button>
            </Radio.Group>
          </Form.Item>

          <Form.Item name="is_active" label="Is it Active?">
            <Radio.Group name="is_active">
              <Radio.Button value="True">Yes</Radio.Button>
              <Radio.Button value="False">No</Radio.Button>
            </Radio.Group>
          </Form.Item>

          <FormItem>
            <Button type="primary" htmlType="submit">
              {this.props.btnText}
            </Button>
          </FormItem>
        </Form>
      </div>
    );
  }
}

export default CustomProductForm;
