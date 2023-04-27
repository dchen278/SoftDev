/*
kibby guoblers: nakib, Jacob Guo
SoftDev pd8
K32 -- animation in canvas JS
2023-04-27t
Time Spent: 0.5 hrs
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var  stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("buttonMovie");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID;

var clear = () => {
    // e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 100;
var growing = true;

var drawDot = () =>{
    clear();
    if(radius === c.height / 2) {growing = false}
    if(radius === 0) {growing = true}
        if (growing){
            radius++;
        }
        else{
            radius--;
        }
        console.log(radius);
        ctx.beginPath();
        ctx.arc(c.width / 2, c.height / 2, radius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.fill();
        window.cancelAnimationFrame(requestID);
        requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
    console.log("stopit invoked...");
    window.cancelAnimationFrame(requestID);
    console.log("requestID cancelled");

};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * 540);
    var rectY = Math.floor(Math.random() * 560);

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height );
        ctx.drawImage( logo, rectX, rectY, rectWidth, rectHeight);
        if (rectY <= 0 || rectY >= c.height - rectHeight ){
            yVel = -yVel;
        }
        if (rectX <= 0 || rectX >= c.width - rectWidth ){
            xVel = -xVel;
        }
        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};



dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);