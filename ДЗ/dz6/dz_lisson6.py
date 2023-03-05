import random

while True:
    user = input("Введите ваше имя: \n")
    if user:
        break

# кол-во очков за правильный ответ
count_answers = 0


def word_reading():
    """ функция рандома букв в слове и ответы пользователя"""
    with open("words.txt", "r") as file:
        global count_answers
        count_answers = 0
        for word in file:
            random_word = random.sample(word, len(word))
            result = "".join(random_word).strip().replace("\n", "")
            user_input = input(f"\nУгадайте слово:\n {result}\n").lower()
            if user_input == "":
                print(f"Неверно! Верный ответ – {word}")
            elif user_input in word:
                print("Верно! Вы получаете 10 очков")
                count_answers += 10
            else:
                print(f"Неверно! Верный ответ – {word}")
        print(f"\n{user} - получил(а) {count_answers} очков")
        return count_answers


def adding_history():
    """функция добавления пользователя и его очков в history"""
    with open("history.txt", "a") as file:
        file.write(f"\n{user} {word_reading()}")


def counter_game():
    """функция кол-во игр"""
    with open("history.txt", "r") as file:
        count = 0
        for i in file:
            if str() in i:
                count += 1
        print(f"Всего игр сыграно: {count}")


def tpo_user():
    """функция максимальный рекорд"""
    with open("history.txt", "r") as file:
        my_list = []
        for i in file:
            result = "".join(i).split()
            integer = int(result[1])
            my_list.append(integer)
        print(f"Максимальный рекорд: {max(my_list)}")


adding_history()
counter_game()
tpo_user()
























































