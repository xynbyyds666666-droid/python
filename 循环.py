"""
num=0
while num<10:
    print("人生苦短，我用python")
    num=num+1
"""
from pickletools import long1

"""
i=0
num=0
while i<=100:
    num=num+i
    i=i+2
else:
    print("总和为：%d"%num)
"""
"""
i=0
num=0
while i<=100:
    if i%2==0:
        num=num+i
      i+=1
else:
    print(f"总和为{num}")
"""
"""
i = 0
num = 0

while i <= 100:
    if i % 2 == 0:
        num += i
    i += 1

# 循环结束后直接打印，不需要 else
print(f"总和为{num}")
"""
"""
msg=input("请输入需要遍历的字符串：")
for c in msg:
    print(f"{c}")
"""
"""
total=0
for c in range(102,501,3):
    total=total+c
print(f"zonghewei:{total}")
"""
"""
total=0
for c in range(100,501):
    if c % 3 == 0:
        total=total+c
print(f"zonghewei:{total}")
"""
#嵌套循环 print自带换行效果输出会自动换行 print("第一行\n第二行\n第三行")也表示换行
"""
long=int(input("请输入长方形的长："))
kuan=int(input("请输入长方形的宽："))
for c in range(kuan):
    for d in range(long):
        print("*",end="  ")
    print()
"""
"""
for c in range(1, 10):
    for d in range(1, c + 1):  # 让 d 从 1 走到 c
        print(f"{d}*{c}={c*d}", end="\t ")
 ，
    print()
"""
"""
for c in range(1, 6):
    for d in range(1, c + 1):
        print("*",end="  ")
    print()
"""
"""
for c in range(1, 9):
    if c % 2 != 0:
        for d in range(1, 9):
            if d % 2 != 0:
                print(".",end="\t")
            elif d % 2 == 0:
                print("。",end="\t")
        print()
    if c % 2 == 0:
        for d in range(1, 9):
            if d % 2 != 0:
                print("。",end="\t")
            elif d % 2 == 0:
                print(".",end="\t")
        print()
"""
"""
yonghu=input("请输入用户名；")
mima=input("请输入密码:")
while yonghu=="admin"and mima=="666888" or yonghu=="zhangsan"and mima=="666889" or yonghu=="taoge"and mima=="888666":
    print("登录成功，进入B站首页")
else:
yonghu=input("请再次输入用户名：")
mima=input("请再次输入密码：")
"""
"""
while True:
    uesname=input("请输入正确的用户名:")
    password=input("请输入正确的密码:")
    if uesname==""or password=="":
        print("输入的不能为空。请重新输入")
       continue
    if uesname=="admin"and password=="666888":
        print("登录成功，进入B站首页")
        break
    elif uesname=="zhangsan"and password=="666889":
        print("登录成功，进入B站首页")
        break
    elif uesname=="taoge"and password=="88666":
        print("登录成功，进入B站首页")
    else:
        print("输入错误，请重新输入:")
"""
"""
for c in range(1,6):
    uesname = input("请输入正确的用户名:")
    password = input("请输入正确的密码:")
    if uesname == "" or password == "":
        print("输入的不能为空。请重新输入")
    continue
    if uesname == "admin" and password == "666888":
        print("登录成功，进入B站首页")
        break
    elif uesname == "zhangsan" and password == "666889":
        print("登录成功，进入B站首页")
        break
    elif uesname == "taoge" and password == "88666":
        print("登录成功，进入B站首页")
        break
    else:
        print("输入错误，请重新输入:")
"""
"""
import random
random_number=random.randint(1,100)
while True:
    user_number=int(input("请输入你猜的数字:"))
    if user_number==random_number:
        print("恭喜你，猜对了")
        break
    elif user_number>random_number:
        print("大了些，接着猜")
        continue
    elif user_number<random_number:
        print("小了些，接着猜")
        continue
    else:
        print("请输入正确的数字格式")
"""
"""
num=0
c=0
while c<=1000:
    if c%5==0:
        num=num+c
    c+=1
print(f"{num}")
"""

"""
num=0
for c in range(1,1001):
    if c%5==0:
        num=num+c
print(f"{num}")
"""
"""
a_number=0
k_number=0
zifuchuan=input("请输入任意只有字母的字符串:")
for c in zifuchuan:
    if c=="a" :
        a_number=a_number+1
    elif c=="k":
        k_number=k_number+1
print(f"a的个数为{a_number},k的个数为{k_number}")
"""
import random
for c in range(1,101):
    shuju=random.randint(1,220)
print(shuju)
















