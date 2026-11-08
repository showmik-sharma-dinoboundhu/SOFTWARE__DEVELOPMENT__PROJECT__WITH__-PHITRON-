var a = [1,2,4,3,7,5,9,8];
var max;
for(var i=0;i<a.length;i++)
{
    for(var j=i+1;j<a.length;j++)
    {
        if(a[i] > a[j])
        {
            max = a[i];
        }
    }
}
console.log(max);