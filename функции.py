s=input('строка')
s1='aAoOeEiIuU'

k=0
for i in range (len(s)):
    if s[i] in s1:
        k += 1
print(k)        
