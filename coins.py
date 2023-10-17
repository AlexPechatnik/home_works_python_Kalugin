# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
# чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх
# , и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
# Пример использования На входе:

# for i in  range(len(coins)):

coins = [0, 1, 1, 0, 1, 1, 0, 0, 0]  
count = 0
count1 = 0

for i in coins:
    if i == 1:
        count += 1
count1 = len(coins) - count
if count > count1:
    print(count1)
else:
    print(count)