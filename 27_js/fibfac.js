// Team David and Nakib (DAN) | David Chen, Nakib Abedin
// SoftDev pd08
// K27 -- Basic functions in JavaScript
// 2023-04-04w
// Time Spent: 0.5 hr

// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(n) {
    if (n < 2) {
        return 1
    }
    return fact(n - 1) * n
}

console.log(fact(2))

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
function fib(n) {
    if (n == 0) return 0;
    if (n <= 2) return 1
    return fib(n - 1) + fib(n - 2)
}

console.log(fib(4))
