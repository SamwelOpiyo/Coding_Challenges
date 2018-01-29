"""
Program to find the reverse of a string using recursion
"""

def reverse(word):
    # exit point of recursive function
    if word is "":
        return word
    else:
        # recursion
        return reverse(word[1:])+word[0]


# Take string input from the user
word = raw_input("Enter a word: ")
# Function Call
print reverse(word)

