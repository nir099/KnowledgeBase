import React, { Component } from "react";

class List extends Component {
  students = [
    { id: 1, name: "Amal", age: 25 },
    { id: 2, name: "Mark", age: 32 },
    { id: 3, name: "Sithum", age: 28 },
    { id: 4, name: "Tony", age: 30 }
  ];

  studentList = this.students.map(student => (
    <Student key={student.id} name={student.name} age={student.age} />
  ));

  render() {
    return <div>{this.studentList}</div>;
  }
}

const Student = props => {
  return (
    <div>
      <h3>
        {props.name} is {props.age} years old
      </h3>
    </div>
  );
};

export default List;
