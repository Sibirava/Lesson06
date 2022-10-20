# Найти модуль числа (всегда значение положительное ) умножить на -1
number = int(input("Input your number: "))

# Вариант 1
if numder < 0:
    number *= -1

# Варинат 2
number = number if number >= 0 else -number
print(number)

# Вариант 3
number = number * (1 if number>=0 else-1)
print(number)

number *= 1 if number >= 0 else -1
print(number)
