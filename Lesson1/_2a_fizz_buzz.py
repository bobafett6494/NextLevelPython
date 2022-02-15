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


def FizzBuzz(number):
    if number % 3 == 0 and number % 5 ==0: # if number % 15 ==0
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Todo: Test the function

assert_equals(FizzBuzz(1),1)
assert_equals(FizzBuzz(2),2)
assert_equals(FizzBuzz(3),"Fizz")
assert_equals(FizzBuzz(5),"Buzz")
assert_equals(FizzBuzz(6),"Fizz")
assert_equals(FizzBuzz(15),"FizzBuzz")

# Todo: Request a number from the user

number = int(input("Insert a number: "))

# Todo: Print a list of fizz-buzzed numbers from 1 to the given number

fizzbuzz_list = []

for n in range(number):
    fizzbuzz_list.append(FizzBuzz(n+1))

print(f'FizzBuzz List: {fizzbuzz_list}')