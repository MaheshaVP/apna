export default function CommentsForm() {
    return(
        <div>
        <h4>Give a Comment</h4>
        <br />
        <input type="text" placeholder="username" />
        <br /><br />
        <textarea placeholder="Remarks"></textarea>
        <br /><br />
        <input type="number" placeholder="rating" />
        <br /><br />
        <button>Add Comment</button>
        </div>
    )
}