string = input("Enter: ").split(" ")
begin = int(string[0])
end = int(string[1])

'''result = ""
for i in range(begin, end + 1):
        result += str(i) + " "
print( result)'''

result = ""
j = end
for i in range(begin, end + 1):
    result += str(j) + " "
    j -= 1
print( result)
