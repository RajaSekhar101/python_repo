n=int(input("Enter Units: "))
if n<=150:
    e=3*n
    print("Electricity bill is ",e)
elif n>150 and n<=350:
    e=3.75*n
    print("Electricity bill is ",(100+e))
elif n>300 and n<=450:
    e=4*n
    print("Electricity bill is ",(250+e))
elif n>450 and n<=600:
    e=4.25*n
    print("Electricity bill is ",(300+e))
else:
    e=5*n
    print("Electricity bill is ",(400+e))