var Person = 
{
    Name : "Showmik Sharma",
    Age : 22,
    From : "Feni",
    University :
    {
        Name : "Northern University of Bangladesh",
        Location : "Kaowla Bazar, Kaowla"
    },
    Collage :
    {
        Name : "Feni Computer Institute",
        Loaction : "Ranir Hat Bazar, Sadar Hospital Road, Feni",
    }
}

console.log(Person);
console.log(Object.keys(Person));
console.log(Object.values(Person));
console.log(Object.entries(Person));

console.log(Person.Collage.Name);
console.log(Person.Collage.Loaction)