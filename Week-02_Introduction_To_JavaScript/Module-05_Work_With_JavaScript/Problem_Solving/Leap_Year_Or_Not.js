var x = 2020;
if((x % 4 == 0 && x % 100 != 0) || (x % 400 == 0))
{
    console.log("Leap Year");
}
else
{
    console.log("Not Leap Year");
}