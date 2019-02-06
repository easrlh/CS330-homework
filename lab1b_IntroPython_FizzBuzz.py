# Prints the numbers 1 through 100
# If the number is divisible by 3, print "Fizz" instead of the number
# If it is divisible by 5 print "Buzz"
# If the number is divisible by both, print "FizzBuzz"

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
