'''
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
Input: Iterable
Output: Iterable
'''
from collections import Counter
def frequency_sort(items):
    # return sorted(items , key = lambda elem: (items.count(elem) , elem) , reverse = True)
    # return sorted(items, key = Counter(items).get , reverse= True , range(count))
    # return [n for n,count in Counter(items).most_common() for i in range(count)]
    # return sorted(items, key=lambda x: (counts[x], x), reverse=True if len(set(items))>2 else False) if items and len(items) != len(set(items)) else items
    return sorted(sorted(items, key=items.index), key=items.count , reverse=True)

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 2, 6,2, 6, 4, 4, 4]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
