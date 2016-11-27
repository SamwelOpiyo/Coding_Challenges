num = int(raw_input("Enter a number: "))
print num > 1 and not any(num % n == 0 for n in range(2,num))
