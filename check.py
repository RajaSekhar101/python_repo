n=input("Enter Value: ")
a=ord(n)
if a>96 and a<123:
    print("You entered an alphabet.. ")
elif a>=48 and a<58:
    print("you entered a Number.. ")
else:
    print("You entered Whitespace.. ")