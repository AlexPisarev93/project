import random


class Number:
    def __init__(self):
        self.number = 0
        self.is_free = True
        self.ran_num()
        self.is_fre()

    def ran_num(self):
        self.number = random.randint(1, 100)

    def is_fre(self):
        self.is_free = bool(random.randint(0, 1))

    def __repr__(self):
        return f"{self.number}, {self.is_free}"


number = Number()


def main():
    list_number = []
    for i in range(10):
        list_number.append(Number())
    for num in list_number:
        if num.is_free is True:
            print(num)


if __name__ == '__main__':
    main()









