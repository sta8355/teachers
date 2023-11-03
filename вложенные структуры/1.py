data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
#print(data[1])
#print(data[0][2])
##summa=0
##for line in data:
##    for elem in line:
##        #print(elem)
##        summa +=elem
##print(summa)        
##summa=0
##for line in data:
##     summa +=sum(line)
##print(summa) 
n=int(input('введите количество учеников'))
data = []
for i in range(n):
    line = input('введите имя балл1 балл2 балл3:').split()
    data.append(line)
pred_1 = 0
pred_2 = 0
pred_3 = 0
for line in data:
    summa = int(line[1])+int(line[2])+int(line[3])
    print(f'сумма баллов ученика {line[0]}:{summa}')
    pred_1 +=int(line[1])
    pred_2 +=int(line[2])
    pred_3 +=int(line[3])
print(f'средний балл по предмету 1:{pred_1/n}')
print(f'средний балл по предмету 2:{pred_2/n}')
print(f'средний балл по предмету 3:{pred_3/n}')
    
