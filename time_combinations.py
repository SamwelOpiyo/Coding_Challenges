"""
Given digits A, B, C, D, E, F, the following script returns the earliest
valid time combination that can be derived using the digits.
"""

from itertools import combinations
from functools import reduce


# Checks Whether time string formed in the format %H:%M:%S is valid
check_valid = lambda list_: [
    each
    for each in filter(
        lambda char_: True
        if int(char_[:2]) < 24
        and int(char_[3:5]) < 60
        and int(char_[6:8]) < 60
        else False,
        list_,
    )
]


# Checks whether all integers in list exist in string
def check_2(list_, string_):
    for each in set(list_):
        if list_.count(each) == string_.count(str(each)):
            pass
        else:
            return False
    return True


# Checks and returns earliest time between two time strings in the format %H:%M:%S
check_earliest_between_two = lambda x, y: x if int(
    x[:2] + x[3:5] + x[6:8]
) < int(
    y[:2] + y[3:5] + y[6:8]
) else y


def solution(A, B, C, D, E, F):
    six_args = [A, B, C, D, E, F]
    # Gets all combinations of two digits possible.
    combinations_2 = [
        f"{each[0]}{each[1]}" for each in combinations(six_args, 2)
    ]

    # Gets all combinations possible of time in the format %H:%M:%S that are valid
    valid_ = check_valid(
        [
            f"{each[0]}:{each[1]}:{each[2]}"
            for each in set(combinations(combinations_2, 3))
        ]
    )

    # Gets all combinations with all integers existing in string same number of times
    possible_from_combinations = [
        each for each in valid_ if check_2(six_args, each)
    ]

    # If results exist, get the earliest time and return it. If not return "NOT POSSIBLE"
    if len(possible_from_combinations) > 0:
        return reduce(check_earliest_between_two, possible_from_combinations)
    else:
        return "NOT POSSIBLE"


if __name__ == "__main__":
    # execute only if run as the entry point into the program

    print(solution(0, 0, 0, 8, 7, 9))
    print(solution(2, 4, 5, 8, 5, 8))
    print(solution(1, 4, 5, 8, 5, 8))
