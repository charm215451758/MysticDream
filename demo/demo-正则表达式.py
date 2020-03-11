import re
pattern = r"mr_\w"  #模式字符串
string = '测试MR_SHOP mr_shop'  #要匹配的字符串
match = re.match(pattern,string,re.I) #只匹配大写字母  如果不匹配会返回None,也不能调用后面三个方法
search = re.search(pattern,string) #如果待匹配的字符串的开头有别的字符，则使用match匹配不了，而需要使用search才能匹配
print(match)
print(search)#只匹配第一个符合表达式的字符串，而不会管后面是否还有符合条件的字符串
if(None != None):
    print("起始位置",match.start())
    print("结束位置",match.end())
    print("匹配数据",match.group())
#验证手机号码是否合法
patternPhone= r'(13[4-9]\d{8})|(15[01289]\d{8})$' #模式字符串
mobile = "13688888888"
match2 = re.match(patternPhone,mobile)
if(None == match2):
    print("这不是中国移动的号码")
else:
    print("这是中国移动号码")
patternHack = r"黑客|抓包|监听|Trojan"
stringTest = "我喜欢看黑客方面的书，特别是关于Trojan的"
match2 = re.match(patternHack,stringTest)   #如果使用match是无法检测到中间的某个字符串的
if (None != match2):
    print("检测到危险字符")
else:
    print("安全")
search2 = re.search(patternHack,stringTest)   #search就可以检测到中间的某个字符串
if (None != search2):
    print("检测到危险字符:"+search2.group())
else:
    print("安全")
findall = re.findall(patternHack,stringTest)   #search就可以检测到中间的某个字符串
if (None != findall):
    print(findall)
    print("隐藏敏感字符")
    print(re.sub(patternHack,"***",stringTest))
else:
    print("安全")
#使用findall()时需要注意的捕获分组概念实例 匹配邮箱名
patternMail = "\w+@(qq|163|126)\.com"
stringMail = "123@163.com 扰乱字符456@126.扰乱com空gg@qq.com"
findMailbox = re.findall(patternMail,stringMail)
print(findMailbox)
#按照如上的写法，得到的数据只有括号内的内容，而不是完整的邮箱名，因为出现括号里，括号里的内容匹配到的部分会被作为结果输出
#如果要匹配完整的邮箱名，则需要使用?:标明这是一个非捕获分组，仅参与正匹配过程，而不作为单独的结果进行输出
patternMailAll = "\w+@(?:qq|163|126)\.com"
findMailboxAll = re.findall(patternMailAll,stringMail,re.A)#第三个参数如果不写排除汉字，则会匹配到扰乱字符串
print(findMailboxAll)
#替换字符串的语法类似,只是多了需要替换的字符串及替换的次数参数
pattern163 = "163|126"
replaceMailbox = re.sub(pattern163,"189",stringMail)
print(replaceMailbox)
#分割字符串的语法类似于替换字符串
splitMailbox = re.split(pattern163,stringMail)
print(splitMailbox)
    
