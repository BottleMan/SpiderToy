# coding=utf-8

from BaseFunc import *

__author__ = 'Bottle'


print u"程序启动"

# 获取「文章列表」
print u"准备获取「文章列表」"
post_indexes = get_post_index(base_url, [])
print u"获取完成"

# 获取「每周 Tip」
for i in range(0, len(post_indexes)):
    title = post_indexes[i][0]
    url = post_indexes[i][1]

    print u"\n准备处理「" + title + u"」 (" + url + u")"

    if is_exist(title, url):
        print u"该文章已经存在,自动跳过"
        continue

    print u"准备获取数据"
    article = get_post(url)
    print u"获取完成"

    print u"准备持久化到数据库"
    do_insert(title, url, article)
    print u"持久化到数据库完成"

print u'\n全部完成'
