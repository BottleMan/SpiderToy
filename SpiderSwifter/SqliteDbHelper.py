# coding=utf-8

import sqlite3

__author__ = 'Bottle'


con = sqlite3.connect('../Database/db.sqlite')


# 执行 SQL 语句
def sqlite_execute(sql, param):
    cu = con.cursor()
    cu.execute(sql, param)
    con.commit()


# 判断数据库中是否存在
def sqlite_is_exist(sql, param):
    cu = con.cursor()
    cu.execute(sql, param)
    rows = cu.fetchall()
    return len(rows) > 0

