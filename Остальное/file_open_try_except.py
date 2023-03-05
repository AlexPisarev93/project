import os

#File = r"C:\Users\Пользователь\Desktop\Python projects\Остальное\Файл.txt"   Это Абсолютный путь
File = os.path.join(r"Файлs.txt") # Это относительный путь

# with open(File, "r") as file:   # w-исправление а-добовление
#     f = file.read()
#     print(f)
#



try:
    with open(File, encoding="utf-8") as file:  # w-исправление а-добовление
        f = file.read()
        print(f)
except FileExistsError:
    print("Невозможно открыть файл")