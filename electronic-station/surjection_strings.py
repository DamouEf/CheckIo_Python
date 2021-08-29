"""
Maybe it's a cipher? Maybe, but we don’t know for sure.
Maybe you can call it "homomorphism" ? I wish I knew this word before.
You need to check that the 2 given strings are isometric.
This means that a character from one string can become a match for characters from another string.
One character from one string can correspond only to one character from another string.
Two or more characters of one string can correspond to one character of another string, but not vice versa.
"""

def isometric_strings(word_1: str, word_2: str):
    # initial data
    cipher_dict: dict = dict()

    if len(word_1) is not len(word_2):
        return False
    
    for a,b in zip(word_1,word_2):
        if a == b:
            continue
        if a not in cipher_dict.keys():
            cipher_dict[a] = b
        elif cipher_dict[a] != b:
            return False
    return True


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
