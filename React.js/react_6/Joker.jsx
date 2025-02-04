import { useEffect, useState } from "react";

export default function Joker() {
    
    const URL = "https://official-joke-api.appspot.com/random_joke";


    const getNewJoke = async() => {
        let response = await fetch(URL);
        let jsonResponse = await response.json();
        console.log(jsonResponse);
        // return jsonResponse;
        setJoke({ setup: jsonResponse.setup , punchline:jsonResponse.punchline});
    }

    useEffect(()=> {async function getFirstJoke() {
        let response = await fetch(URL);
        let jsonResponse = await response.json();
        console.log(jsonResponse);
        // return jsonResponse;
        setJoke({ setup: jsonResponse.setup , punchline:jsonResponse.punchline});
    }
    getFirstJoke();
    },[])

    let [joke,setJoke] = useState(getNewJoke);

    

    return(
        <div>
            <h2>Joke</h2>
            <h4>{joke.setup}</h4>
            <h4>{joke.punchline}</h4>
            <button onClick={getNewJoke}>New Joke</button>
        </div>
    )
}