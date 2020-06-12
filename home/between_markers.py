'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers.
But there are a few important conditions:
The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.
'''

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    # creative solution
    # b=text.index(begin)+len(begin) if begin in text else 0
    # e=text.index(end) if end in text else len(text)
    # return text[b:e]

    #clear solution
    start =  text.find(begin)
    finish =  text.find(end)
    

    if start!=-1 and finish!=-1:
        if start < finish:
            return text[start+len(begin):finish]
        else:
            return ''
    elif start!=-1 and finish == -1:
        return text[start+len(begin):]
    elif start == -1 and finish!=-1:
        return "No"
    elif not start and not finish:
        return text[:end]
    else:
        return text



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple qd', '>', '<'))
    between_markers('What is >apple qd', '>', '<')

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
