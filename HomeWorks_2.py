# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)
number = int(input("Введите трехзначное число: "))
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10 

sum_of_digits = digit1 + digit2 + digit3

print("Сумма цифр: ", sum_of_digits)

# # n = 123

# digit1 = n // 100
# digit2 = (n // 10) % 10
# digit3 = n % 10 

# res = digit1 + digit2 + digit3
# # print(res)