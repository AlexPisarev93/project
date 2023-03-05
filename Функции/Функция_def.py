def name_shark(name, old):
    text = f"""Меня зовут {name}, мне {old} лет"""
    print(text)


name_shark("Федор", 18)
name_shark("Max", 27)


#функция с инпутом тест
user1 = int(input())
user2 = int(input())

def calculator(a, b):
    if a == b:
        print("числа равны")
    elif a != b:
        print("числа разные")


calculator(user1, user2)


# * это оператор упаковки аргументов
def name_collegs(*names):
    print(names)


name_collegs("Vika", "Alex", "Sasha")


# функция глобал - обращается к глобальной переменной.
x = 50
def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
func()
print('Значение x составляет', x)


# функция нанлокал - обращается к глобальной переменной.
def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()

# функция с ключевыми аргументами.
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)


# функция с ключевыми аргументами со списком и словарем.
def total(a=29, *fio, **data):
    print("мне", a)

    for i in fio:
        print("fio", i)

    for k, v in data.items():
        print(k,v)


print(total(29, "Alex", "Pisarev", passport = 23432142))


# Если некоторые ключевые параметры должны быть доступны только по ключу, а не как
# позиционные аргументы, их можно объявить после параметра со звёздочкой
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
        count += extra_number
        print(count)

total(10, 1, 2, 3, extra_number=50)
#total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.


# вычисление среднего значения
def avg(items):
    count_i = 0
    for i in items:
        count_i = i + count_i
    print(round(count_i / len(items)))



avg([20, 1000, 999])