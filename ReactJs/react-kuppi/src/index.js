import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import List from "./List";
import Fragments from "./Fragments";
import Counter from "./Counter";
import ObjectState from "./ObjectState";
import StateHandle from "./StateHandle";
import reportWebVitals from "./reportWebVitals";

ReactDOM.render(
  <React.StrictMode>
    <StateHandle />
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
