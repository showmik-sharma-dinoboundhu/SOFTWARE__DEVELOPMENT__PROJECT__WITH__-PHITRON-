function sumTwoNum (a, b)
{
    console.log(a)
    console.log(b)
    var sum = a+b;
    console.log(sum);
}

sumTwoNum(10, 20);

// Default parameter.
function sumTwoNum (a = 0, b = 0)
{
    console.log(a)
    console.log(b)
    var sum = a+b;
    console.log(sum);
}

sumTwoNum(10);