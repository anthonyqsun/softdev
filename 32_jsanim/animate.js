var c = document.getElementById("playground");
var ctx = c.getContext("2d");

ctx.strokeStyle = "black";
ctx.fillStyle = "blue";

var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var radius = 0;
var growing = true;
var requestID;

var drawDot = () => {

    window.cancelAnimationFrame(requestID)
    console.log("Cancelled")

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
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame( requestID );

    var rectWidth = 125
    var rectHeight = 100

    var rectX = Math.floor(Math.random() * c.width) - rectWidth;
    if (rectX < rectWidth) {
        rectX += rectWidth;
    };

    var rectY = Math.floor(Math.random() * c.height) - rectHeight;
    if (rectY < rectHeight) {
        rectY += rectHeight;
    };

    var speed = 5;

    var xVel = (Math.random()-0.5) * 2 * speed;
    while (xVel == 0) {
        xVel = (Math.random()-0.5) * 2 * speed;
    };

    var yVel = Math.pow(-1,Math.floor(Math.random()*2)) * Math.sqrt(Math.pow(speed,2)-Math.pow(xVel,2));
    while (yVel == 0) {
        yVel = (Math.random()-0.5) * 2 * speed;
    };

    console.log(xVel)
    console.log(yVel)


    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        //ctx.fill Rect(rectX, rectY, rectWidth, rectHeight);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

        if ((rectX < 0) || (rectX + rectWidth >= c.width)) {
            xVel *= -1;
        };

        if ((rectY < 0) || (rectY + rectHeight >= c.height)) {
            yVel *= -1;
        };
        
        rectX += xVel;
        rectY += yVel;

        requestID = window.requestAnimationFrame(dvdLogo)
    }
    dvdLogo();
}

var stopIt = () => {
    console.log(requestID)
    window.cancelAnimationFrame(requestID)
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup)
stopButton.addEventListener("click", stopIt);