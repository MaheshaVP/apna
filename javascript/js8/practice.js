//qs 1 square and sum the array elements using the arrow function and then find the average of the array
let nums = [1,2,3,4,5];

const square = nums.map((a) => a * a);
console.log(square);

let sum = square.reduce((ace,cur) => ace + cur, 0);

let avg = sum / nums.length;
console.log(avg);


//qs 2
let numbers = [2,4,6,8,-2,-4];

console.log(numbers.map((b) => b + 5));


//qs 3
let strings = ["adam","bob","catlyn","donald","eve"];
console.log(strings.map((c) => c.toUpperCase()));


//qs 4
const doubleAndReturnArgs = (arr, ...args) => [
    ...arr,
    ...args.map((d) => d*2),
];

doubleAndReturnArgs ([1,2,3],4,4); 
doubleAndReturnArgs ([2],10,4);
console.log(doubleAndReturnArgs);


//qs 5
const mergeObjects = (obj1,obj2) => ({...obj1 , ...obj2});

console.log(mergeObjects({a:1,b:2},{c:3,d:4}));