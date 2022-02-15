"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""


# Helper method to test equality
def equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'

# Todo: Create a function that produces the factorial of a number

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)

# Todo: Test factorial function

equals(factorial(3), 6)
equals(factorial(2), 2)
equals(factorial(4), 24)

# Todo: Request a number from the user

number=int(input("Type in a number: "))
# Todo: Print a list of factorials from 0 to the given number

list_factorials=[]

for n in range(number):
    list_factorials.append(factorial(n))

print(f"Factorial list: {list_factorials}")
