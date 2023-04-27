/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
        have questions about,
            or otherwise deem notable.
        	
            Write with your future self or teammates in mind.
        	
            If you find yourself falling out of flow mode, consult 
            other teams
            MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team DAN :: David Chen, Nakib Abedin 
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-20
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function (x) { //function is being assigned to a variable; never seent his before
    var j = 30;
    return j + x;
};


//instantiate an object
var o = {
    'name': 'Thluffy',
    age: 1024,
    items: [10, 20, 30, 40],
    morestuff: { a: 1, b: 'ayo' },
    func: function (x) {
        return x + 30;
    }
};


var addItem = function (text) {
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};


var removeItem = function (n) {
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};


var red = function () {
    var items = document.getElementsByTagName("li");
    for (var i = 0; i < items.length; i++) {
        items[i].classList.add('red');
    }
};


var stripe = function () {
    var items = document.getElementsByTagName("li");
    for (var i = 0; i < items.length; i++) {
        if (i % 2 == 0) {
            items[i].classList.add('red');
        } else {
            items[i].classList.add('blue');
        }
    }
};

const insertAnswer = (type, arg, answer) => {
    let answerDiv = document.getElementById(`${type}-val`); // ` is a template literal, allows for string interpolation
    answerDiv.innerHTML = `<code>${type}(${arg}) = ${answer}</code>`
};

//insert your implementations here for...
// FIB
var fibonacci = function fib(n) {
    // the answers before 4 are the same as the index
    if (n < 4) {
        return n;
    }
    let a = 1;
    let b = 1;
    let c = 2;
    // start at 4 because we already have the first 3 answers
    // loop until we reach the index
    for (let i = 4; i <= n; i++) {
        a = b;
        b = c;
        c = a + b;
    }

    insertAnswer('fib', n, c);
    return c;
}


// var fibonacci = function fib(n) {
//     if (n == 0) return 0;
//     if (n <= 2) return 1;
//     return fib(n - 1) + fib(n - 2);
// }
// FAC
var factorial = function fac(n) {
    let answer = 1;
    for (let i = 1; i <= n; i++) {
        answer *= i;
    }
    insertAnswer('fac', n, answer);
    return answer;
}


// GCD
var gcd = function gcd(a, b) {
    let answer = 1;
    for (let i = 1; i <= Math.min(a, b); i++) {
        if (a % i == 0 && b % i == 0) {
            answer = i;
        }
    }
    insertAnswer('gcd', `${a}, ${b}`, answer);
    return answer;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.

const myFxn = (param1, param2) => {
    if (Math.max(param1, param2) % Math.min(param1, param2) == 0)
        return Math.min(param1, param2);
    else
        return gcd(Math.min(param1, param2), Math.max(param1, param2) % Math.min(param1, param2));
};




