for(var i=0;i<10;i++)
{
    console.log(i,".","Say My Name!!!!");
}

var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
console.log(names[3]);

for(var i=0;i < names.length;i++)
{
    console.log(names[i]);
}

for(var i=0;i < names.length;i++)
{
    console.log(names);
}

// Condition under Loop:
for(var i=0;i < names.length;i++)
{
   if (names[i] == "Showmik")
   {
    console.log("Found");
    break;
   }
   else 
    {
        console.log("Not Found");
    }
}
