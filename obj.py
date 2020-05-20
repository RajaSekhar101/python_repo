print("Welcome to the Student Management Program")
class Student:  
    def __init__ (self, name, age, gender, favclass):  
        self.name   = name  
        self.age    = age  
        self.gender = gender  
        self.fac = favclass  
    def a(self):
        print("Name=",self.name,"Age=",self.age,"Gender=",self.gender,"Favorate num=",self.fac)
choice = int(input("Make a Choice: " ))
c=1
while (c>0):
    if (choice==1):  
        print("STUDENT")  
        namer =input("Enter Name: ")  
        ager = input("Enter Age: ")  
        sexer = input("Enter Sex: ")  
        faver = input("Enter Fav: ") 
        c=0
    elif(choice==2):
        print("TESTING LINE")
        c=0
    elif(choice==3):
        print("Exit")
        c=0
s = Student(namer, ager, sexer, faver)
b=Student("sai",30,"M",5)
c=Student("prema",29,"F",6)
a =[]
a.append(s)
a.append(b)
a.append(c)
for i in range(0,len(a)):
    a[i].a()