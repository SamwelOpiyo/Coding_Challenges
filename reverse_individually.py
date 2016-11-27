user_input = raw_input("Enter a sentence: ")


def reverse(string):
    return ' '.join(s[::-1] for s in string.split(' '))
    
if type(user_input) == str:
    print reverse(user_input)
else:
    string = str(user_input)
    print reverse(string)
