a1 = 10
b2 = 20
matrix=[[1,2,3],[4,5,6],[7,8,9],[a1,[13,14,[15,16,'OK']],12, b2]]
search = 'OK'
for i in matrix:
    print('Level 1: ', i)
    if search in i:
        print('Win: ')
        break
    else:
        for vtoroy in i:
            print("Level 2: ", vtoroy)
            if search == vtoroy:
                print("Win: ")
                break
            else:
                if type(vtoroy) is list:
                    for tretiy in vtoroy:
                        print(tretiy)
                        if search == tretiy:
                            print("Win: ")
                            break
                        else:
                            if type(tretiy) is list:
                                for chetv in tretiy:
                                    print(chetv)
                                    if search == chetv:
                                        print("Win: ")
                                        break