import random
s=[]
k=0
for m in range(10):
    k=0
    for i in range(1000):
        s=[]
        for j in range(23):
            z=random.randint(1,365)
            s.append(z)
        if len(s)==len(set(s)):
            k+=1
    print("{} ".format(k/1000),end="")



