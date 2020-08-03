'''
Your task is to decrypt the secret message using the Morse code (#https://en.wikipedia.org/wiki/Morse_code).
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
'''

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code: str) -> str:
    list_words: list = []
    for word in code.split('  '):
        elements = ''
        for lettre in word.split():
            elements += MORSE[lettre]
        list_words.append(elements)
    result = ' '.join(list_words).capitalize()
    return result

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder("... --- -- .   - . -..- -"))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")