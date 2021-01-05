/**
 * Asynchronous Js
 */

// 1

function capitalize(word) {
    return word.toUpperCase();
}

let capitalized = capitalize('myself');

console.log(capitalized);

console.log('done')

// 2

function capitalize(word, done) {
    done(word.toUpperCase());
}

capitalize('myself', (capitalized) => {
    console.log(capitalized);
})

console.log('done');

// 3 

function Alpha(word, done) {
    done(word.toUpperCase());
}

function Bravo(word) {
    console.log(word)
}

Alpha('myself', Bravo)

console.log('done');

// 4

// Traditional Function
let func = function (a) {
    return a + 100;
}

// Arrow Function Break Down

// i. Remove the word "function" and place arrow between the argument and opening body bracket
func = (a) => {
    return a + 100;
}

// ii. Remove the body brackets and word "return" -- the return is implied.
func = (a) => a + 100;

// iii. Remove the argument parentheses
func = a => a + 100;

// 5

function capitalize(word, done) {
    process.nextTick(() => {
        done(word.toUpperCase());
    })
}

capitalize('myself', (capitalized) => {
    console.log(capitalized);
});

console.log('done');

// 6

const bar = () => console.log("bar")

const baz = () => console.log("baz")

const foo = () => {
    console.log("foo")
    bar()
    baz()
}

foo()

// 7

const bar = () => console.log('bar')

const baz = () => console.log('baz')

const foo = () => {
    console.log('foo')
    setTimeout(bar, 0)
    baz()
}

foo()

// 8

function delay(seconds, callback) {
    setTimeout(callback, seconds * 1000);
}

delay(2, () => {
    console.log('waited 2 seconds');
})

delay(3, () => {
    console.log('waited another 3 seconds');
})

delay(4, () => {
    console.log('waited another 4 seconds');
})

// 9

function delay(seconds, callback) {
    setTimeout(callback, seconds * 1000);
}

delay(2, () => {
    console.log('waited 2 Seconds');
    delay(3, () => {
        console.log('waited another 3 Seconds');
        delay(4, () => {
            console.log('waited another 4 Seconds');
        })
    })
})

// 10

let delay = (seconds) => new Promise((resolve) => {
    setTimeout(() => {
        resolve(seconds)
    }, seconds * 1000);
})

delay(5)
    .then((time) => console.log(`waited ${time} seconds`))

// 11

let delay = (seconds) => new Promise((resolve) => {
    setTimeout(() => {
        resolve(seconds)
    }, seconds * 1000);
})

delay(2)
    .then(time => {
        console.log(`waited ${time} seconds`)
        return time;
    })
    .then(time => time * 6)
    .then(timeX6 => console.log(`time into 6 is ${timeX6}`))

// 12

let delay = (seconds) => new Promise((resolve, reject) => {

    throw new Error('I\'m going sidewayd :( ')

    setTimeout(() => {
        resolve(seconds)
    }, seconds * 1000);
})

delay(2)
    .then(time => {
        console.log(`waited ${time} seconds`);
    })
    .catch(error => console.log(`Promise says \'${error.message}\'`))


// 13

let delay = (seconds) => new Promise((resolve, reject) => {

    if (seconds < 3) {
        reject(new Error(`${seconds} is too short`))
    }

    setTimeout(() => {
        resolve(seconds)
    }, seconds * 1000);
})

delay(2)
    .then(time => {
        console.log(`waited ${time} seconds`);
    })
    .catch(error => console.log(`Promise says \'${error.message}\'`))

// 14

var delay = (seconds, callback) => {
    if (seconds > 4) {
        callback(new Error(`${seconds} is way too long!`));
    } else {
        setTimeout(() => {
            callback(null, `The ${seconds} delay is over`);
        }, seconds * 1000);
    }
}
/**
 * It is a rule in a callback function to pass the error if exists as the first argument 
 * and to pass everything else as a second argument
 * 
 * Therefore to make this process much easier, promisify is introduced so that you can call 
 * functions that pass usual callbacks as promises 
 */

/** 
 * wihtout promisify 
 * 
 */
delay(4, (error, message) => {
    if (error) {
        console.log(`Error ${error}`);
    } else {
        console.log(message);
    }
})

/**
 * With promisify
 */
var { promisify } = require('util');
var promisedDelay = promisify(delay)

promisedDelay(3)
    .then(console.log)
    .catch(error => console.log(`Caught error : ${error}`));


// 15

function delay(seconds) {
    return new Promise((resolve) => {
        setTimeout(() => { resolve(seconds) }, seconds * 1000);
    })
}

delay(2)
    .then(() => console.log('waited 2 seconds'))
    .then(() => delay(3))
    .then(() => console.log('waited another 3 seconds'))
    .then(() => delay(4))
    .then(() => console.log('waited another 4 seconds'))

// 16

function delay(seconds) {
    return new Promise((resolve) => {
        setTimeout(() => { resolve(seconds) }, seconds * 1000);
    })
}

Promise.all([
    delay(2),
    delay(3),
    delay(4)
])
    .then(() => console.log('done'))
    .catch((error) => console.error(error))

// 17 

function delay(seconds) {
    return new Promise((resolve) => {
        setTimeout(() => { resolve(seconds) }, seconds * 1000);
    })
}

Promise.race([
    delay(2),
    delay(3),
    delay(4)
])
    .then(() => console.log('done'))
    .catch((error) => console.error(error))

// 18

function delay(seconds) {
    return new Promise((resolve) => {
        setTimeout(() => { resolve(seconds) }, seconds * 1000);
    })
}

(async () => {
    await delay(2);
    console.log('waited 2 seconds');
    await delay(3);
    console.log('waited another 3 seconds');
    try {
        await delay(4);
        console.log('waited another 4 seconds');
    } catch (error) {
        console.error(error);
    }
})();


