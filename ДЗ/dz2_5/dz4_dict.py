# словари
words_easy = {
    "family":"семья",
    "hand":"рука",
    "people":"люди",
    "evening":"вечер",
    "minute":"минута"}

words_medium = {
    "believe":"верить",
    "feel":"чувствовать",
    "make":"делать",
    "open":"открывать",
    "think":"думать"}

words_hard = {
    "rural":"деревенский",
    "fortune":"удача",
    "exercise":"упражнение",
    "suggest":"предлагать",
    "except":"кроме"}

levels = {
   0:"Нулевой",
   1:"Так себе",
   2:"Можно лучше",
   3:"Норм",
   4:"Хорошо",
   5:"Отлично"}

# правильные ответы
correct_answers = {}
# неправильные ответы
incorrect_answers = {}
# счетчик правильных ответов
guessed_words = 0

user = input("\nВведите один из уровней сложности (легкий, средний, сложный): \n").lower()

# блок для словаря words_easy
if user == "легкий":
   print("\nВыбран уровень сложности, мы предложим 5 слов, подберите перевод.")
   input("\nНажмите Enter.\n")
   words = words_easy
   for k, v in words.items():
       print(f"{k}, {len(v)}, начинается на {v[0]}")
       user_answer = input().lower()
       if user_answer == v:
           print(f"Верно {k} - это {v}\n")
           correct_answers = {**{k:True}, **correct_answers}
           guessed_words += 1

       elif user_answer != v:
           print(f"Неверно {k} - это {v}\n")
           incorrect_answers = {**{k:False}, **incorrect_answers}

   correct_answers = '\n'.join(correct_answers)
   incorrect_answers = '\n'.join(incorrect_answers)
   print(f"Правильно отвечены слова: \n{correct_answers} \n\nНеправильно отвечены слова: \n{incorrect_answers}")
   print(f"\nВаш ранг: {levels[guessed_words]}")

# блок для словаря words_medium
elif user == "средний":
    print("\nВыбран уровень сложности, мы предложим 5 слов, подберите перевод.")
    input("\nНажмите Enter.\n")
    words = words_medium
    for k, v in words.items():
        print(f"{k}, {len(v)}, начинается на {v[0]}")
        user_answer = input().lower()
        if user_answer == v:
            print(f"Верно {k} - это {v}\n")
            correct_answers = {**{k:True}, **correct_answers}
            guessed_words += 1

        elif user_answer != v:
            print(f"Неверно {k} - это {v}\n")
            incorrect_answers = {**{k:False}, **incorrect_answers}

    correct_answers = '\n'.join(correct_answers)
    incorrect_answers = '\n'.join(incorrect_answers)
    print(f"Правильно отвечены слова: \n{correct_answers} \n\nНеправильно отвечены слова: \n{incorrect_answers}")
    print(f"\nВаш ранг: {levels[guessed_words]}")

# блок для словаря words_hard
elif user == "сложный":
    print("\nВыбран уровень сложности, мы предложим 5 слов, подберите перевод.")
    input("\nНажмите Enter.\n")
    words = words_hard
    for k, v in words.items():
        print(f"{k}, {len(v)}, начинается на {v[0]}")
        user_answer = input().lower()
        if user_answer == v:
            print(f"Верно {k} - это {v}\n")
            correct_answers = {**{k:True}, **correct_answers}
            guessed_words += 1

        elif user_answer != v:
            print(f"Неверно {k} - это {v}\n")
            incorrect_answers = {**{k:False}, **incorrect_answers}

    correct_answers = '\n'.join(correct_answers)
    incorrect_answers = '\n'.join(incorrect_answers)
    print(f"Правильно отвечены слова: \n{correct_answers} \n\nНеправильно отвечены слова: \n{incorrect_answers}")
    print(f"\nВаш ранг: {levels[guessed_words]}")



else:
    print("Введите верное значение!")








