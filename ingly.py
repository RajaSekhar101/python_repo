a=input("Enter String:")
b="ing"
c="ly"
if len(a)<3:
    print("The modified String is ",a)
elif b in a:
    d=a+c
    print("The modified String is ",d)
else:
    d=a+b
    print("The modified String is ",d)