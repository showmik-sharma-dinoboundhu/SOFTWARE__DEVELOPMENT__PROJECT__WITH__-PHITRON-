alert("Myself Javascript_Connection")

console.log("Hello it's me");


// A collection of tag like array
var h1 = document.getElementsByTagName("h1");
console.log(h1);


// For single line-
var title = document.getElementById("title").style.color = "red";

// Remove Color:
document.getElementById("title").style.removeProperty("color");

console.log(title);



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

// TypeOf-
console.log(typeof input);


// Div tag
var parent = document.getElementById("parent").innerHTML;
console.log(parent);



// Parent-child access:
var testdiv = document.getElementsByClassName("test");
console.log(testdiv)
console.log(testdiv[0].childNodes);
console.log(testdiv[0].childNodes[1]);
var testdiv = document.getElementsByClassName("test");

console.log(testdiv[0]);
console.log(testdiv[0].children[0]);
console.log(testdiv[0].children[0].parentNode);
console.log(testdiv[0].children[0].parentNode.parentNode);
console.log(testdiv[0].children[0].parentNode.parentNode.parentNode);




// JS to insert in website:
var newdiv = document.getElementById("newdiv");
var p = document.createElement("p");
p.innerText = "Notun Ami";
newdiv.appendChild(p);



// Function:
var newdiv = document.getElementById("newdiv");

function createEl() {
    var p = document.createElement("p");
    p.innerText = "Notun Ami";
    newdiv.appendChild(p);
}

createEl();



// addEvenLister:
document.getElementById("submit-btn").addEventListener("click",function(e){
    console.log("yess bosss");
    var inputValue = document.getElementById("input").value;
    console.log(inputValue);
})



document.getElementById("input").addEventListener("blur", function(e) {
    console.log("hello");
    console.log(e.target.value);
});