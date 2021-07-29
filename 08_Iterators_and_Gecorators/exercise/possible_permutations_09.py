# 9.Possible permutations
import itertools


def all_permutations(sequence):
    if len(sequence) == 0:
        return []

    if len(sequence) == 1:
        return [sequence]

    permutations_list = []

    for i in range(len(sequence)):
        m = sequence[i]

        remLst = sequence[:i] + sequence[i + 1:]

        for p in all_permutations(remLst):
            permutations_list.append([m] + p)
    return permutations_list


def possible_permutations(sequence):
    permutations = all_permutations(sequence)
    # permutations = itertools.permutations(sequence)

    for p in permutations:
        yield p


[print(n) for n in possible_permutations([1, 2, 3])]
