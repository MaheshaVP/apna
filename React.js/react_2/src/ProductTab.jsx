import Product from "./Product";


function ProductTab() {
    return(
        <>
        <Product title="Phone" price={12000}/>
        <Product title="Laptop" price={25000}/>
        <Product title="Tab" price={"Free"}/>
        </>
    );
}

export default ProductTab;