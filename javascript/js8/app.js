//Array Methods

//forEach
let arr = [1,2,3,4,5];

arr.forEach((el) => {
    // console.log(el);
});

// arr.forEach(function(el) {
//     console.log(el);
// });

// let print = function(el) {
//     console.log(el);
// };

// arr.forEach(print);

let arr1 = [{
    name:"kalyan",
    marks:86
},{
    name:"jeethu",
    marks:66
},{
    name:"mahesh",
    marks:56
}];

// arr1.forEach((student) => {
//     console.log(student);
// })

//Map
let num = [1,2,3,4];

let double = num.map((el) => {
    return el**2;
});
// console.log(double);


let student1 = [{
    name:"kalyan",
    marks:86
},{
    name:"jeethu",
    marks:66
},{
    name:"mahesh",
    marks:56
}];

let gpa = student1.map((value) => {
    return value.marks / 10;
});

//Filter
let nums = [1,2,3,4,5,6,7,8,9,10,11,12];

let ans = nums.filter((el) => {
    return el%2 == 0;
});

//Every
let arr2 = [2,4,6];
let find = arr2.every((el)=>el%2 == 0);

//Reduce
let num1 = [1,2,3,4];
let finalVal = num1.reduce((res,el) => {
// console.log(res);
return res+el 
});
// console.log(finalVal);

//Reduce find the maximum of an array
let arr3 = [1,2,3,4,5,6,7,8];

// let max = -1;

// for(let i=0;i<arr3.length;i++) {
//     if(max<arr3[i]){
//         max=arr3[i];
//     }
// }

// console.log(max);

let max = arr3.reduce((max,el) => {
    if(max<el){
        return el;
    }else{
        return max;
    }
});
// console.log(max);

//practice qs multiplication of 10
let nums2 = [10,20,30,40];


let ans1 = nums.every((el) => el % 10 == 0);
console.log(ans1);


function getMin(nums2) {
let min = nums2.reduce((min,el) => {
    if(min<el) {
        return min;
    }else{
        return el;
    }
});

console.log(min);
}
