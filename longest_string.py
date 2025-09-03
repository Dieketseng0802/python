strings = ['mo', 'mojo', 'mojane', 'tshepos']

def longest_string(list_of_strings):
    longest_string = ''
    for string in list_of_strings:
        if len(string) > len(longest_string):
            longest_string = string
        elif len(string) == len(longest_string):
              print(f"{string} and {longest_string}longest_string are the longest words")
    return longest_string