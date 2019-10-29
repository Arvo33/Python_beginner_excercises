from typing import List, Optional

from ex_11_check_primality_functions import get_number


def fibonacci_numbers(user_number: int) -> Optional[List[int]]:
    if user_number == 1:
        return None
    num1, num2 = 0, 1
    output_list = [0, 1]
    while len(output_list) < user_number:
        output_list.append(num1 + num2)
        num1, num2 = num2, num1 + num2
    return output_list


def fibonacci_numbers_recursively(user_number: int, num1=0, num2=1, output_list: list = None) -> Optional[List[int]]:
    if output_list is None:
        output_list = [0, 1]
    user_number -= 1
    if user_number == 0 or user_number == 1:
        return None
    output_list.append(num1 + num2)
    fibonacci_numbers_recursively(user_number, num2, num1 + num2, output_list)
    return output_list


if __name__ == '__main__':
    user_number = get_number('How many Fibonacci numbers would you like to generate?')
    print(fibonacci_numbers(user_number))
    print(fibonacci_numbers_recursively(user_number))
