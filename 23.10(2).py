string = input("Enter: ").split(" ")
numbers = []
for i in range(int(string[0]), int(string[1])):
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        if count > 2:
            break
        j += 1
    if count == 2:
        numbers.append(i)
print("Простые", numbers)
