
# Оператор return используется для возврата из функции, т.е. для прекращения её работы
# и выхода из неё. При этом можно также вернуть некоторое значение из функци
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


print(maximum(2, 3))


# return место пробела

def mymax(first, second):
  if first > second:
    return(first)
  return(second)


print(mymax(10, 100))
print(mymax(10, 10))
print(mymax(0, 1))


# проверка строки на букву
def has_rrr(word):
    if "р" in result:
        return True
    return False


word = input().lower()
result = has_rrr(word)
print(result)


# деление нацело — x//y , остаток от деления — x%y (перевод времени в секунды)
def get_min_sec(sec):
    result = {"min": value // 60, "sec": value % 60}

    return result


value = int(input())
result = get_min_sec(value)
print(result)

# формула вычесление площади круга
def get_square(radius):
    get_square = radius ** 2 * 3.14
    return get_square


radius = int(input())
square = get_square(radius)
print(square)