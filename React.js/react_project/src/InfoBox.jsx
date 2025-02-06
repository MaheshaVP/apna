import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import './InfoBox.css'
import WbSunnyIcon from '@mui/icons-material/WbSunny';
import ThunderstormTwoToneIcon from '@mui/icons-material/ThunderstormTwoTone';
import AcUnitTwoToneIcon from '@mui/icons-material/AcUnitTwoTone';

export default function InfoBox({info}) {
    const INIT_IMG = "https://plus.unsplash.com/premium_photo-1678066986924-120fdbdf3439?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";


    const Hot_Img = "https://images.unsplash.com/photo-1524594081293-190a2fe0baae?q=80&w=1776&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";
    const Cold_Img = "https://plus.unsplash.com/premium_photo-1678066986924-120fdbdf3439?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";
    const Rain_Img = "https://images.unsplash.com/photo-1536329978773-2f8ac431f330?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";

    // let info = {
    //     city : "Delhi",
    //     country : "IN",
    //     name : "Tumkur",
    //     feelsLike : 24.84,
    //     temp : 25.05,
    //     tempMin : 25.05,
    //     tempMax : 25.05,
    //     humidity : 47,
    //     weather : "haze",
    //     windspeed : "5.53",
    // }

    return(
        <div className="InfoBox">
        <div className='cardContainer'>
            <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 140 }}
        image={
            info.humidity > 80 ?
            Rain_Img :
            info.temp > 15 ? 
            Hot_Img : 
            Cold_Img
        }
        title="green iguana"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {info.city} {
                info.humidity > 80 ?
                <ThunderstormTwoToneIcon/> :
                info.temp > 15 ? 
                <WbSunnyIcon/> : 
                <AcUnitTwoToneIcon/>
          }
        </Typography>
        <Typography variant="body2" sx={{ color: 'text.secondary' }} component={"span"}>
         <p>Temperature = {info.temp}&deg;C</p>
         <p>Humidity = {info.humidity}</p>
         <p>Min Temp = {info.tempMin}&deg;C</p>
         <p>Max Temp = {info.tempMax}&deg;C</p>
         <p>Wind Speed = {info.WindSpeed}</p>
         <p>The weather can be described as <b>{info.weather}</b> and feels {info.feelslike}&deg;C</p>
        </Typography>
      </CardContent>
    </Card>
    </div>

        </div>
    )
}