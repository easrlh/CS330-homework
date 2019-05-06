## CS330: Programming Language Project (PLP) Assignments 5 & 6: Functions, Parameters, and Scope ##
#### By Eva Lynch ####
[[Source]](https://www.w3schools.com/js/js_functions.asp)

Being able to write functions that can be called more than once and sent different information each time is a huge part 
of most programming languages. However, there are a lot of variations in how functions are declared, where they are placed, 
how they accept parameters and how the function output is returned. Plus, you have to watch out for issues with scope and 
naming: some languages (e.g. Java) keep variables visible only inside of their own functions, while others (e.g. Perl) will 
have everything visible globally unless you use the keyword 'my'. In order to find out how your language handles these issues, 
answer the following questions and write code for each one that demonstrates the answers:

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

A function can refer to and call itself. There are three ways for a function to refer to itself:
- the function's name
- arguments.callee
- an in-scope variable that refers to the function
For example, consider the following function definition:

`var foo = function bar() {
   // statements go here
};`

4. Can functions in your language accept multiple parameters? Can they be of different data types?

Yes, JavaScript functions can accept multiple parameters of any type desired. 
The types of paramteres are not statically typed, so whatever parameters get passed in at runtime will be accepted.

5. Can functions in your language return multiple values at the same time?



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

Engineers at Mozilla had this to say:
>Primitive parameters (such as a number) are passed to functions by value; the value is passed to the function, 
but if the function changes the value of the parameter, this change is not reflected globally or in the calling function.

>If you pass an object (i.e. a non-primitive value, such as Array or a user-defined object) as a parameter and the 
function changes the object's properties, that change is visible outside the function.
[(Source)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

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



9. Are variables passed by value or by reference? (Hint: write a function that alters its input, but doesn't return it. 
Pass it a variable, and see if the alteration is visible in main after you call the function)



10. If you run this code (or the equivalent) in your language, what is the output? What does that tell you about 
how the language handles assignments?

`char [] a = {'c','a','t'} char [] b = {'d','o','g'} a=b`

`b[1] = 'u'`

`print a print b`


Make your answers as clear as possible, and provide code that shows how you tested the questions and the results that you get.
