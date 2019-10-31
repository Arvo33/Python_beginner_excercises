# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates
# Extras: Write two different functions to do this - one using a loop and constructing a list, and another using sets.


def remove_duplicates(input_list: list) -> list:
    return list(set(input_list))


def remove_duplicates_with_loop(input_list: list) -> list:
    output = []
    for element in input_list:
        if element not in output:
            output.append(element)
    return output


if __name__ == '__main__':
    list1 = [5, 8, 'apple', 'spam', 'apple', 8, 12]
    print(remove_duplicates(list1))
    print(remove_duplicates_with_loop(list1))
