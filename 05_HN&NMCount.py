#!/usr/bin/env python
# coding: utf-8


import re


# 导入文件

file=open("1600017460_StatData.txt","r")
mydata=file.read()
file.close()
data=mydata.splitlines()


# 截取测验数据
testdata = data
n = len(testdata)

# 择出河南和内蒙古的部分
for i in range(n):
    if testdata[i]=='410000000000河南省':
        start_hn = i
    elif testdata[i]=='420000000000湖北省':
        end_hn = i
    elif testdata[i]=='150000000000内蒙古自治区':
        start_nm = i
    elif testdata[i]=='210000000000辽宁省':
        end_nm = i

hn_list = testdata[start_hn:end_hn]
nm_list = testdata[start_nm:end_nm]


# 定义函数将最低一级村委会名字中的汉字滤出
def setpool(ls):
    strRE = r'(\s*)([0-9]{12})(.*)(村委会)'
    charpool = []
    for name in ls:
        if re.findall(strRE,name):
            corename = re.findall(strRE,name)[0][2]
            for token in corename:
                charpool.append(token)
    return charpool


# 定义函数统计村委会名字中汉字频率
def poolcount(ls):
    count={}
    countlist=[]
    for _ in ls:
        if _ in count:
            count[_] = count[_]+1
        else:
            count[_] = 1
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
    for key, value in count.items():
        temp = [key,value]
        countlist.append(temp)
    return countlist



# main函数
if __name__=="__main__":
    charpool_hn = setpool(hn_list)
    charpool_nm = setpool(nm_list)
    hncount = poolcount(charpool_hn)
    nmcount = poolcount(charpool_nm)
    i = 1
    hw=open("1600017460_ComputingData.txt",'a+')
    print()
    print("=================第五题=================",file=hw)
    print("======分别统计内蒙古和河南村委会常用字======",file=hw)
    print("排名\t字（内蒙古）\t统计数（内蒙古）\t字（河南）\t统计数（河南）",file=hw)
    while i<=100:
        hn = hncount.pop()
        nm = nmcount.pop()
        print(f"{i}\t{nm[0]}\t{nm[1]}\t{hn[0]}\t{hn[1]}",file=hw)
        i+=1
    hw.close()
