### Assignment 3: Data Types and Naming Conventions ###
#### By Eva Lynch ####

This assignment will be a guide to representing different types of data in JavaScript. We will cover naming conventions...

#### JavaScript Naming Coventions ####
Every language has it's own naming conventions, as in the way the language's community has agreed to write and format code written in that language, to improve code readability and ease of code maintenance. A language could have certain ways it prefers class names to be written, which could be different from how variables should be written and method names and so on. These style guidelines could also have rules for white space, indentation, and how to write comments. Some examples of different naming conventions are camel case (varName), using underscores (var_name), whether the first letter can be capitalized or if that's reserved for class names, if numbers and symbols can be used, and many more. 

Some examples of the different naming conventions for JavaScript are: 

Camel case for variables and functions, and they must start with a lower case letter
- int: `var count = 3;` and `var graduationYear = 2021;`
- string: `var firstName = "Eva";`
- floating-point number: `var price = 10.9;` and `var taxRate = 0.20;`
- boolean: `var complete = true;`
- array/list: `var values = ["Corgi", "Husky", "Poodle"];`
- hash/dictionary: `var h = new HashTable();`

#### Additional JavaScript Data Notes ####
Note #1: The data type of your variable is decided by how you code the right hand side of the statement, so the type can be changed simply like so: `var carName = "Volvo";` prints a string, Volvo. If later on in the program you code `carName = 5;` JavaScript will allow this and print the 5 as an integer.

Note #2: When performing math operators on ints and floats, the result follows widening conversion. This means that the resulting value will be a float and not a string. Example: `4 + 2.1` returns `6.1`.

Note #3: Arrays in JavaScript can hold primitive data types, objects, methods, you name it. The elements do not have to match in type. Some examples of array instantiation: 
- `var array_name = [item1, item2, ...];`
- `var fruits = ["Banana", 5, "Apple", "Mango"];`
- `var cars = new Array("Saab", "Volvo", "BMW");`
- `var person = ["John", "Doe", 46];`
- `var person = {firstName:"John", lastName:"Doe", age:46};` (In this example, `person.firstName` returns John)

Some examples of assignment to indexes of an array:

- `myArray[0] = Date.now;` 
- `myArray[1] = myFunction;`
- `myArray[2] = myCars;` where `myCars` is another array

### Extra Discussion Questions ###
1) Are the naming conventions for JS enforced by the compiler/interpreter, or are they just standards in the community? 

The naming conventions are not enforced by the interpretor. They are solely community standards.

2) Is JavaScript statically or dynamically typed?

JavaScript is dynamically typed, meaning that types can change at run time. To give a small description over static vs. dynamic typing from [here](https://www.quora.com/Is-JavaScript-a-dynamically-typed-or-statically-typed-language):  
>The idea of dynamic types is that makes code flexible, i.e. if you’ve got a function which returns a number, you don’t actually have to return a number, you can return anything you like.

>With static types, it’s felt that applying rules to what types can be used is a benefit. The idea being that if you’ve got a function which accepts an int, you don’t need to check if an int has been passed to it, as the compiler won’t let anything else happen."

\[[Some general tips on navigating JS types!](https://medium.com/@xiaoyunyang/javascript-is-a-loosely-typed-language-meaning-you-dont-have-to-specify-what-type-of-information-137408d54fc7)\]

4. If you put this line (or something similar) in a program and try to print x, what does it do? If it
doesn't compile, why? Is there something you can do to make it compile?
x = "5" + 6

5. Describe the limitations (or lack thereof) of your programming language as they relate to the coding portion of the assignment (adding ints and floats, storing different types in lists, etc). Are there other restrictions or pitfalls that the documentation mentions that you need to be aware of?

6. How do type conversions work in your language? Are the conversions narrowing or widening, and do they work by default or do they have to be declared by the programmer?
