def is_palindrome(word):
    reversed_str = str[::-1]
    if word == reversed_str:
        print(True)


is_palindrome("level")
is_palindrome("sagas")
is_palindrome("hero")
is_palindrome("drama")

# try:
#     assert is_palindrome("level") == True
#     assert is_palindrome("sagas") == True
#     assert is_palindrome("hero") == False
#     assert is_palindrome("drama") == False
#
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
#
# else:
#     print("Все хорошо, все работает")
