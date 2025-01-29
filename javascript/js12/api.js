// let jsonRes = 
// '{"fact":"Kittens remain with their mother till the age of 9 weeks.","length":57}'

// let validRes = JSON.parse(jsonRes);
// console.log(validRes.length);

// let student = {
//     name : "mahesh",
//     marks : 84,
// }

// let stu = JSON.stringify(student);
// console.log(stu);


// fetch
// let url = "https://catfact.ninja/fact";

// fetch(url)
// .then((res) => {
//     return res.json();
//     })
//     .then((data) => {
//         console.log("data1 =", data.fact);
//         return fetch(url);
//     })
//     .then((res) => {
//         return res.json();
//     })
//     .then((data2) => {
//         console.log("data2 =",data2.fact);
//     })
// .catch((err) => {
//     console.log("ERROR :",err);
// });


let url2 = "https://catfact.ninja/fact";

async function getFacts() {
    try{
        let res = await fetch(url2);
        let data = await res.json();
        console.log("data = ",data.length);

        // let res2 = await fetch(url2);
        // let data2 = await res2.json();
        // console.log("data2 = ",data2.fact);
    }catch(e) {
        console.log("error - ",e);
    }   
    console.log("bye");
}

