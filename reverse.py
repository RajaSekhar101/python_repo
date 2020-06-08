def con(f):
    sums=0
    if f<10:
        return f
    else:
        while f>0:
            rev=int(f%10)
            f=int(f/10)
            sums=(sums*10)+rev
    return sums
f=int(input("Enter Number:"))
print("Concate of two strings are: ",con(f))