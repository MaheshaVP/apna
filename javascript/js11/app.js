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


setTimeout(() =>  {
    console.log("apna college");
},2000);

console.log("hello...");

