#!/usr/bin/env python
# coding: utf-8


# 导入文件

file=open("1600017460_StatData.txt","r")
mydata=file.read()
file.close()
data=mydata.splitlines()




# 创建编号和地区性质的对应关系

d = {'111':'主城区','112':'城乡结合区','121':'镇中心区','122':'镇乡结合区','123':'特殊区域','210':'乡中心区','220':'村庄'}



# 截取试验数据

testdata = data
len(testdata)



# 创建空字典，以备统计
count = {'111':0,'112':0,'121':0,'122':0,'123':0,'210':0,'220':0}

# 遍历统计个数
n = len(testdata)
for i in range(n):
    key = testdata[i][-3:]
    if key in d:
        count[key]=count[key]+1

# 查看结果
count



# 输出结果到txt
hw=open("1600017460_ComputingData.txt","w")

print("=================第四题=================",file=hw)
print("======分别统计各分类最基层统计单位数量======",file=hw)
for key in d.keys():
    print(f'{key}\t{d[key]}\t{count[key]}',file=hw)

hw.close()


# In[ ]:
