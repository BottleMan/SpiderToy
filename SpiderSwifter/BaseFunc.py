# coding=utf-8

import urllib2
import re
from pyquery import PyQuery as pq

__author__ = 'Bottle'

base_url = "http://swifter.tips/"


# 获取模板页
def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    req = urllib2.Request(
        url=url,
        headers=headers
    )

    response = urllib2.urlopen(req)
    return response.read()


# 获取「本周 Tip」
def get_latest_post(_the_page):

    print u"获取「本周 Tip」"

    v_source = pq(_the_page)
    latest_post = v_source.find("#latest-post").text()

    print(latest_post)
    print u"「本周 Tip」 获取完成"

    return latest_post


# 获取「文章列表」
def get_post_index(_url, _pre_arr):
    v_source = pq(url=_url)

    # 向后翻页
    older_post_a = v_source.find(".post-navigation .older-posts")
    if len(older_post_a) > 0:
        _pre_arr += get_post_index(base_url + older_post_a.eq(0).attr("href"), _pre_arr)

    # 获取本页文章列表
    post_indexes = v_source.find(".post-list a")
    curr_arr = []
    for i in post_indexes:
        post_index = post_indexes(i)
        title = post_index.find("h4").text()
        url = post_index.attr("href")
        curr_arr.append((title, url))

    return curr_arr + _pre_arr


# 获取文件结构元组
def get_tuple(item):
    (_foler_name, _file_name) = re.findall("&file=(.*?)/(.*)", item)[0]
    _url = "http://tool.sufeinet.com" + item

    return (_url, _foler_name, _file_name)


# 获取桌面路径
def get_desktop():
    import os

    return os.path.expanduser(r"~/Desktop/")

# 创建本地目录
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path + u' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + u' 目录已存在'
        return False


# 做一些装逼的事
def make_some_shit():
    import time

    print '    ______  __   ____  ____  ______________    ______'
    time.sleep(0.5)
    print '   / __ ) \/ /  / __ )/ __ \/_  __/_  __/ /   / ____/'
    time.sleep(0.5)
    print '  / __  |\  /  / __  / / / / / /   / / / /   / __/   '
    time.sleep(0.5)
    print ' / /_/ / / /  / /_/ / /_/ / / /   / / / /___/ /___   '
    time.sleep(0.5)
    print '/_____/ /_/  /_____/\____/ /_/   /_/ /_____/_____/   '
    time.sleep(0.5)
    print '                                                     '
    print '   ___   ____ _________  ____  ______  ___   ____ '
    time.sleep(0.5)
    print '  |__ \ / __ <  / ____/ / __ \/ ____/ |__ \ ( __ )'
    time.sleep(0.5)
    print '  __/ // / / / /___ \  / / / /___ \   __/ // __  |'
    time.sleep(0.5)
    print ' / __// /_/ / /___/ /_/ /_/ /___/ /_ / __// /_/ / '
    time.sleep(0.5)
    print '/____/\____/_/_____/(_)____/_____/(_)____/\____/  '
    time.sleep(0.5)
    print '                                                  '
