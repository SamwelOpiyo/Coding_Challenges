"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24].

If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

# create sublists without item at index(each) using x[:each] + x[each + 1:].
# find the product using reduce and product function, lambda a, b: a * b.

prod = lambda x: [
    reduce(lambda a, b: a * b, x[:each] + x[each + 1:]) for each in range(len(x))
]
