"""Домашнее задание. Тема 4: генераторы."""


def hw_11(n):
    """Генератор простых чисел до n.

    Генератор выдаёт все простые числа, не превышающие n (по возрастанию).
    Для n < 2 не выдаёт ничего.

    Примеры:
        list(hw_11(10)) == [2, 3, 5, 7]
        list(hw_11(2)) == [2]
        list(hw_11(1)) == []
    """
    for number in range(2, n + 1):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


def hw_12(items, times):
    """«Прокручивание» последовательности.

    Генератор выдаёт элементы items по кругу times раз. Для times == 0
    или пустого items не выдаёт ничего.

    Примеры:
        list(hw_12([1, 2], 2)) == [1, 2, 1, 2]
        list(hw_12(["a"], 3)) == ["a", "a", "a"]
        list(hw_12([1, 2], 0)) == []
        list(hw_12([], 5)) == []
    """
    for _ in range(times):
        yield from items


def hw_13(items, size):
    """Разбиение на куски.

    Генератор выдаёт списки по size элементов; последний список может
    быть короче. Для пустого items не выдаёт ничего.

    Примеры:
        list(hw_13([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
        list(hw_13([1, 2], 5)) == [[1, 2]]
        list(hw_13([], 3)) == []
    """
    if size <= 0:
        raise ValueError("Размер должен быть положительным")
    for index in range(0, len(items), size):
        yield list(items[index:index + size])


def hw_14(items):
    """Соседние пары элементов.

    Генератор выдаёт кортежи соседних элементов: (items[0], items[1]),
    (items[1], items[2]), ... Для последовательности короче двух элементов
    не выдаёт ничего.

    Примеры:
        list(hw_14([1, 2, 3])) == [(1, 2), (2, 3)]
        list(hw_14(["a", "b"])) == [("a", "b")]
        list(hw_14([1])) == []
        list(hw_14([])) == []
    """
    for index in range(len(items) - 1):
        yield items[index], items[index + 1]
