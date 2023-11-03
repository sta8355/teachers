tuple_1=(1, 2, 3, 4 5, 6, 7, 8, 9)
n=int(input('удалить число:'))
if n in tuple_1:
    ind =tuple_1.index(n)
    print( ind)      
    print(tuple_1[:ind]+tuple_1[ind+1:])
else:
    print('такого нет')
    print(tuple_1)
