/*
DAN: David Chen and Nakib Abedin
SoftDev pd8
k30 -- JS Paint
2023-04-24
Time Spent: 1.0 hr
*/

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingCOntext2D object
var ctx = c.getContext("2d");

// needed or else the shapes will be white and will blend in with the background
ctx.strokeStyle = "red";
ctx.fillStyle = "red";

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if(mode === "rect"){
        mode = "circle";
    }else{
        mode = "rect";
    }
};

var drawRect = function(e){
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("rect mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 75, 100);
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("circle mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 75, 0, 2 * Math.PI, true);
    ctx.stroke();
    ctx.fill();
}

//var draw = function(e){
var draw = (e) => {
    if(mode === "rect") drawRect(e);
    else drawCircle(e);
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    // console.log("not cleared");
    ctx.clearRect(0,0,c.width,c.height);
    // console.log("cleared");
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);


