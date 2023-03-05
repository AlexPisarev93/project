# рекурсивная функция вывод 1234554321
def recursion(value):
    print(value)
    if value < 5:
        recursion(value + 1)
    print(value)


recursion(1)

# вычисление факториала
def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


total = fact(10)
print(total)