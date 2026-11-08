var num = [1,2,2,4,3,5,3,6,4,7,8,7,8,9,9,10]
var unique = [];

for (var i = 0; i < num.length; i++)
{
    if (!unique.includes(num[i]))
    {
        unique.push(num[i]);
    }
}
console.log(unique)