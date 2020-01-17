import React, { Component } from "react";

    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Start Game </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="description">Player's Phone Number</Label>
                  <Input
                    type="text"
                    name="players_phone_number"
                    defaultValue=""
                    onChange={this.handleChange}
                    placeholder="+1xxx xxx xxxx"
                  />
                </FormGroup>
              </Form>


            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Launch
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }
