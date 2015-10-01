# coding=utf-8

from BaseFunc import *

__author__ = 'Bottle'


print u"程序启动"


#print u"准备获取模板页…"
url = 'http://swifter.tips/'
the_page = get_page(url)
#print u"获取模板页完成…"

#print(the_page)


#latest_post = get_latest_post(the_page)

post_index = get_post_index(the_page)

exit()


print u"准备解析模板页…"
items = get_sub_url(the_page)
print u"解析模板页完成…"


print u"准备解析文件结构…"
tuples = []

for i in range(0, len(items)):
    tuples.append(get_tuple(items[i]))
else:
    print u'循环获取元组完成'
print u"解析文件结构完成…"


print u"Now, Let's Have Some Fun…"
desktop_path = get_desktop()
for i in range(0, len(tuples)):

    # 组建参数
    item_url = tuples[i][0]
    folder_name = tuples[i][1]
    file_name = tuples[i][2]

    print u"开始搞 - " + item_url

    # 新建文件夹
    mkpath = desktop_path + "\\SuFeiCode\\" + folder_name
    mkdir(mkpath)

    print u"准备获取文件内容…"
    # 获取文件内容
    the_page = get_page(item_url)
    file_content = get_file_content(the_page)
    print u"获取文件内容成功…"

    print u"准备写入文件内容…"
    print u"路径:" + mkpath + "\\" + file_name
    # 写入文件
    file_object = open(mkpath + "\\" + file_name, 'w')
    file_object.writelines(file_content)
    file_object.close()
    print u"写入文件内容成功…"
    print u"搞定一个\n"

else:
    print u'全部搞定'

make_some_shit()

print u'按回车退出'
raw_input(' ')
