f = open('data.txt', 'r+', encoding = 'UTF-8')
for i in range(100):
    print(i)
    f.write(str(i)+'\n')
f.close()
