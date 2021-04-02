import pandas as pd
import jieba.analyse


def sort_key(keylist):
    '''
    高频关键词排序
    :param keylist: 关键词列表
    :return:
    '''
    percentage_number = int(keylist.count()*percentage)
    keyword_string = keylist.to_string()
    res = jieba.analyse.extract_tags(keyword_string,
                                     percentage_number)
    print(percentage_number, res)
    return res


def write_excel(res_ls, sheet_name, writer):
    df = pd.DataFrame(res_ls)
    df.to_excel(writer, sheet_name)


def run(sheet_name, writer):
    tb = pd.read_excel("附件1/景区评论.xlsx", sheet_name)
    res_ls = {}
    length = 0
    for i in tb:
        res_ls[i] = sort_key(tb.get(i))
        if len(res_ls[i]) > length:
            length = len(res_ls[i])

    # 补齐队列，长度保持一致
    for i in res_ls:
        i_len = len(res_ls.get(i))
        if i_len < length:
            res_ls[i].extend([""] * (length - i_len))

    write_excel(res_ls, sheet_name, writer)


# 百分比
percentage = 0.15
writer = pd.ExcelWriter("附件1/景区评论.xlsx")
ls = [u"表一", u"表二", u"表三", u"表四", u"表五"]
for x in ls:
    run(x, writer)
writer.save()
