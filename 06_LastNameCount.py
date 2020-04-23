#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


# 导入文件

file=open("1600017460_StatData.txt","r")
mydata=file.read()
file.close()
data=mydata.splitlines()


# In[3]:


# 截取测验数据

testdata = data
n = len(testdata)


# In[4]:


# 定义函数将最低一级村委会名字中的汉字滤出
def setpool(ls):
    strRE = r'(\s{3,})([0-9]{12})(.)'
    charpool = []
    for name in ls:
        if re.findall(strRE,name):
            corename = re.findall(strRE,name)[0][2]
            charpool.append(corename)
    return charpool


# In[5]:


# 导入姓氏

lnfile=open("lastname.txt","r")
mylndata=lnfile.read()
lnfile.close()
mylndata

strRE1 = r'[0-9]*(\S)'
lnlst = re.findall(strRE1,mylndata)


# In[6]:


# 定义函数统计村委会名字中汉字频率
def poolcount(ls):
    # 建立计数字典和列表
    count={}
    countlist=[]
    # 为每个姓氏建立字典key
    for ln in lnlst:
        count[ln] = 0
    for _ in ls:
        if _ in count:
            count[_] = count[_]+1
    count = {k: v for k, v in sorted(count.items(), key=lambda item: -item[1])}
    for key, value in count.items():
        temp = [key,value]
        countlist.append(temp)
    return countlist


# In[7]:


# main函数
if __name__=="__main__":
    charpool = setpool(testdata)
    charcount = poolcount(charpool)
    hw=open("1600017460_ComputingData.txt",'a+')
    print()
    print("=================第六题=================",file=hw)
    print("========统计带有不同姓氏的地名数量=========",file=hw)
    print("姓氏\t统计数",file=hw)
    for char in charcount:
        print(f"{char[0]}\t{char[1]}",file=hw)
    hw.close()


# In[ ]:




