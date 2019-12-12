a=['A','ABA','ABACABA']
def fj(n):
    if(n==0):
        return a[0]
    else:
        return str(a[n])=str(fj(n-1))+chr(ord('A')+n-1)+str(fj(n-1))
print(fj(3))


