#用户输入和while循环
#用户输入，使用inpu()函数
from turtle import Turtle


name = input('请输入你的名字： ')
print(f'hello {name}')

#判断一个数是奇数还是偶数
num = int(input('请输入一个数：　'))#int()用于将字符串转化为整数
if num % 2 == 0: #%是求模运算，即返回两个数相除的余数
    print(f'{num}是偶数')
else:
    print(f'{num}是奇数')

#while循环
#示例，使用while循环让用户控制程序何时结束
print('我是复读机，输入quit以退出程序')
msg = ''
while msg != 'quit':
    msg = input('请输入：')
    if msg != 'quit':
        print(msg)
    else:
        pass

#使用标志，清晰地控制程序运行
print('我是复读机二号')
msg = ''
status0 = True #这里的status0是为了方便控制循环运行的，便被称为标志
while status0:
    msg = input('请输入： ')
    if msg == 'quit':
        status0 = False
    else:
        print(msg)

#使用break退出循环
print('我是复读机三号')
msg = ''
while True:
    msg = input('请您输入： ')
    if msg == 'quit':
        break
    else:
        print(msg)

#使用continue从头开始循环
#输出所有偶数
num0 = 0
while num0 < 10:
    num0 += 1
    if num0 % 2 != 0:
        continue #与break不同的是，它会使循环返回第一行重新执行（从num0+=1）
    print(num0)
