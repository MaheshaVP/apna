//Qs1
let buttton = document.createElement("button");
let input = document.createElement("input");
buttton.innerText = "click me!";

document.querySelector("body").append(input);
document.querySelector("body").append(buttton);

//Qs2
buttton.setAttribute("id","btn");
input.setAttribute("placeholder","username");

//Qs3
let btn = document.querySelector("#btn");
btn.classList.add("btnStyle");

//Qs4
let h1 = document.createElement("h1");
h1.innerHTML = "<u>DOM Practice</u>";
document.querySelector("body").append(h1);

//Qs5
let para = document.createElement("p");
para.innerHTML = "Apna College <b>Delta</b> practice";
document.querySelector("body").append(para);

