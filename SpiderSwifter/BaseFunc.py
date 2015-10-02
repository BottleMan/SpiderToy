# coding=utf-8

import re
import HTMLParser
import time
from pyquery import PyQuery
from SqliteDbHelper import *

__author__ = 'Bottle'

base_url = "http://swifter.tips/"
base_insert_sql = "INSERT INTO Swifter (Title, Url, Content, PostDate, SyncDate, IsValid) VALUES (?,?,?,?,?,1)"
base_exist_sql = "SELECT * FROM Swifter WHERe Title=? AND Url=?"


# 获取「文章列表」
def get_post_index(_url, _pre_arr):
    v_source = PyQuery(url=_url)

    # 向后翻页
    older_post_a = v_source.find(".post-navigation .older-posts")
    if len(older_post_a) > 0:
        _pre_arr = get_post_index(base_url + older_post_a.eq(0).attr("href"), _pre_arr) + _pre_arr

    # 获取本页文章列表
    post_indexes = v_source.find(".post-list a")
    curr_arr = []
    for i in post_indexes:
        title = post_indexes(i).find("h4").text()
        url = post_indexes(i).attr("href")
        curr_arr.append((title, url))

    return curr_arr + _pre_arr


# 获取「每周 Tip」
def get_post(_url):
    v_source = PyQuery(url=(base_url+_url))
    paras = v_source.find(".post-content").children()
    article = ""
    for i in paras:
        para_html = paras(i).html(method='html')

        # 【0】替换 code
        if paras(i).is_("pre"):
            link = re.compile("<code.*?>([\s\S]*?)</code>")
            para_html = "```\n" + re.sub(link, r'\1', para_html) + "```"

        # 替换 inline code
        link = re.compile("<code>([\s\S]*?)</code>")
        para_html = re.sub(link, r'`\1`', para_html)

        # 替换 strong
        link = re.compile("<strong.*?>([\s\S]*?)</strong>")
        para_html = re.sub(link, r'**\1**', para_html)

        # 替换 a
        link = re.compile("<a.*? href=\"(.*?)\">([\s\S]*?)</a>")
        para_html = re.sub(link, r'[\2](\1)', para_html)

        # 替换 p
        link = re.compile("<p.*?>([\s\S]*?)</p>")
        para_html = re.sub(link, r'\1', para_html)

        # 替换 li
        link = re.compile("<li>([\s\S]*?)</li>")
        para_html = re.sub(link, r'* \1', para_html)

        # 替换 HTML 转义字符
        html_parser = HTMLParser.HTMLParser()
        para_html = html_parser.unescape(para_html)

        # 添加 blockquote
        if paras(i).is_("blockquote"):
            para_html = ">" + para_html

        # 添加到 article
        article += para_html + "\n\n"

    return article


# 执行插入新的数据
def do_insert(title, url, article):
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    param = (title, url, article, "", cur_time)
    sqlite_execute(base_insert_sql, param)


# 判断数据库中是否已经存在
def is_exist(title, url):
    param = (title, url)
    return sqlite_is_exist(base_exist_sql, param)

