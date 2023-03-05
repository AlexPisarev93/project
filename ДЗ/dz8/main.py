import random
import json

from class_Q import Question


def get_data():
    """Функция чтения файла json"""
    with open("question.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    """Логика вопрос, ответ, вывод"""
    question_list: list[Question] = []
    for i in get_data():
        question_list.append(Question(i["q"], i["d"], i["a"]))
    random.shuffle(question_list)
    count = 0
    points = 0
    for i in question_list:
        print(f"\n{i.build_question()}")
        i.question = True
        user_answer = input("\nВаш ответ: ").lower().strip()
        i.answer_user = user_answer
        if i.is_correct():
            count += 1
            points += i.get_points()
            print(i.build_positive_feedback())
            i.get_points()
        else:
            print(i.build_negative_feedback())
    print(f"\nВот и все!"
          f"Отвечено {count} вопроса из {len(question_list)}\n"
          f"Набранно {points} баллов")





if __name__ == '__main__':
    main()