//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (bToggler.innerHTML == "rect|circ" || mode == "circ") {
        bToggler.innerHTML = "Rectangle";
        mode = "rect"}
    else {
        bToggler.innerHTML = "Circle";
        mode = "circ";
    }
}

var drawRect = function(x,y) {
    console.log("rect is reached")
    ctx.fillRect(x, y, 100, 300)
}

var drawCircle = function(x,y) {
    ctx.beginPath();
    ctx.strokeStyle = 'black';
    ctx.arc(x,y, 100, 0, 2* Math.PI);
    ctx.stroke();
    ctx.fill();
    
}

var draw = (e) => {
    var mouseX = e.offsetX //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillStyle = "red";

    if (mode == "rect") {
        drawRect(mouseX, mouseY)
    }
    else {
        drawCircle(mouseX, mouseY)
    }
}

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
var bToggler = document.getElementById("buttonToggle")
var clearB = document.getElementById("buttonClear")

bToggler.addEventListener("click", toggleMode)
clearB.addEventListener("click", () => {ctx.clearRect(0,0, c.width, c.height)})