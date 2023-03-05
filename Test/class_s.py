class Bottle:
    def __init__(self, color, *volume):
        self.color = color
        self.volume = volume

    def get_color(self):
        return self.color

    def get_volume(self):
        return self.volume

    def __repr__(self):
        return f"Цвет {self.color},кол-во {self.volume}"


class Shelve:
    def __init__(self):
        self.bottles: list = []

    def add_bottle(self, bottle):
        self.bottles.append(bottle)

    def get_number_of_bottles(self):
        return self.bottles

    def __repr__(self):
        return f"{len(self.bottles)}"


bottle = Bottle("red", 1, 2, 3)
bottle1 = Bottle("black", 1, 2, 10)
print(bottle, bottle1)
shelve = Shelve()
shelve.add_bottle(bottle1.volume)
print(shelve.get_number_of_bottles())


