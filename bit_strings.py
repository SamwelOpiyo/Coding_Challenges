# Binary String Expressions
# Problem: Given an input "bit pattern" which is a string containing only the characters '0', '1' and '?' output a list of all "bit strings" which match the pattern where '?' acts as a wild card. Output is flexible. It can be an array, a print out of each result to the console, etc.

# For example:
# "0"    -> ["0"]
# "1"    -> ["1"]
# "?"    -> ["0", "1"]
# "1?"   -> ["10", "11"]
# "?01?" -> ["0010", "0011", "1010", "1011"]


def get_bit_strings(bit_pattern):
    return_list = []
    for each in range(len(bit_pattern)):
        if bit_pattern[each] == "?":
            if len(return_list) > 0:
                new_list = [item + "0" for item in return_list] + [
                    item + "1" for item in return_list
                ]
                return_list = new_list
            else:
                return_list.append("0")
                return_list.append("1")
        else:
            if len(return_list) > 0:
                return_list = [
                    item + bit_pattern[each] for item in return_list
                ]
            else:
                return_list.append(bit_pattern[each])
    return return_list


print(get_bit_strings("0"))
print(get_bit_strings("1"))
print(get_bit_strings("?"))
print(get_bit_strings("1?"))
print(get_bit_strings("?01?"))
print(get_bit_strings("??1?"))
print(get_bit_strings("????"))
