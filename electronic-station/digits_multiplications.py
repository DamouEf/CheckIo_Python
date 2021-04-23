"""
You are given a positive integer. 
Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405.
The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.
Output: The product of the digits as an integer.
Precondition: 0 < number < 106
"""

from functools import reduce
def digits_multiplications(number: int) -> int:

    list_integer: list = (list("".join(str(number).split('0'))))
    result: int = int(reduce((lambda el, next_el: int(el)*int(next_el)) , list_integer))
    return result


if __name__ == '__main__':
    print('Example:')
    print(digits_multiplications(1000))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digits_multiplications(123405) == 120
    assert digits_multiplications(999) == 729
    assert digits_multiplications(1000) == 1
    assert digits_multiplications(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
