string = input("введите номер дня")

dayofweek = str(datetime.datetime.now().weekday())
if string == "1":
    print("понедельник")
elif string =="2":
    print("вторник")
elif string =="3":
    print("среда")
elif string == "4":
    print("четверг")
elif string =="5":
    print("пятница")
elif string =="6":
    print("суббота")
elif string =="7":
    print("воскресенье")

else:
    print("день не соотвецтвует")