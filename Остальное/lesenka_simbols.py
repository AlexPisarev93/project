# Лесенка из чего либо
line = "13fet35kk54"
intenger = ""
streep = ""
for i in line:
    if i == str(i):
        intenger += i
        print(intenger)



# Звездочки или любые символы Х на Х
def print_square(x, y):

    for i in range(y):
        print("*" * x)


user_x = int(input())
user_y = int(input())

print_square(user_x, user_y)