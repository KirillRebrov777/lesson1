# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    """ Возврщает сумму наибольших двух аргументов из трёх """
    list_of_args = [a, b, c]
    sum = max(list_of_args)
    list_of_args.remove(sum)  # удаляем наибольший элемент
    sum += max(list_of_args)  # добавляем следующий наибольший элемент
    return sum


# вызов функции
first = int(input('Введите первый аргумент: '))
second = int(input('Введите второй аргумент: '))
third = int(input('Введите третий аргумент: '))
print(my_func(first, second, third))