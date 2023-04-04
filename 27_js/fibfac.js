// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(num) {
    if (num > 1) {
        return num * fact(num - 1)
    }
    return 1
}

function fib(num) {
    if (num < 2) {
        return num
    }
    return fib(num - 1) + fib(num - 2)
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
