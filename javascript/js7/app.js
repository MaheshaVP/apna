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
console.log("Hi there!");

setTimeout(() => {
    console.log("apna college");
}, 2000);

console.log("welcome to");


//set interval
console.log("Hi there!");

let id = setInterval(() => {
    console.log("apna college");
}, 2000);

console.log(id);

//