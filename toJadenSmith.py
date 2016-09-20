def toJadenCase():
    string=raw_input("Enter a sentence to be capitalized:")
    # ...
    if string=="":
        return null
    else:
        return ' '.join([s[0].upper() + s[1:] for s in string.split(' ') if len(s)>0])
print toJadenCase()
