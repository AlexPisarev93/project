name_user = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут: ")

print(f"Привет, {name_user}, начинаем тренировку!")

# кол-вл правильныйх ответов
response_counter = 0
# кол-во баллов
total_points = 0
# кол-во баллов за один правильный ответ
points_answer = 10


first_question = input("My name ___ Vova. ")
if first_question.lower() == "is":
  response_counter += 1
  total_points += 10
  print(f"Ответ верный!\nВы получаете {points_answer} баллов!")
else:
  print("Неправильно.\nПравильный ответ: is")

second_question = input("I ___ a coder. ")
if second_question.lower() == "am":
  response_counter += 1
  total_points += 10
  print(f"Ответ верный!\nВы получаете {points_answer} баллов!")
else:
  print("Неправильно.\nПравильный ответ: am")

third_question = input("I live ___ Moscow. ")
if third_question.lower() == "in":
  response_counter += 1
  total_points += 10
  print(f"Ответ верный!\nВы получаете {points_answer} баллов!")
else:
  print("Неправильно.\nПравильный ответ: in")

# процент правильных ответов
percent_responses = round(response_counter / 3 * 100)

print(f"""Вот и всё, {name_user}!
Вы ответили на {response_counter} вопросов из 3 верно.
Вы заработали {total_points} баллов.
Это {percent_responses} процентов.""")