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

a = int(input("Число 1: "))
b = int(input("Число 2: "))
if a > b:
    print(str ("a"))
