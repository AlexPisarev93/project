class Maigic:
    """# вызывается всегда перед инициализатором, и запускается перед init"""
    def __new__(cls, *args, **kwargs):
        print("вызов __new__")
        return super().__new__(cls)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"{a}, {b}")

    def __del__(self):
        pass


maigic = Maigic(1, 2)