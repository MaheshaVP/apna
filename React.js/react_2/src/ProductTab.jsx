import Product from "./Product";


function ProductTab() {
    
    let styles = {
        display:"flex",
        flexWrap:"wrap",
        justifyContent : "center",
        alignItems : "center",
    };

    return(
        <div style={styles}>
        <Product title="computer" idx={0}/>
        <Product title="mouse"  idx={1}/>
        <Product title="Apple pencil" idx={2}/>
        <Product title="keyBoard"  idx={3}/>
        </div>
    );
}

export default ProductTab;