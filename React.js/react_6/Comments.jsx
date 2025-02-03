import { useState } from "react"
import './Comments.css'
import CommentsForm from "./CommentsForm";

export default function Comments() {
    let [comments,setComments] = useState([{
        username : "@mahii",
        remarks : "great job",
        rating : 4,
    }]);

    let addNewComment = (comment) => {
        setComments((currComment) => [...currComment,comment]);
        console.log("added new comment");
    }

    return(
        <div>
        <h3>All comments</h3>
        {comments.map((comment,idx)=> (
            <div className="comments" key={idx}>
            <span>{comment.remarks}</span>
            &nbsp;
            <span>(rating = {comment.rating})</span>
            <p>{comment.username}</p>
        </div>
        ))}
        
        <hr />
        <CommentsForm addNewComment={addNewComment} />
        </div>
    )
}