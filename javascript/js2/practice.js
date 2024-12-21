//qs1
let num=20;
if(num%10 == 0){
    console.log("good");
}else{
    console.log("bad");
}

//qs2
// let name=prompt("please enter your name");
// let age=prompt("please enter your age");
// alert(name + " is " + age +" years old");

//qs3
let quarter = 1;
switch(quarter){
    case 1: console.log("jan,feb,mar");
    break;
    case 1: console.log("apr,may,jun");
    break;
    case 1: console.log("jul,aug,sept");
    break;
    case 1: console.log("oct,nov,dec");
    break;
    default: console.log("not a quarter");
}

//qs4
let str="apple";
if((str[0]=='a')||(str[0]=='A')&&(str.length>5)){
    console.log("golden string");
}else{
    console.log("not a golden string");
}

//qs5
let a = 5;
let b = 18;
let c = 13;
if(a>b) {
    if(a>c){
        console.log(a, "is largest");
    }else{
        console.log(c, "is largest");
    }
}else{
    if(b>c) {
        console.log(b, "is largest");
    }else{
        console.log(c, "is largest");
    }
}

//qs6
let num1 = 32;
let num2 = 47852;
if((num1%10) == (num2%10)) {
    console.log("last numbers have same digits",num1%10);
}else{
    console.log("last numbers are different digits");
}
