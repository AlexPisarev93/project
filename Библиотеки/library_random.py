
# библиотека рандома
import random
print(random.randint(30, 100))

from  random import randint
print(randint(1, 20))

# перемешивает список рандомно
list = [1, 2, 3, 4, 5, 100]
random.shuffle(list)
print(list)

# случайно вытаскивает буквы из строки (переменная, сколько букв вытащить)
name = "AlexPidsrev"
items = random.sample(name, 2)
result = "".join(items)
print(result)