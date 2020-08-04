'''
In this mission you need to create a password verification function.
Those are the verification conditions:
the length should be bigger than 6;
should contain at least one digit.
Input: A string.
Output: A bool.
'''

def is_acceptable_password(password: str) -> bool:
    return ((len(password) > 6) and (any(char.isdigit() for char in password)))

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")