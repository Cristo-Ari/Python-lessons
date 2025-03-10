import random
from colorama import Fore, Style, init

количество_чисел_в_конечном_масиве = 100
отклонение_от_нуля = 800

def сгенерировать_массив_чисел_в_отрезке(число_от, число_до, размер_массива):
    return [generate_non_zero_random(число_от, число_до) for _ in range(размер_массива)]

def generate_non_zero_random(min_value, max_value):
    случайное_число = 0
    while случайное_число == 0:
        случайное_число = random.randint(min_value, max_value)
    return случайное_число

def разделить_индексы_по_знакам(числовой_массив):
    индексы_положительных_чисел = []
    индексы_отрицательных_чисел = []
    
    for индекс, значение in enumerate(числовой_массив):
        if значение > 0:
            индексы_положительных_чисел.append(индекс)
        elif значение < 0:
            индексы_отрицательных_чисел.append(индекс)
    
    return индексы_положительных_чисел, индексы_отрицательных_чисел

import random

def получить_случайные_значения_из_массива(массив, количество_значений):
    количество_элементов = len(массив)
    
    if количество_значений > количество_элементов:
        raise ValueError("Количество запрашиваемых значений больше количества элементов в массиве")
    
    случайные_значения = random.sample(массив, количество_значений)
    return случайные_значения


def заполнить_случайными_числами_указанные_индексы(массив, массив_индексов, диапазон_от, диапазон_до):
    if диапазон_от > диапазон_до:
        raise ValueError("Начальный диапазон не может быть больше конечного диапазона.")
    
    for индекс in массив_индексов:
        if 0 <= индекс < len(массив):
            рандомное_целое_число = generate_non_zero_random(диапазон_от, диапазон_до)
            print(f"значение под индексом {индекс} заменяется на {рандомное_целое_число}")
            массив[индекс] = рандомное_целое_число
        else:
            raise IndexError(f"Индекс {индекс} выходит за пределы массива.")
    
    return массив

def выровнять_количество_положительных_и_отрицательных_чисел(массив):
    индексы_положительных_чисел, индексы_отрицательных_чисел = разделить_индексы_по_знакам(массив)
    
    количество_положительных_чисел = len(индексы_положительных_чисел)
    количество_отрицательных_чисел = len(индексы_отрицательных_чисел)

    превышение_положительных_чисел = (количество_положительных_чисел - количество_отрицательных_чисел)//2

    if превышение_положительных_чисел > 0:
        print(f"Количество положительных чисел больше на {abs(превышение_положительных_чисел)}")
        случайные_индексы_отрицательных_чисел = получить_случайные_значения_из_массива(индексы_положительных_чисел, превышение_положительных_чисел)
        return заполнить_случайными_числами_указанные_индексы(массив, случайные_индексы_отрицательных_чисел, -отклонение_от_нуля, 0)

    elif превышение_положительных_чисел < 0:
        print(f"Количество отрицательных чисел больше на {abs(превышение_положительных_чисел)}")
        случайные_индексы_отрицательных_чисел = получить_случайные_значения_из_массива(индексы_отрицательных_чисел, abs(превышение_положительных_чисел))
        return заполнить_случайными_числами_указанные_индексы(массив, случайные_индексы_отрицательных_чисел, 0, +отклонение_от_нуля)

    else:
        print("массив уже сбалансирован")
        return массив

def print_colored_array(array):
    for number in array:
        if number > 0:
            print(f"{Fore.GREEN}{number}{Style.RESET_ALL}", end=' ')
        elif number < 0:
            print(f"{Fore.RED}{number}{Style.RESET_ALL}", end=' ')
        else:
            print(f"{Fore.YELLOW}{number}{Style.RESET_ALL}", end=' ')
    print()

def отсортировать_отрицательные_значения_по_индексам(массив):
    индексы_положительных_чисел, индексы_отрицательных_чисел = разделить_индексы_по_знакам(массив)
    отрицательные_значения = [массив[индекс] for индекс in индексы_отрицательных_чисел]
    отрицательные_значения.sort()
    for индекс, значение in zip(индексы_отрицательных_чисел, отрицательные_значения):
        массив[индекс] = значение
    
    return массив


def сгенерировать_сбалансированный_массив():
    return выровнять_количество_положительных_и_отрицательных_чисел(
        сгенерировать_массив_чисел_в_отрезке(
            -отклонение_от_нуля,
            +отклонение_от_нуля,
            количество_чисел_в_конечном_масиве
        )
    )

массив = отсортировать_отрицательные_значения_по_индексам(сгенерировать_сбалансированный_массив())
print_colored_array(массив)
массив = выровнять_количество_положительных_и_отрицательных_чисел(массив)

print()
#print_colored_array(массив)

print_colored_array([sum(массив)])
