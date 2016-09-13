def sum_string():
    number=raw_input("Input a string of numbers separated by spaces eg 1 2 3 4 5:")
    number_list=number.split()
    numbers=[]
    for r in number_list:
        numbers.append(int(r))
    return sum(numbers) 
print sum_string()

