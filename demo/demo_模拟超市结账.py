def fun_checkout(money):
    '''功能：计算商品合计金额并进行折扣处理
       money:保存商品金额的列表
       返回值:商品的合计金额和折扣后的金额
    '''
    money_old = sum(money)
    money_new = money_old
    if 500 <= money_old < 1000:#享受9折优惠
        money_new = '{:.2f}'.format(money_old*0.9)
    elif 1000 <= money_old < 2000:#8折
        money_new = '{:.2f}'.format(money_old*0.8)
    elif 2000 <= money_old < 3000:
        money_new = '{:.2f}'.format(money_old*0.7)
    elif 3000 <= money_old:
        money_new = '{:.2f}'.format(money_old*0.6)
    return money_old,money_new #返回总金额和折扣后的金额
#调用函数
print("="*10+"\n开始结算"+"="*10)
list_money = []
while True:
    inmoney = float(input("请输入商品金额(输入0表示输入完毕):"))
    if 0 == int(inmoney):
        break #退出循环
    else:
        list_money.append(inmoney)
        money = fun_checkout(list_money)
print("合计金额:",money[0],"应付金额",money[1])
