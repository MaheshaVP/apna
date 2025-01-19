//cat facts
let btn = document.querySelector("button");

let url1 = "https://dog.ceo/api/breeds/image/random"

btn.addEventListener("click", async()=> {
    // let fact = await getFact();
    // let p= document.querySelector("#result");
    // p.innerText = fact;
    let link = await getImage();
    // console.log(link);
    let img = document.querySelector("#result");
    img.setAttribute("src",link);
    console.log(link);
});

// let url = "https://catfact.ninja/fact";

async function getImage() {
    try{
        let res = await axios.get(url1);
        return res.data.message;
        return res.data.fact;
    } catch(e){
        console.log("error - ", e);
        return "/";
    }
}




