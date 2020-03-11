import re
str ="天上地下唯you独尊"
print(len(str.encode())) #什么参数都不带就是utf-8编码
print(len(str.encode("gbk"))) #计算gbk编码下的字符长度 参数可以是单引也可以是双引
#使用切片功能可以方便地对字符串进行截取 注意左含右不含，边界不一样
print(str[0:2])
print(str[:9])
print(str[2:])
#切片除了截取连续的内容还可以指定步长，跳着截取
print(str[0:6:2])
print(str[4::3])
#切片截取如果不存在是不会报错的，但使用索引值截取是会报错的，比如下面这样写
#print(str[20])
#字符串分割函数split()  系统自带的这个函数是只能指定单个分隔符的
str2 = " 天\n 地 一 片     苍 茫    "
print(str2.split()) #默认会将所有分隔符都包含
print(str2.split(" "))#以空格作为分隔符的写法
print(str2.split("\n"))#指定分隔符

#为了将如上字符串中的多个分隔符都指定为分隔符，就需要使用到re模块了 正则表达式
#re模块的split()函数可以使用多个分隔符对句子进行分割，其中不同的分隔符要用 “|” 隔开

print(re.split(r' ',str2))#用空格作为分隔符的写法
print(re.split(r'\n',str2)) #用\n作为分隔符的写法

#检测字符串 count() find() index()
str3 = "@笑傲江湖 @书剑恩仇录 @神雕侠侣 @侠客行 #倚天屠龙记 #碧血剑 #鸳鸯刀"
print(str3.count("@",8,16))  #对指定字符串计数
print(str3.find("@",8,16))   #返回首次出现指定字符串的所在位置
print(str3.find("&"))    #如果不存在会返回-1
#判断一个字符串是否存在推荐使用in语句，要查找出现的位置推荐使用find
print("@" in str3)
print("(" in str3)
#index()查找到的子字符串不存在时会抛出异常 没有Find方法友好
# index()和find()方法都有从右开始查找的类似方法rindex() rfind()
# startwith() 用来判断是否以某个字符开头 返回布尔值
# endwith() 用来判断是否以某个字符结尾 返回布尔值
print(str3.startswith("@"))  #如果是在ide中，可以省略print,但写在这里不行
print(str3.startswith("*"))
print(str3.endswith("#"))
print(str3.endswith("刀"))
#大小写转换upper()lower()与C#一样
#strip() lstrip()
str4 = " ***http://www.baidu.com \t \n\r**"
print(str4.strip())
print(str4.strip("*"))
print(str4.lstrip("*"))
print(str4.rstrip("*"))
#格式化字符串实例 方式一：%方式
template = '编号：%09d\t公司名称:%s \t 官网:http://www.%s.com' #定义模板
item1 =(7,"百度","baidu") #要转换的项 只能用元组，不能用列表
item2= (12,"网易","163")
print(template%item1)
print(template%item2)
#格式化字符串 方式二：format()
#说明:大于号>表示右对齐 比如显示为007
#     小于号<表示右对齐 比如显示为700
#     等于号不存在
#向上尖括号表示居然对齐,比如显示为070，如果是偶数位,则从n/2+1位置显示,比如0700
templateFormat1 ='编号：{:>8s}\t公司名称:{:s} \t 官网:http://www.{:s}.com'
templateFormat2 ='编号：{:0^8s}\t公司名称:{:s} \t 官网:http://www.{:s}.com'
context1=templateFormat1.format("7","百度","baidu")
context2=templateFormat2.format("7","百度","baidu")
print(context1)
print(context2)
print("货币形式:${:,.2f}美元".format(123+21341)) #以货币形式显示
print("{0:.1f}用科学计数法显示:{0:E}".format(120000.1)) #用科学计数法表示
print("{0:d}的十六进制是:{0:#x}".format(100)) #十六进制显示
print("天才是由{:.0%}的天分，加{:.0%}的努力".format(0.01,0.99))
#编码转换 encode()向二进制转换 decode()将二进制转换为字符串
byteGBK = str.encode('gbk')
print(byteGBK)
byteUTF8 = str.encode()
print(byteUTF8)
stringGBK=byteGBK.decode('gbk')
print(stringGBK)
stringUTF8=byteUTF8.decode()
#stringGB2312=byteUTF8.decode('gb2312')--不能解码
stringGB2312=byteGBK.decode('gb2312')
print(stringUTF8)
print(stringGB2312)

