// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
// callable f(x), uses local value of j
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
// can do o.func(x) to call the anonymous function held by func
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


// doesn't modify already colored list elements
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
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

function gcd(a,b) {
  if (a==0) {
    return b
  }
  if (b==0) {
    return a
  }
  x = Math.max(a,b)
  y = Math.min(a,b)
  return gcd(y, x%y)
    
}

console.log("fact 4: "+fact(4))
console.log("fib 4: "+fib(4))
console.log("gcd(2,3): "+gcd(2,3))

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return param1+param2;
};


