def calculator(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя!!!')
    return int(a) / int(b)


if __name__ == '__main__':
    print(calculator(2, 3))