"""
s=[12,45,56,78,89,"A",True,"Hello"]
print(s[0])
print(s[-8])
print(s[-1])
s[5]="ABCD"
print(s)
del s[6]
print(s)
"""
"""
s=["A","C","H","K","L","B","D","X"]
print(s)
s.append("value")
print(s)
s.insert(2,"p")
print(s)
s.remove("A")
print(s)
s.reverse()
print(s)
s.sort()
print(s)
"""
"""
num_number=[]
for i in range(10):
    num=int(input("请输入1个有效数字:"))
    num_number.append(num)
print(num_number)
num_number.sort()
print(num_number)
print(f"最小值为:{num_number[0]}")
print(f"最大值为:{num_number[9]}")
print(f"平均值为:{sum(num_number)/len(num_number)}")
"""
""""
s=["2","3","4","5","6"]
s.remove("2")
print(s)
s.sort()
print(s)
s.pop(2)
print(s)
s.reverse()
print(s)
s.append("A")
print(s)
s.insert(2,"p")
print(s)
s.remove("A")
print(s)
"""
"""
num1=[]
for i in range(101):
    num2=int(input("请输入10个数字:"))
    num1.append(num2)
num1.sort()
print(num1)
print(f"最大值为:{num1[9]}")
print(f"最小值:{num1[0]}")
print(f"平均值为:{sum(num1)/len(num1)}")
"""
"""
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]
num_list=[*num_list1,*num_list2]
print(num_list)
 new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)
"""
"""
num_list=[12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list=[]
for num in num_list:
    if num%2==0:
        new_list.append(num**2)
print(new_list)
"""

num_list=[12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)
