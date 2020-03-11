# 导入模块
import sqlite3
# 创建连接对象
conn =sqlite3.connect("mystic.db")
##创建游标对象
cur = conn.cursor()
##执行SQL语句
cur.execute("create table user(id int(10) primary key,name varchar(50))")
##关闭游标
cur.close()
##关闭连接对象
conn.close()
