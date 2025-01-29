import { useState } from "react";

export default function Counter () {
    let [count , setCount] = useState(0); //initialization
    // console.log("componant rendered");
    // console.log(`count = ${count}`);
    // console.log(count);


    let incCount=()=> {
        // setCount((currCount)=> {
        //     return currCount + 1;
        // });
        // setCount((currCount)=> {
        //     return currCount + 1;
        // });
    
    setCount(count + 1);
        // setCount(count+1);
        // console.log(`inside isccount , count = ${count}`)

    }

    return(
        <div>
            <h3>count is = {count}</h3>
            <button onClick={incCount}>Increase Count</button>
        </div>
    );
}

