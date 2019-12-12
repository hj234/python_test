import math
for i in range(10001):
    m=int (math.sqrt(i+100))
    n=int (math.sqrt(i+268))
    if(m*m==(i+100) and n*n==(i+268)):
        print(i)
        break
