var person = 
{
    Name: "SHowmik SHarma",
    hands: 2,
    friends: 5,
    age: 22,
    leg: 2,
    collage:
    {
        Name: "Feni Computer Institute",
        Location: "Ranir Hat Bazar, Sadar Hospital Road, Feni",
    }
}

console.log(person);
console.log(Object.keys(person));
console.log(Object.values(person));
console.log(Object.entries(person));

// Single single object values access:
console.log(person.age);
console.log(person.hands);
console.log(person.leg);

// Object inside object value access:
console.log(person.collage.Name);
console.log(person.collage.Location);