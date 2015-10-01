# -*- coding: utf-8 -*-

__author__ = 'Bottle'

import urllib2
import re

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


# 获取文件目录树
def get_sub_url(_the_page):
    tree_file = re.findall("<ul id=\"browser\" class=\"filetree\">[\s\S]*</ul>", _the_page)
    return re.findall("<a href=\"(.*?)\">.*?</a>", ''.join(tree_file))


# 获取文件内容
def get_file_content(_the_page):
    return re.findall("<textarea.*id=\"rightcp_txtCode\".*>([\s\S]*)</textarea>", _the_page)[0]


# 获取文件结构元组
def get_tuple(item):
    (_foler_name, _file_name) = re.findall("&file=(.*?)/(.*)", item)[0]
    _url = "http://tool.sufeinet.com" + item

    return (_url, _foler_name, _file_name)


# 获取桌面路径
def get_desktop():
    import _winreg

    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, \
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
    return _winreg.QueryValueEx(key, "Desktop")[0]


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



print u"程序启动"
print u"准备获取模板页……"
url = 'http://tool.sufeinet.com/CodePreview/CodeView.aspx'
the_page = get_page(url)
print u"获取模板页完成……"

print u"准备解析模板页……"
items = get_sub_url(the_page)
print u"解析模板页完成……"

print u"准备解析文件结构……"
tuples = []

for i in range(0, len(items)):
    tuples.append(get_tuple(items[i]))
else:
    print u'循环获取元组完成'
print u"解析文件结构完成……"

print u"Now, Let's Have Some Fun……"
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

    print u"准备获取文件内容……"
    # 获取文件内容
    the_page = get_page(item_url)
    file_content = get_file_content(the_page)
    print u"获取文件内容成功……"

    print u"准备写入文件内容……"
    print u"路径:" + mkpath + "\\" + file_name
    # 写入文件
    file_object = open(mkpath + "\\" + file_name, 'w')
    file_object.writelines(file_content)
    file_object.close()
    print u"写入文件内容成功……"
    print u"搞定一个\n"

else:
    print u'全部搞定'

make_some_shit()

print u'按回车退出'
raw_input(' ')
