i=1
def move(n,From,To):
    global i
    print("第{}个步骤:第{}个盘子{}----->{}".format(i,n,From,To))
    i+=1
    return ''
def han(n,From,Denpend_on,To):
    if n==1:
        move(1,From,To)
    else:
        han(n-1,From,To,Denpend_on)
        move(n,From,To)
        han(n-1,Denpend_on,From,To)
    return ''
n=eval(input("请输入汉诺塔的层数："))
a,b,c='A','B','C'
print(han(n,a,b,c,))
















