# Как заменить условную конструкцию на условную операцию
# a < b
# a = int(input("Input a:"))
# b = int(input("Input b:"))

# max = b
# if a > b:
#     max = a
# else:
#     max = b
# print(max)

# conditional operation  тернарный тип операций (3 операнта)
# _ if _ else _ (услловно показана операция)
# max = a if a > b else b
# print(max)




#РЕФАКТОРИНГ!!!!!!
#conditional operation
def find_max(a, b):
    max = a if a > b else b
    return max

def user_input():
    a = int(input("Input a:"))
    b = int(input("Input b:"))
    return a,b #МОЖНО ВЕРНУТЬ НЕСКОЛЬКО ПЕРЕМЕННЫХ

def user_print(msg):
    print(msg)
    return


#full script
a, b = user_input()
max = find_max(a, b)
msg = f"max number is{max}"
# или #user_print(max)



#base program
# x = int(input("Input x:"))
# y = int(input("Input y:"))
# max = find_max(x, y)
# print(max)