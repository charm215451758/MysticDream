#集合是不重复元素的集合
set1 ={"水瓶座","射手座","双鱼座","双子座"}
print(set1)
set2 ={"水瓶座","射手座","双鱼座","双子座","射手座"}
print(set2)
##集合是不能使用索引获取元素的，集合是无序的，元素位置是不定的
hands = {"杨过","黄药师","洪七公"}
sword = {"杨过","小龙女","公孙大娘"}
print("精通拳掌的侠客：",hands)
print("精通刀剑的侠客：",sword)       
##定义空集合 需要使用set()而不能使用｛｝,因为这代表着一个空字典
setEmpty = set()
print(type(setEmpty))
#可以通过set()函数将列表可以转换为集合，转换后将自动去重
listTest =['双子座', '射手座', '双鱼座', '水瓶座','水瓶座']
print(listTest)
setTest = set(listTest) #转换成集合
print(setTest)
listBack = list(setTest) #集合转换为列表
print(listBack)
##添加元素、删除元素
setTest.add("金牛座")
print(setTest)
setTest.remove("金牛座")
if "金牛座" in setTest:
    setTest.remove("金牛座")
##setTest.remove("金牛座") #移除一个不存在的元素时会报错，为保证代码正确，移除前要先判断
#pop()方法会随机移除一个元素
temp=setTest.pop()
print(setTest)
print(temp)
#清空集合 与删除集合是不同的
setTest.clear()
print(setTest)
del setTest
#实例 晚年改变修炼方向，精修剑法
hands.remove("黄药师")
sword.add("黄葯师")
print("晚年精通拳掌的侠客：",hands)
print("晚年精通刀剑的侠客：",sword)
#交集，并集，补集，差集演示
print("交集：既精通拳掌又精通刀剑的侠客：",hands&sword)
print("并集：成名的所有侠客：",hands|sword)
print("差集：只精通拳掌的侠客:",hands-sword)
print("对称差集：只精通单一武功的侠客:",hands^sword)

