import random  #导入生成随机数模块
list1 = []  #定义空列表
for i in range(10):
    list1.append(random.randint (10,100))  #向列表中添加随机数
print(list1)


'''
列表推導式如下
'''
list2 = [random.randint (10,100) for x in range(10)]  #中間是用空格分隔的，而不是逗號
print("用列表推導式生成的列表："+str(list2))

#生成1-10內的偶數平方的列表
list3=[i*i for i in range(2,11,2)]
print("偶數平方列表："+str(list3))

#通過列表生成新的列表  比如所有商品價格打五折
price = [8888,5600,3465,7981,3350,9931]
print("打折前價格：",end="\n")
for index,p in enumerate(price):
    print(index,p,"\t",end="\n")
sale = [j*0.5 for j in price]
print("所有商品打折后價格：",end="\n")
for index,p in enumerate(sale):
    print(index,p,"\t",end="\n")
#如果只針對價格高于5000元的打五折，就需要添加條件
sale2 =[k*0.5 for k in price if k>=5000]
print(sale2)

