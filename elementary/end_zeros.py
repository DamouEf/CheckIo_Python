'''
Try to find out how many zeros a given number has at the end.
Input: A positive Int
Output: An Int. 
'''


def end_zeros(num: int) -> int:
    # count how many zero in the end
    count: int = 0
    for index in range(len(str(num))-1 , -1, -1):
        if str(num)[index] == '0':
            count+=1
            continue
        return count
    return count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
