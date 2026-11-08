// Array Destructuring:
let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const [first, second, b, c] = num;
console.log(first);
console.log(second);
console.log(b);
console.log(c);


// Object Destructuring:
let obj = {
    name : "Showmik",
    age : "15",
    friends : 10,
    github : "yes",
    status : "Single",
};

let age = obj.age;
let names = obj.name;
console.log(age);
console.log(names);

// another way to print output:
let { ages } = obj;




// Nested array-object destruturing:
let t = [
    {
    name : "Showmik",
    age : "15",
    friends : ["dev","dut","dinoboundhu"],
    github : "yes",
    status : "Single",
    },

    {},

    {}
]
console.log(t.length);
console.log(t);
console.log("\n");
console.log(t[0].friends[2]);