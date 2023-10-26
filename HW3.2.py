"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
"""

list_1 = [1, 12, 6, 7, 8, 15]
k = 3


# Введите ваше решение ниже

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)


# for i in list_1:
#     if i >= max_list:
#         max_list = i
#         if k == i:
#             num = i
            
# if max_list < k:
#     print(max_list)
# else:
#     print(num)
