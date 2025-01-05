//ById
let smallImages = document.getElementsByClassName("oldImg");

for(let i=0;i<smallImages.length;i++) {
    smallImages[i].src = "assets/spiderman_img.png";
    console.log(`value of image no. ${i} is changed`);
}

//ByTagName
console.dir(document.querySelector("h1"));

console.dir(document.querySelector("#description"));

console.dir(document.querySelector(".oldImg"));

console.dir(document.querySelectorAll("div a"));

//Manipulating Attributes
let links = document.querySelectorAll(".box a");

for(let i=0;i<links.length;i++) {
    links[i].style.color = "yellow";
}

let head = document.getElementsByTagName("h1");
head[0].style.color = "green";

// for (link of links) {
//     link.style.color = "purple";
// }

