from random import sample, randint
from string import ascii_letters, digits, punctuation

# import nltk
from nltk.corpus import words


def generate_password(strong: bool = True) -> str:
    if not strong:
        return ''.join(sample(words.words(), 2))
    return ''.join(sample(f'{ascii_letters}{digits}', randint(9, 12)) + sample(punctuation, randint(1, 3)))


def user_interface() -> None:
    user_input = input('\n(press \'y\' to generate password; press \'w\' for weak password; press \'e\' to exit ' \
                       'program)\n')
    if user_input == 'e':
        return None
    elif user_input == 'y':
        print(generate_password())
    elif user_input == 'w':
        print(generate_password(False))
    else:
        print('Inserted unapropriate value. Try again.')
    user_interface()


if __name__ == '__main__':
    # nltk.download('words')
    print('Do you want to generate password?')
    user_interface()
