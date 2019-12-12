import operator
def cmp1(a, b):
    return a[0]*a[1] - b[0]*b[1]
n = int(input())
a =[]
for i in range(n):
    x , y = map(int,input().strip().split())
    z = x*y
    a.append((x,y,z))
a.sort(key=operator.itemgetter(2))
print(a)