cmd = "left"

match cmd:
    case "top":
        print("вверх")
    case "left":
        print("Влево")
    case "right":
        print("вправо")

print("Проверка завершена")



cmd = 1

match cmd:
    case str() as command:
        print(f"строковая команда {command}")
    case bool() as command:
        print(f"булевая команда {command}")
    case int() as command:
        print(f"другая команда {command}")
    case _:
        print("другая команда")

print("Проверка завершена")
