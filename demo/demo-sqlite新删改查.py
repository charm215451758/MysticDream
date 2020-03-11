# 导入模块
import sqlite3
# 创建连接对象
conn =sqlite3.connect("mystic.db")
##创建游标对象
cur = conn.cursor()
##执行SQL语句
##为避免sql注入，建议使用占位符?来操作
##cur.execute("insert into user(id,name) values(1,'黄葯师')")
##sql = "insert into user(id,name) values(?,?)"
##cur.execute(sql,(2,"欧阳峰"))

##批量插入数据时,使用executemany,数据可以用字典 但要是以元组作为元素的
##strIndex = (i for i in range(2,10))
##strName =["杨过","郭靖","洪七公","黄蓉","郭襄","一灯大师"]
##data ={key:value for key,value in tuple(zip(strIndex,strName))}
##print(data)
##data = {(3,'杨过'),(4,'郭靖')}
##sql = "insert into user(id,name) values(?,?)"
##cur.executemany(sql,data)

##更新和删除的语句不同而已，用法类似
##三种查询方式fetchone() fetchall() fetch
selectSql1 = "select * from user"
cur.execute(selectSql1)#需要先执行查询语句，才能用fetch()获取到结果
print(cur.fetchone())#获取一条的函数没有参数,如果已经取过了，只会再取剩余的数据
##print(cur.fetchmany(2))
print(cur.fetchall())

##关闭游标
cur.close()
##提交事务
conn.commit()#查询语句是不需要提交事务的
##关闭连接对象
conn.close()
