"""
Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it - function should return False.
Input: A string.
Output: a boolean.
"""
from string import ascii_uppercase, digits
def is_all_upper(text: str) -> bool:
    
    # initial data
    all_digit: bool = (all([char.isdigit() for char in text]))
    if "".join(text.split()) == "":
        return False 
    allowed_chars = set(ascii_uppercase + digits +" ")
    return set(text).issubset(allowed_chars) and not(all_digit)

    # simple solution
    # if not text.strip() or text.isdecimal(): return False
    # return text == text.upper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('123UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('123UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    assert is_all_upper("     ") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
