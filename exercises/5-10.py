'''
练习5-10：检查用户名 按下面的说明编写一个程序，模拟 网站如何确保每位用户的用户名都独一无二。
创建一个至少包含5个用户名的列表，并将其命名 为current_users 。 
再创建一个包含5个用户名的列表，将其命名 为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。 
遍历列表new_users ，对于其中的每个用户名，都检查它 是否已被使用。如果是，就打印一条消息，指出需要输入 别的用户名；否则，打印一条消息，指出这个用户名未被 使用。
确保比较时不区分大小写。换句话说，如果用户 名'John' 已被使用，应拒绝用户名'JOHN' 。（为此，需 要创建列表current_users 的副本，其中包含当前所有 用户名的小写版本。）
'''
current_users = ['krau','xiaoming','ah','cos0','lihua']
new_users = ['krau','lihua','xiaogang','leao','xiaolv']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'用户名{new_user}已被使用')
    else:
        print(f'用户名{new_user}可以使用')