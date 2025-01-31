import { useState } from "react"
import './Lottery.css'
import {genTickets,sum} from './helper';


export default function Lottery() {
    let[ticket,setTicket] = useState(genTickets(3));
    let isWinning = sum(ticket) === 15;

    let buyTicket=() => {
        setTicket(genTickets(3));
    }

    return (

        <div>
            <h1>Lottery ticket</h1>
            <div className="ticket">
                <span>{ticket[0]}</span>
                <span>{ticket[1]}</span>
                <span>{ticket[2]}</span>
            </div><br />
            <button onClick={buyTicket}>Buy Ticket</button>
            <h3>{isWinning && "Congraduations you won"}</h3>
        </div>
    )
}