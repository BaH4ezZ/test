'''# string = input().split(" ")
#
# if int(string[0]) == int(string[1]):
#     print("Числа равные", string[0])
# else:
#     if int(string[0]) > int(string[1]):
#         print("2 число: ", int(string[1]))
#         print("1 число: ", int(string[0]))
#     else:
#         print("2 число: ", int(string[0]))
#         print("1 число: ", int(string[1]))

string = input().split(" ")
numbers =[]
for i in string:
    numbers.append(int(i))
numbers.sort()

print(numbers)'''

'''a = int(input("Число 1: "))
b = int(input("Число 2: "))
if a > b:
    print(str("a"))
elif a < b:
    print(str("b"))
else:
    print("число неизвестно")'''


'''string = input("Введите число от 1 до 100: ")
print(string)
if 0 < int(string[0]) > 100:
    print("Введите число вне диапазона")
else:
    number = int(string)
    # print(number)
if number % 3 == 0 and number % 5 != 0:  # 17 / 5 -> 3.2, 18 / 3 -> 5.0
    print("Fizz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 15 == 0:
    print("FizzBuzz")
else:
    print("Число: ",number)
'''

'''string = input("Введите число и степерь: ").split(" ")
number = int(string[0])
stepen - int(string[1])

if 0 <= stepen <= 7:
    result = number ** stepen
    print("Результат: ", result)'''

string = input("ВВедите стоимость, с кого звоним, куда звоним: ").split(" ")
price = float(string[0])
# mtot = 0 #  с мтс на теле 0.2 m
# mtob = 1 # с мтс на билайн 0.3 b
# ttob = 2 # c теле на билайн 0.4 t
# mtom = 3 # мтс 0.1
# btob = 4 # билайн 0.1
# ttot = 5 # теле 0.1
if string[1] =="m" and string[2] =="t":
    result = price * 0.2
    print(result)
elif string[1] == "m" and string[2] == "b":
        result = price * 0.3
        print(result)
elif string[1] == "t" and string[2] == "b":
        result = price * 0.4
        print(result)
elif string[1] == "m" and string[2] == "m":
        result = price * 0.1
        print(result)
elif string[1] == "b" and string[2] == "b":
        result = price * 0.1
        print(result)
elif string[1] == "t" and string[2] == "t":
        result = price * 0.1
        print(result)


