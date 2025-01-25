
import "./Product.css"
import Price from "./Price";

function Product ({title,idx}) {
  let oldPrice = ["12000","600","9000","18200"]
  let newPrice = ["11000","500","6000","14000"]
  let description = [
    ["run faster","computer"],
    ["cursor moving faster","mouse"],
    ["used to touch screen","pencil"],
    ["wired keyboard","typing tool"],
  ]

  return (
    <div className="Product">
      <h4>{title}</h4>
      <p>{description[idx][0]}</p>
      <p>{description[idx][1]}</p>
      <p>{description[idx][2]}</p>
      <p>{description[idx][3]}</p>

      <Price oldPrice={oldPrice[idx]} newPrice={newPrice[idx]}/>
    </div>
   
  );
}

export default Product;