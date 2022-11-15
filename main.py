from functions import *

score = 0
user_name = input("Введите Ваше имя: ")

# Открываем файл со словами для его вывода.
with open("words.txt", encoding="utf8") as words:
    for word in words:
        word = word[0:-1]
        format_word = iterate_letters(word)

        # Блок вывода вопроса и принятия ответа
        print(f"Угадайте слово: {format_word}")
        user_input = input()

        # Блок сравнения ответа
        if user_input.lower() == word:
            print("Верно! Вы получаете 10 баллов.")
            score += 10
        else:
            print(f"Неверно! Верный ответ {word}.")

# Открываем файл с историей для записи прошедшей игры.
with open("history.txt", "a", encoding="utf8") as historys:
    historys.write(f"{user_name} - {score}\n")

# Открываем файс с историей для анализа игр.
with open("history.txt", encoding="utf8") as historys:
    history_count = 0
    max_score = 0
    for history in historys:
        history_count += 1
        name, score = history.split(" - ")
        if max_score < int(score):
            max_score = int(score)

    print(f"Всего игр сыграно: {history_count}")
    print(f"Максимальный рекорд: {max_score}")
