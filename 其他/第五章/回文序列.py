s='love python language!'
a=''
# t=len(s)
# for i in range(t):
#     a+=s[-1]
#     s=s[0:len(s)-1]
# print(a)
def dog(m):
    if m=='':
        return m
    else:
        return m[-1]+dog(m[0:-1])
print(dog(s))
