/**
 * Hoisting 
 */

// 1

printVariable(fish)

function printVariable(name) {
    console.log(name)
}

var fish = "stingRay"

// 2

function printVariable(name) {
    console.log(name)
}

var fish = undefined

printVariable(fish)

fish = "stringRay"

// 3

printVariable(fish)

function printVariable(name) {
    console.log(name)
}

let fish = "stingRay"

// 4 

printVariable(fish)

function printVariable(name) {
    console.log(name)
}

const fish = "stingRay"

// 5

multiplyAndPrint(5, 8); // Prints 40

function multiplyAndPrint(a, b) {
    console.log(a * b);
}

// 6

multiplyAndPrint(6, 7); // Throws 'TypeError: multiplyAndPrint is not a function'
addAndPrint(5, 8); // Throws 'ReferenceError: Cannot access 'addAndPrint' before initialization'

var multiplyAndPrint = function (a, b) {
    console.log(a * b);
}

let addAndPrint = (a, b) => {
    console.log(a + b);
}

// 7

let student_1 = new Student("Janith", 19); // ReferenceError: Cannot access 'Student' before initialization

class Student {
    constructor(name, id) {
        this.name = name;
        this.id = id;
    }
}

// 8

let student_1 = new Student("Janith", 19); // ReferenceError: Cannot access 'Student' before initialization
let teacher_1 = new Teacher("Ravindu", 95); // TypeError: Teacher is not a constructor

let Student = class {
    constructor(name, id) {
        this.name = name;
        this.id = id;
    }
}

var Teacher = class {
    constructor(name, id) {
        this.name = name;
        this.id = id;
    }
}




