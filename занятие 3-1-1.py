
st=input('ввод строки: числа через пробел')
s=0
print(st)
sp=st.split()
print(sp)

for i in sp:
      s+=int(i)

print(s/len(sp))
