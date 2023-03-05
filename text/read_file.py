# file = open("read.txt", "rt") # rt = read text
# content = file.read() #метод вывода всего содержимого
# print(content)
# file.close()

with open("read.txt", "rt") as file:
    for line in file:
        print(line)