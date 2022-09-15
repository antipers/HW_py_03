# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def fuuunc():
    lestt = []
    for i in range(len(listt)):
        lestt.append(round(listt[i] - int(listt[i]), 2))
    print(f"преобразованный список выглядит следующим образом - {lestt}")
    maxx = max(lestt)
    minn = min(lestt)
    answer = maxx - minn
    return answer


listt = [1.1, 1.2, 3.1, 10.01]
print(f" инициальный список- {listt}")
print(fuuunc())
