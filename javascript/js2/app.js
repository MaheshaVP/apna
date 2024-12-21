let color = "grey";
//traffic colors
if(color === "red") {
    console.log("stop light color is red");
}else if(color === "yellow") {
    console.log("slow down light color is yellow");
}else if(color==="green") {
    console.log("go light color is green");
}else{
    console.log("traffic light is broken");
}

let age=35 ;
if(age>18) {
    console.log("you can vote");
}else{
    console.log("you can not vote");
}

let size = "M";
if(size=="XL"){
    console.log("price is Rs.250");
}else if(size=="L"){
    console.log("price is Rs.200");
}else if(size=="M"){
    console.log("price is Rs.100");
}else if(size=="S"){
    console.log("price is Rs.50");
}

let marks = 85;
if(marks >=35){
    console.log("pass");
    if(marks >= 80){
        console.log("Grade : 0");
    }else{
        console.log("Grade : A");
    }
}else{
    console.log("better luck next time");
}

let result=45;
if((result>=30 && result<=80) || !false){
    console.log("pass");
}


let str = "apple";
if(str[0]==='a' && str.length>=3) {
    console.log("good string");
}else {
    console.log("try another word");
}

let num=12;
if((num%3 ===0)&&((num+1==15)||(num-1==11))){
    console.log("safe");
}else{
    console.log("unsafe");
}

if(undefined) {
    console.log("it has true value");
}else {
    console.log("it has false value");   
}

let num1=0;
if(num1){
    console.log("num is 0");
}else{
    console.log("num is not 0");
}

let day=10;
switch(day){
    case 1:
        console.log("Monday");
        break;
        case 2:
        console.log("Tuesday");
        break;
        case 3:
        console.log("Wednesday");
        break;
        case 4:
        console.log("Thursday");
        break;
        case 5:
        console.log("Friday");
        break;
        case 6:
        console.log("Saturday");
        break;
        case 7:
        console.log("Sunday");
        break;
        default:
            console.log("wrong entry");
}

//alert
console.error("error");
console.warn("warning");

//prompt
let name= prompt("enter your name:");
let msg=("welcome"+name+"!");
console.log(name);