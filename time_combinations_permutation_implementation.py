#!/usr/bin/python3


"""
Given digits A, B, C, D, E, F, the following script returns the earliest
valid time combination that can be derived using the digits.

Permutation Implementation.
"""

from itertools import permutations
from functools import reduce


# Checks Whether time string formed in the format %H%M%S is valid
check_valid = lambda list_: [
    each
    for each in filter(
        lambda char_: True
        if int(char_[:2]) < 24
        and int(char_[2:4]) < 60
        and int(char_[4:6]) < 60
        else False,
        list_,
    )
]

# Checks and returns earliest time between two time strings in the format %H%M%S
check_earliest_between_two = (
    lambda x, y: x
    if int(x[:2] + x[2:4] + x[4:6]) < int(y[:2] + y[2:4] + y[4:6])
    else y
)


def solution(A, B, C, D, E, F):
    six_args = [A, B, C, D, E, F]
    # Gets all combinations of six digits possible.
    solution_combinations = [
        f"{each[0]}{each[1]}{each[2]}{each[3]}{each[4]}{each[5]}"
        for each in set(permutations(six_args, 6))
    ]

    # Gets all combinations possible of time in the format %H%M%S that are valid
    valid_combinations = check_valid(solution_combinations)

    # If results exist, get the earliest time and return it in the format %H:%M:%S.
    # If not return "NOT POSSIBLE"
    if len(valid_combinations) > 0:
        earliest_time = reduce(check_earliest_between_two, valid_combinations)
        return f"{earliest_time[:2]}:{earliest_time[2:4]}:{earliest_time[4:6]}"
    else:
        return "NOT POSSIBLE"


if __name__ == "__main__":
    # execute only if run as the entry point into the program

    print(solution(0, 0, 0, 8, 7, 9))
    print(solution(2, 4, 5, 8, 5, 8))
    print(solution(1, 4, 5, 8, 5, 8))
