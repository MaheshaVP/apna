//stack
function hello() {
    console.log("inside hello function");
    console.log("hello");
}

function demo() {
    console.log("calling hello function");
    hello();
}

console.log("calling demo function");
demo();
console.log("done,bye!");

//function callback
function one() {
    return 2;
}

function two() {
    return one() + one();
}

function three() {
    let ans = two() + one();
    console.log(ans);
}
three();

//Single threaded language
let a = 25;
console.log(a);
let b = 10;
console.log(b);
console.log(a+b);


// setTimeout(() =>  {
//     console.log("apna college");
// },2000);

// console.log("hello...");

//callback hell

h1 = document.querySelector("h1");

function changeColor (color1,delay,nextColorChange) {
    setTimeout (() => {
        h1.style.color = color1;
        if(nextColorChange) nextColorChange();
    },delay);
}

changeColor("red",1000, ()=>{
    changeColor("orange",1000, () => {
        changeColor("yellow",1000, () => {

        });
    });
});

// changeColor("red",1000);
// changeColor("green",2000);
// changeColor("orange",3000);

function savetoDb(data) {
    let internetSpeed = Math.floor(Math.random() * 10 ) + 1;
    if(internetSpeed > 4) {
        console.log("your data was saved", data);
    }else{
        console.log("weak connection");
    }
}

savetoDb("Apna College");




