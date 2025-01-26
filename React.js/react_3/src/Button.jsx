
function Greet(event) {
    console.log("Good morning");
    console.log(event);
}

function printBye() {
    console.log("bye");
}

function onHover () {
    console.log("hover moved on button");
}

function OnDouble () {
    console.log("you clicked twice")
}

export default function Button () {
    return (
        <div>
            <button onClick={Greet}>Click me</button>
            <p onClick={printBye}>this para is for event demo</p>

            <button onMouseOver={onHover}>Hover over me</button>
            <br />
            <br />
            <button className="dbl" onDoubleClick={OnDouble}>double click</button>
        </div>
    );
}