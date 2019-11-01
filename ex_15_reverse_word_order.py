# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
# the user the same string, except with the words in backwards order.


def reverse_sentence(sentence: str) -> str:
    return ' '.join(list(reversed(sentence.split())))


def reverse_sentence_2(sentence: str) -> str:
    return ' '.join(sentence.split()[::-1])


if __name__ == '__main__':
    my_sentence = 'My name is Ally.'
    print(reverse_sentence(my_sentence))
    print(reverse_sentence_2(my_sentence))
