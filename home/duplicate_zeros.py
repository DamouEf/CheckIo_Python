"""
"Sometimes, zeros resemble very tasty donut.
And every time we finish a donut, we want another, and then another, and then another..."
You are given a list of integers. Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P) and return the result as any Iterable. Let's look on the example:
[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Input: A list of integers.
Output: A list on another Iterable (tuple, generator, iterator) of integers.
"""

from collections.abc import Iterable


def duplicate_zeros(donuts: list) -> Iterable:
    result: list = []
    for elem in donuts:
        if elem == 0:
            result.append(elem)
        result.append(elem)
    return result


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
