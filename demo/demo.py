wujue = ["東邪","西毒","南帝","北丐","中神通","東邪","西狂","南僧","北俠","中頑童"]
for index,team in enumerate(wujue):
    if (index+1)%5==0:
        print(team+'\n',end="")#換行輸出
    else:
        print(team+'\t',end="")#不換行輸出
