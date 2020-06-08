def swaps(f,s):
    temp=s
    s=f
    f=temp
    print("After swaping numbers are ",f," and ",s)
f=int(input("Enter First Number: "))
s=int(input("Enter Second Number: "))
print("Before swaping numbers are ",f," and ",s)
swaps(f,s)