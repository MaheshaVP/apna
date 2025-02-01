import { useState } from "react";

export default function Form() {

    let [formData,setFormData] = useState({
        fullName: "",
        userName : "",
        password : "",
    })


    // let handleNameChange = (event) => {
    //     setFullName(event.target.value);
    //     console.log(setFullName);
    // }

    // let handleUserName = (event) => {
    //     setUserName(event.target.value);
    //     console.log(setUserName);
    // }

    let handleInputChange = (event) => {
        // let fieldName = event.target.name;
        // let newValue = event.target.value;
        // console.log(fieldName);  //FullName
        // console.log(newValue);   //TypeValue

        setFormData((currData) => {
            // currData[fieldName] = newValue;
            return {...currData,[event.target.name]:event.target.value};
        });
    };

    let handleSubmit = (event) => {
        event.preventDefault();
        console.log(formData);
        setFormData({
            fullName: "",
        userName : "",
        password : "",
        })
    }
    
  
    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="fullName">Full Name : </label>
            <input 
            placeholder="Enter your name" 
            type="text" 
            value={formData.fullName} 
            id="fullName"
            name="fullName"
            onChange={handleInputChange}
            />
            <br /><br />

            <label htmlFor="userName">UserName : </label>
            <input 
            placeholder="Enter userName" 
            type="text" 
            value={formData.userName} 
            id="userName"
            name="userName"
            onChange={handleInputChange}
            />
            <br /><br />

            <label htmlFor="password">Password : </label>
            <input 
            placeholder="Enter password" 
            type="password" 
            value={formData.password} 
            id="password"
            name="password"
            onChange={handleInputChange}
            />
            <br /><br />

            <button >Submit</button>
        </form>
    );
}
