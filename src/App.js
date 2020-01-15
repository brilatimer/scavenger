import React, { Component } from "react";
import './App.css';
import Modal from "./components/Modal";
import LaunchModal from "./components/LaunchModal";
import axios from "axios";
import {auth} from "./actions";

var BASE_URL = '/';
if (window.location.href.indexOf("3000") > -1) {
  BASE_URL = "http://localhost:8000/"
}

class App extends Component {
  constructor(props) {
    super(props);

      
 
    this.state = {
      activeItem: {
        players_phone_number: "",
        game_title: "",
        clues: [],
      },
      scavengerList: []
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get(BASE_URL + "api/scavenger/")
      .then(res => this.setState({ scavengerList: res.data }))
      .catch(err => console.log(err));
  };
  renderTabList = () => {
    return (
      <div className="my-5 tab-list"> 
      </div>
    );
  };
  renderItems = () => {
    return this.state.scavengerList.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`scavenger-title mr-2`}
          title={item.players_phone_number}
        >
          {item.game_title}
        </span>
        <span>

        <button
            onClick={() => this.launchItem(item)}
            className="btn btn-success mr-2"
          >
            {" "}
            Launch{" "}
          </button>

          <button
            onClick={() => this.editItem(item)}
            className="btn btn-info mr-2"
          >
            {" "}
            Edit{" "}
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete{" "}
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(BASE_URL + `api/scavenger/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post(BASE_URL + "api/scavenger/", item)
      .then(res => this.refreshList());
  };

  handleDelete = item => {
    axios
      .delete(BASE_URL + `api/scavenger/${item.id}`)
      .then(res => this.refreshList());
  };
  createItem = () => {
    const item = { players_phone_number: "", game_title: "", clues: [] };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  launchToggle = () => {
    this.setState({ launchModal: !this.state.launchModal });
  };

  launchItem = item => {
    this.setState({ activeItem: item, launchModal: !this.state.launchModal });
  };

  handleLaunchStart = item => {
    this.launchToggle();
    if (item.id) {
      axios
        .put(BASE_URL + `api/scavenger/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    // axios
    //   .post("api/scavenger/", item)
    //   .then(res => this.refreshList());
  };

  render() {
    return (
      <main className="content">
        <h1 className="text-black text-uppercase text-center my-4">
          quest
          <img src="https://cdn.clipart.email/fec5d675df1c0a4bc31fac155efad05a_cute-duck-clipart-6-clipart-station_610-612.jpeg" alt="secretary bird" width="50" height="50"></img>
        </h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3"> 
            <a className="logout-link" href={BASE_URL + "accounts/logout"}>logout</a>
              <div className="">
                <button onClick={this.createItem} className="btn btn-primary">
                  New Scavenger Hunt
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}

{this.state.launchModal ? (
          <LaunchModal
            activeItem={this.state.activeItem}
            toggle={this.launchToggle}
            onSave={this.handleLaunchStart}
          />
        ) : null}

      </main>
    );
  }
}

export default App;