'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
'''

import re
def checkio(words: str) -> bool:
    # simple solution 
    '''
    list_words =  words.split(' ')
    count = 0
    for elem in list_words:
        if any(char.isdigit() for char in elem):
            count = 0
            continue
        count+=1
        if count >= 3:
            return True
    return False'''
    return bool(re.search(r"(\b[a-zA-z]+\b\s){2,}\b[a-zA-Z]+\b", words))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
