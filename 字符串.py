"""
s="hello-python"
print(s[4])
print(s[-4])
for i in s:
    print(i)
print(s[0:5:1])
print(s[:5:])
"""
from operator import truediv

"""
s="hello-python-hello-world"
index=s.find("-")
print(index)
c=s.count("o")
print(c)
su=s.upper()
print(su)
sl=s.lower()
print(sl)
ss=s.strip()
print(ss)
slist=s.split("-")
print(slist)
sr=s.replace("-","_")
print(sr)
print(s.startswith("o"))
print(s.endswith("d"))
"""
"""
while True:
  yx=input("请输入你的邮箱")
  i=yx.count(".")
  s=yx.count("@")
  if i>=1:
      if s==0:
          print("你输入的邮箱格式错误")
          continue
      elif s==1:
          print("你输入的邮箱格式正确")
          break
      elif s>1:
          print("你输入的邮箱地址正确")
          break
  else:
      print("你输入的邮箱格式错误")
      continue
"""
"""
if "." in yx .是否在邮箱中
"""
"""
result=[]
for i in range(1,11):
    s=input("请输入10个字符串：")
    fs=s[ : :-1]
    new=fs.upper()
    result.append(new)
print(result)
for t in result:
    print(t)
result用于存贮变完的十字符串，列表可以存储字符串
"""













































































































































































































