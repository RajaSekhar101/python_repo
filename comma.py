a=input("Enter String").split(",")
b=[]
for i in range(0,len(a)):
    b.append(ord(a[i]))
b.sort()
del a[:]
for i in range(0,len(b)):
    a.append(chr(b[i]))
print(a)