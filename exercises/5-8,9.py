'''
练习5-8：
以特殊方式跟管理员打招呼,创建一个至少包含5 个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。
遍历用户名列表，并向每位用户打印一条问候消息
练习5-9：
处理没有用户的情形 在为完成练习5-8编写的程序 中，添加一条if 语句，检查用户名列表是否为空
'''
users = ['admin','krau','ah','leao','hanmiao']
if users: #当列表至少有一个元素时，它为True
    for user in users:
        if user == 'admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print(f'Hello {user.title()},thank you for logging in again.')
else:
    print('We need to find some users!')