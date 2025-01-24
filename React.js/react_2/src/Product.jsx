/* eslint-disable react/prop-types */

import "./Product.css"

function Product ({title,price}) {
    // console.log(props.title);
  return (
    <div className="Product">
        <h1>{title}</h1>
        <p>Price : {price}</p>
    </div>
   
  );
}



export default Product;