//qs1
let arr = [1,2,3,4,5,6,2,3];

let num =2;

for(let i=0;i<arr.length;i++){
    if(arr[i] == num){
        arr.splice(i,1);
    }
}

console.log(arr);

//qs2
let number = 345267;
let count = 0;

let copy = number;

while(copy>0) {
    count++;
    copy = Math.floor(copy/10);
}
console.log(count);

//qs3
let number1 = 287152;
let sum = 0;

let copy1 = number1;

while(copy1>0) {
    digit = copy1%10;
    sum += digit;
    copy1 = Math.floor(copy1/10);
}

console.log(sum);

//qs4
let n = 5;
let factorial = 1;

for(let i=1;i<=n;i++){
    factorial *= i;
}

console.log('factorial of ${n} is  ${factorial}');

//qs5
let arr1 = [2,5,4,2,7,1,8];
let largest = 0;

for(let i=0;i<=arr1.length;i++) {
    if(largest<arr1[i]) {
        largest = arr1[i];
    }
}
console.log(largest);