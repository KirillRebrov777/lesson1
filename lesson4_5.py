# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
from operator import mul
from random import randrange

# формирование исходного списка
num = int(input('Введите необходимое количество элементов списка: '))
initial_list = [randrange(100, 1001, 2) for i in range(num)]

# проведение вычисления
result = reduce(mul, initial_list)

# вывод исходного списка и результата
print(initial_list)
print(result)