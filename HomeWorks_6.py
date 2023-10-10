# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым 
# билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# number = input("Введите шестизначное число : ")

# half_length = len(number) // 2
# first_half = int(number[:half_length])
# second_half = int(number[half_length:])

# f_digit1 = first_half // 100
# f_digit2 = (first_half // 10) % 10
# f_digit3 = first_half % 10 
# sum_first = f_digit1 + f_digit2 + f_digit3

# s_digit1 = second_half // 100
# s_digit2 = (second_half // 10) % 10
# s_digit3 = second_half % 10 
# sum_second = s_digit1 + s_digit2 + s_digit3

# while sum_first == sum_second:
#     print('Счастливый билет! ')
#     print(f'{sum_first} - {sum_second}')
#     break
# else:
#     print('Билет не считается счастливым! ')
#     print(f'{sum_first} - {sum_second}')

# n = str(385916)

# # Введите ваше решение ниже


# half_length = len(n) // 2
# first_half = int(n[:half_length])
# second_half = int(n[half_length:])
# print(int(n[:half_length]))
# print(int(n[half_length:]))



# f_digit1 = first_half // 100
# f_digit2 = (first_half // 10) % 10
# f_digit3 = first_half % 10 
# sum_first = f_digit1 + f_digit2 + f_digit3

# s_digit1 = second_half // 100
# s_digit2 = (second_half // 10) % 10
# s_digit3 = second_half % 10 
# sum_second = s_digit1 + s_digit2 + s_digit3

# while sum_first == sum_second:
#     print('yes')
#     break
# else:
#     print('no')


n = 385916

# Введите ваше решение ниже



first_half = n // 1000
second_half = n % 1000

f_digit1 = first_half // 100
f_digit2 = (first_half // 10) % 10
f_digit3 = first_half % 10 
sum_first = f_digit1 + f_digit2 + f_digit3

s_digit1 = second_half // 100
s_digit2 = (second_half // 10) % 10
s_digit3 = second_half % 10 
sum_second = s_digit1 + s_digit2 + s_digit3

while sum_first == sum_second:
    print('yes')
    break
else:
    print('no')