"""
num_map={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖','.':'点'}
num_str=input("请输入一个数字:")
result=''.join([num_map[num] for num in num_str if num in num_map])
print(result)

import random
nums=set()
while len(nums)<5:
    n=random.randint(0,10)
    nums.add(n)
    print(list(nums))

for x in range(0,21):
    for y in range(0,34):
        z=100-x-y
        if z%3==0 and 5*x+3*y+z//3==100:
            print(f"公鸡{x}只 母鸡{y}只 小鸡{z}只")

num=input("请输入一个四位整数:")
if len(num)==4 and num==num[::-1]:
    print(f"{num}是回文数")
else:
    print(f"{num}不是回文数")

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def is_palindrome(n):
    return str(n)==str(n)[::-1]
result=[x for x in range(2,1001) if is_prime(x) and is_palindrome(x)]
print(f"2~1000的回文素数{result}")

for num in range(100,1000):
    a=num//100
    b=(num//100)%10
    c=num%10
    if a**3+b**3+c**3==num:
        print(num)

sales=float(input("请输入员工的销售额:"))
base_salary=2000
commission=0
if sales<=3000:
    commission=0
elif 3000<sales<=7000:
    commission=sales*0.1
elif 7000<sales<=10000:
    commission=sales*0.15
else:
    commission=sales*0.2
total_salary=base_salary+commission
print(total_salary)

import math
total=29.5
car1=4
times1=3
car2=2.5
left=total-car1*times1
times2=math.ceil(left/car2)
print(f"还需要运送{times2}次")


import re
s='Do not trouble trouble till trouble troubles you'
r='[a-zA-Z]+'
res=re.findall(r,s)
print(res)
print(res.count('trouble'))
"""
text="Do not trouble trouble till trouble troubles you"
clean_text=text.lower().replace(',','').replace('.','').replace('!','').replace('?','')
words=clean_text.split()
words_count={}
for word in words:
    words_count[word]=words_count.get(word,0)+1
print(words_count)