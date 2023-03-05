from utils import load_random_word
from classes import Player


def main():
    """Логика и условие"""
    user_name = input("Ввведите имя игрока: \n")
    player = Player(user_name)
    basicword = load_random_word()
    print(f"Привет {user_name}.")
    print(f"Составьте {basicword.quantity_valid_words()} слов из слова: {basicword.current_word}")
    print(f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите (стоп)\n"
          f"Поехали, ваше первое слово?")
    count = 0
    while count < basicword.quantity_valid_words():
        user_result = input().lower().strip()
        if len(user_result) < 3:
            print("Это слово короткое.")
        elif user_result in ("стоп", "stop"):
            print("Игра окончена, статистика:")
            break
        elif player.check_used_words(user_result) is True:
            print("Было уже.")
        elif basicword.word_check(user_result) is False:
            print("Это неудачное слово.")
        else:
            player.add_word(user_result)
            count += 1
            print("Слово подходит.")

    print(f"Вы угадали {player.quantity_used_words()} слов!")


if __name__ == '__main__':
    main()

