var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names);
console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
console.log("Length: ",names.length);

// Array add or Push:
names.push("Dinogon");
console.log(names);

// Array Pop or remv:
names.pop();
console.log(names);

// Array add front:
names.unshift("Mona");
console.log(names);

// Array remv front:
names.shift();
console.log(names);

// Array concat :
console.log(names.concat("Nittanondo"));



// Array Reverse:
console.log(names.reverse())

// Array slice:
var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names.slice(2,4));

// Array Join:
var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names.join("-"));
console.log(names.join(" "));

// Index of:
var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names.indexOf("Showmik"));
console.log(names.indexOf("Show"));

// Include:
var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names.includes("Devdut"));