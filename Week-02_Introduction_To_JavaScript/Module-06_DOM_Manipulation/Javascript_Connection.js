// alert("Myself Javascript_Connection")

console.log("Hello it's me");


// A collection of tag like array
var h1 = document.getElementsByTagName("h1");
console.log(h1);


// For single line-
var title = document.getElementById("title").style.color = "red";
console.log(title);

// Remove Color:
document.getElementById("title").style.removeProperty("color");


// Two or more than tag in class:
var child = document.getElementsByClassName("child");
console.log(child[0]);
console.log(child[1]);
console.log(child);


// Image Tag attribute-
var img = document.getElementById("img");
console.log(img.getAttribute("src"));

// Image tag set attribute-
img.setAttribute("alt", "picture");
console.log(img.getAttribute("alt")); 

img.classList.add("testClass");
console.log(img);


// Text-
var hero = document.getElementById("hero");
console.log(hero.innerText);

// Input-
var input = document.getElementById("input");
console.log(input.value);


// Div tag
var parent = document.getElementById("parent").innerHTML;
console.log("parent");