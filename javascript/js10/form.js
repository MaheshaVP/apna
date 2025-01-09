// let form = document.querySelector("form");

// form.addEventListener("submit", function(event) {
//     event.preventDefault();
//     console.dir(form);
//     // alert("form submited");
//     let user = this.elements[0];  //form element
//     let pass = this.elements[1];

//     console.log(user.value);
//     console.log(pass.value);
    

//     alert(`Hi ${user.value}, your password is set to ${pass.value}`);
// });





// let form = document.querySelector("form");

// form.addEventListener("submit",function(event) {
//     event.preventDefault();

//     alert("you submitted the form");
// });

//     let user = document.querySelector("#user");
//     let pass = document.querySelector("#pass");


//     user.addEventListener("change", function(event) {
//         event.preventDefault();
//         console.log("change event");
//         console.log("final value = ",this.value);
        
//     });


//     pass.addEventListener("change",function() {
//         console.log("change event");
//         console.log("final value = ",this.value);
//     });

   


let inp = document.querySelector("#text");
let p = document.querySelector("p");

inp.addEventListener("input",function() {
    console.log(inp.value);
    p.innerText = inp.value;
});