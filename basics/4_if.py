#if语句，对应《python编程从入门到实践第二版》第5章

#判断两个值是否相等，用==（两个等号），相等时返回True，否则返回False
wife = 'Miku'
print(wife =='Miku')
# == 判断是大小写敏感的
print(wife == 'miku')#将会输出False
#如果不希望大小写影响判断，可以在判断时都转换为小写
print(wife.lower()=='miku')#lower()不会直接修改变量的值，只是读取变量的值并将其小写再进行后续操作
#若要都大写可使用.upper()方法

#判断是否不相等，使用!=。!常常是表示‘非’的
print(wife != 'Miku')

#判断多条件
#and 和，都为True时返回True
age_0 = 16
age_1 = 14
print(age_0 > 15 and age_1 <=15)
#or 或，至少有一个真就返回真
print(age_0 == 15 or age_1 > 12)

#in检查特定值是否在列表中，如果在，返回True
waifus = ['miku','ayanami','sakira']
print('sakira' in waifus)
#not in检查特定值是否不在列表中，如果不在，将返回Ture
print('miku' not in waifus)

#布尔表达式，如下
Miku_is_my_wife = True
Krau_love_miku = True

#if-else语句
if 'miku' in waifus:
    print('miku is my wife')
else:
    print('miku is also my wife')
#if-elif-else语句，判断多种条件之一
if wife == waifus[0]:
    print(f'{waifus[0]} is my wife!'.title())#此处f'{}'可以在字符串中输出变量的值
elif wife == waifus[1]:
    print(f'{waifus[1]} is my wife!'.title())
elif wife == waifus[2]:
    print(f'{waifus[2]} is my wife!'.title())#elif可以是多个
else:
    print('you are all my wife'.title())
#else是可以省略不写的，如果省略，程序会在所有条件都不符合时不进行任何操作
#if-elif-else结构一旦遇到为真的条件时将会执行对应的代码块，之后跳过整个结构，即使之后还有为真的条件
#如果你不想让它这样，那不妨多写几个if