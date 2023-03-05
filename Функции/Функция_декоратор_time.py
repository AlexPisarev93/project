import time

# время работы той или иной функции в милисекундах
def test_time(fank):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = fank(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"время работы {dt} секунд")
        return res

    return wrapper


@test_time
def calculator(a, b):
    c = a + b
    print(c)


calculator(10, 12)