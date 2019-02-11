
# Due: February 6th at the beginning of class

# Eva Lynch

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print(s0 + "\n")

print (solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = "\\d"
if re.search(pattern, s0):
    print("It starts with 'T'!" + "\n")
else:
    print("My regex is incorrect, it should detect the 'T'!" + "\n")

print (solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words into a list.
#    Extract the first word into a variable and print it
pattern = ''
words = re.split(pattern, s0)
print (words)
print ("\n")
first_word = words[0]
print ("The first word is: '" + first_word + "'\n")

print (solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = ''
words = re.split(pattern, s0)
for word in words:
    print (word + "\n")


print (solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern = "Mary"
if re.search(pattern, s1):
    print("Mary is in sentence.")
else:
    print("Mary not found")
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern = "[0-9]{4}"
if re.search(pattern, s1):
    print("A 4 digit num is in sentence.")
else:
    print("4 digit number not found")
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
b_year = re.search(pattern, s1)
if b_year:
    print("The person was born in " + b_year.group())
else:
    print("No year found")

print (solution_separator)

# 5) okay so these aren't printing right but I know the patterns are right
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern = "dog\b"
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
matches = re.search(pattern, s2)
if matches:
    print("These are the matches: " + matches.group())
else:
    print("There are no matches")
# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
pattern = "dog/b"
matches = re.findall(pattern, s2, re.I)
if matches:
    print(str(matches.group()))
else:
    print("No match found")
# d) Write a regular expression to match "dog" or "fog"
pattern = "[f|d]{1}og\b"
# e) Print all outputs.
match = re.findall(pattern, s2)
if match:
    print("matches = " + str(match.group()))
else:
    print("no matches")

print (solution_separator)

# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern = "[0-9]{5}"
match = re.match(pattern, s3)
if match:
    print(match.group())
else:
    print("nope")
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
pattern = "\d*\b"
numbers = re.findall(pattern, s3)
for num in numbers:
    print (num + "\n")

print (solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
pattern = "\s{2}"
match = re.sub(pattern, "", s4)
print (match)

print (solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern = "begin.+end"
match = re.findall(pattern, s5)
if match:
    print(match[0])
else:
    print("error")
# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern = "begin\s\w+\s\w+\s\w+\send\b"
match = re.search(pattern, s5)
if match:
    print(match)
else:
    print("error")
# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
arr = []
pattern = r"begin\s(\w+\s(\w+\s){0,2})end"
matches = re.findall(pattern, s5)
for item in matches:
    match = item[0]
    arr.append(match)
# d) Print all outputs.
print(arr)

print (solution_separator)

# 9)
s6 = "The date 5/17/1982 is trickier to get"

# a) Write a regular expression to extract the date.
pattern = "\d\D\d{2}\D\d{4}"
match = re.search(pattern, s6)
# b) Capture the date in a variable f_date
f_date = match.group()

# c) Split the date and store it as month, day, year
a = re.split("/", f_date)
month = a[0]
day = a[1]
year = a[2]
print(month)
print(day)
print(year)
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
if int(month) < 10 and int(day) < 10:
    comp_date = year + "-0" + month + "-0" + day
elif int(month) < 10:
    comp_date = year + "-0" + month + "-" + day
elif int(day) < 10:
    comp_date = year + "-" + month + "-0" + day
else:
    comp_date = year + "-" + month + "-" + day
# e) Print comp_date
print(comp_date)

print (solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
# b) Use the code above to convert them into yyyy-mm-dd format.
# c) Print the dates in chronological order

print (solution_separator)
