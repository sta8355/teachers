##tuple_1 = tuple()
##tuple_2 = tuple([1, 2, 3])
#print(type(tuple_2))
#tuple_1 =(1, 2, 3, 2) # создали кортеж
##elem_1= tuple_1[0]
##print(elem_1)
##a, b, c = tuple_1
##print(a, b, c)
#for i in tuple_1:
##    print(i)
##tuple_1 =(1, 2, 3, 2, 4)
##print(tuple_1.count(2))
##print(tuple_1.index(2))
##print(max(tuple_1))
#______________________
##tuple_1=(1, 2)
##tuple_2=(3, 4)
##tuple_3 = tuple_1 + tuple_2
##print(tuple_3)
#____________________
##def f (a, b, c):
##    print(a, b, c)
##
##tuple_1= (1, 2, 3)
##f(*tuple_1)
#______________________
##def f (a, b, c):
##    sum= a + b + c
##    raz = a - b - c
##    return sum, raz
##
##tuple_1= (1, 2, 3)
##rez= f(*tuple_1)
##print(type(rez))
##print(rez)

##users = {
##    ("Иван","Иванов"):"89051238908",
##    ("Петр","Петров"):"89081238908",
##    }
##print(users.get(("Иван","Иванов")))

tuple_1=([1, 2, 3], [4, 5, 6])
print(tuple(tuple_1))
tuple_1[0].append(4)#добавили
print(tuple_1)
tuple_1[0].remove(4)#удалили
print(tuple_1)
spis = tuple_1[0]
print(spis)
for i in range (10):
    spis.append(i)
print(spis)
print(tuple_1)
