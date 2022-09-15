# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def find_mult(a, b, x):
    listt = [randint(a, b) for i in range(x)]
    lestt = []
    print(listt)
    if len(listt) % 2 == 1:
        for i in range(len(listt)//2+1):
            lestt.append(listt[i]*listt[x-1])
            x = x - 1
        return lestt
    else:
        for i in range(len(listt)//2):
            lestt.append(listt[i]*listt[x-1])
            x = x - 1
        return lestt


print(find_mult(1, 10, 6))
