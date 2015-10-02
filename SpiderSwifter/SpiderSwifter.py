# coding=utf-8

from BaseFunc import *

__author__ = 'Bottle'


print u"程序启动"

articles = []

# 获取「文章列表」
print u"准备获取「文章列表」"
post_indexes = get_post_index(base_url, [])
print u"获取完成"

# 获取「每周 Tip」
for i in range(0, len(post_indexes)):
    print u"准备获取「" + post_indexes[i][0] + u"(" + post_indexes[i][1] + u")」内容"
    article = get_post(post_indexes[i][1])
    articles.append((post_indexes[i][1], article))
    print u"获取完成"

make_some_shit()

print u'按回车退出'
raw_input(' ')
