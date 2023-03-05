
#функция декоратор
# т.е вставляет строку меджу строк, это нужно что бы не повторятся а просто вызывать функцию когда это нужно
def fanc_dekorator(fank):
    def wrapper():
        print("----Hello----")
        fank()
        print("----world----")

    return wrapper


def some_fank():
    print("----Alex----")


f = fanc_dekorator(some_fank)
f()