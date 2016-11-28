text = raw_input("Enter a sentence: ")
list_text = text.split(' ')
print ' '.join(n[1:]+n[0]+'ay' if n[-1] not in ["!","?"] else n for n in list_text)
