/**
 * Variables and Scope 
 */

// 1

let mammal = "cat"

function printVar() {
    console.log(mammal);
}

printVar()

// 2

function printVar() {
    let mammal = "cat"
    console.log(mammal)
}

console.log(mammal)

// 3

let age = 40;

if (age > 21) {
    var gap = age - 21;
}

console.log(`You are ${gap} years over drinking age`);

// 4

let age = 40;

if (age > 21) {
    let gap = age - 21;
}

console.log(`You are ${gap} years over drinking age`);