def high_and_low():
    number=raw_input("Input a string of numbers separated by spaces eg 1 2 3 4 5:")
    number_list=number.split()
    numbers=[]
    for r in number_list:
        numbers.append(int(r))
    return "{0} {1}".format(max(numbers), min(numbers))
print high_and_low()
