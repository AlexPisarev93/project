import random
print("\nПривет, сегодня мы потренируемся\nрасшифровывать азбуку Морзе.")
# бесконечный цикл, пока юзер не нажмет Enter
while True:
    user = input("\nНажмите Enter и начнем\n")
    if user in "":
        break


# список слов для зашифровки
words = ["sleep", "war", "snake", "board", "door"]
# ответы True False
answers = []
# нумерация слов
number_words = 1


def random_word():
    ''' функция рандомного слова из списка word '''
    word_list = random.choice(words)
    return word_list



def morse_encode(word):
    ''' функция зашифровки слова'''
    morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"}
    result = []
    for i in word:
        result.append(morse_code[i])
        word_result = " ".join(result)
        return word_result



# работа цикла до 5 слова включительно, и проверка юзера на правильность.
while number_words <= 5:
    word = random_word()
    print(f"Слово {number_words} - {morse_encode(word)}")
    number_words += 1
    user_answer = input().lower().strip()
    if user_answer == word:
        print(f"Ответили верно это - {word}\n")
        answers.append(True)

    else:
        print(f"Ответили неверно это - {word}\n")
        answers.append(False)


def print_statistics(answers):
    ''' функция подсчета результатов '''
    total_tasks = len(answers)
    total_true = 0
    total_false = 0
    print(f"Всего задач - {total_tasks}")
    for i in answers:
        if i == True:
            total_true += 1
        elif i == False:
            total_false += 1
    print(f"Верно отвечено - {total_true}\nНеверно отвечено - {total_false}")
    print(f"Это {round(total_true / total_tasks * 100)} процентов верно отвеченых слов")


print_statistics(answers)



















