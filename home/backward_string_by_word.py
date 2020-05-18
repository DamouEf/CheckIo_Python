'''
In a given string you should reverse every word, but the words should stay in their places.
Input: A string.
Output: A string.
Precondition: The line consists only from alphabetical symbols and spaces.
'''
def backward_string_by_word(text: str) -> str:
    return ' '.join([''.join(reversed(elem)) 
            for elem in text.split(' ')])

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('hello abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
