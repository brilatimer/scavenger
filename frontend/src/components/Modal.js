import React, { Component } from "react";
import ClueFormList from "./ClueFormList";

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

      updateCluesCallback = updatedClues => {
        const activeItem = { ...this.state.activeItem, clues: updatedClues };
        this.setState({ activeItem });
      }

      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> New Scavenger Hunt </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="title">Game Title</Label>
                  <Input
                    type="text"
                    name="game_title"
                    defaultValue={this.state.activeItem.game_title}
                    onChange={this.handleChange}
                    placeholder="Game Title"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Player's Phone Number</Label>
                  <Input
                    type="text"
                    name="players_phone_number"
                    defaultValue={this.state.activeItem.players_phone_number}
                    onChange={this.handleChange}
                    placeholder="Player's Phone Number"
                  />
                </FormGroup>
                <ClueFormList
                  activeItemClues={this.state.activeItem.clues}
                  updateCluesCallback={this.updateCluesCallback}
                />
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Save
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }
