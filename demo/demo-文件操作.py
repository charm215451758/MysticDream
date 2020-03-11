info0 ='操作文件演示'
print(info0)
print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('status.txt','r',encoding='utf-8') #自动创建文件
print("\n即将显示……\n")
print(file.read())
print(file.closed)
file.close()
print(file.closed)
file2 = open('picture.jpg','rb')
print(file2)


info1 ='为了防止遗忘关闭文件，可以使用with语句'
print(info1)
info2 ='模拟写入动态信息,模式要使用w'
print(info2)
with open('test.txt','w+',encoding='utf-8') as file4: #打开文件
    file4.write('您使用了一张加速卡，小鸟撸起袖子加油吃饲料了')
    file4.flush()
info3 = '追加信息演示，模式要改为a'
print(info3)
with open('test.txt','a',encoding='utf-8') as file4: #打开文件
    file4.write('\n您使用了一张加速卡，小鸟撸起袖子加油吃饲料了')
    file4.flush()

list1 = ["六指琴魔","倚天屠龙记","鹿鼎记","天山童姥"]

with open('test.txt','a',encoding='utf-8') as file4: #打开文件
##    file4.write(list1) #这个方法只允许写入字符串，不允许直接写list
    file4.writelines(list1) #这个方法就可以写入列表 但会将内容写到同一行
    file4.writelines([line + "\n" for line in list1]) #使用列表推导式
    file4.flush()

file5 = open('test.txt','r',encoding='utf-8')
print(file5.read())
print('判断文件是否已关闭',file4.closed)

#区别：file.read(size) 读取指定字符 只能r或r+模式 不能读取列表
#seek(size)方法是移动光标位置，utf-8一个中文占3个字符，dbk一个中文占两个
with open('test.txt','r',encoding='utf-8') as file4: #打开文件
    file4.seek(134)
    string =file4.read(20)
    file4.writelines
    print(string)
#逐行读取内容方法一
with open('test.txt','r',encoding='utf-8') as file4: #打开文件
    number = 0 #记录行号
    while True:
        number += 1
        line = file4.readline() #读取一行
        if "" == line:
            break #跳出循环
        print(number,line,end = "\n")
    print("\n","="*30,"结束","="*30,"\n")
#逐行读取内容方法二
#readlines()方法会将内容全部读取到一个列表中,即可以一起输出，也可以通过读取迭代对象的方式逐行
with open('test.txt','r',encoding = 'utf-8') as file6:
    strings = file6.readlines()
    for str in strings:
        print(str)
        



    

