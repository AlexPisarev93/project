
# функция замыкания
def say_name(name):
    def sey_goodbay():
        print("Hello\n" + name + "\nand by")

    return sey_goodbay


closure = say_name("Alex")
closure()


# Счетчики Создание в одной функции 2 или более счетчика которые работают отдельно друг от друга.
def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter(1)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())


# удаление символов из любой строки
def strip_string(strip_char=" "):
    def do_strip(string):
        return string.strip(strip_char)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?/,.-")
print(strip1("Hello Python!..."))
print(strip2("Hello Python!..."))