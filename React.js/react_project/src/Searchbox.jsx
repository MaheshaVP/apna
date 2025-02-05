import './Searchbox.css'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from 'react';


export default function SearchBox() {
    let [city,setCity] = useState(" ");
    let API_URL = "https://api.openweathermap.org/data/2.5/weather";
    let API_KEY = "e898d24789628501dd17c483f3e9f1fb";

    let getWeatherInfo = async() => {
       let response = await fetch(`${API_URL}?q=${city}&appid=${API_KEY}&units=metric`);
       let jsonResponse = await response.json();
       console.log(jsonResponse);

       let result = {
        name : jsonResponse.name,
        temp : jsonResponse.main.temp,
        pressure : jsonResponse.main.pressure,
        tempMax : jsonResponse.main.temp_max,
        tempMin : jsonResponse.main.temp_min,
        humidity : jsonResponse.main.humidity,
        weather : jsonResponse.weather[0].description,
        Country : jsonResponse.sys.country,
       }
       console.log(result);
    }

   
    let handleChange = (evt) => {
        setCity(evt.target.value);
    };

    let handleSubmit = (event) => {
        event.preventDefault();
        console.log(city);
        setCity("");
        getWeatherInfo();
    };

    return(
        <div className='SearchBox'>
            <h3>Search for the Weather</h3>
            <form  onSubmit={handleSubmit}>
            <TextField 
            id="city" 
            label="City Name"
             variant="outlined" 
             required 
             value={city} 
             onChange={handleChange}/>
            <br /><br />
            <Button variant="contained" type='submit'>
            Send
            </Button>

            </form>
        </div>
    )
}