##1、导入模块
import pymysql
##2、创建连接
conn = pymysql.connect(host='localhost',user='root',db='mystic',password='charm')
##3、创建游标
cur = conn.cursor()
##4、执行SQL操作
cur.execute("select * from t_user")
cur.execute("select version()")
data = cur.fetchall()
print(data)

##5、关闭游标
cur.close()
##6、关闭连接
conn.close()
