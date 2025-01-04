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

//default parameters
function sum(a,b=2) {
    return a+b;
}
// console.log(sum(5,6));

//spread arrray
let arr4 = [1,2,3,4,5];
let newArr = [...arr4];


let chars = [..."hello"];

let odd = [1,3,5,7,9];
let even = [2,4,6,8];

let nums1 = [...odd, ...even];

//spread with object literals
const data = {
    email : "ironman@gmail.com",
    password : "abcd",
};

const datacopy = {...data, id:123};

let arr5 = [1,2,3,4,5];
let obj1 = {..."hello"};



function sum(...arg) {
    for (let i=0;i<arg.length;i++) {
        console.log("you gave us : ",arg);
    }
}

function min(msg,...args) {
    console.log(msg);
    return args.reduce((min,el) => {
        if(min>el) {
            return el;
        }else{
            return min;
        }
    })
}

function sum1 (...args) {
    return args.reduce((sum,el) => sum+el);
}

//  Destructing
let names = ["tony","bruce","peter","steve","abc","xyz"];
// let winner = names[0];
// let runnerup = names[1];
let [winner,runner,secondRunner,...others] = names;
console.log(names);

const student2 = {
    name : "karan",
    age : 28,
    class : 9,
    subjects : ["hindi","english","maths","science"],
    username : "@karan",
    password : "abcd"
};

let {username:user,password:pass} = student2;


