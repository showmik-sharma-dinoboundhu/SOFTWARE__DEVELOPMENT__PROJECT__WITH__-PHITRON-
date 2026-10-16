var n1 = "showmik sharma"
console.log(n1);

let n2 = "Dinoboundhu Sharma"
console.log(n2);

const n3 = "Devdut Sharma"
console.log(n3);


function name(param)
{
    if (true)
    {
      var  x = 20;
    }
    console.log(x);   
}

console.log(name())




// Inside Functio:
function names(param)
{
    if (true)
    {
      let  x = 20;
    }
    console.log(x);   
}

console.log(names())


function named(param)
{
    if (true)
    {
      const  x = 20;
    }
    console.log(x);   
}

console.log(named())





// Outside fun:
function names(param)
{
    if (true)
    {
      let  x = 20;
      console.log(x);   
    }
}

console.log(names())


function named(param)
{
    if (true)
    {
      const  x = 20;
      console.log(x);   
    }
}

console.log(named())



// Let vs Const:
// let:
let na = "Showmik "
console.log(na);
na = "Showmik Sharma";
console.log(na);        // Name can change


// const:
const nam = "Showmik ";
console.log(nam);
nam = "SHowmik Sharma"
console.log(nam);       // can't change.