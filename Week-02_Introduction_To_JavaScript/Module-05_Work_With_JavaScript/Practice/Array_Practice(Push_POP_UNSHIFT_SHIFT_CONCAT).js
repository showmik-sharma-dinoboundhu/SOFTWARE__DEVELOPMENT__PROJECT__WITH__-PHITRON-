var names = ["Showmik", "Nittanondo", "Devdut", "Dinoboundu"];
console.log(names);
console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
console.log(names[3]);
console.log(names.length);

// push:
names.push("Dingon");
console.log(names);

// pop:
names.pop();
console.log(names);

// Unshift:
names.unshift("Mona");
console.log(names);

// Shift:
names.shift();
console.log(names);

// Concat:
console.log(names.concat("Dingon"));

// Reverse:
console.log(names.reverse());

// slice:
var names = ["Showmik", "Devdut", "Devgon", "Dinoboundhu"];
console.log(names.slice(1,4));

// Join:
console.log(names.join(" "));
console.log(names.join("-"));

// IndexOf:
console.log(names.indexOf("Showmik"));
console.log(names.indexOf("Show"));

// Include:
console.log(names.includes("SHowmik"));
console.log(names.includes("Showmik"));