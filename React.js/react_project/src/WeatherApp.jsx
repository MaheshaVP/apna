import { useState } from "react";
import InfoBox from "./InfoBox";
import SearchBox from "./Searchbox";


export default function WeatherApp() {
    const [weatherInfo,setWeatherInfo] = useState({
        city : "Delhi",
        country : "IN",
        name : "Tumkur",
        feelsLike : 24.84,
        temp : 25.05,
        tempMin : 25.05,
        tempMax : 25.05,
        humidity : 47,
        weather : "haze",
        WindSpeed : "5.53",
    });

    let updateInfo = (newinfo) => {
        setWeatherInfo(newinfo);
    }

    return(
        <div style={{textAlign : "center"}}>
            <h1>Weather App</h1>
            <SearchBox updateInfo={updateInfo}/>
            <InfoBox info={weatherInfo}/>
        </div>
    )
}