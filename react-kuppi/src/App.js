import React, { Component, Fragment } from "react";
import List from "./List";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    // this.increment = this.increment.bind(this);
  }

  increment = event => {
    this.setState({ count: Math.floor(Math.random() * 100) });
  };

  conditionalFun = value => {
    if (value === 0) {
      return <p>Zero</p>;
    } else {
      return <p>Other</p>;
    }
  };

  render() {
    return (
      <>
        <h4>{this.state.count}</h4>
        <button onClick={event => this.increment(event)} on>
          Increment
        </button>
        {/* <button hidden={true}>Decrement</button>
        <p hidden={true}>Zero</p>
        <p hidden={false}>Other</p> */}
        {this.conditionalFun(0)}
        {/* <List /> */}
      </>
    );
  }
}

export default App;
