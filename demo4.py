# -*- coding = utf-8 -*-
# @Time : 2022/3/10 12:25
# @Author : everr
# @File : demo4
# @Software: PyCharm
# for i in range(5):
#     print(i)
# for i in range(0,10,3):
#     print(i)
# for i in range(-10,-100,-30):
#     print(i)
# name = "chengdu"
# for x in name:
#     print(x)
# a=["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])

# i=0
# while i <5:
#     print("当前是第%d次执行循环"%(i+1))
#     print("i=%d"%i)
#     i+=1\

# 1到一百求和
# n=100
# sum = 0
# counter = 1
# while counter <=n:
#     sum= sum + counter
#     counter+=1
# print("1到%d 的和为%d"%(n,sum))
#
# # while i<=100:
#     i+=i
#     i+1
#     print(i)

#
# i=0
# while i<10:
#     i=i+1
#     print("-"*30)
#     if i==5:
#         break
#     print(i)

#99乘法表打印输出
for x in range(1,10):
    print("\t")
    for y in range(1,x+1):
        result = x * y
        print("%d * %d = %d"%(x,y,x*y),end="\t")