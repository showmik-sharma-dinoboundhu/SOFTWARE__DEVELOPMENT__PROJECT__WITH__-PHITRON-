var names = ["Showmik", "Devgon", "Devdut", "Dinoboundhu", "Nittanondo"];
var x = names[0];
for(var i=0;i<names.length;i++)
{
    if(names[i].length > x.length)
    {
        x = names[i];
    }
}
console.log(x);