import json


def load_students():
    with open("students.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def load_professions():
    with open("professions.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_student_by_pk(pk):
    for student in load_students():
        if student['pk'] == pk:
            return student


def get_profession_by_title(title):
    for profession in load_professions():
        if profession['title'] == title:
            return profession


def check_fitness(student, profession):
    students_skill = set(student['skills'])
    profession_skill = set(profession['skills'])
    has = students_skill.intersection(profession_skill)
    lacks = profession_skill.difference(has)
    fit_percent = len(has) / len(profession_skill) * 100

    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": round(fit_percent)
    }


