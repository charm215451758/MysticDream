import os #导入模块
print(os.name) #判断系统名称,nt代表windows系统
print(os.linesep)#该系统下的默认换行符是什么？ windows是\r\n
print(os.sep)#该系统下的默认路径分隔符
print(os.getcwd())#获取当前目录
with open('test.txt','r',encoding='utf-8') as file: #使用相对路径来打开
    print(file.read())
print('演示打开当前目录下子文件夹的文件,路径分隔符应使用\\或者/，不要单独使用\，以避免与文件名构成转义，如果觉得写双斜杠麻烦，可以在文件路径前加r，即使用原义字符')
##with open('Tools\\demo\\beer.py','r',encoding='utf-8') as file2: #使用相对路径来打开
##    print(file2.read())
with open(r'Tools\demo\beer.py','r',encoding='utf-8') as file2: #使用相对路径来打开
    print(file2.read())
print("="*20,"分隔符","="*20)
print("绝对路径演示，通过abspath()获取，可以通过os.path.join()来拼接路径,注意拼接路径函数是不会判断路径是否真实存在，需要在拼接前自己判断，如果出现多个绝对路径，将以最后一次出现的为准，即从后往前拼）")
print(os.path.abspath(r"Tools\demo\beer.py"))
print(os.path.abspath('test.txt'))
print(os.path.join(r'd/python',r'test.txt'))#这就是一个不存在的路径
print("="*20,"分隔符","="*20)
print("演示如果判断路径是否存在,目录判断不区分大小写，path.exists")
print(os.path.exists(r"d/python"))
print(os.path.exists(r"d:\progra~1\python"))
print(os.pardir)
print("os.mkdir(path,mode=0o777) 在unix上后面的参数是无效的，一般不修改,创建前应该判断是否存在")
if not os.path.exists("D:\\Program Files\\demo"):
    print(os.mkdir("D:\\Program Files\\demo"))
else:
    print("该目录已经存在")
print("="*20,"分隔符","="*20)
print("创建一个递归函数来创建目录,为说明makedirs函数的功能，模拟写一个递归函数来达到相应的效果，实际使用中可以直接使用makedirs()函数")
def mkdir_mystic(path):
    if not os.path.isdir(path):  #判断路径是否为路径
        mkdir_mystic(os.path.split(path)[0])
    else:
        return
    os.mkdir(path) #创建目录
mkdir_mystic("D:\\Program Files\\demo\\test2020")
if not os.path.exists("D:\\Program Files\\demo\\test2019"):
    os.makedirs("D:\\Program Files\\demo\\test2019")
print("="*20,"分隔符","="*20)
print("删除目录使用os.rmdir，与创建相反，在删除前需要先判断一下目录是否存在，如果目录下存在文件，则会提示目录不为空")
if os.path.exists("D:\\Program Files\\demo\\test2019"):
    os.rmdir("D:\\Program Files\\demo\\test2019")
print("如果要删除存在文件的目录，则需要使用shutil.rmtree函数，但此操作需要非常谨慎")
import shutil
if os.path.exists("D:\\Program Files\\demo\\test2019"):
    shutil.rmtree("D:\\Program Files\\demo\\test2019")
print("="*20,"分隔符","="*20)
print("遍历目录")
path = r"D:\Program Files\python\Tools\demo"
for root,dirs,files in os.walk(path,True): #遍历目录
    for name in dirs:
        print("目录:",os.path.join(root,name)) #输出遍历到的目录
    for file in files:
        print("\t文件：",os.path.join(root,file))
print("删除文件演示")
pathNew = r"D:\Program Files\python\Tools\demo\testNew.txt"
with open(pathNew,'w+') as file8:
    file8.write("用来存放删除文件演示文件的内容")
if os.path.exists(pathNew):
    os.remove(pathNew)
else:
    print("textNew不存在")
print("重命名函数os.rename(源路径_含文件扩展名,新路径_含新文件扩展名,重命名前也要先判断源文件是否存在),也可以用这个函数来重命名目录，不过只能重命名最后一级")
print("os.stat(path)可以显示文件的基本信息，即文件属性里的详细信息，比如创建日期，大小等")
#格式化时间函数
def formatTime(longtime):
    '''将长的时间格式化为日常使用的时间格式
    '''
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))
#格式化文件大小函数
def formatByte(number):
    '''格式化文件大小的函数
    '''
    for(scale,label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
        if number >=scale:
            return "%.2f %s" %(number*1.0/scale,label)
        elif 1 == number:
            return "1字节"
        else: #小于1KB
            byte = "%.2f" %(number or 0)
    return (byte[:-3] if byte.endswith(".00") else byte) + "字节"  

fileinfo = os.stat(r"demo.py") #获取文件信息
print("文件完整路径：",os.path.abspath(r"demo.py")) #获取文件完整路径
print("索引号：",fileinfo.st_ino)
print("设备名：",fileinfo.st_dev)
print("文件大小：",formatByte(fileinfo.st_size))
print("最后一次访问时间：",formatTime(fileinfo.st_atime))
print("最后一次修改时间：",formatTime(fileinfo.st_mtime))
print("最后一次状态变化的时间：",formatTime(fileinfo.st_ctime))



