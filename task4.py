# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# V1.0

def bin(number):
    n = ""
    while number > 0:
        y = str(number % 2)
        n = y + n
        number = int(number / 2)
    return n

number = int(input("Введите желаемое число: "))
print(bin(number))


# V2.0
# number = int(input("Введите желаемое число: "))
# bi_number= bin(number)
# print(bi_number)
