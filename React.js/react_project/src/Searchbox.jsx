import './Searchbox.css'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from 'react';


export default function SearchBox({updateInfo}) {
    let [city,setCity] = useState("");
    let [error,setError] = useState(false);
    let API_URL = "https://api.openweathermap.org/data/2.5/weather";
    let API_KEY = "e898d24789628501dd17c483f3e9f1fb";

    let getWeatherInfo = async() => {
        try{
            let response = await fetch(`${API_URL}?q=${city}&appid=${API_KEY}&units=metric`);
       let jsonResponse = await response.json();
       console.log(jsonResponse);

       let result = {
        city : city,
        feelslike : jsonResponse.main.feels_like,
        temp : jsonResponse.main.temp,
        pressure : jsonResponse.main.pressure,
        tempMax : jsonResponse.main.temp_max,
        tempMin : jsonResponse.main.temp_min,
        humidity : jsonResponse.main.humidity,
        weather : jsonResponse.weather[0].description,
        Country : jsonResponse.sys.country,
        WindSpeed : jsonResponse.wind.speed,
       }
       console.log(result);
       return result;
        }catch(err) {
            throw err;
        }
    }

   
    let handleChange = (evt) => {
        setCity(evt.target.value);
    };

    let handleSubmit = async(event) => {
        try{
            event.preventDefault();
        console.log(city);
        setCity("");
        let newinfo = await getWeatherInfo();
        updateInfo(newinfo);
        }catch(err) {
            setError(true);
        }
        
    };

    return(
        <div className='SearchBox'>
            <form  onSubmit={handleSubmit}>
            <TextField 
            id="city" 
            label="City Name"
             variant="outlined" 
             required 
             value={city} 
             onChange={handleChange}/>
            <br /><br />
            <Button variant="contained" type='submit' className='btn'>
            Search
            </Button>
            {error && <p style={{color:"red"}}>No such place found in our API</p>}
            
            </form>
        </div>
    )
}