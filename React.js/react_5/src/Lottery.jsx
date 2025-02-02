import { useState } from "react"
import './Lottery.css'
import {genTickets,sum} from './helper';
import Ticket from "./Ticket";


export default function Lottery({n,winningSum}) {
    let[ticket,setTicket] = useState(genTickets(n));
    let isWinning = sum(ticket) === winningSum;

    let buyTicket=() => {
        setTicket(genTickets(n));
    }

    return (

        <div>
            <h1>Lottery ticket</h1>
            <Ticket ticket={ticket}/>
            <button onClick={buyTicket}>Buy Ticket</button>
            <h3>{isWinning && "Congraduations you won"}</h3>
        </div>
    )
}


