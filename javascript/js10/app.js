// //onclick
// let btns = document.querySelectorAll("button");

// for(btn of btns) {
//     btn.onclick = sayHello;
//     btn.onmouseenter = function () {
//         console.log("you entered a button");
//     };
//     console.dir(btn);
// }

// // btn.onclick = function () {
// //     prompt("do you want to click the button");
// //     alert("button was clicked");
// // }

// function sayHello () {
//     alert ("Hello");
// }


// // btn.onclick = sayHello;

//eventlistener
let btns = document.querySelectorAll("button");

for(btn of btns) {
    // btn.onclick = sayHello;
    // btn.onclick = sayName;
    // btn.addEventListener ("click",sayHello);
    // btn.addEventListener ("click",sayName);
    btn.addEventListener("dblclick", function () {
        console.log("you double clicked me");
    });

}

function sayHello () {
   alert ("Hello");
}

function sayName () {
    alert ("Nrupathunga University");
}

