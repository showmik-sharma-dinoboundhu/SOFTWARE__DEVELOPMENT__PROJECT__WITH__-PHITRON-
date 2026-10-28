// Filter:
const product = [
    {id: 1, name: "Realme", price: 450, color: "Black"},
    {id: 2, name: "Xaomi", price: 400, color: "Blue"},
    {id: 3, name: "Apple", price: 500, color: "White"},
    {id: 4, name: "Tecno", price: 200, color: "Neon Blue"}  
];

const r = product.filter((pd => console.log(pd)))
console.log("\n");
const result = product.filter((pd => pd.color == "Black"))
console.log(result);