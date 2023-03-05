questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# кол-вл правильныйх ответов
correct_answer = 0
# кол-во баллов за один правильный ответ
points_answer = 0

user_ready = input("\nПривет! Предлагаю проверить свои знания Английского! \nНапиши 'ready', что бы начать: \n")
if user_ready.lower() == "ready":
  # цикл обращения к спискам по индексу
  for question in range(len(questions)):
    print("\n" + questions[question])

    # кол-во попыток
    attempt = 3
    # цикл пока не выполнено условие
    while attempt > 0:
      user_answer = input("Ответ: ")
      if user_answer == answers[question]:
        correct_answer += 1
        points_answer += attempt
        print(f"Ответ верный! {points_answer}: балла")
        # принудительное завершение цикла
        break

      else:
        attempt -= 1
        if attempt == 0:
          print(f"Неправильно. Правильный ответ: {answers[question]}")
          break
        print(f"Осталось попыток: {attempt}, попробуйте еще раз!")

  # переменная подсчета процентов
  percent = (correct_answer / len(questions)) * 100

  print(f"\nВот и все! Вы ответили на {correct_answer} вопросов из {len(questions)} верно, это {int(percent)} процентов.")
  print(f"И заработали {points_answer}: баллов")
else:
  print("Кажется, вы не хотите играть. Очень жаль.")






