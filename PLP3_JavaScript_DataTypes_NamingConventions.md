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

Note #3: Arrays in JavaScript can hold primitive data types, objects, methods, you name it. The elements do not have to match in type. Some examples: 
- `var array_name = [item1, item2, ...];`
- `var fruits = ["Banana", 5, "Apple", "Mango"];`
- `var cars = new Array("Saab", "Volvo", "BMW");`
- `var person = ["John", "Doe", 46];`
- `var person = {firstName:"John", lastName:"Doe", age:46};` (In this example, `person.firstName` returns John)
- `myArray[0] = Date.now;` 
- `myArray[1] = myFunction;`
- `myArray[2] = myCars;` where `myCars` is another array
