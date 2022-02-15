"""
FizzBuzz is a classic programming challenge.

For every number from 1 to n,
print Fizz if the number is divisible by 3,
print Buzz if the number is divisible by 5,
print FizzBuzz if the number is divisible by 3 and 5,
otherwise, print the original number otherwise
"""


# Simple test helper function
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Write a function that returns:
#  "Fizz" if the number is divisible by 3
#  "Buzz" if the number is divisible by 5
#  "FizzBuzz" if the number is divisible by 3 and 5
#  the number otherwise


# Todo: Test the function


# Todo: Request a number from the user

def FizzBuss(number):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number & 5 == 0:
        print("Buzz")
    else:
        print(number)

def game():
    number = int(input("Insert a number: "))
    FizzBuss(number)

game()

# Todo: Print a list of fizz-buzzed numbers from 1 to the given number

