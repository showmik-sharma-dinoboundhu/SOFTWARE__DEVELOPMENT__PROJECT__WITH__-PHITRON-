var n1 = 10;
var n2 = 30;
console.log(n1+n2);

var n3 = 20.22;
var n4 = 40.66;
var result = parseInt(n3+n4);
console.log(result);

var add = parseFloat(n3+n4);
console.log(add);


// string & num sum:
var n5 = "100";
var n6 = 100;
console.log(typeof(n5), typeof(n6))
console.log(n5+n6)


// String convert into num
console.log(parseInt(n5)+n6);


// No need to convert in sub, mul, div & Reminder
console.log(n5-n6);
console.log(n5*n6);
console.log(n5/n6);
console.log(n5%n6);


// Bcz of convertion in sum:
var t = "Myself ";
var t1 = "Showmik Sharma"; 
console.log(t+t1);


// Fraction num fix:
var nu = 100.57898;
console.log(parseFloat(nu).toFixed(2));