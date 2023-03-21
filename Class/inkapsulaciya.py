class Point:
    """сеттеры и геттеры
    _х - предупреждает програмиста о защищенности но ничего не предпринимает
    __х - режим приватности, можно использовать только внутри класса"""
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, x):
        """приватный метод"""
        return type(x) in (int, float)

    def set_coord(self, x, y):
        """setter"""
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Должно быть число")

    def get_coord(self):
        """getter"""
        return self.__y, self.__x


point = Point(10, 20)
point.set_coord(20, 30)
print(point.get_coord())
