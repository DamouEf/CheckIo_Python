"""
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: A number as an integer.

Output: The answer as a string.
"""

# Your optional code here
# You can import some modules or create additional functions
DIVISION_3: str = 'Fizz'
DIVISION_5: str = 'Buzz'
DIVISION_3_5: str = 'Fizz Buzz'

def checkio(number: int) -> str:
    if (number%3 == 0 and number%5 == 0):
        return DIVISION_3_5
    if (number%3 == 0):
        return DIVISION_3
    if (number%5 == 0):
        return DIVISION_5
    return str(number)

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")