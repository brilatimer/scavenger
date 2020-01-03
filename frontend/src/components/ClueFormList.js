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

const ClueFormList = (props) => {
  const clueElements = props.activeItemClues.map((clue, i) => {

    return (

      <div>
      <Label for="name">Question {i + 1}</Label>
      <Input
      
      type="text"
      name="question"
      defaultValue={clue.question}
      // onChange={this.handleChange}
      placeholder="Question"
/>
      <Label for="name">Answer</Label>
      <Input
      type="text"
      name="answer"
      defaultValue={clue.answer}
      // onChange={this.handleChange}
      placeholder="Answer"
/>
      <Label for="name">Hint</Label>
      <Input
      type="text"
      name="hint"
      defaultValue={clue.hint}
      // onChange={this.handleChange}
      placeholder="Hint"
    />
    </div>
    
);
  });

  return (
    <div className="clueElements">
      <div>{clueElements}</div>
    </div>
  );
}


export default ClueFormList;