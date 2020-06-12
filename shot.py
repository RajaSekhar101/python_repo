a=input("Enter Name: ").split(" ")
z=[]
for i in range(0,len(a)):
    s=a[i]
    if i==len(a)-1:
        b=s
    else:
        b=s[0]
    z.append(b)
for i in range(0,len(z)):
    print(z[i],".",end='')