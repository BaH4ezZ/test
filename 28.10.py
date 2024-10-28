result = []
for i in range(100, 1000):
    s = str(i)
    num = []
    for j in s:
        num.append(j)
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
        if num[0] == num[1] and num[1] == num[2]:
            result.append(int(num[0] + num[1] + num[2]))
print(result)

s = input("Enter: ").split(" ")
numbers = []
for i in range(int(s[0]), int(s[1]) + 1):
    num = []
    for x in str(i):
        num.append(x)
    for j in range(10):
        if num.count(str(j)) == 2:
            numbers.append(i)
print(len(numbers))