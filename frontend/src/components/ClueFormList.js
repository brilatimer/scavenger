import React, { Component } from "react";
// import './styles/ClueFormList.css';
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

export default class ClueFormList extends Component {
  constructor(props) {
    super(props);
    console.log(this.props.activeItemClues)
    this.state = {
      activeItemClues: this.props.activeItemClues
    };
  }

handleChange = e => {
  let { name, value } = e.target;
  let index = e.target.id.split("+")[0];
  const clues = [ ...this.state.activeItemClues];
  clues[index][name]=value;
  // activeItemClues[e.target.id][name] = value;
  this.setState({ activeItemClues: clues});
  this.props.updateCluesCallback(clues);
  };

  addClue = () => {
    const clues = [ ...this.state.activeItemClues];
    clues.push({question : "", answer: "", hint : ""});
    this.setState({ activeItemClues: clues});
  }


  render() {
  return (
    <div className="clueElements">
      <div>{this.state.activeItemClues.map((clue, i) => {
              return (
                <div>
                <Label for="name">Question {i + 1}</Label>
                <Input
                id={`${i}+question`}
                type="text"
                name="question"
                defaultValue={clue.question}
                onChange={this.handleChange}
                placeholder="Question"
            />
                <Label for="name">Answer</Label>
                <Input
                id={`${i}+answer`}
                type="text"
                name="answer"
                defaultValue={clue.answer}
                onChange={this.handleChange}
                placeholder="Answer"
            />
                <Label for="name">Hint</Label>
                <Input
                id={`${i}+hint`}
                type="text"
                name="hint"
                defaultValue={clue.hint}
                onChange={this.handleChange}
                placeholder="Hint"
              />
              </div>
            );
            })}</div>
    <Button color="info" onClick={this.addClue}>
      Add Clue
    </Button>
    </div>
  );
}}
