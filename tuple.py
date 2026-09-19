from http.cookiejar import time2isoz

"""
t1=(80,95,78,50,76,80,85,20)
print(t1)
print(type(t1))
print(t1[0])
print(t1[-1])
print(t1[0:5:1])
print(t1.count(80))
print(t1.index(80))
a,*b=t1
print(a)
print(b)
"""
"""
t1=(80,95,78,50,76,80,85,20)
a,*b,c=t1
print(a)
print(b)
print(c)
"""
"""
a=100
b=200
c=300
a,b,c=c,a,b
print(a)
print(b)
print(c)
"""
b=[]
c=[]
d=[]
for i in range(1,4):
 yuwen=int(input(f"请输入第{i}位同学语文成绩"))
 shuxue=int(input(f"请输入第{i}位同学数学成绩"))
 yingyu=int(input(f"请输入第{i}为同学英语成绩"))
 b.append(yuwen)
 c.append(shuxue)
 d.append(yingyu)
 a=[yuwen,shuxue,yingyu]
 print(f"第{i}位同学的总分为{sum(a)}")
print(f"语文平均分为{sum(b)/len(b)}")
print(f"数学平均分为{sum(c)/len(c)}")
print(f"英语平均分为{sum(d)/len(d)}")
b.sort()
c.sort()
d.sort()
print(f"语文最低分为{b(0)}")
print(f"数学最低分为{c(0)}")
print(f"英语最低分为{d(0)}")
e=b[ : : -1]
f=c[ : : -1]
g=d[ : : -1]
print(f"英语最高分为{e(0)}")
print(f"英语最高分为{f(0)}")
print(f"英语最高分为{g(0)}")












