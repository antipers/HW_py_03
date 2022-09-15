# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint



def find_sum(a,b,x):
        listt = [randint(a, b) for i in range(x)]
        print(listt)
        sum = 0
        for i in range(len(listt)):
                if i % 2 != 0:
                        sum += listt[i]
        return sum


print(find_sum(1,10,5))