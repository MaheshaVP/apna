function hello() {
    console.log("hello");
}
// hello();

function printName () {
    console.log("apna college");
    console.log("mahesh");
}
// printName();

//loops
function print1to5 () {
    for(let i=1;i<=10;i++){
        console.log(i);
    }
}
// print1to5();

function isAdult() {
    let age = 16;
    if(age>=18) {
        console.log("adult");
    }else{
        console.log("not adult");
    }
}
// isAdult();

//practice qs1 print poem
function printPoem () {
    console.log("Twinkle Twinkle ,little star");
    console.log("How i wonder what you are");
} 
// printPoem();


//practice qs2 dice roll
// function dice () {
//     let roll =(Math.floor(Math.random() * 6)+1);
//     console.log(roll);
// }
// dice();


function rollDice () {
    let rand = (Math.floor(Math.random() * 6) + 1);
    console.log(rand);
}
// rollDice();

//functions with arguments
function printName1 (name,age) {
    console.log(`${name}'s age is ${age}.`);
}
printName1("Mahesh",21);

function sum (a,b) {
    console.log(a+b);
}
sum(2,3);
