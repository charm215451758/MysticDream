print("BMI指数计算")
height = float(input("请输入身高(单位：米)："))
weight = float(input("请输入体重(单位：千克）："))
bmi = weight / (height * height) #计算公式

print("您的bmi指数为：",bmi)
if bmi < 18.5:
    print("偏瘦")
if bmi >=18.5 and bmi <24.9:
    print("标准")
if bmi >=24.9 and bmi <29.9:
    print("偏胖")
