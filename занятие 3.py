
st=input('ввод строки: числа через пробел')
s=0
print(st)
sp=st.split()
print(sp)
st1=''.join(sp)
print(st1)
for i in range(len(st1)):
      s+=int(st1[i])

print(s/len(st1))
