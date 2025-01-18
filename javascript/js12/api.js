let jsonRes = 
'{"fact":"Kittens remain with their mother till the age of 9 weeks.","length":57}'

let validRes = JSON.parse(jsonRes);
console.log(validRes.fact);

let student = {
    name : "mahesh",
    marks : 84,
}

let stu = JSON.stringify(student);
console.log(stu);

