# 6.1随机密码的生成
import random
k=0
while k<8:
    t=random.randint(ord('0'),ord('z')+1)
    if ord('0')<=t<=ord('9') or ord('A')<=t<=ord('Z') or ord('a')<=t<=ord('z'):
        k = k + 1
        print(chr(t), end='')






