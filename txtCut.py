import jieba
excludes = {"06","2020","2019","所以","这个","10","我们","可以","很多","没有","比较",
            "就是","还是","里面","不过","时间","一个","但是","非常","真的","05","11","30","项目"
            ,"一定","小时","建议","感觉","如果","还有","园区","景点","进去","特别","景区","每个","其他","觉得"
            ,"地方","07","游玩","超级","主要","门口"
            }
txt = open("附件1/景区评论1.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "A01" or word == "A01#":
        rword = "A01山"
    elif word == "A02" or word == "A02#":
        rword = "东部A02"
    elif word == "A03" or word == "A03#":
        rword = "A03景区"
    elif word == "A04" or word == "A04#":
        rword = "A04景区"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))

