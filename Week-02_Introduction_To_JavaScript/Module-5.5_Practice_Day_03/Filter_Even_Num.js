var a = [1,2,4,3,7,5,9,8];
var even = 0, odd = 0;
for(var i=0;i<a.length;i++)
{
   if(a[i] % 2 == 0)
   {
    even++;
   }
   else
   {
    odd++;
   }
}
console.log(even);
console.log(odd);