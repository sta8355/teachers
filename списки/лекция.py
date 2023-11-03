##my_list = []
##text = ' '
##text_list = list(text)
##print(my_list)
##print(text_list)
##b=4325
##my_list = [1, 2, 'tri',4, 5, True, b]
##print(my_list)
##n = my_list[6]
##print(n)
##my_list [0] = 5
##print(my_list)
##my_list [-1]= 3
##print(my_list)
my_list = [1, 2, 3, 4, 5, 3, 7, 8, 9]
##for i in my_list:
##    print(i, end = ' ')
##dlina = len(my_list)
##print(f'длина=: {dlina}')
##print(sum (my_list))
### среднее арифметическое
##print(sum(my_list)/dlina)
##print(max(my_list))
##print(min(my_list))
# добавление и вставка элементов в список
##my_list.append(11)
##print(my_list)
##my_list.insert(8,10)
##print(my_list)
### удаление элементов из списка
##my_list.remove(3)
##print(my_list)
### удалить элемент из списка по индексу
##del my_list [2]
##print (my_list)
### проверка наличия элемента в списке
##if 5 in my_list:
##    print ('yes')
##else: print ('no')
## объединение списков:
# вывод элементов списка на экран по одному:
##my_list = [1, 2, 3, 4, 5]
##for i in range(len(my_list)-1):
##    #print (f'{i} элемент списка = {my_list[i]}')
##    print (my_list [i], my_list[i+1])
#сортировка списка
my_list = [3, 1, 5, 23, 65, 11]
##my_list.sort() # метод sort() сортирует исходный список, а не создает новый
##print(my_list)
##my_list.sort(reverse = 1) # 1 или True сортировка в обратном порядке
##print(my_list)
##sort_list = sorted (my_list) # используется для создания нового отсортированного списка
##print(sort_list)
#развернем список
print(my_list)
my_list.reverse()
print(my_list)
