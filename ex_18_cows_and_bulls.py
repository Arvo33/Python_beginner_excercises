# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
# a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and
# tell the user at the end.
from random import sample
from textwrap import wrap
from typing import Tuple, List, Dict, Optional


def get_number(message: str = 'Insert number:') -> Optional[str]:
    while True:
        try:
            user_input = input(f'{message}\n')
            if user_input.lower() == 'exit':
                return None
            int(user_input)
            return user_input
        except ValueError:
            print('Invalid input. Please try again.')


def play_cows_and_bulls(digits: int = 4) -> None:
    print('Let\'s start "bulls and cows" game!\n(to end game type \'exit\')\n')
    secret_number = generate_number(digits)
    user_input = []
    tries = 0
    while list(secret_number) != user_input:
        tries += 1
        user_input = input_number(digits)
        if user_input is None:
            print(f'Game over. You tried {tries} times.')
            return None
        output = compare_numbers(secret_number, user_input)
        print(f'Bulls: {output["bulls"]} Cows: {output["cows"]}')
    print(f'Congratulations! You guessed the number. It took {tries} tries')


def generate_number(digits: int = 4) -> Tuple[int]:
    return tuple(sample(range(0, 9), digits))


def input_number(digits: int) -> Optional[List[int]]:
    while True:
        user_number = get_number(f'Insert {digits} digits number (without duplicates):')
        if user_number is None:
            return None
        user_number = [int(digit) for digit in wrap(str(user_number), 1)]
        if len(user_number) != digits:
            print(f'Number has to contain {digits} digits.')
            continue
        elif check_duplicates(user_number):
            print('Number contains duplicates. Try again.')
            continue
        return user_number


def check_duplicates(number: List[int]) -> bool:
    if len(number) != len(set(number)):
        return True
    return False


def compare_numbers(secret_number: Tuple[int], user_number: List[int]) -> Dict[str, int]:
    output = {'bulls': 0, 'cows': 0}
    position = 0
    for digit in user_number:
        if digit == secret_number[position]:
            output['bulls'] += 1
        elif digit in secret_number:
            output['cows'] += 1
        position += 1
    return output


if __name__ == '__main__':
    play_cows_and_bulls(4)
