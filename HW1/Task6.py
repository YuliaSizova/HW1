# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к.
# 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

num_ticket = int(input('Введите число:'))

num_ticket_half1 = num_ticket // 1000
sum_num_ticket_half1 = (num_ticket_half1//100) + \
    (num_ticket_half1//10) % 10+(num_ticket_half1 % 10)

num_ticket_half2 = num_ticket % 1000
sum_num_ticket_half2 = (num_ticket_half2//100) + \
    (num_ticket_half2//10) % 10+(num_ticket_half2 % 10)

if sum_num_ticket_half1 == sum_num_ticket_half2:
    print(f'{num_ticket}->Yes')
else:
    print(f'{num_ticket}->No')
