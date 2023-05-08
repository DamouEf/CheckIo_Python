"""
You are given a list of integers.
Your task in this mission is to find, how many times the sorting direction was changed in the given list.
If the elements are equal - the previous sorting direction remains the same,
if the sequence starts from the same elements - look for the next different to determine the sorting direction.

There are three sorting directions:

on the chunk 1, 2, 2 - up (increasing);
on the chunk 2, 1 - down (decreasing);
and on the chunk 1, 2, 2 - up again.
So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up.
That's the result your function should return.

Input: A list of integers.
Output: Integer.
"""

UP: str = "UP"
DOWN: str = "DOWN"


def changing_direction(elements: list[int]) -> int:
    
    previous: int = None
    current_direction: str = None
    previous_direction: str = None
    result: int = 0

    for index, elem in enumerate(elements):
        if index == 0 or previous == elem:
            previous = elem
            continue

        if elem < previous:
            current_direction = DOWN
        elif elem > previous:
            current_direction = UP
        previous = elem

        if previous_direction == None:
            previous_direction = current_direction
            continue

        if current_direction != previous_direction:
            result += 1
            previous_direction = current_direction
            continue

    return result

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
