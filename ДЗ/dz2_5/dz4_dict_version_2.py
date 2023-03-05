
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
answers_correct = {}
# неправильные ответы
incorrect_answers = {}
# счетчик правильных ответов
guessed_words = 0

words = {"легкий":words_easy,
         "средний":words_medium,
         "сложный":words_hard}
while True:

    user = input("\nВведите один из уровней сложности (легкий, средний, сложный): \n").lower()
    if user in words:
        break
    else:
        print("Нет такого уровня:")



print("\nВыбран уровень сложности, мы предложим 5 слов, подберите перевод.")
input("\nНажмите Enter.\n")

# блок для словаря words
for k, v in words[user].items():
    print(f"{k}, {len(v)} букв, начинается на {v[0]}")
    user_answer = input().lower()

    if user_answer == v:
        print(f"Верно {k} - это {v}\n")
        answers_correct = {**{k: True}, **answers_correct}
        guessed_words += 1


    elif user_answer != v:
        print(f"Неверно {k} - это {v}\n")
        incorrect_answers = {**{k: False}, **incorrect_answers}


answers_correct = '\n'.join(answers_correct)
incorrect_answers = '\n'.join(incorrect_answers)
print(f"Правильно отвечены слова: \n{answers_correct} \n\nНеправильно отвечены слова: \n{incorrect_answers}")
print(f"\nВаш ранг: {levels[guessed_words]}")



































