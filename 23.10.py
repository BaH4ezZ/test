while True:
    chislo = int(input("Enter: "))
    if chislo == 7:
        print("Good Bye")
        break
    elif chislo > 0:
        print("Положительное")
    elif chislo < 0:
        print("Отрицательное")
    elif chislo == 0:
        print("НОЛЬ")

