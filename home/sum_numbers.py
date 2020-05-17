''' 
In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.

The text consists from numbers, spaces and english letters

Input: A string.

Output: An int.
'''


def sum_numbers(text):
    return sum([int(c) for c in text.split() if c.isdigit()])

if __name__ == '__main__':
    print(sum_numbers("my 1st number is 9 and 20nd numb3r is 7"))
