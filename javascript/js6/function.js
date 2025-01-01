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
// printName1("Mahesh",21);


function sum (a,b) {
    console.log(a+b);
}
// sum(2,3);


//practice qs4 average of 3 numbers
function calcAvg (a,b,c) {
    let avg = (a+b+c)/3;
    console.log(avg);
} 
// calcAvg(4,6,8);

//print multiplication table of a number
function printTable (n) {
    for(let i=n; i<=n*10; i+=n) {
    console.log(i);
    }
}
// printTable(22);

//return value
function sum1(a,b) {
    console.log("Hello");
    return a+b;
}


// console.log(sum1(1,3));


function isAdult1(age) {
    if(age >= 18){
        return "adult";
    }else{
        return "not adult";
    }
    console.log("bye bye");

}
// console.log(isAdult1(21));

//practice qs3 return sum of numbers from 1 to n
function getsum(n) {
    let sum = 0;

    for(let i=1;i<=n;i++) {
        sum += i;
    }
    return sum;
}
// console.log(getsum(18));


//practice qs4 return concatenation of strings
let str = ["hi","hello","bye","!"];

function concat(str) {
    let result = " ";

    for(let i=0; i<str.length ;i++) {
        result += str[i];
    }

    return result;
}

// console.log(str);



//scope
let sum3 = 54; //global scope

function calSum(a,b) {
    let sum3 = a+b;    //function scope
    // console.log(sum3);
}
calSum(1,2);    
// console.log(sum3);

//block scope
for (let i=1;i<=5;i++){
    // console.log(i);
}


//just practice

// let age3 = 18;
// if(age3 >= 18) {
//     let char = 'A';
//     console.log(char);
// }else{
//     let char = 'C';
//     console.log(char);
// }


//lexical scope
function outerFunc () {
    let x = 5;
    let y = 6;
    function innerFunc () {
        let a =10;
        // console.log(x);
        // console.log(y);
    }
    innerFunc();
    console.log(a); 
}



//practice qs5 

let greet = "Hello"; //global scope

function changeGreet () {
    let greet = "Namaste";  //function scope
    // console.log(greet);
    function innerGreet () {
        // console.log(greet);  //lexical scope
    }
    innerGreet();
}
// console.log(greet);
changeGreet();



let name = "Mahesh";

let sum4 = function(a,b) {
    return a+b;
}
sum4(2,6);


let helllo = function() {
    console.log("hello Mahesh");

}

helllo = function() {
    console.log("namaste");
}

//High order function

function multipleGreet (func,count) {  //higher order function
    for (let i=1;i<=count;i++) {
        func();
    }
}

let greet1 = function () {
    console.log("hello");
}

// multipleGreet(greet1,5);

//Higher order functions
function oddOrEvenTest (request) {
    if(request == "odd") {
        let odd = function(n) {
            console.log(!(n%2==0));
        }
        return odd;
    }else if (request == "even") {
        let even = function(n) {
            console.log(n%2 == 0);
        }
        return even;
    }else{
        console.log("wrong req");
    }
}

let request = "even"; //odd
oddOrEvenTest("odd");

//Methods
const calculator = {
    num: 45,
    add: function (a,b) {
        return a+b
    },
    sub: function (a,b) {
        return a-b
    },
    mul: function (a,b) {
        return a*b
    }

};







