var num = 78;
if(num % 2 == 0)
{
    console.log("Even");
}
else
{
    console.log("Not Even or Odd");
}

// Condition Loop:
var num = [55, 56, 77, 80, 0];
var even = 0, odd = 0, Zero = 0;
for(var i=0;i<num.length;i++)
{
    if(num[i] % 2 == 0)
    {
        even ++;
    }
   
    else
    {
      odd++;
    }
    if(num[i] == 0)
    {
        Zero ++;
    }
}
console.log("Even Count: ",even);
console.log("Odd Count: ",odd);
console.log("Zero Count: ",Zero);