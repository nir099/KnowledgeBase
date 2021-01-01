import React, { Component } from 'react';

class Statehandle extends Component {
    constructor(props){
        super(props);
        this.state = {
            person: {
                name: "Yashod",
                age: 24,
                email: "yashod@abc.com"
            },
            company: "ABC"
        }
        this.increaseAge = this.increaseAge.bind(this);
    }

    increaseAge(){
        this.setState((prevProps) => ({
            person : {
                ...prevProps.person,
                age: prevProps.person.age + 1
            }
        }));
        // this.setState((prevProps) => ({
        //     person.age : prevProps.person.age + 1
        // }));
        // this.setState((prevProps) => ({
        //     person : {
        //         age: prevProps.person.age + 1
        //     }
        // }));
    }

    render() { 
        return ( 
        <> 
            <h2>My name is {this.state.person.name} and I am {this.state.person.age} old.</h2>
            <h2>My email is {this.state.person.email}</h2>
            <h2>Company is {this.state.company}</h2>
            <button onClick={this.increaseAge}> Increase age</button>
        </>
        );
    }
}
 
export default Statehandle;