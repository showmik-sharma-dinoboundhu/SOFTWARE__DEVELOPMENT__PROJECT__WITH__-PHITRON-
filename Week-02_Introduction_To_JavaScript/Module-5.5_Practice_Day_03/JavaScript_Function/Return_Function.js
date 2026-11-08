function sumTwoNum (a, b)
{
    var sum = a+b;
    return sum;
}

var output = sumTwoNum(100,200);
console.log(output);


function multifly(a)
{
    var mul = a*a;
    return mul;
}
var ans = multifly(10);
console.log(ans);


function test1()
{
    return "Hello";
}
function test2()
{
    return test1() + " World";
}
var exec = test2();
console.log(exec);