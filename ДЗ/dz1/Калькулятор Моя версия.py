what = input("Какое действие выполняем  +, -, *, / : ")
a = float( input( "Введи первое число: "))
b = float( input( "Введи второе число: "))

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " - str(c))
elif what == "*":
    c = a * b
    print("Result: " + str(c))
elif what == "/":
    c = a / b
    print("Result: " + str(c))
else:
    print("Что то пошло не так!!!")










