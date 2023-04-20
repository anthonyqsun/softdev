// Team BA :: Bachelor of Arts in SoftDev
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-20R
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("effect pp-mode");

var functionButton = document.getElementById("function");
functionButton.addEventListener('click', change);

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };  // document.getElementById("li1")  // document.getElementById("li1")
        // document.getElementById("li2")
        // document.getElementById("li3")
        // document.getElementById("li4")
        // document.getElementById("li5")
        // document.getElementById("li6")
        // document.getElementById("li7")
        // document.getElementById("li7")


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


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
// FIB
function fib(n) {
    if (n < 2) {
        return n;
    }
    else {
       return fib(n-1) + fib(n-2); 
    }
}


// FAC
function fact(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return n * fact(n-1);
    }
}

// GCD
function gcd(n,m) {
    if (!m) {
        return n;
        }
        
        return gcd(m, n % m);    

}

function doMathFx(n, fun, id) {
  if (document.getElementById(id).innerHTML == "") {
    document.getElementById(id).innerHTML=fun(n);
  }
  else {
    document.getElementById(id).innerHTML="";
  }
}

function doGCD(n, m, id) {
  if (document.getElementById(id).innerHTML == "") {
    document.getElementById(id).innerHTML=gcd(n, m);
  }
  else {
    document.getElementById(id).innerHTML="";
  }
}


//EVERYTHING FUNCTION TO CHANGE HTML
function change() {
  document.getElementById("li0").innerHTML="fact of 5: " + fact(5);
  document.getElementById("li1").innerHTML="gcd of 5 and 20: "+ gcd(5,20);
  document.getElementById("li2").innerHTML="fib of 9: " + fib(9);
  document.getElementById("li3").innerHTML="fact of 9: " + fact(9);
  document.getElementById("li4").innerHTML="gcd of 90 and 70: " + gcd(90,70);
  document.getElementById("li5").innerHTML="fib of 20: " + fib(20);
  document.getElementById("li6").innerHTML="fact of 23: " + fact(23);
  document.getElementById("li7").innerHTML="gcd of 79 and 53: " + gcd(79,53);
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};
