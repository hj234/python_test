import operator
n = int(input())
x , y =map(int,input().strip().split())
a = []
mul = x
ans = 0
for i in range(n):
    x , y = map(int,input().strip().split())
    a.append((x,y,x*y))
a.sort(key=operator.itemgetter(2))
for i in range(n):
    ans = max(ans,mul//a[i][1])
    mul *= a[i][0]
print(ans)
