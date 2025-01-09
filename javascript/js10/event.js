// let btn = document.querySelector("button");
// let  p = document.querySelector("p");
// let h1 = document.querySelector("h1");
// let  h3 = document.querySelector("h3");


// function changeColor () {
//     console.dir(this.innerText);
//     this.style.backgroundColor = "blue";
// }

// btn.addEventListener("click", changeColor);

// p.addEventListener("click", changeColor);

// h1.addEventListener("click", changeColor); 

// h3.addEventListener("click", changeColor);


//keyboard events
// let btn = document.querySelector("button");

// btn.addEventListener("dblclick", function(events) {
//     console.log(events);
//     console.log("button clicked");
// });

let inp = document.querySelector("input");

// inp.addEventListener("keydown", function() {
//     console.log("key was pressed");
// });

inp.addEventListener("keyup", function(events) {
    // console.dir(inp);
    console.log("key = ",events.key);
    console.log("code = ",events.code);

    if(events.code == "KeyU") {
        console.log("characters move forward");
    }else if(events.code == "KeyD") {
        console.log("Move backward");
    }else if(events.code == "KeyL") {
        console.log("Move left");
    }else if(events.code == "KeyR") {
        console.log("Move right");
    }
});

