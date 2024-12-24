for(let i=1;i<=12;i++) {
    console.log(i);
}

console.log("odd numbers");

for(let i=1;i<=15;i=i+2){
    console.log(i);
}

console.log("backwards");

for(let i=15;i>=1;i=i-2){
    console.log(i);
}

console.log("even numbers");

for(let i=2;i<=10;i=i+2){
    console.log(i);
}

console.log("backwards");

for(let i=10;i>=2;i=i-2){
    console.log(i);
}

console.log("multiplication table of 5");

for(let i=6;i<=60;i=i+6){
    console.log(i);
}


//multiplication of 5
// let n = prompt("write your number");
// n = parseInt(n);

// for(let i=n;i<=n*10;i=i+n){
//     console.log(i);
// }

//nested loops
for (let i=1;i<=5;i++){
    console.log('outer loop ${i}');
    for(let j=1;j<=4;j++){
        console.log(j);
    }
}

//while loop
console.log("while loop");
let i=1;
while(i<=6){
    console.log(i);
    i++;
}

//favourate movie
// let favMovie = "Avator";
// let guess = prompt("enter your favourate movie");
// while((guess != favMovie)&&(guess!='quit')) {
//     console.log("correct");
//     guess = prompt("wrong guess. please try again");
// }

// if(guess == favMovie) {
//     console.log("congrats");
// }else{
//     console.log("quit");
// }

//break
console.log("break");
let f=1;
while(f<=5){
    if(f==3){
        break;
    }
    console.log(f);
    f++;
}
console.log("we used break at 3");

//loops with array
console.log("loops with array");
let fruits = ["mango","apple","banana","litchi","orange"];
fruits.push("pineapple");
for(let i=0;i<=fruits.length;i++){
    console.log(i,fruits[i]);
}

//reverse
console.log("reverse");
let fruits2 = ["mango","apple","banana","litchi","orange"];
fruits2.push("pineapple");
for(let i=fruits2.length-1;i>=0;i--){
    console.log(i,fruits2[i]);
}

// //loops with nested arrays
// let hero = [
//     ["ironman","spyderman","thor"],
//     ["superman","wonder man","flash"]
// ]

// for (let i=0;i<length.hero;i++){
//     console.log(i,hero[i],hero[i].length);
//     for(let j=0;j<hero[i].length;j++){
//      console.log("j=${j},${hero[i][j]}")
//      }
// }

//student
let student = [["aman",95],["shradda",94.4],["karan",100]];

for (let i=0;i<student.length;i++){
    console.log("info of students #${i}");
    for (let j=0;j<student[i].length;j++){
        console.log(student[i][j]);
        }
}