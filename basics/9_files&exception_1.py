#python文件操作与异常处理

#读取文件
'''
同级目录下存在一个pi_digits.txt文件，它存储了圆周率30位
打开这个文件并输出：
'''
with open('pi_digits.txt') as file_obj:
    txt_contents = file_obj.read()
print(txt_contents)
'''
第一行，open()函数打开了名为pi_digits.txt的文件，返回一个文件对象。
而前面with的作用是，当不需要再访问文件时，将其关闭。（若不这样做，文件将保持开启，占用资源）
第二行，使用方法read()读取文件对象内容，并将其赋值给txt_contents。
'''

'''
open()可以接受文件路径，无论是相对路径还是绝对路径。
这让你能够读取任何位置的文件
'''
with open(".\pi_digits.txt") as file_obj2:
    txt_contents = file_obj2.read()
print(txt_contents)

#逐行读取文件
filename = 'pi_digits.txt'
with open(filename) as file_obj3:
    for line in file_obj3:
        print(line.rstrip())#.rstrip()用于删除空行

#将逐行内容存入列表，使用readlines()方法
with open('pi_digits.txt') as file_obj4:
    lines = file_obj4.readlines()

print(lines)


#写入文件
'''
open()也可用于写入文件，只要传入另一个实参指定模式即可
如下示例将创建一个coding.txt文件，并写入'Love?Rather coding!'
open()的第二个实参'w'表示写入模式。
'r'读取模式、'w'写入模式、'a'附加模式、'r+'读写模式
'''
write_file_name = 'coding.txt'
with open(write_file_name,'w') as file_obj5:
    file_obj5.write('Love?Rather coding!')

'''
'w'模式会覆盖文件内容写入，若只想在原有内容下附加，可以使用'a'
'''
with open(write_file_name,'a') as file_obj6:
    file_obj6.write('\nI just chasing my Dream')


#使用try-except处理异常
'''
例如，print(1/0)让0作为分母，显然会报错，阻止程序运行。
若想友好地处理这一异常，可以使用try-except语句
'''
try:
    print(1/0)
except:
    print('零不能做分母')

'''
上面的代码可以描述为
尝试执行print(1/0)，若不引发异常，则正常执行。
若引发异常，则执行except后的语句

当有些代码依赖于try后的代码才能正常运行时，可以添加else语句，如下
'''
#计算倒数
try:
    n = int(input('请输入一个不为0的整数：'))
except:
    print('请输入一个不为零的整数！')
try:
    answer = 1/n
except:
    print('请检查输入是否正确')
else:
    print(answer)