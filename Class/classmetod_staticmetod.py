class Vector:
    """Метод класса он обращается к атрибутам в классе
       а статик метод он работает независимо
       сам по себе
       класс метод
       можно обращаться для проверки к классу
       к атрибутам
       и делать разного рода проверки"""
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm(x, y):
        return x * x + y * y


v = Vector(10, 20)
print(Vector.norm(20, 40))


