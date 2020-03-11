def filterchar(string):
    ''' 功能:过滤危险字符 比如黑客，并将危险字符过滤后输出
        string:需要过滤的字符串
        没有返回值
    '''
    import re  #导入模块
    pattern = r'黑客|抓包|监听|Trojan' #需要过滤的字符串
    sub = re.sub(pattern,"@_@",string)
    print(sub)
#定义空函数
def empty():
    pass

#调用函数
about = "我是白帽子，不过我还是喜欢研究Trojan"
filterchar(about)
def function_tips():
    '''功能:每天输出一条励志文字
    '''
    import datetime
    mot = ["周一:早起的鸟儿有虫吃",
           "周二:少壮不努力，老大徒伤悲",
           "周三:不要等到明天再去追逐梦想，明天太遥远",
           "周四:目标即定，只需要努力，终会成功",
           "周五:做对的事情比把事情做对更重要",
           "周六:成功将属于那些从不说No的人",
           "周日:方法总比困难多"
        ]
    day = datetime.datetime.now().weekday()  #获取当前星期
    print(mot[day])
function_tips()
#演示值传递与引用传递的区别
def demo(obj):
    print("oldValue:",obj)
    obj += obj
#值传递调用
print("="*10,"值传递","="*10)
mot = "天下无不散之聚会" #不可变对象
print("函数调用前:",mot)
demo(mot)
print("函数调用后:",mot)

print("="*10,"引用传递","="*10)
#列表就是不可变对象
mot2 = ["周一:早起的鸟儿有虫吃",
           "周二:少壮不努力，老大徒伤悲",
           "周三:不要等到明天再去追逐梦想，明天太遥远",
           "周四:目标即定，只需要努力，终会成功",
           "周五:做对的事情比把事情做对更重要",
           "周六:成功将属于那些从不说No的人",
           "周日:方法总比困难多"
        ]
print("函数调用前:",mot2)
demo(mot2)
print("函数调用后:",mot2)
#如果设置参数默认值时，就必须按形参的顺序来写实参，有默认值的参数可以不填写，可以通过
#函数名.__defaults__来查看默认值的内容
#对于固定参数的函数来说，使用默认值和调用的时候指定参数名，能有效防止参数输入错误导致的意外
#如下示例 如果连续调用的话，就会有不符合需求的结果输出
def demo(obj=[]):  #定义函数并为参数设置默认值
    print("obj的值",obj)
    obj.append(1)
demo()
demo()
#两次调用结果不同，这是不理想的函数，在开发时不应该出现，应修改如下
def demo(obj=None):  #定义函数并为参数设置默认值
    if(None==obj):
        obj=[]
    print("obj的值",obj)
    obj.append(1)
demo()
demo()
#可变参数表示可以是0个，1-n个参数用星号标识，可以通过列表传入,列表可以是二维的
def coffee(*coffeeName):
    print("\n我喜欢的咖啡有:")
    for item in coffeeName:
        print(item) #输出咖啡名称
coffee("花果山")
coffee("卡布奇诺","蓝山")
listCoffee = ["蓝山","猫屎","黑"]
coffee(listCoffee)

def coffee2(*coffeeName):
    for list_name in coffeeName:
        for item in list_name:
            print("我喜欢的咖啡"+item[0]+"产自:"+item[1]) #输出咖啡名称

list2D = [["猫屎","美国"],["黑","越南"]]
coffee2(list2D)
#带两个**的可变参数，表示接收任意多个类似关键字参数一样的显式赋值的实际参数，并放到一个字典中
#如果是固定搭配的内容，使用字典传入也是可以的
def coffee3(**coffeeName):
    for key,value in coffeeName.items():
            print("我喜欢的咖啡"+key+"产自:"+value) #输出咖啡名称

coffee3(蓝山='美国',黑咖啡='越南')
dictCoff={'蓝山':'天火','黑咖啡':'地星'}
coffee3(**dictCoff)
#演示全局变量和局部变量
pinetree = "我是一棵松树" #全局变量(松树)
def fun_christmastree(): #定义一个函数
    '''功能：一个梦
       无返回值
    '''
    pinetree = "挂上彩灯，礼物，我变成了一颗圣诞树" #定义局部变量
    print(pinetree)

def fun_chrismasMan():#圣诞老人选上了这棵树当礼物
    '''功能：圣诞老人的魔法，让梦变成现实
    无返回值
    '''
    global pinetree
    pinetree = "挂上彩灯，礼物，我变成了一颗圣诞树"#通过global变更全局变量的值
    
#函数体外
print("下雪了")
print("="*15,"开始做梦","="*15)
fun_christmastree()
print("梦醒了")
print(pinetree)
print("圣诞老人感动了，使用魔法实现了这棵树的梦想")
fun_chrismasMan()
print(pinetree)

#匿名函数 lambda 演示
bookinfo = [('侠客行',22.50,120),('陆小凤-剑神一笑',22.30,190),('陆小凤-幽灵山庄',22.50,128),('陆小凤-银钩赌坊',25.50,120)]
print("打折中的武侠小说信息:",bookinfo)
bookinfo.sort(key = lambda x :(x[1]/x[2],x[0])) #指定排序规则 打折率=折后价/原价
print("排序后的武侠小说作息:",bookinfo)
