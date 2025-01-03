//qs1
let arrayAverage = (arr) => {
    let total = 0;
    for (let number of arr) {
        total += number;
    }
    return total / arr.length;
};

let arr = [1,2,3,4,5,6,7,8];
// console.log(arrayAverage(arr));

//qs2
let num = 5;
const isEven = (num) => num % 2 == 0;


//qs3
const object = {
    message : ('Hello, world'),

    logMessage() {
        console.log(this.message);
    }
};

setTimeout(object.logMessage , 1000);

//qs4
let length = 4;
function callback() {
    console.log(this.length);
}
const object1 = {
    length : 5,
    method(callback) {
        callback();
    },
};

object1.method(callback, 1,2);

