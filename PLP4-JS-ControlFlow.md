### CS330: Programming Language Project (PLP) Assignment 4: Control flow ###
#### By Eva Lynch ####

What does control flow look like in JavaScript? Read on to find out and look at PLP4-examples.js in this repo for running code examples.

#### Discussion Questions: ####

1. What types of conditional statements are available in your language?

JavaScript allows for if/else, if/else if/else, for, for/each, while, do/while, and break and continue statements within those.
Here are some examples and relevent information for these types of statements.

One-condition  if/else  statement (e.g. "if x == 2"):

 `if (condition) {`
 
  `statement_1;`
  
`} else {`

  `statement_2;`
  
`}`

and expanded:

`if (condition1) {`

  `//  block of code to be executed if condition1 is true`
  
`} else if (condition2) {`

  `//  block of code to be executed if the condition1 is false and condition2 is true`
  
`} else {`

  `//  block of code to be executed if the condition1 is false and condition2 is false`
`}`

These conditions could have any of the following comparison operators:
`==` equal to

`===` equal in value and type

`!=` not equal

`!==` not equal in valor and type

`>` greater than

`<` less than

`>=` greater than or equal to

`<=` less than or equal to

For loop:

`for (statement 1; statement 2; statement 3) {`
  `// code block to be executed`
`}`

Statement 1 is executed (one time) before the execution of the code block.

Statement 2 defines the condition for executing the code block.

Statement 3 is executed (every time) after the code block has been executed.

[(Source)](https://www.w3schools.com/js/js_loop_for.asp)

For/each Loop (Enhanced For loop):

`var person = {fname:"John", lname:"Doe", age:25}; // object declaration `

`var text = "";`

`var x;`

`for (x in person) {`

  `text += person[x];`
  
`}`

`console.log(text) // returns JohnDoe25`

(Same source as For Loop)

While Loops:

`var i = 0;`

`var words = [];`

`while (i < 10) { // must contain a loop limiter`

  `text += "The number is " + i;`
  
  `i++; // must change the limiter's variable to avoid a forever loop`
  
`}`

`console.log(words) // returns The number is 0The number is 1The number is 2 etc.`

Do/While Loop:

`do {`
  `// code block to be executed`
`}`
`while (condition);`

Switch-case  statement:

`switch (expression) {`

  `case label_1:`
  
    statements_1
    [break;]
    
  `case label_2:`
  
    statements_2
    [break;]
    ...
    
  `default:`
  
    statements_def
    [break;]
    
`}`

Break  and  continue  statements:

To review, break statements "jump out" of loops and continue statements "jump over" one iteration in loops.

Some examples:

This example stops the loop when i === 3, at which point the program will continue after the code block, if there is any code.
`for (i = 0; i < 10; i++) {`
  `if (i === 3) { `
    `break; `
  `}`
  `text += "The number is " + i;`
`}`

This example skips an iteration of the for loop if i === 3.
`for (i = 0; i < 10; i++) {`
  `if (i === 3) { `
    `continue; `
  `}`
  `text += "The number is " + i;`
`}`

[(Source 1)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
[(Source 2)](https://www.w3schools.com/js/js_break.asp)

2. Does your language use short-circuit evaluation? If so, make sure that your code includes an example.

Yes, multi-condition if/else statements (`&&`, `||` and `!`) are accepted in JS conditionals! They would look like this:

`(a > 0 && b > 0)`

`(a > 0 || b > 0)`

`(!(a > 0 || b > 0))`

3. How does your programming language deal with the “dangling else” problem?

JavaScript handles the ambiguity of dangling elses by analyzing the curly braces of the else and attaching it to to 
appropriate if. Be wary of not using brackets in your single line if/elses because the ambiquity may strick again. [(Source 1)](https://en.wikipedia.org/wiki/Dangling_else) [(Source 2)](https://stackoverflow.com/questions/7117873/do-if-statements-in-javascript-require-curly-braces)

4. Does your language include multiple types of loops (while, do/while, for, foreach)? If so, what are they and how 
do they differ from each other?

Yes, all of these. While there are examples above of each, the differences are as follows:

For loops are controlled by variable that aren't objects, while for/each loops typically are controlled by iterating through an object.
While loops have their control variables defined at the beginning of the loop rather than at the end like in a do/while. This means that if the controlling variable is false, a do/while loop would run once before being caught by the controlling variable. A while loop would not run once because the control variable would catch the falseness at the start. 

5. Can you use break or continue statements (or something similar) to control iteration?

Yes! See the examples above or in the PLP4-example.js code.

6. If your language supports switch or case statements, do you have to use “break” to get out of them? Can you use “continue”
to have all of them evaluated?

Using a break is optional for each case, so if you wanted to evaluate all cases, just omit the breaks and the program will go through all of them until hitting a break or a default (which automatically has a break, whether or not you hard code one in). The use of continues as "short cuts" in switch statments is not allowed in JavaScript. [(Source)](https://stackoverflow.com/questions/18076238/continue-allways-illegal-in-switch-in-js-but-break-works-fine)
