export default function price({oldPrice,newPrice}) {
    let oldstyles = {
        textDecorationLine : "line-through",
    }; 
    let newStyles = {
        fontWeight : "bold",
    };
    let styles = {
        backgroundColor : "grey",
        height : "30px",
        width : "200px",
        borderBottomLeftRadius : "15px",
        borderBottomRightRadius : "15px",

    };

    return(
        <div style={styles}>
            <span style={oldstyles}>{oldPrice}</span>
            &nbsp; &nbsp; &nbsp;
            <span style={newStyles}>{newPrice}</span>
        </div>
    );
} 