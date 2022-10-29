#python字典与集合，对应对应《python编程从入门到实践第二版》第6章

#创建字典，使用花括号{}
human_1 = {'color':'yellow','height':175}# 用 : 关联两个值，即键值对
print(human_1['color'])
print(human_1['height'])#通过 键 查找 值 ，就是“字典”的含义

#向字典中添加键值对
human_1['weight'] = 65 #直接 字典[新键]=值，即可把新的键值对添加到字典末尾
print(human_1)
#修改字典中的值也是类似的
human_1['height'] = 180

#字典可以包含任意数量的键值对，包括空字典
human_2 = {}

#删除键值对
#与列表类似，可使用del
del human_1['color']
print(human_1)

#字典的格式可以是多行，这会让代码更加美观，尤其是字典内容很多的时候
human_2 = {
    'height':177,
    'weight':68,
    'age':18,
    'gender':'male',
}

#使用get()访问字典，避免引发错误
#当要访问的键值对在字典中不存在时，使用方括号访问便会引发错误。
#可以使用get()，使之返回一个默认值，避免错误
print(human_2.get('color','不存在该值'))#当color在字典中不存在时，将会输出“不存在该值”，如果不给出get()的第二个参数，将会返回None

#遍历字典
#遍历键值对
for key,value in human_2.items(): #item()方法用于返回一个键值对列表
    print(key)
    print(value)#可以看到，字典中的每个键和值分别 依次赋给了key和value，当然这两个变量是可以随意命名的

#遍历所有键，使用keys()方法
for key in human_2.keys():
    print(key)
#实际上，默认遍历时便是只遍历所有键，但最好加上keys方法，便于阅读
#keys()方法返回的是一个包含所有键的列表，正如题item()方法返回的是一个包含所有键值对的列表

#遍历所有值，使用values()方法
for value in human_2.values():
    print(value)

#使用特定顺序遍历列表
#比如可以使用sorted()方法，按照字母顺序遍历
for key in sorted(human_2.keys()):
    print(key)


#当字典中的值出现重复时候，可以使用集合剔除重复项
humangender = {
    'krau':'me',
    'ah':'he',
    'xiaolv':'she',
    'hanmiao':'he',
}
#可以看到这个字典中两个值都是he，可以使用set()方法创建一个集合，集合中的元素都是独一无二的
for gender in set(humangender.values()):
    print(gender)

#集合，也使用花括号创建，但存储的不是键值对
langs = {'c','py','go'}
print(langs)


#嵌套
#在列表中嵌套字典
humans = [human_1,human_2]
print(humans)
#同样的，可以在字典中嵌套列表，在字典中嵌套字典......