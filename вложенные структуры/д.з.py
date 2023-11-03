pascal_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1]

    ]
pascal_dict = {}
##k=0
##for line in pascal_triangle:
##     pascal_dict[k] = line
##     k +=1
#print( pascal_dict)    
for i in range(len(pascal_triangle)):
    pascal_dict[i] = pascal_triangle[i]
print( pascal_dict)   
