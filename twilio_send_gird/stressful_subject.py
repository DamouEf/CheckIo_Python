'''
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP,"
they just can't have any other letters interspersed between them.
Input: Subject line as a string.
Output: Boolean. 
'''

def is_stressful(subj: str) -> bool:
    if subj.isupper():
        return True
    if subj[-3:] in ['!!!']:
        return True
    for index , string in enumerate(subj.split()):
        if ''.join([word for index, word in enumerate(string) if (index is 0 or (word is not subj[index-1] and index is not 0)) and word.isalpha()]).lower() in ["help", "asap", "urgent"]:
            return True
    return False



if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
