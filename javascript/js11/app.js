// //stack
// function hello() {
//     console.log("inside hello function");
//     console.log("hello");
// }

// function demo() {
//     console.log("calling hello function");
//     hello();
// }

// console.log("calling demo function");
// demo();
// console.log("done,bye!");

// //function callback
// function one() {
//     return 2;
// }

// function two() {
//     return one() + one();
// }

// function three() {
//     let ans = two() + one();
//     console.log(ans);
// }
// three();

// //Single threaded language
// let a = 25;
// console.log(a);
// let b = 10;
// console.log(b);
// console.log(a+b);


// setTimeout(() =>  {
//     console.log("apna college");
// },2000);

// console.log("hello...");

//callback hell


h1 = document.querySelector("h1");

function changeColor (color1,delay) {
    return new Promise((resolve,reject)=> {
        setTimeout (() => {
            h1.style.color = color1;
            resolve("color changed");
        },delay);
    });
}

changeColor("red",1000)
.then(()=> {
    console.log("red color was completed");
    return changeColor("orange",1000);
})
.then(()=>{
    console.log("orange color was completed");
    return changeColor("green",1000)
})
.then(()=> {
    console.log("green color was completed");
    return changeColor("yellow",1000)
})
.then(()=> {
    console.log("yellow color was completed");
    return changeColor("blue",1000)
})
.then(()=> {
    console.log("blue color was completed");
});


// changeColor("red",1000, ()=>{
//     changeColor("orange",1000, () => {
//         changeColor("yellow",1000, () => {
//             changeColor("green",1000, ()=> {
//                 changeColor("blue",1000, ()=> {

//                 });
//             });
//         });
//     });
// });


// changeColor("red",1000);
// changeColor("green",2000);
// changeColor("orange",3000);

//Nested 

// function savetoDb(data,success,failure) {
//     let internetSpeed = Math.floor(Math.random() * 10 ) + 1;
//     if(internetSpeed > 4) {
//         success();
//         // console.log("your data was saved", data);
//     }else{
//         failure();
//         // console.log("weak connection");
//     }
// }

// savetoDb("Apna College" , 
// ()=>{
//     console.log("success: your data was saved");
//     savetoDb("hello world", ()=> {
//         console.log("success2:  data2 saved");
//         savetoDb("mahesh", ()=> {
//             console.log("success3:  data3 saved");
//         }, ()=> {
//             console.log("failure3:  data3 not saved");
//         });

//     }, ()=> {
//         console.log("failure2:  data2 not saved");
//     });
// },
// ()=> {
//     console.log("failure: weak connection, data  not saved"); 
// });



//using of promise


// function savetoDb(data) {    
//     return new Promise ((resolve,reject) => {
//         let internetSpeed = Math.floor(Math.random() * 10 ) + 1;
//         if(internetSpeed > 4) {
//             resolve("success : data was saved");
//         }else{
//             reject("failure : week connection");
//         }
//     });
// }

// savetoDb("apna college")
// .then((result)=> {
//     console.log("data1 saved.");
//     console.log("result of promise :",result);
//     return savetoDb("hello world");
// })
// .then((result) => {
//     console.log("data2 saved.");
//     console.log("result of promise :",result);
//     return savetoDb("mahesh");
// })
// .then((result)=> {
//     console.log("data3 saved.");
//     console.log("result of promise :",result);
// })
// .catch((error)=> {
//     console.log("promise was rejected");
//     console.log("error of promise :",error);
// })




