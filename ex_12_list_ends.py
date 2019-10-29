# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.


def list_ends(input_list: list) -> list:
    if len(input_list) > 1:
        return [input_list[0], input_list[-1]]
    return input_list


if __name__ == '__main__':
    input_list = [5, 10, 15, 20, 25]
    print(list_ends(input_list))
