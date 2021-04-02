#coding=utf-8
#CalThreeKingdomsV2.py
import sys
import xlrd
import xlwt
import pprint
import openpyxl
import openpyxl.styles
from openpyxl.styles import Font,colors
import jieba

import jieba.analyse




def readExcel(path):
    workbook=xlrd.open_workbook(path)
    # workbook=openpyxl.load_workbook(path)
    # print(workbook.sheet_names())
    table=workbook.sheets()[0]
    return table


if __name__=='__main__':

    book1=readExcel("附件1/景区评论.xlsx")
    nrows=book1.nrows
    print(nrows)
    list1=[]
    for i in range(nrows-1):
        # print(book1.row_values(i)[0])
        # for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        #     txt = book1.row_values(i)[2].replace(ch, " ")  # 将文本中特殊字符替换为空格
        # item = txt.strip('\n\r').split('\t') #制表格切分
        # print item
        seg_list = jieba.cut(str(book1.row_values(i+1)[0]))
        print(1)
        print(seg_list)
        # tags = jieba.analyse.extract_tags(item[0]) #jieba分词
        # for t in tags:
        #     list1.append(t)
        # list1.append(book1.row_values(i)[2])
    #     统计不重复词汇

    # print(str(list1))
    print(list1)
    excludes = {"，","：","“","。","”","、","；"," ","！","？","　","\n"}

    words = jieba.lcut(str(list1))

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # for word in excludes:
    #     del counts[word]

    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(5):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


