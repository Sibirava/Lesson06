import math
#
# math.ceil()
# math.floor()
# math.trunc()
# round  2м параметром можно указать количество знаков после  запятой
# int()

number = float(input("Input your number: "))

mathRound1 = (round(number + 0.5) if number > 0 else round(number - 0.5))
print(mathRound1)     #не оправдывает округления, косячит

mathRound2 = (int(number + 0.5) if number > 0 else int(number - 0.5))
print(mathRound2)



def real_math_round(number):
    return int(number + 0.5) if number > 0 else int(number - 0.5)



