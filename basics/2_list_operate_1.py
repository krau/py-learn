#python操作列表，对应《python编程从入门到实践第二版》第4章4.4之前（不含）

members = ['krau','ah','hanmiao']
#for循环遍历列表
for member in members: #for循环将把members中的元素依次与member关联，并都执行下面的操作
    print(member)
    print(f'{member.title()},welcome to yuzunion!')#title()将首字母大写


#range()生成数字序列
for i in range(1,10):
    print(i)
#这个循环将会依次打印1-9，因为range是在10停止的，不包括10

#使用range()创建数字列表
nums_list_1to10 = list(range(1,10))
print(nums_list_1to10)

#range()指定步长（公差）
nums_list_1to10_2 = list(range(1,10,2))#第三个数字指定了步长，即每次加2
print(nums_list_1to10_2)

#for与range结合，可以生成各种数列。如下是整数1~10的平方
nums_list_1to100 = []
for num in range(1,11):
    nums_list_1to100.append(num**2)#**表示乘方运算
print(nums_list_1to100)

#数字列表简单统计运算，以上面的nums_list_1to100为例
print(min(nums_list_1to100))#最小值
print(max(nums_list_1to100))#最大值
print(sum(nums_list_1to100))#求和

#列表解析，一种一行代码生成列表的方法（其实就是合并起来写）
list_analysis = [value**2 for value in range(1,11)]
print(list_analysis)
#这种语法的使用方法是
# 列表名 = [表达式 for 变量 in 数列]

