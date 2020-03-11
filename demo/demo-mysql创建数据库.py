##1、导入模块
import pymysql
##2、创建连接
conn = pymysql.connect(host='localhost',user='root',db='mystic',password='charm')
##3、创建游标
cur = conn.cursor()
##4、执行SQL操作
cur.execute("drop table if exists books")
sql = """
create table books(
id int(8) not null auto_increment,
name varchar(50) not null,
category varchar(50) not null,
price decimal(10,2) default null,
publish_time date default null,
primary key(id)
)engine = myisam auto_increment = 1 default charset = utf8mb4;
"""

cur.execute(sql)
sql2 = "select * from information_schema.`TABLES` where TABLE_NAME='books'"
data = cur.execute(sql2)
print(data)                   
##5、关闭游标
cur.close()
##6、关闭连接
conn.close()
