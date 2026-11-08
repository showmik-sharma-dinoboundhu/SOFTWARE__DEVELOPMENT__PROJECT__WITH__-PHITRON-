console.log(1);
console.log(2);
name(3);
featched(4);
timer(5);
console.log(6);

function name(x)
{
    console.log(x);
}

// Late output
function featched(x)
{
  fetch('https://fakestoreapi.com/products/1')
    .then(res => res.json())
    .then(data => 
    {
        console.log(data);
    })
    .catch(err =>
    {
        console.log(err);
    });
}

// set timer if getting time extra then left
function timer(x)
{
    setTimeout(() => console.log(x), 2000);
}

