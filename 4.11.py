print(" " *19,"_" *44)
i = 1
while i < 40:
    if i <=20:
        print(" " * 20 + "|",
          "*" * i, " " * (40 - i * 2), "*" * i, "|")
    else:
        print(" " * 20 + "|",
              "*" * (40 - i), " " * (i - 20) * 2), "*" * (40 - i), "|"
print(" " * 19, "-" * 36)



#     print(" " *20 + "|",
#           "*" * i if i <= 20 else "*" * (40 - i),
#           " ", * (40 - i) if i <=20 else " " * i,
#           "|")
#     i += 1
# print(" " *19,"-" *44)
