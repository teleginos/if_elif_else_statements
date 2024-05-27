def comparison_of_numbers(number_1: int, number_2: int, number_3: int) -> int:
    """
    Сравнивает 3 числа и возвращает количество совпадающих чисел
    :param number_1: первое число
    :param number_2: второе число
    :param number_3: третье число
    :return: количество совпадающих чисел.
    """
    if number_1 == number_2 and number_3 == number_1:
        return 3
    elif number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
        return 2
    else:
        return 0


first: int = int(input('Введите первое число: '))
second: int = int(input('Введите второе число: '))
third: int = int(input('Введите третье число: '))

if __name__ == '__main__':
    print(comparison_of_numbers(first, second, third))
