# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_fibo(number):
    fibo_numbers = []
    f1, f2 = 1, 1
    for i in range(number-1):
        fibo_numbers.append(f1)
        f1, f2 = f2, f1 + f2
    f1, f2 = 0, 1
    for i in range (number):
        fibo_numbers.insert(0, f1)
        f1, f2 = f2, f1 - f2
    return fibo_numbers

number = int(input('Введите нужное число: '))
print(get_fibo(number))