// One-condition  if/else  statement (e.g. "if x == 2"):
var x = 1;
if (x < 5) {
  console.log("x is less than 5");
} else {
  console.log("x is greater or equal than 5");
}

// Multiple conditions if/else statement
var x = 1;
if (x < 5 && x === 1) {
  console.log("x is less than 5 and equal in value and type to 1")
} else if (x < 5) {
  console.log("x is less than 5 but not equal in type and value to 1")
} else {
  console.log("x is not less than 5")
}

// For loop:
for (i = 0; i < 10; i++) {
  console.log(i)
}

// For/each Loop (Enhanced For loop):

var person = {fname:"John", lname:"Doe", age:25}; // object declaration 

var text = "";
var x;
for (x in person) {
  text += person[x];
}

console.log(text);

// While Loops:
i = 0;
var words = [];
while (i < 10) { // must contain a loop limiter
  words += "The number is " + i;
  i++; // must change the limiter's variable to avoid a forever loop
}
console.log(words);

// Do/While Loop:
x = 0;

do {
  console.log("I will print this until I've printed 10 times.")
  x++;
}
while (x < 10);

// Switch-case  statement:

// switch (expression) {
  // case label_1:
    // statements_1
    // [break;]
  // case label_2:
    // statements_2
    // [break;]
  // default:
    // statements_def
    // [break;]
// }

// Break  and  continue  statements:
var toPrint = "";

for (i = 0; i < 10; i++) {
  if (i === 3) { 
    break; 
  }
  toPrint += "The number is " + i;
}

console.log(toPrint);
toPrint = "";

for (i = 0; i < 10; i++) {
  if (i === 3) { 
    continue; 
  }
  toPrint += "The number is " + i;
}

console.log(toPrint);

if (x < 10) {
  x += 1;
}

var x = 8;
