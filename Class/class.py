class Car:
    def __init__(self, name):
        self.wheels = 4
        self.doors = 4
        self.mirror = 2
        self.owner = name

    def turn_on(self):
        print("Заводим двигатель.")

    def turn_off(self):
        print("Заглушить двигатель")


subaru = Car("Alex")
print(subaru.owner)



# __repr__ __str__ для вывода в принт ПРОВЕРКА
class Bottle:
    def __init__(self, color, volume=0.0):
        self.color = color
        self.volume = volume

    def __repr__(self):
        return f"{self.color}, {self.volume}"


bottle = Bottle("Red", 0.7)
bottle_w = Bottle("White", 0.3)
bottle_b = Bottle("Black", 1.0)
print(bottle.__repr__())
print(bottle_b.__repr__())
print(bottle_w.__repr__())
