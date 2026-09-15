"""
age=int(input("请输入你的年龄:"))
if age>=18:
    print("已成年")
else:
    print("未成年")
print("祝你游玩愉快")
"""
from idlelib.colorizer import prog_group_name_to_tag

"""
long=int(input("请输入你的身高:"))
if long>=120:
    print("你的身高超出120cm，游玩需要购票10元:")
else:
    print("你的身高未超出120cm,可以免费游玩:")
print("祝你游玩愉快")
"""
"""
num=int(input("请输入一个数字"))
if num>0:
    print(f"{num}是一个正数")
elif num<0:
    print("%d是一个负数"%num)
else :
    print("是0")
"""
"""
man=input("请输入你的用户名：")
mimi=input("请输入你的密码：")
if man=="admin" and mimi=="666888":
    print("登陆成功")
elif man=="root" and mimi=="547527":
    print("登录成功")
elif man=="zhangsan" and mimi=="123456":
    print("登录成功")
else:
    print("登录失败")
"""
"""
long1=input("请输入第一条边长:")
long2=input("请输入第二条边长:")
long3=input("请输入第三条边长:")
if long1+long2<=long3 or long2+long3<=long1 or long1+long3<=long2:
    print("不能构成三角形")
elif long1==long2!=long3 or long2==long3!=long1 or long3==long1!=long2:
    print("等腰三角形")
elif long1==long2==long3:
    print("等边三角形")
else:
    print("普通三角形")
"""
"""
num1=int(input("请输入第一个数字："))
num2=int(input("请输入第二个数字："))
nextion=input("请输入计算关系：")
match nextion:
    case"+" :
        print(f"和为{num1+num2}")
    case"-":
        print(f"差为{num1-num2}")
    case"*":
        print("乘积为%2.2f"%(num1*num2))
    case"/" if num2!=0 :
        print("除为%2.2f"%(num1/num2))
    case _:
        print("%s%s%s"%(num1,num2,nextion))
"""
"""
eding=int(input("请输入额定电压"))
shiji=int(input("请输入实际电压"))
if eding>shiji:
    print("正常")
elif eding<shiji:
    print("严重过流")
elif eding==shiji:
    print("警告")
"""
"""
i=0
num=0
while i<=100:
    num+=i
    i+=2
print(num)
"""
"""
i=0
num=0
while i<=100:
    if i%2==0:
        num+=i
        i+=1
    elif i%2!=0:
         i+=1
print(num)
"""
"""
for i in range(1,7):
    for j in range(1,i):
     print(j,end=" ")
    print()
"""
for i in range(1,9):
    if i%2!=0:
        for j in range(1,9):
            if j%2!=0:
                print(".",end=" ")
            if j%2==0:
                print("。",end=" ")
    if i%2==0:
        for j in range(1,9):
            if j%2==0:
                print(".",end=" ")
            if j%2!=0:
                print("。",end=" ")
    print()
