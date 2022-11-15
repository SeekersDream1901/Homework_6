from random import shuffle


def iterate_letters(word):
    """
    Перебирает буквы в слове и добавляет буквы в список,
    перемешивает буквы в списке
    соединяет список в слово
    и возвращает слово перемешанным
    """
    format_word = []
    for letter in word:
        format_word.append(letter)
    shuffle(format_word)
    format_word = "".join(format_word)
    return format_word
