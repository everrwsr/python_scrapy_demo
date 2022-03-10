# -*- coding = utf-8 -*-
# @Time : 2022/3/10 11:55
# @Author : everr
# @File : demo3
# @Software: PyCharm
# if True:
#     print("true")
# else :
#     print("false")
# score =87
# if score >=90:
#     print("本次考试，等级为A")
# elif score >=80 and score <90:
#     print("B")
# else:
#     print("本次考试，等级为E")
xingbie = 1 # 1代表男，0代表女生
danshen = 1  # 1代表单身，0代表有男女朋友
# if xingbie  == 1:
#     print("nan")
#     if danshen ==1:
#         print("geini")
#     else:
#         print("给你找一个")
# else:
#     print("女生")
#     print("...")
# import random
# x=random.randint(0,2)
# print(x)
import random

x = int(input("请输入：剪刀（0）、石头（1）、布（2）：_"))
if type(x)== str:
    print("输入非法")
elif x==0:
    print("你的输入为：剪刀（0）")
elif x==1:
    print("你的输入为：石头（1）")
elif x==2:
    print("你的输入为：布（2）")
y =random.randint(0,2)
print("随机生成数字为:%d"%y)
if x<y:
    print("哈哈，你输了：）")
elif x==y:
    print("哈哈，平手哦：）")
elif x==0 and y==2:
    print("哈哈，你输了：）")
else :
    print("哈哈，你赢了：）")
