# Take two lists and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of
# Python using at least one list comprehension.

from random import randint, sample


def common_part(list1: list, list2: list):
    return list(set(list1) & set(list2))


def common_part_2(list1: list, list2: list):
    return list(set([x for x in list1 for y in list2 if x == y]))


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print(common_part(a, b))
    print(common_part_2(a, b))

    c = sample(range(1, 30), randint(1, 15))
    d = sample(range(1, 30), randint(1, 15))

    print()
    print(c)
    print(d)
    print(common_part_2(c, d))
