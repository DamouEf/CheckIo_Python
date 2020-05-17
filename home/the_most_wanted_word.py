'''
You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.
'''
def most_wanted(text):
    total = 0
    lower = text.lower()
    most = lower[0]
    for i in lower:
        if i.isalpha():
            if lower.count(i) > total:
                most = i
                total = lower.count(i)
            elif lower.count(i) == total:
                if i < most:
                    most = i
                    total = lower.count(i)
    return most


if __name__ == '__main__':
    print("Example:")
    print(most_wanted("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_wanted("Hello World!") == "l", "Hello test"
    assert most_wanted("How do you do?") == "o", "O is most wanted"
    assert most_wanted("One") == "e", "All letter only once."
    assert most_wanted("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted("abe") == "a", "The First."
    print("Start the long test")
    assert most_wanted("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")