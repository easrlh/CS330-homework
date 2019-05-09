## CS330: Programming Language Project (PLP) Assignments 5 & 6: Functions, Parameters, and Scope ##
#### By Eva Lynch ####

Being able to write functions that can be called more than once and sent different information each time is a huge part 
of most programming languages. However, there are a lot of variations in how functions are declared, where they are placed, 
how they accept parameters and how the function output is returned. Plus, you have to watch out for issues with scope and 
naming: some languages (e.g. Java) keep variables visible only inside of their own functions, while others (e.g. Perl) will 
have everything visible globally unless you use the keyword 'my'. So, how does JavaScript handle functions? Let's find out.

1. What is the syntax for declaring a function in your language?

`function funcName(parameter1, parameter2) {` 

  `// do something`
  
`}`

2. Are there any rules about where the function has to be placed in your code file so that it can run 
(i.e., before main, after main, in the same file, in the same folder, etc)?

Variables defined inside a function cannot be accessed from anywhere outside the function, because the 
variable is defined only in the scope of the function. However, a function can access all variables and 
functions defined inside the scope in which it is defined. In other words, a function defined in the global 
scope can access all variables defined in the global scope. A function defined inside another function can 
also access all variables defined in its parent function and any other variable to which the parent function 
has access. [(Source)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

3. Does your language support recursive functions? If so, write one.

A function can refer to and call itself. An example from [freeCodeCamp](https://medium.freecodecamp.org/recursion-in-javascript-1608032c7a1f):

`function factorial( n ) {

  if ( n === 1 ) {
  
    return 1;
    
  }
  
  return n * factorial( n - 1 );
  
}`

4. Can functions in your language accept multiple parameters? Can they be of different data types?

Yes, JavaScript functions can accept multiple parameters of any type desired. 
The types of paramteres are not statically typed, so whatever parameters get passed in at runtime will be accepted.

5. Can functions in your language return multiple values at the same time?

A function in JavaScript cannot return multiple values. That said, you can get equivalent results if you save the multiple variables you want to return into an array and return that instead!

Here's a code example from [TutorialRepublic](https://www.tutorialrepublic.com/faq/how-to-return-multiple-values-from-a-function-in-javascript.php):

`<script>`

`// Defining function`

`function divideNumbers(dividend, divisor){`

    var quotient = dividend / divisor;
    
    var obj = {
        dividend: dividend,
        divisor: divisor,
        quotient: quotient 
    };
    return obj;
    
`}`
 
`// Store returned value in a variable`

`var all = divideNumbers(10, 2);`

`// Displaying individual values`

`alert(all.dividend); // 0utputs: 10`

`alert(all.divisor); // 0utputs: 2`

`alert(all.quotient); // 0utputs: 5`

`</script>`

6. Declare a variable (say, x) in the main body of your program. Then declare a variable of the same name inside of a loop. 
Is there a conflict? Is the old variable overwritten or do you now have two variables of the same name?

The variable is completely overwritten, no errors raised. 
`var x = 5;`

`console.log(x);`

`for (var i = 0; i < 10; i++) {`

    var x = i;
    
`}`

`console.log(x);`

The outputs to VS Code's integrated command line (for a refresher on VS Code's integrated terminal, please refer 
to Installing JS in this repo) were `5` and `9`.

7. What if the other x is inside a function?

Engineers at [Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) had this to say:
>Primitive parameters (such as a number) are passed to functions by value; the value is passed to the function, 
but if the function changes the value of the parameter, this change is not reflected globally or in the calling function.

>If you pass an object (i.e. a non-primitive value, such as Array or a user-defined object) as a parameter and the 
function changes the object's properties, that change is visible outside the function.

From experience, I would agree. 
The `var x` inside of the function is independent from the main program's `var x` 
unless the function's x is returned and assigned to the main's x like so:

`var x = 5;`

`console.log(x);` 

(returns 5)

`for (var i = 0; i < 10; i++) {
    var x = i;
}`

`console.log(x);`

(returns 9)

`function test(number) {
    var x = 111;
    number = 222;
    console.log(x);
    console.log(number);
    return number;
}`

(returns 111 and then 222)

`console.log(x);`

(returns 9)

`x = test(x);`

`console.log(x);`

(returns 222)

And with non-primitive types:

`function myFunc(theObject) {
  theObject.make = 'Toyota';
}`

`var mycar = {make: 'Honda', model: 'Accord', year: 1998};`

`var x, y;`

`x = mycar.make; // x gets the value "Honda"`

`myFunc(mycar);`

`y = mycar.make; // y gets the value "Toyota"`

               // (the make property was changed by the function)

8. Can you have variables that are globally accessible? What are the rules for creating them?

Any variable created outside of a function are automatically global. This means that every function of the web page running the javascript can access the variable (which is also includes functions and objects). Something also to be wary on is assigning a value to an undeclared variable. Because you haven't declared the variable inside of the function, it will be automatically assigned as a global variable. [(Source)](https://www.w3schools.com/js/js_scope.asp)

9. Are variables passed by value or by reference?

Primitive variables are passed by value and non-primitive tyoes (objects) are passed by reference. This is demonstrated through these code snippets:

`var a = 5`
`var b = a`

`console.log(a) // returns 5`
`console.log(b) // returns 5`

`a = 1`

`console.log(a) // returns 1`
`console.log(b) // returns 5`

This demonstration of primitive type passed exemplifies that the value of a was passed to b in the second line, prompting the creation of a new spot in memory to hold the variable b and it's value (equal to the value of a). 

Now, let's look at what happens when passing non-primitive types:

`var a = [1, 2, 3];`
`var b = a;`

`console.log(a); //returns [ 1, 2, 3 ]`
`console.log(b); //returns [ 1, 2, 3 ]`

`b[1] = 10;`

`console.log(a); //returns [ 1, 10, 3 ]`
`console.log(b); //returns [ 1, 10, 3 ]`

This example demonstrates that the reference of a, which held the value of a, was passed into b on the seocnd line. This means that a and b occupy the same space in memeory and that anything done to a effects the other or vice versa.

10. If you run this code (or the equivalent) in your language, what is the output? What does that tell you about 
how the language handles assignments?

`char [] a = {'c','a','t'} char [] b = {'d','o','g'} a=b`

`b[1] = 'u'`

`print a print b`

*see the answer to discussion question #9*
