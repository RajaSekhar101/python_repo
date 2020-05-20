def jumpingOnClouds(c):
    jump_count=0
    i=0
    while i<len(c) :
        if c[i+2]==0:
            jump_count=jump_count+1
            i=i+2
        else:
            jump_count=jump_count+1
            i=i+1
    return jump_count
n=input().split(",")
c=list(map(int,n))
a=jumpingOnClouds(c)
print(a)