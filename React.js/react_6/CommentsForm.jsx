import { useState } from "react"

export default function CommentsForm({addNewComment}) {
    let [formData,setFormData] = useState({
        username : "",
        remarks: "",
        rating : 5,
    })
    
    let [isvalid,setIsValid] = useState(true);

    let handleInputChange = (event) => {
        setFormData((currData) => {
            return {...currData,[event.target.name]:[event.target.value]}
        })
    }


    let handleSubmit = (event) => {

        if(!formData.username) {
            console.log("user name is null");
            setIsValid(false);
            event.preventDefault();
            return;
        }
        console.log(formData);
        addNewComment(formData);
        event.preventDefault();
        setFormData({
            username : "",
        remarks: "",
        rating : 5,
        })
    }

    let handleReset = (event) => {
        event.preventDefault();
        setFormData({
            username : "",
            remarks: "",
            rating : 5,
        })
    }

    return(
        <div>
        <h4>Give a Comment</h4>

        <form onSubmit={handleSubmit}>

        <label htmlFor="username">UserName </label>
        <input type="text" 
        placeholder="username" 
        value={formData.username} 
        onChange={handleInputChange}
        name="username"
        id="username"/>
        {!isvalid && <p style={{color:"red"}}>username cannot be empty</p>}
        <br /><br />

        <label htmlFor="remarks">Remarks </label>
        <textarea
         placeholder="add few Remarks" 
         value={formData.remarks}
         onChange={handleInputChange}
         name="remarks"
         id="remarks">Remarks </textarea>
        <br /><br />

        <label htmlFor="rating">Rating </label>
        <input type="number" 
        placeholder="rating" 
        min={1} 
        max={5}
        value={formData.rating}  
        onChange={handleInputChange}
        name="rating"
        id="rating"/>
        <br /><br />

        <button onClick={handleReset}>Reset</button>
        &nbsp;
        <button>Add Comment</button>
        </form>
        
        </div>
    )
}

