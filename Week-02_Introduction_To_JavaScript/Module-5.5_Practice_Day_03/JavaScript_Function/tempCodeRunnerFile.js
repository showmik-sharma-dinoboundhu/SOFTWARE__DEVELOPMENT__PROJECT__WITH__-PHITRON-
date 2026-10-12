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