var num = [12,3,64,56,76,34,88];

console.log("Asscending Order: ")
for(var i=0;i<num.length;i++)
{
    for(var j=i+1;j<num.length;j++)
    {
        if(num[i] < num[j])
        {
            var tmp = num[i];
            num[i] = num[j];
            num[j] = tmp;
        }
    }
}
console.log(num)

console.log("Descending Order: ")
for(var i=0;i<num.length;i++)
{
    for(var j=i+1;j<num.length;j++)
    {
        if(num[i] > num[j])
        {
            var tmp = num[i];
            num[i] = num[j];
            num[j] = tmp;
        }
    }
}
console.log(num)