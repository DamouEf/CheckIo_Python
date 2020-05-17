'''
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer.
Precondition: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''
def checkio(array: list) -> int:
    # simple solution 
    # if not len(array):
    #     return 0
    # multiple = array[-1]
    # result = 0
    # for index , elem in enumerate(array, start=0):
    #     if index%2 == 1:
    #         continue
    #     result += int(elem)
    # return result * multiple
    
    return array[-1] * reduce(lambda el, next_el: el + next_el, [el for i, el in enumerate(array) if i % 2 == 0]) if len(array) > 0 else 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0