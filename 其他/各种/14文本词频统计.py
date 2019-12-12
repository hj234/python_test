import jieba
txt = open("test.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
f = open("a.txt","w+")
for i in range(100):
    word,count = items[i]
    f.write("{0:<10}{1:>5}\n".format(word,count))
    print("{0:<10}{1:>5}".format(word,count))
