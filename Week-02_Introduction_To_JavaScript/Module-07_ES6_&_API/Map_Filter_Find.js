// Map:
const num =[2, 2];

let tmp = [];
// Using for loop:
for(let i=0; i<num.length; i++)
{
    let element = num[i];
    let square = element * element;
    tmp.push(square);
}
console.log(tmp);


// using Map:
let square = num.map(x => x*x);
console.log(square);




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


console.log("\n");

// Find:
const res = product.find(pd => pd.id == 1);
const re = product.find(pd => pd.color == "Black");
console.log(res);
console.log(re);