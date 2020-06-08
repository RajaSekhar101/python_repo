import time
def sums(n):
    count=0
    start_t=time.time()
    for i in range(0,n):
        count=count+1
    end_t=time.time()
    return end_t
n=int(input("Enter Number:"))
print("Time taken to execute is: ",sums(n))