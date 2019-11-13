# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns (
# then prints) an appropriate boolean. Extras: Use binary search.

from typing import List, Union

from ex_11_check_primality_functions import get_number


def check_element_on_list(user_list: List[Union[int, float]], number: Union[int, float]) -> bool:
    user_list.sort()
    return number in user_list


def check_element_on_list_binary_search(user_list: List[Union[int, float]], number: Union[int, float]) -> bool:
    new_list = sorted(user_list)

    while True:
        middle_index = len(new_list) // 2
        if new_list[middle_index] == number:
            return True
        elif len(new_list) == 1:
            return False
        elif number > new_list[middle_index]:
            new_list = new_list[middle_index:]
        else:
            new_list = new_list[:middle_index]


if __name__ == '__main__':
    user_list = [1, 5, 8, 13, 14, 17, 25, 35, 68, 128, 3]
    number = get_number()
    print(check_element_on_list(user_list, number))
    print(check_element_on_list_binary_search(user_list, number))
