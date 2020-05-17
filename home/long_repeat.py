'''
There are four substring missions that were born all in one day and you shouldn’t need more than one day to solve them.
All of these missions can be simply solved by brute force, but is it always the best way to go?
(you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
This mission is the first one of the series.
Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one, which makes it the answer.

Input: String.

Output: Int.
'''

def long_repeat(line):
    if line == "":
        return 0
    n = 0
    s = []
    for i in range(len(line)-1):
        if line[i]==line[i+1]:
           n+=1
           s.append(n)

        else:
            n=0
    if not s:
        return 1
    return max(s)+1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')