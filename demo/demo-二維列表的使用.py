'''
生成房間號，1101-1109 2101-2109 共7层
'''
room=[]  #先定义一个空列表
for i in range(1,8):  #楼层
   room.append([]) #每层添加一个空楼层列表
   for j in range(1,10): #房间数
       room[i-1].append(i*1000+100+j) #索引是从0开始，每层楼添加房间号
print(room)

#按如上逻辑用列表推导式重写
room2 =[[i*1000+100+j for j in range(1,10)] for i in range(1,8)]
print("用列表推导式重写后："+str(room2))

#变更版式，将横版变成竖版显示
str1 = "飞雪连天射白鹿"
str2 = "笑书神侠倚碧鸳"
str3 = "仙鹤已随云影杳"
str4 = "神针犹带月光寒"
yitian = [list(str1),list(str2),list(str3),list(str4)]
#如果直接输出二维内容排版就不像了，需要使用二维列表的两层循环输出才行
for s in yitian:
    print(s)
print("\n----横版----")
for i in yitian:
    for j in i:
        print(" "+j,end="")
    print(end="\n")
#第二种输出形式，按每隔四个字换行来指定输出，缺点不灵活，一会将语句换内容，就能看出效果
print("第二种形式输出")
for i in range(4):  #循环的行
    for j in range(7): #循环每一行的字
        if 6==j:       #一行中的最后一个字，因为range是不包含end的4这个索引的
            print(yitian[i][j])  #换行输出
        else:
            print(yitian[i][j],end="")#不换行输出
print("\n----竖版----")

yitian.reverse()
for i in range(7): # 反过来先循环每行的每个字
    for j in range(4): #行数
         if 3==j:
             print(" "+yitian[j][i])
         else:
             print(" "+yitian[j][i],end="")
