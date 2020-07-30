'''
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
'''

def date_time(time: str) -> str:
    #replace this for solution
    months = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }
    date_time = time.split()
    date = date_time[0]
    time = date_time[1]
    minutes_str = 'minutes'
    hours_str = 'hours'
    if int(time.split(':')[1]) == 1:
        minutes_str = 'minute'
    if int(time.split(':')[0]) == 1:
        hours_str = 'hour'
    result = f"{int(date.split('.')[0])} {months[int(date.split('.')[1])]} {int(date.split('.')[2])} year {int(time.split(':')[0])} {hours_str} {int(time.split(':')[1])} {minutes_str}"
    return result

if __name__ == '__main__':
    print("Example:")
    # print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute", "football"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
