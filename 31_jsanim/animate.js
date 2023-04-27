var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.strokeStyle = "black"
ctx.fillStyle = "pink";

var requestID; // init global var for use with animation frames

var radius = 0;
var growing = true;

var drawDot = () => {

    if (requestID) {
        window.cancelAnimationFrame(requestID)
        console.log("Cancelled")
    }

    //wipe the canvas
    ctx.clearRect(0, 0, c.width, c.height);

    //repaint the circle
    console.log("drawing...")
    console.log("radius: " + radius)
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();

    if (growing) {
        radius++;
    }
    else {
        radius--;
    };

    if (radius == c.width/2) {
        growing = false;
        console.log("growing set to false")
    }
    if (radius == 0) {
        growing = true;
        console.log("growing set to true")
    };

    
    requestID = window.requestAnimationFrame(drawDot);

    /*

    ...and somewhere (when/where is the right time?)
    Update requestID to propagate the animation/
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
    */
};

var stopIt = () => {
    console.log("stopIt invoked...");
    /* YOUR CODE HERE
        ...to stop the animation
        You will need window.cancelAnimationFrame()
    */
    window.cancelAnimationFrame(requestID)
    console.log("cancelID: " + requestID)
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);