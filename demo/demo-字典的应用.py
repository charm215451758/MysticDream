import random
#字典的创建方式二  方法一就是直接将对应的内容按格式手写到字典中
key = ["东邪","西毒","南帝","北丐","中神通"]
value = ["黄药师","欧阳锋","段智兴","洪七公","王重阳"]
zipTop5 = zip(key,value)  #转换为zip对象
print(zipTop5)
top5 = dict(zipTop5) #将zip转换为字典
print(top5)

#创建方法三 通过元组来创建字典 元组是圆括号 不可变的序列 注意是英文半角
#不过这样创建的字典是以整个元组作为键的，与上面不同
newKey = ("东邪","西狂","南僧","北侠","中顽童")
newValue = ["黄药师","杨过","一灯大师","郭靖","周伯通"]
newTop5 = {newKey:newValue}
print(newTop5)

#通过dict来创建字典
newTop3 = dict(六脉神剑="段誉",降龙无双="萧峰",天命逍遥="虚竹")
print(newTop3)

#通过字典推导式来创建字典
newWrongTop5 = {i:j for i,j in zip(key,newValue)}
print("错乱阴阳:")
print(newWrongTop5)


#创建值为空的字典
newTop5 = dict.fromkeys(newKey)
print(newTop5)

#删除字典与清空字典内容的区别：del为删除整个字典 dict.clear()只是清空内容
newTop5.clear()
print(newTop5)

##del newTop5
##print(newTop5) #这句就会报错，因为已经删除了这个字典 NameError: name 'newTop5' is not defined

#访问字典中的键和值 需要通过键来访问而不是索引
print(top5["东邪"])
#当没有把握时，可通过get方法来尝试访问,如果不存在就会返回None而不是报错,或者指定查不到的默认值
print(top5.get("东狂"))
print(top5.get("东狂","不存在此封号"))

#通过字典可以串联数据，达到类似关系数据库的效果 例如下面这个例子
ablity = ["弹指神通","蛤蟆功","一阳指","降龙十八掌","先天功"]
zipRealation = zip(value,ablity)
realation = dict(zipRealation)
print(realation)
print("五绝里面的东邪叫什么名字？他的绝技是什么？")
print("他叫："+top5.get("东邪")+"\n他的绝技是"+realation.get(top5.get("东邪")))

##字典遍历的方式
print(top5.items)
for item in top5.items():
    print(item)
for key,value in top5.items():
    print(key+"的名字是:"+value)
for key in top5.keys():
    print(key)
for value in top5.values():
    print(value)
#添加，修改，删除  如果添加的键已经存在则是覆盖效果，即修改原有的值
top5["中顽童"] = "周伯通"
print(top5)
if("中顽童" in top5):
    del top5["中顽童"]
    print(top5)
##字典推导式
randomdict ={i:random.randint(10,100) for i in range(1,5)}
print(randomdict)



