#python操作列表，对应《python编程从入门到实践第二版》第4章4.4及其之后

#切片，圈定列表某一部分
phones = ['pixel3','mix4','k20p','pixel2','honor8']
print(phones[0:3])#输出包含索引为0，1，2的元素的’子列表‘
print(phones[:3])#不指定第一个索引会自动从0开始
print(phones[1:])#不指定第二个索引会自动到最后
print(phones[:])#都不指定就是从头到尾，可利用此创建列表的副本
phones_copy = phones[:]
print(phones_copy)
#这和直接把phones赋值给phones_copy是不一样的，若直接赋值，实际上只是给同一个列表关联了两个变量名字，当修改列表时，这两个变量都会同步修改
#例如，给phones添加一个元素
phones.append('readmi')
#然后看看phones和phones_copy这两个列表现在是什么样的
print('phones列表',phones)
print('phones_copy列表',phones_copy)
#但如果直接赋值将是下面的效果
my_phones = phones
phones.append('oppo')
print(phones)
print('可以看到即使是对phones进行修改，my_phones也将输出和phones一样的列表',my_phones)


#遍历切片
for phone in phones[0:3]:
    print(phone.title())


#元组，不能变的列表
#创建元组，使用圆括号
dimensions = (10,20)
print(dimensions[0])
print(dimensions[1])

#元组中的数据是不能被修改的，如果尝试修改将会报错，以下被注释的代码将会报错
# dimensions[0] = 20
#但是可以重新定义元组来修改元组的值
l = 20
w = 10
dimensions = (l,w)#重新定义元组是合法的
print(dimensions)
#但即使改变元组中存储的变量的值，元组也不会改变
l = 500
w = 200
print(dimensions)#可以看到元组还是没变

#如果需要创建只有一个元素的元组，也需要带上逗号，因为元组使用逗号来标识
onlyonetuple = (1,)

#遍历元组，和遍历列表没有什么区别