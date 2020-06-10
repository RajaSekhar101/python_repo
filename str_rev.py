a=input("Enter a String:")
n=len(a)
if n%4==0:
    b=a[::-1]
    print("Reversed String is ",b)
else:
    print("String length is not a multiple of 4 ")
    