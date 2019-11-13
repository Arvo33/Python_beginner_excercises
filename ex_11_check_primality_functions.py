# Ask the user for a number and determine whether the number is prime or not.


def get_number(message: str = 'Insert number:') -> int:
    while True:
        try:
            return int(input(f'{message}\n'))
        except ValueError:
            print('Invalid input. Please try again.')
            # get_number()


def is_prime(number: int) -> bool:
    if number <= 0:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    user_number = get_number()
    print(is_prime(user_number))
