# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым 
# билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# number = int(input("Введите шестизначное число : "))

number = int(385916)

half_length = len(number) // 2
first_half = number[:half_length]
second_half = number[half_length:]

first_half = number // 100
first_half = (number // 10) % 10
first_half = number % 10 
sum_first = digit1 + digit2 + digit3

first_half = number // 100
first_half = (number // 10) % 10
first_half = number % 10 
sum_second = digit1 + digit2 + digit3

while sum_first == second_half:
    print('Счастливый билет! ')
else:
    print('Билет не считается счастливым! ')