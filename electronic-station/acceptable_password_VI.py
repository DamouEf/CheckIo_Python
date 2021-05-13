"""
In this mission you need to create a password verification function.
Those are the verification conditions:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10

Input: A string.
Output: A bool.
"""


def is_acceptable_password(password: str):
    # initial data
    is_digit: list = [char.isdigit() for char in password]
    length_password: int = len(password)

    # coditions
    bigger_than_6: bool = (length_password > 6)
    bigger_than_9: bool = (length_password > 9)
    digit_condition: bool = (any(is_digit) and not all(is_digit))
    contain_password: bool = ("PASSWORD" not in password.upper())
    contain_3_words: bool = (len({word.upper() for word in password}) >= 3)

    result: bool = ((bigger_than_6 and digit_condition) or (bigger_than_9)) and (contain_password and contain_3_words)
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('password12345'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
