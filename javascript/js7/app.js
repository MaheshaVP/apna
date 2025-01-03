//This Keyword
const student = {
    name : "Mahesh",
    age : 25,
    eng : 23,
    math : 93,
    phy : 97,
    getAvg() {
        console.log(this);
        let avg = (this.eng + this.math + this.phy) / 3;
        console.log(`${this.name} got avg marks ${avg}`);
    }
}


function getAvg() {
    console.log(this);
}


//try and catch
try{
    console.log(a);
}catch{
    // console.log("variable a doesn't defined");
}

//misselaneous functions
//Arrow Functions
const sum = (a,b) => {
    console.log(a+b);
}

const cube = (n) => {
    return n*n*n;
}

const pow = (a,b) => {
    return a ** b;
}


const hello = () => {
    console.log("Hello world");
}

//arrow function
const mul = (a,b) => {
  return  a*b;
};

//set timeout
// console.log("Hi there!");

setTimeout(() => {
    // console.log("apna college");
}, 2000);

// console.log("welcome to");


//set interval
// console.log("Hi there!");

let id = setInterval(() => {
    // console.log("apna college");
}, 2000);

console.log(id);

//this with arrow function
const student1 = {
    name : "mahesh",
    marks : 95,
    prop : this,  //global scope
    getName : function () {
        console.log(this);
        return this.name;
    },
    getMarks : () => {
        console.log(this);
        return this.marks;  //parents scope
    },
    getInfo1: function () {
        setTimeout(() => {
            console.log(this);
        },2000);
    },
    getInfo2: function () {
        setTimeout( function () {
            console.log(this);
        },2000);
    },
};


//practice qs
//find square root 
const square = (n) => { 
   return n*n;
}
// console.log(square(4));

//print hello world 5 times
let id1 = setInterval(() => {
    console.log("Hello world");
},2000);

setTimeout(() => {
    clearInterval(id1);
    console.log("clear interval ran");
},10000);


