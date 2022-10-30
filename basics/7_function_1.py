#Python自定义函数，对应《python编程从入门到实践第二版》第8章8.6(不含)以前内容

#定义函数，使用def，最简单的一个例子如下
def hello():
    #输出问候语
    print('Hello!')

hello()

#向函数传递参数
def hello(username):
    print(f'Hello,{username.title()}!')
#在这里，username被称为形参，而下面传入的’krau’就称为实参
hello('krau')


#传递实参
#位置实参，按实参的顺序传递给形参
def human_info(name,height,weight,gender):
    #显示一个人的信息
    print(f'''
My name is {name.title()}
My height is {height},and weight is {weight}
Im a {gender}''')

human_info('krau','178','65','male')
#可以看到实参按照顺序依次传递给了形参

#关键字实参，按照名称传递实参
human_info(height='178',name='krau',gender='male',weight='65')


#给参数确定默认值
def pet_info(pet_name,pet_animal='cat'):
    #显示宠物信息
    print(f'{pet_name.title()} is my pet , it is a {pet_animal}')

#若不给出pet_animal，则会使用默认值cat
pet_info('ah')
#也可以给默认值为空字符串，即''，这样做的话，这个参数将变成可选的


#返回值，函数处理数据并返回的值
#让函数返回值，使用return
def name_format(first_name,last_name):
    #返回格式化好的姓名
    full_name = f'{first_name} {last_name}'
    return full_name.title()

print(name_format('acher','krau'))
#这里只是一个示例，所以未免有些脱裤子放屁

#函数可以返回任意类型的值，比如返回字典
def build_human(name,age):
    person = {'name':name,'age':age}
    return person
me = build_human('krau',18)
print(me)


#传递列表
def yuzu_hello(names):
    for name in names:
        print(f'Hello,{name.title()}!')

members = ['krau','ah','hanmiao']
yuzu_hello(members)

#当需要处理一个列表，但不想让函数对列表产生影响时，可以传入列表的副本
yuzu_hello(members[:])


#传递任意数量的实参，不需首先指定多少形参
def do_math1(*derivatives):
    #什么都导不出来
    for derivative in derivatives:
        print(f'{derivative} 导不出来')

do_math1('lnx','2x','ex')
#可以看到，*derivatives创建了一个名为derivatives的元组，传入的实参都存入其中

'''
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意 数量实参的形参放在最后。
Python先匹配位置实参和关键字实参， 再将余下的实参都收集到最后一个形参中。
'''
def do_math2(diffculity,*integrals):
    #什么都积不回去
    for integral in integrals:
        print(f'{integral}积不回去，因为它的难度是{diffculity}')

#Python先匹配位置实参和关键字实参， 再将余下的实参都收集到最后一个形参中。
do_math2('easy','fx','gx','hx')

#使用任意数量的关键字实参
#有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
#可以使用字典中的键值对解决这一问题
def build_profile(first,last,**user_info):
    '''创建一个包含用户所有信息的字典'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

krau_info = build_profile('acher','krau',age=18,gender='male')
print(krau_info)
#可以看到**user_info使python创建了一个名为user_info的字典，age和gender都存入了其中

'''
注意 你经常会看到形参名**kwargs 
它常常用于收集任意数量的关键字实参。
'''