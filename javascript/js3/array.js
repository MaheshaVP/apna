let names = ["mahesh","manoj"];
console.log(names);

let names1 = ["shekara","kana"];
console.log(names1);

names.concat(names1);

let game = [['X',null ,'O'],[null ,'X',null ],['O',null ,'X']];
console.log(game);

//qs1
let arr = [7,9,0,-2];
let n = 4;
// let ans = arr.slice(0,n);
// console.log(ans);


//qs2
let ans = arr.slice(arr.length-n);
console.log(ans);

//qs3
// let str = prompt("please enter a string");
// if(str.length==0) {
//     console.log("string is empty");
// }else{
//     console.log("string is not empty");
// }

//qs4
let str1 = "ApNaCoLlEgE";
let idx = 3;
if(str1[idx] == str1[idx].toLowerCase()) {
    console.log("character is lowercase");
}else{
    console.log("character is  not lowercase");
}

//qs5
let str2 = prompt("please enter a string");
console.log('original string = '+str2);
console.log('string without spaces = '+str2.trim());

//qs6
let arr1 = ["hello",'a',23,64,99,-6];
let item = 64;
if(arr1.indexOf(item) !=-1) {
    console.log("element exists in array");
}else{
    console.log("element doesn't exists in array");
}

let arr2 = [1,2,3,4,6];
arr2[-1];
console.log(arr2);