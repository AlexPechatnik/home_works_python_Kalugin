"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
"""

list_1 = [1, 2, 3, 4, 5]
k = 2
max_list = 0
num = 0
# Введите ваше решение ниже
# Определяем самое большое значение числа в листе
for i in list_1:
    if i >= max_list:
        max_list = i
        if k == i:
            num = i
            
if max_list < k:
    print(max_list)
else:
    print(list_1[1])
