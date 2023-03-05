from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    user_pk = input("Введите номер студент: \n")
    if user_pk.isdigit():
        student = get_student_by_pk(int(user_pk))
        if student:
            print(f'Студент {student["full_name"]}\nЗнает {", ".join(student["skills"])}')
            prof_title = input(f'Выберете специальность для оценки студента {student["full_name"]}: ').lower().strip()
            profession = get_profession_by_title(prof_title)
            if profession:
                fit = check_fitness(student, profession)
                print(f'Пригодность {fit["fit_percent"]}%\n'
                      f'{student["full_name"]} знает {", ".join(fit["has"])}...\n'
                      f'{student["full_name"]} не знает {", ".join(fit["lacks"])}')
            else:
                quit("Такой специальности нет")
        else:
            quit("Такого студента нет")
    else:
        quit("Вы ввели неккоректно номер студента")


if __name__ == '__main__':
    main()
